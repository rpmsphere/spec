%define docdir %{_defaultdocdir}/watchman 
%define rundir /run/watchman
Name:           watchman
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre-devel
BuildRequires:  python2-devel
Requires:       pcre
Version:        4.9.0
Release:        1
URL:            https://facebook.github.io/watchman/
Summary:        A file watching service
# the thirdparty code is partially MIT-licensed or at least some such
License:        Apache-2.0 and MIT
Group:          System/Monitoring
Source0:        https://github.com/facebook/watchman/archive/v%version.tar.gz#/%{name}-%{version}.tar.gz
# tmpfiles.d configuration for statedir
Source1:        watchman.conf
Source2:        watchman@.service
Source3:        watchman@.socket
# prevent the build system overwriting the autotools docdir in a hard-coded way
Patch0:         %{name}_4.7.0_makefile-am.diff
# fix build with gcc 7 regarding switch/case fall through logic
# this is already fixed upstream, but they have no new release and also
# refactored a lot of code, for example hash.c is now hash.cpp, that's why I
# made my own patch against 4.7.0
Patch1:         fallthrough.diff

%description
Watchman exists to watch files and record when they change. It can also trigger
actions (such as rebuilding assets) when matching files change.

* Watchman can recursively watch one or more directory trees (we call them
roots).
* Watchman does not follow symlinks. It knows they exist, but they show up the
same as any other file in its reporting.
* Watchman waits for a root to settle down before it will start to trigger
notifications or command execution.
* Watchman is conservative, preferring to err on the side of caution; it
considers files to be freshly changed when you start to watch them or when it
is unsure.
* You can query a root for file changes since you last checked, or the current
state of the tree
* You can subscribe to file changes that occur in a root

%package python
Summary:        A python package for talking to the watchman service
# from python/setup.py
License:        MIT
Group:          System/Monitoring

# NOTE: the additional scripts like watchman-make are written in python. I
# guess those scripts don't justify another subpackage, so I add them as a
# bargain to the python bindings.
%description python
Provides Python bindings for directly talking to the watchman service from
within Python.

Additionally, some Python tools that are part of watchman will be installed.

# %%package ruby
# There's also a ruby interface included in watchman.
# The integration into autotools is done via ruby's bundler.
# We can use gem2rpm to create a spec file for it, but it's probably better
# not to make it a subpackage but an independent package rubygem-watchman

%prep
%setup -q
%patch0
#patch1 -p 1

# There is some basic support for watchman to run under systemd:
#
# 	https://github.com/facebook/watchman/commit/2985377eaf8c8538b28fae9add061b67991a87c2
#
# It uses inetd style activation of watchman via systemd based on the socket
# it normally creates per user in /run/watchman/<user>-state.
#
# The unit files aren't currently shipped by upstream. Instead I've added
# them as extra source files. The two files for service and socket are
# template systemd unit files. This way multiple instances of watchman can be
# setup for each user in the system.
#
# It's a bit unclear what the best group ownership and mode bits for the
# socket should be (see watchman@.socket). I'm currently going for more secure
# mode bits.
#
# Does it make sense to run watchman globally as a daemon as root?
#
# -> The developer emphasises that it's supposed to be per user:
#
# https://github.com/facebook/watchman/issues/8
#
# But using the systemd template unit file we can also setup a watchman
# instance for the root user, if desired.
#
# watchman wants to install a statedir in <prefix>/var/run. This statedir is
# supposed to have the sticky bit set, so any user can create sub-directories
# in it for their private state.
#
# Due to systemd handling of /run & /var/run we need to change this to a
# tmpfiles.d approach. We still need to configure with --enable-statedir,
# however, because otherwise the code wouldn't operate with the statedir any
# more but resort to statedirs in /tmp:
#
# https://facebook.github.io/watchman/docs/cli-options.html#quick-note-on-default-locations
#
# We could patch this, but for now I pass the correct enable-statedir which
# gives the code to the right behaviour and location. The statedir that's
# installed via 'make install' is then removed again and replaced by the
# correct tmpfiles.d handling. Otherwise rpmlint barks about evil permissions
# of the statedir (world-writable).
#
# There's no man page for this package as the developer prefers his readme in
# markdown format and also doesn't believe in man pages in the 21st century:
#
# https://github.com/facebook/watchman/issues/30

