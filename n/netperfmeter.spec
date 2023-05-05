Name: netperfmeter
Version: 1.9.3
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
#sed -i 's|sys/sysctl.h|linux/sysctl.h|' src/cpustatus.cc

%build
./autogen.sh
#autoreconf -ifv
#configure
#make

%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{_datadir}/%{name}
install -m644 src/*.R %{buildroot}%{_datadir}/%{name}

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/*
%{_datadir}/man/man1/*.1*
%{_datadir}/netperfmeter

%changelog
* Sun Jan 01 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.3
- Rebuilt for Fedora
* Fri Nov 04 2016 Thomas Dreibholz <dreibh@simula.no> 1.4.0~rc2.0
- Initial RPM release
