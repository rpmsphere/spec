Name:           nemesis
Version:        1.7
Release:        1
Summary:        TCP/IP Packet Injection Suite
License:        BSD-4-Clause
Group:          Productivity/Networking/Diagnostic
URL:            https://troglobit.com/projects/nemesis/
Source:         https://github.com/troglobit/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libnet-devel

%description
A commandline-based IP stack for Linux. The suite is broken down by
protocol and allows for scripting of injected packet streams from
shell scripts.

Key features:
 * support for ARP, DNS, ICMP, IGMP, OSPF, RIP, TCP, UDP protocols
 * layer 2 or layer 3 injection
 * packet payload from file

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}/%{_datadir}/doc

%files
%doc docs/CREDITS ChangeLog.md README.md
%license LICENSE
%{_bindir}/nemesis
%{_mandir}/man1/nemesis*.1*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
* Thu Aug  2 2018 mardnh@gmx.de
- Correct license
* Sun Jul 29 2018 jengelh@inai.de
- Ensure neutrality of description. Remove future goals.
* Mon Jun 18 2018 mardnh@gmx.de
- Initial package, version 1.5
