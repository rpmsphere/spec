Name: netperfmeter
Version: 1.7.0
Release: 1
Summary: Network performance meter for the UDP, TCP, MPTCP, SCTP and DCCP protocols
License: GPL-3.0
Group: Applications/Internet
URL: http://www.iem.uni-due.de/~dreibh/netperfmeter/
Source: http://www.iem.uni-due.de/~dreibh/netperfmeter/download/%{name}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: lksctp-tools-devel
BuildRequires: valgrind-devel
BuildRequires: bzip2-devel
BuildRequires: glib2-devel

%description
NetPerfMeter is a network performance meter for the UDP, TCP, SCTP and DCCP
transport protocols over IPv4 and IPv6. It simultaneously transmits
bidirectional flows to an endpoint and measures the resulting flow bandwidths
and QoS. The results are written as vector and scalar files. The vector files
can e.g. be used to create plots of the results.

%prep
%setup -q
sed -i 's|sys/sysctl.h|linux/sysctl.h|' src/cpustatus.cc

%build
autoreconf -if

%configure
make

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/*
%{_datadir}/man/man1/*.1*
%{_datadir}/netperfmeter/plot-netperfmeter-results.R
%{_datadir}/netperfmeter/plotter.R

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.0
- Rebuilt for Fedora
* Fri Nov 04 2016 Thomas Dreibholz <dreibh@simula.no> 1.4.0~rc2.0
- Initial RPM release
