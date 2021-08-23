Name: f5vpn-login
Summary: FirePass Command Line VPN Client
Version: 2020
Release: 1
Group: Applications/Communications
License: GPL-3
URL: https://github.com/zrhoffman/f5vpn-login
Source0: %{name}-master.zip
Requires: ppp
Requires: net-tools
Requires: python3
BuildArch: noarch

%description
This software allow you to connect to an F5 Networks VPN server (BIG-IP APM)
without using their proprietary VPN client.

%prep
%setup -q -n %{name}-master

%build

%install
install -Dm755 %{name}.py %{buildroot}%{_bindir}/%{name}

%files
%doc CHANGELOG.md README.md COPYING
%{_bindir}/%{name}

%changelog
* Sun Aug 15 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2020
- Rebuilt for Fedora
