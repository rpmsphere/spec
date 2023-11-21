Name:         sswf
Summary:      Script SWF Format
URL:          https://www.m2osw.com/sswf
Group:        Flash
License:      GPL
Version:      1.8.4
Release:      12.1
Source0:      https://switch.dl.sourceforge.net/sswf/sswf-%{version}-src.tar.bz2
BuildRequires: libjpeg-devel

%description
Script SWF (SSWF) is a C/C++ library and scripting language to
dynamically create Adobe Flash animations in SWF format.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q
sed -i "s|'\\\\0'|NULL|" src/libas/compiler.c++

%build
autoreconf -ifv
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --disable-rpm-docs \
    --disable-debug \
    --disable-yydebug \
    --enable-shared
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_datadir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
#{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.4
- Rebuilt for Fedora
