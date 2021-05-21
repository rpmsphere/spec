Name: ume-config-user
License: GPL
Group: Applications/System
Summary: User configuration for Ubuntu Mobile
Version: 0.1
Release: 1
Source0: start-hildon
BuildArch: noarch
Requires: GConf2, matchbox-window-manager, gtk2-engine-sapwood
Requires: moblin-clutter-home, marquee-plugins
Requires: hildon-desktop, hildon-theme-mobile-basic

%description
This package provides user configuration files for Ubuntu Mobile.
It is useful by itself in a chroot as well as being a base package
for other ume-config packages to build on.

%prep
%setup -T -c

%build

%install
%__rm -rf %{buildroot}
install -m755 -D %{SOURCE0} %{buildroot}%{_bindir}/start-hildon

%post
[ -d /home/ume ] || useradd ume
ln -sf %{_bindir}/start-hildon /home/ume/.xsession
echo 'Before relogin, please set the password of the user "ume" if needed.'

%postun
rm -f /home/ume/.xsession

%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/start-hildon

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu Jun 5 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.1-1.ossii
- Initial package
