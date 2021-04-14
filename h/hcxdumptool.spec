%undefine _debugsource_packages

Name: hcxdumptool
Summary: Small tool to capture packets from wlan devices
Version: 6.0.0
Release: 1
Group: Network
License: MIT
URL: https://github.com/ZerBea/hcxdumptool
Source0: https://github.com/ZerBea/hcxdumptool/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: openssl-devel

%description
Tool to capture wpa handshacke from Wi-Fi networks and run several tests to
determine if Wi-Fi access points or clients are vulnerable to brute-force
atacks.

%prep
%setup -q

%build
make %{?_smp_mflags} PREFIX=/usr

%install
make install PREFIX=/usr DESTDIR=%{buildroot}
install -d %{buildroot}%{_mandir}/man1/
install -m644 manpages/* %{buildroot}%{_mandir}/man1/

%files
%doc changelog README.md license.txt docs/*
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Dec 12 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 6.0.0
- Rebuilt for Fedora

