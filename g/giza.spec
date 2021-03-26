Name: giza
Summary: A scientific plotting library for C/Fortran built on cairo
Version: 0.9.4
Release: 8.1
Group: Applications/Multimedia
License: GPL
URL: http://giza.sourceforge.net/
Source0: http://sourceforge.net/projects/giza/files/%{name}-%{version}.tar.gz
BuildRequires: gcc-gfortran
BuildRequires: cairo-devel

%description
Giza is an open, lightweight scientific plotting library built on top of cairo
that provides uniform output to multiple devices. Provides uniform output to
pdf, ps, png and X-Window. Written in C with no dependencies(other than cairo)
as a direct replacement for PGPLOT.

%package devel
Summary: Development files for giza
Requires: %{name}

%description devel
Header files and Libraries for the package Giza.

%prep
%setup -q -n %{name}

%build
%configure
make

%install
mkdir -p %{buildroot}/usr/lib %{buildroot}%{_includedir}
make install FFLAGS=-fPIC PREFIX=/usr DESTDIR=%{buildroot}

%files
%{_docdir}/%{name}
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%exclude %{_libdir}/lib*.a
%exclude %{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Nov 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.4
- Rebuild for Fedora
