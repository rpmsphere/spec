Name: massivethreads
Version: 1.00
Release: 1
Summary: Light weight thread library
Group: Development/Libraries
License: BSD-2
URL: https://github.com/massivethreads/massivethreads
Source0: https://github.com/massivethreads/massivethreads/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: sqlite-devel
Requires: python2

%description
MassiveThreads is a Lightweight Thread Library for High Productivity Languages.

%package devel
Summary: Development files for MassiveThreads
Requires: %{name}

%description devel
Development files for MassiveThreads.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/drview

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_libdir}/lib*.so
%exclude %{_libdir}/lib*.*a
%{_includedir}/*

%changelog
* Fri Jun 12 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.00
- Rebuild for Fedora
