Name: xiwtool
Version: 0.12
Release: 6.1
Summary: Wireless Network Scanning and Configuration for Linux Desktops
License: GPLv2
Group: User Interface/X Hardware Support
URL: http://sourceforge.net/projects/xiwtool/
Source0: http://sourceforge.net/projects/xiwtool/files/%{name}-%{version}.tar.gz
#BuildRequires: wireless-tools
BuildRequires: pam-devel
BuildRequires: libX11-devel
BuildRequires: libXpm-devel
Requires: xorg-x11-fonts-75dpi

%description
On Linux systems that have a wireless network interface, xiwtool can scan
and view statistics for nearby Wireless Access Points, including automatic
connections to public WAPs like those in coffee shops and libraries.
Xiwtool has many internal features that provide reliable network scanning
and management in crowded environments.

Xiwtool also checks your your machine and notifies you if the system needs
any drivers or networking tools to connect to nearby networks. The program
can diagnose connection issues with WPA and WPA2 authenticated networks,
and also has tools to evaluate legacy networks that use WEP encryption.

%prep
%setup -q
sed -i '/read sudo_resp/d' configure

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure --with-root-account=no --with-interfaces=/etc/sysconfig/network-scripts --with-ifstate=/etc/sysconfig/network-scripts
make

%install
%make_install -i

%files
%doc ChangeLog COPYING AUTHORS README NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Dec 17 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.12
- Rebuilt for Fedora
