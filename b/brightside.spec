Name:           brightside
Version:        1.4.0
Release:            24.4
Summary:        Add reactivity to the corners and edges of your GNOME desktop
Group:          Applications/Productivity
License:        GPL
URL:            https://catmur.co.uk/~ed/main/brightside/
Source0:        https://home.jesus.ox.ac.uk/~ecatmur/brightside/download/brightside-1.4.0.tar.bz2
Patch0:         %{name}-gconf-mouse-speed.patch
Patch1:         %{name}-libwnck.patch
Patch2:         %{name}-Makefile.patch
Patch3:         %{name}-desktop.patch
Patch4:         %{name}-2ce4295c0dadf7e562dfa6266315bae7ed18b9f8.diff
Requires(pre):  GConf2
Requires(post): GConf2
BuildRequires:  intltool
BuildRequires:  gettext, libX11-devel
BuildRequires:  libwnck-devel >= 2.6.0
BuildRequires:  libgnomeui-devel >= 2.6.0
BuildRequires:  libglade2-devel >= 2.2.0
BuildRequires:  desktop-file-utils
BuildRequires:  w3m udisks2

%description
Brightside provides "edge flipping" to allow you to switch to the adjacent
workspace simply by pressing your mouse against the edge of the screen.

Besides that Brightside also allows you to assign configurable actions to
occur while you rest the mouse in a corner of the screen.

%prep
%setup -q
%patch 0 -b .patch0
%patch 1 -b .libwnck
%patch 2 -b .X11
%patch 3 -b .desktop
%patch 4 -p1 -b .several

%build
%configure
sed -i 's|$(LIBS)|$(brightside_LDFLAGS)|' src/Makefile
make %{?_smp_mflags} CFLAGS+=-Wno-format-security

%install
rm -rf $RPM_BUILD_ROOT
# For GConf apps: prevent schemas from being installed at this stage
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --vendor ""                       \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications      \
  --delete-original                                    \
  $RPM_BUILD_ROOT/%{_datadir}/control-center-2.0/capplets/brightside.desktop

# Note: the find_lang macro requires gettext
%find_lang Brightside

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%post
# For GConf apps: install schemas as system default
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null

%preun
# For GConf apps: uninstall app's system default schemas
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-uninstall-rule \
  %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :

%files -f Brightside.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/brightside.schemas
%{_datadir}/pixmaps/brightside-48.png
%{_datadir}/applications/*.desktop

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.0
- Rebuilt for Fedora
* Sat Dec 01 2012 josef radinger <cheese@nosuchhost.net> - 1.4.0-13
- add patch4 taken from https://github.com/rswarbrick/brightside/commit/2ce4295c0dadf7e562dfa6266315bae7ed18b9f8.diff
* Sat Sep 03 2011 josef radinger <cheese@nosuchhost.net> - 1.4.0-12
- add libX11
- modify desktop-file
* Sun Apr 02 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.4.0-11
- Update URL
- Use desktop-file-install
* Mon Feb 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.4.0-10
- Rebuilt for Fedora Extras 5
* Wed Aug 17 2005 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 1.4.0-9
- rebuild
* Thu Jul 21 2005 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 1.4.0-8
- rebuild
* Mon May 23 2005 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 1.4.0-7
- ExcludeArch: ppc ppc64 for now (#158560)
* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.4.0-6
- rebuild on all arches
* Wed Apr 13 2005 Adrian Reber <adrian@lisas.de> - 1.4.0-5
- added patch from freebsd to compile against newer libwnck:
  https://www.freebsd.org/cgi/cvsweb.cgi/ports/x11/brightside/files/patch-src_brightside.c
* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt
* Wed Dec 08 2004 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 0:1.4.0-3
- BR intltool
* Sun Dec 05 2004 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 0:1.4.0-0.fdr.2
- Applied gconf-patch from Adrian Reber
* Tue Nov 30 2004 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 0:1.4.0-0.fdr.1
- Initial RPM release
