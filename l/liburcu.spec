Name:         liburcu
Summary:      Userspace Read-Copy-Update Library
URL:          http://lttng.org/urcu
Group:        System
License:      LGPL
Version:      0.8.0
Release:      8.1
Source0:      http://lttng.org/files/urcu/userspace-rcu-%{version}.tar.bz2

%description
liburcu is a userspace RCU (read-copy-update) library. This data
synchronization library provides read-side access which scales
linearly with the number of cores. It does so by allowing multiples
copies of a given data structure to live at the same time, and by
monitoring the data structure accesses to detect grace periods after
which memory reclamation is possible.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q -n userspace-rcu-%{version}
sed -i 's|static inline pid_t gettid(void)|inline pid_t gettid(void)|' tests/common/thread-id.h

%build
%configure
sed -i 's|-Wall|-Wall -Wl,--allow-multiple-definition|' tests/benchmark/Makefile
make %{_smp_mflags -O}

%install
make %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_libdir}/lib*.so.*

%files devel
%{_datadir}/doc/*
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.0
- Rebuilt for Fedora
