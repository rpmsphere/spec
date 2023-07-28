%undefine _debugsource_packages

Name:           netvisix
Version:        1.4.0
Release:        1
Summary:        Visualizes the network packet flow between hosts
License:        GPL-3.0+
Group:          Productivity/Networking/Other
URL:            https://github.com/bewue/Netvisix
Source0:        https://github.com/bewue/Netvisix/archive/%{version}.tar.gz#/Netvisix-%{version}.tar.gz
Source1:        %{name}.policy
Source2:        icon.png
Source3:        %{name}.desktop
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
BuildRequires:  pkgconfig(libtins)
BuildRequires:  polkit

%description
Netvisix listens on your local network interface and visualizes the network
packet flow between hosts. Also packet statistics per host are available.

Supported Protocols (colored and handeld in statistics): ARP, IPv4, IPv6, ICMP,
ICMPv6, IGMP, TCP, UDP, DNS, DHCP, DHCPv6

%prep
%setup -q -n Netvisix-%{version}
sed -i 's|stdint.h|cstdint|' libtins/include/tins/ip_address.h

%build
cd Netvisix
qmake-qt5
make %{?_smp_mflags} PREFIX=/usr

%install
install -Dm 0755 Netvisix/Netvisix %{buildroot}%{_bindir}/%{name}
install -Dm 0644 %{SOURCE1} %{buildroot}%{_datadir}/polkit-1/actions/org.opensuse.policykit.%{name}.policy
install -Dm 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm 0644 %{SOURCE3} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc LICENSE README*
%{_bindir}/%{name}
%{_datadir}/polkit-1/actions/org.opensuse.policykit.%{name}.policy
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Jul 02 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.0
- Rebuilt for Fedora
* Thu Sep 20 2018 ecsos@opensuse.org
- Add netvisix-include.patch to fix build error for Tumbleweed.
* Sun Jul  3 2016 avvissu@yandex.by
- Update to 1.3.0:
  * add support for multiple ipv4 & ipv6 addresses (host info popup)
- Add %%%%includedir_tins
* Fri May 22 2015 avvissu@yandex.ru
- Update to 1.2.0:
  * add http protocol handling
  * improved dns/hostname handling
* Fri May 15 2015 avvissu@yandex.ru
- Update to 1.1.0:
  * added hostname lookup (optional)
  * minor display changes
- Add BuildRequires: pkgconfig(Qt5Network)
* Thu May  7 2015 avvissu@yandex.ru
- Initial release
