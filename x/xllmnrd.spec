Name: xllmnrd
Summary: An IPv6 LLMNR responder daemon
Version: 2.0
Release: 3.1
Group: System Environment/Daemons
License: GPL
URL: https://www.vx68k.org/xllmnrd
Source0: https://sourceforge.net/projects/xllmnrd/files/%{name}-%{version}.tar.gz

%description
xllmnrd allows Microsoft Windows clients to get the IPv6 address of a GNU/Linux
server on the same local network without any DNS configuration and thereby
effectively complements Samba which provides NetBIOS name resolution for IPv4.

%prep
%setup -q
sed -i 's|SIZE_MAX|IFA_MAX|' src/ifaddr.c

%build
%configure
make

%install
%make_install

%files
%doc AUTHORS ChangeLog README COPYING NEWS
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8.*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Thu Feb 01 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
