Name:           cattle
Version:        1.4.0
Release:        1
Summary:        A toolkit for the Brainfuck programming language
License:        GPLv2+
URL:            https://kiyuko.org/software/cattle
Source0:        https://kiyuko.org/software/cattle/releases/%{name}-%{version}.tar.xz

%description
Cattle can be embedded in any application to give it the ability to inspect
and run Brainfuck programs; to make the interaction between the hosting
application and the Brainfuck interpreter completely transparent, Cattle can
be configured to use a custom set of I/O routines instead of the default ones.

%package devel
Summary:        Development headers and libraries for cattle
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers and libraries for cattle.

%prep
%setup -q
mkdir build

%build
cd build
../configure --prefix=/usr --libdir=%{_libdir}
make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}

%files
%{_docdir}/%{name}-*
%{_libdir}/lib%{name}-*.so.*

%files devel
%{_includedir}/*
%{_libdir}/girepository-1.0/Cattle-1.0.typelib
%{_libdir}/libcattle-1.0.a
%{_libdir}/libcattle-1.0.so
%{_libdir}/pkgconfig/cattle-1.0.pc
%{_datadir}/gir-1.0/Cattle-1.0.gir
   
%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.0
- Rebuilt for Fedora
