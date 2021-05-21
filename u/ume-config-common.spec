Name: ume-config-common
License: GPL
Group: Applications/System
Summary: Common configuration for Ubuntu Mobile
Version: 0.11
Release: 1
Source: ume-config-common_0.11.tar.gz
BuildArch: noarch
Requires: xorg-x11-server-Xephyr, GConf2, matchbox-windows-manager, gtk2-engine-sapwood, hildon-desktop

%description
This package provides common configuration files for Ubuntu Mobile.
It is useful by itself in a chroot as well as being a base package
for other ume-config packages to build on.

%prep
%setup -q -n ume-config-common

%build

%install
%__rm -rf %{buildroot}
install -m755 -D 25ume-config-common_startup %{buildroot}/etc/X11/Xsession.d/25ume-config-common_startup
install -m755 -D ume-gui-start %{buildroot}/usr/share/ume-config-common/ume-gui-start
install -m755 -D ume-xephyr-start %{buildroot}/usr/bin/ume-xephyr-start
install -m644 -D moblin.xpm.gz %{buildroot}/boot/grub/moblin.xpm.gz
install -m644 -D kbdconfig %{buildroot}/home/ume/.matchbox/kbdconfig

%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root)
/etc/X11/Xsession.d/25ume-config-common_startup
/usr/share/ume-config-common/ume-gui-start
/usr/bin/ume-xephyr-start
/boot/grub/moblin.xpm.gz
/home/ume/.matchbox/kbdconfig

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Tue Jun 3 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.11-1.ossii
- Initial package
