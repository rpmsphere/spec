Name:           ap-hotspot
Version:        0.3.1
Release:        1
Summary:        Access Point Mode Hotspot
License:        GPL-3.0
Group:          Productivity/Networking/Other
URL:            http://www.webupd8.org/2013/06/how-to-set-up-wireless-hotspot-access.html
Source0:        https://launchpad.net/~nilarimogard/+archive/ubuntu/webupd8/+files/ap-hotspot_%{version}-1~webupd8~0.tar.gz
Source9:        %{name}.1
Requires:       dnsmasq
Requires:       hostapd
Requires:       iw
BuildArch:      noarch

%description
A script to create an infrastructure WiFi hotspot (access point mode).

%prep
%setup -q -n %{name}-0.3

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp %{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
cp %{SOURCE9} %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc debian/changelog debian/copyright
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
* Sun Jun 19 2016 dap.darkness@gmail.com
- Initial build (0.3.1).
