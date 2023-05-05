%undefine _debugsource_packages
%global _version 2021-03-27

Name:           quickjs
Version:        %(echo %{_version}|tr - .)
Release:        2
Summary:        A small and embeddable Javascript engine
License:        BSD
URL:            https://bellard.org/quickjs/
Source0:	https://bellard.org/quickjs/quickjs-%{_version}.tar.xz

%package devel
Summary:	Development files for package %{name}
Requires:	%{name}

%description
QuickJS supports the ES2020 specification 1 including modules, asynchronous
generators, proxies and BigInt. It supports mathematical extensions such as
big decimal float float numbers (BigDecimal), big binary floating point numbers
(BigFloat), and operator overloading.

%description devel
Header files and Libraries for package %{name}.

%prep
%setup -q -n quickjs-%{_version}
sed -i 's|lib/quickjs|%{_lib}/quickjs|' Makefile qjsc.c
sed -i 's|/usr/local|/usr|' Makefile

%build
%make_build

%install
%make_install

%files
%doc Changelog LICENSE doc/*
%{_bindir}/*

%files devel
%doc examples
%{_includedir}/%{name}
%{_libdir}/%{name}

%changelog
* Tue Jan 17 2023 Zephyr Lykos <fedora@mochaa.ws> - 2021.03.27-2
- Fix qjsc library path
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2021.03.27-1
- Rebuilt for Fedora
