Name:           create_ap
Version:        0.4.6
Release:        1
Group:          System/Servers
Summary:        Creates a NATed or Bridged WiFi Access Point
License:        BSD
URL:            https://github.com/oblique/create_ap
Source0:        https://github.com/oblique/create_ap/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       hostapd

%description
This script creates a NATed or Bridged WiFi Access Point.

%prep
%setup -q

%build

%install
%make_install

%files
%doc LICENSE README.md
%config(noreplace) %{_sysconfdir}/create_ap.conf
%{_bindir}/create_ap
%{_unitdir}/create_ap.service
%{_datadir}/bash-completion/completions/create_ap

%changelog
* Thu Dec 07 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.6
- Initial Fedora package
* Thu Dec 22 2016 guillomovitch <guillomovitch> 0.4.6-1.mga6
+ Revision: 1076386
- imported package create_ap
