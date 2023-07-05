Name:         libfirm
Summary:      Program Intermediate Representation Modeling Library
URL:          https://sourceforge.net/projects/libfirm/
Group:        Compiler
License:      GPL
Version:      1.21.0
Release:      6.1
Source0:      https://sourceforge.net/projects/libfirm/files/%{name}/%{version}/%{name}-%{version}.tar.bz2

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%description
libFirm is a C library implementing the Firm low-level intermediate
representation. Firm is used to represent computer programs in a
computer program in order to analyse and transform it. In Firm
programs are represented in a graph based SSA form.

%prep
%setup -q

%build
autoreconf -ifv

./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir}
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.21.0
- Rebuilt for Fedora
