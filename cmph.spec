%global debug_package %{nil}

Name:         cmph
Summary:      C Minimal Perfect Hashing (CMPH) Library
URL:          http://sourceforge.net/projects/cmph/
Group:        Algorithm
License:      MPL
Version:      2.0
Release:      9.1
Source0:      http://sourceforge.net/projects/cmph/files/%{name}/%{name}-%{version}.tar.gz

%description
A perfect hash function maps a static set of n keys into a set of m
integer numbers without collisions, where m is greater than or equal
to n. If m is equal to n, the function is called minimal. CMPH is a
minimal perfect hashing library with a C API.

%prep
%setup -q

%build
./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir} \
    --disable-shared
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_bindir}/%{name}
%{_includedir}/*.h
%{_libdir}/lib%{name}.*
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora
