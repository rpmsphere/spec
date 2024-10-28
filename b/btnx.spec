Name:           btnx
Version:        0.4.11
Release:        9.1
Summary:        Mouse Button Extension
# https://www.ollisalonen.com/btnx/btnx-%{version}.tar.gz
Source:         btnx-%{version}.tar.bz2
Patch1:         btnx-remove_Werror.patch
URL:            https://www.ollisalonen.com/btnx/
Group:          Hardware/Other
License:        GNU General Public License version 2 (GPL v2)
BuildRequires:  libdaemon-devel
BuildRequires:  gcc make glibc-devel pkgconfig
BuildRequires:  autoconf automake libtool

%description
btnx is a daemon that enables rerouting of mouse button events through uinput
as keyboard and other mouse button combinations.

For example, you can configure an extra mouse button to send a Ctrl+Alt+Right
command to switch workspaces. This is especially useful for mice with more
buttons than Gnome or KDE can properly handle, or mice that need evdev and a
100 step howto to register button events at all.

btnx integrates revoco, a program that allows changing MX Revolution's wheel
behavior.

%prep
%setup -q
%patch 1

%build
echo "libdaemon lib flags: $(pkg-config --libs libdaemon)"
export init_scripts_path=/etc/init.d
export config_path="%{_sysconfdir}/btnx"
export init_tool=no
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
export SUSE_ASNEEDED=0
%configure
%__make %{?_smp_flags}

%install
%__rm -rf "$RPM_BUILD_ROOT"
export init_scripts_path=/etc/init.d
export config_path="%{_sysconfdir}/btnx"
export init_tool=no
make DESTDIR=$RPM_BUILD_ROOT install
touch "$RPM_BUILD_ROOT%{_sysconfdir}/btnx/btnx_config"
%__install -d "$RPM_BUILD_ROOT/usr/sbin"
%__ln_s ../../etc/init.d/btnx "$RPM_BUILD_ROOT/usr/sbin/rcbtnx"

%files
%doc AUTHORS ChangeLog COPYING NEWS README
/etc/init.d/btnx
/usr/sbin/rcbtnx
%dir %{_sysconfdir}/btnx
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/btnx/btnx_config
%config(noreplace) %{_sysconfdir}/btnx/events
%{_sbindir}/btnx

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.11
- Rebuilt for Fedora

* Sun Aug 10 2008 guru@unixtech.be
- new upstream version

* Thu Apr 17 2008 guru@unixtech.be
- new package
