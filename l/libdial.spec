%undefine _debugsource_packages

Summary: Library to display a clock or a dial
Name: libdial
Version: 2.2
Release: 1
License: GPLv2
URL: https://www.tzclock.org
Group: Applications/Productivity
Source: https://www.tzclock.org/releases/%{name}-%{version}.tar.bz2
BuildRequires: pkgconfig desktop-file-utils gcc
BuildRequires: gtk3-devel

%description
This package contains necessary library files for libdial applications.

%package devel
Summary: libdial development files
Provides: libdial-devel
Group: Development/Libraries

%description devel
This package contains necessary header files for libdial development.

%prep
%setup -q

%build
%configure 
make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -s -m 755 .libs/libdial.so.2.0.1 $RPM_BUILD_ROOT%{_libdir}/libdial.so.2.0.1
install -s -m 755 .libs/libdial.a $RPM_BUILD_ROOT%{_libdir}/libdial.a
install -m 644 pkgconfig/dial.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/dial.pc
install -m 644 src/dialsys.h $RPM_BUILD_ROOT%{_includedir}/dialsys.h
ln -s libdial.so.2.0.1 $RPM_BUILD_ROOT%{_libdir}/libdial.so.2
ln -s libdial.so.2 $RPM_BUILD_ROOT%{_libdir}/libdial.so

%files
%doc COPYING AUTHORS
%{_libdir}/libdial.so*

%files devel
%{_libdir}/pkgconfig/dial.pc
%{_includedir}/dialsys.h
%{_libdir}/libdial.a

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuilt for Fedora
* Sat Dec 14 2013 Chris Knight <chris@theknight.co.uk> 1.0.2-1
- Change to allow pointer to save function on init.
* Mon Oct 29 2012 Chris Knight <chris@theknight.co.uk> 1.0.1-1
- Change to newer version of the colours.
* Thu May  3 2012 Chris Knight <chris@theknight.co.uk> 1.0.0-1
- First development version of the library.