%build
./autogen.sh
# There is a single gcc strict aliasing problem in "bser.c" which is used to
# build a shared-object "bser.so" that is used in the python package. It can't
# be easily fixed, however, because the aliasing problem arises in
# python2-devel headers. It's the same situation as described here:
#
# https://lists.fedoraproject.org/pipermail/scm-commits/2010-September/496900.html
#
# So let's build everything with no strict aliasing then
export CFLAGS="%optflags -fno-strict-aliasing"
%configure \
	--without-ruby \
	--enable-statedir=%{rundir} \
	--enable-lenient \
	--docdir=%{docdir} # see Patch0, docs should be placed in the packages subdir
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%define build_tmpfiles %{buildroot}%{_tmpfilesdir}
%define build_tmpfile_conf %{build_tmpfiles}/%{name}.conf
# don't package this installed state directory, we just need to configure with
# --enable-statedir for the code to be compiled with support for it, otherwise
# watchman falls back to using statedirs in /tmp.
rm -rf $RPM_BUILD_ROOT/%{rundir}
# install the tmpfiles.d file instead for creating the statedir during runtime
# with sticky bit as expected by watchman
install -d -m 0755 %{build_tmpfiles}
install -m 0644 %{SOURCE1} %{build_tmpfile_conf}

%define build_unitdir %{buildroot}%{_unitdir}
install -D -m 444 %{SOURCE2} %{build_unitdir}/%{name}@.service
install -D -m 444 %{SOURCE3} %{build_unitdir}/%{name}@.socket

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}*

%files
%define tmpfile_conf %{_tmpfilesdir}/%{name}.conf
%doc %{docdir}
%_bindir/watchman

%{tmpfile_conf}
# avoid rpmlint warning tmpfile-not-in-filelist
%ghost %{rundir}

%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}@.socket

%files python
%{python_sitearch}
# additional python tools for working with watchman, not strictly part of the
# python bindings, actually
%_bindir/watchman-*

%pre
%service_add_pre %{name}@.socket %{name}@.service

%post
# NOTE: when updating a warning is printed:
#
# Failed to try-restart watchman@s*: Unit name watchman@s* is not valid
#
# A similar warning is emitted during uninstall
#
# This seems to be an error in the generic systemd macros, they're not dealing
# correctly with template unit files.
%service_add_post %{name}@.socket %{name}@.service
# to initially create the statedir without reboot
# NOTE: This macro is not available in older versions of systemd-rpm-macros,
# causing builds on openSUSE_Leap < 42_2 to fail currently.
%tmpfiles_create %{tmpfile_conf}

%preun
%service_del_preun %{name}@.socket %{name}@.service

%postun
%service_del_postun %{name}@.socket %{name}@.service

%changelog
* Wed Mar 20 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.9.0
- Rebuilt for Fedora
* Tue Jun 20 2017 matthias.gerstner@suse.com
- fallthrough.diff: fix gcc 7 build issues
* Wed Nov 16 2016 jengelh@inai.de
- Replace %%jobs by %%_smp_mflags; drop unnecessary %%clean section.
- Avoid multiple invocation of %%service_*.
* Thu Nov 10 2016 matthias.gerstner@suse.com
- added subpackage for python bindings
- added systemd unit files for service and socket for inetd style spawning of
  watchman user instances via systemd
* Tue Nov  8 2016 mgerstner@suse.de
- initial version using the buildservice
- no support for systemd, python or ruby bindings yet
