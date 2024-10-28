Name: massivethreads
Version: 1.00
Release: 2
Summary: Light weight thread library
Group: Development/Libraries
License: BSD-2
URL: https://github.com/massivethreads/massivethreads
#Source0: https://github.com/massivethreads/massivethreads/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0: %{name}-master.zip
BuildRequires: sqlite-devel
BuildRequires: automake
Requires: python2

%description
MassiveThreads is a Lightweight Thread Library for High Productivity Languages.

%package devel
Summary: Development files for MassiveThreads
Requires: %{name}

%description devel
Development files for MassiveThreads.

%prep
%setup -q -n %{name}-master
sed -i '570i extern int pthread_yield_foo (void) __asm__ ("" "pthread_yield");' src/myth_wrap_pthread.c
sed -i 's|__wrap(pthread_yield)|__wrap(pthread_yield_foo)|' src/myth_wrap_pthread.c

%build
%configure
%make_build

%install
%make_install
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/drview

%files
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_libdir}/lib*.so
%exclude %{_libdir}/lib*.*a
%{_includedir}/*

%changelog
* Sun Sep 4 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.00
- Rebuilt for Fedora
