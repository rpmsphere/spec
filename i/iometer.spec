%undefine _debugsource_packages

Summary: I/O subsystem measurement and characterization tool
Name: iometer
Version: 1.1.0
Release: 4.1
License: GPL
Group: Applications/System
URL: https://www.iometer.org/
Source: https://dl.sf.net/iometer/iometer-stable/%{version}/iometer-%{version}-src.tar.bz2
BuildRequires: gcc-c++ libaio-devel

%description
Iometer is an I/O subsystem measurement and characterization tool for
single and clustered systems.

%prep
%setup -q
sed 's|IA64|AARCH64|' src/Makefile-Linux.ia64 > src/Makefile-Linux.aarch64

%build
%{__make} %{?_smp_mflags} -C src -f Makefile-Linux.%{_arch} all

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/dynamo %{buildroot}%{_bindir}/dynamo

%clean
%{__rm} -rf %{buildroot}

%files
%doc *.txt src/scripts/ src/iomtr_kstat/ misc/
%{_bindir}/dynamo

%changelog
* Mon Mar 23 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuilt for Fedora
* Thu Jun 12 2014 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Updated to release 1.1.0.
* Sat Aug 28 2004 Dag Wieers <dag@wieers.com> - 0.0.20040730-1
- Initial package. (using DAR)
