Name: ume-config-netbook
License: GPL
Group: Applications/System
Summary: netbook configuration for Ubuntu Remix
Version: 0.3
Release: 2
Source: ume-config-netbook_0.3ubuntu2.tar.gz
URL: https://launchpad.net/netbook-remix
BuildArch: noarch
Requires: maximus

%description
This package provides common configuration files for Ubuntu Mobile.
It is useful by itself in a chroot as well as being a base package
for other ume-config packages to build on.
 
%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}
install -m644 -D xorg.conf %{buildroot}%{_sysconfdir}/X11/xorg.conf
install -m644 -D autostart/maximus-autostart.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/maximus-autostart.desktop
install -m644 -D netbook-modules %{buildroot}%{_sysconfdir}/event.d/netbook-modules

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/X11/xorg.conf
%{_sysconfdir}/xdg/autostart/maximus-autostart.desktop
%{_sysconfdir}/event.d/netbook-modules

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Jun 6 2008 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3-2.ossii
- Initial package
