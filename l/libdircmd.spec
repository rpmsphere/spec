%undefine _debugsource_packages

Summary: Directory command library
Name: libdircmd
Version: 5.0
Release: 1
License: GPLv2
URL: https://www.tzclock.org
Group: Applications/Productivity
Source: https://www.tzclock.org/releases/%{name}-%{version}.tar.bz2
BuildRequires: libselinux-devel libacl-devel openssl-devel gcc

%description
dircmd consists of a general purpose directory library.
 
%package devel
Summary: libdircmd development files
Provides: dircmd-devel
Group: Development/C

%description devel
This package contains necessary header files for libdircmd development.

%prep
%setup -q

%build
%configure 
make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT/etc
install -s -m 755 .libs/libdircmd.so.5 $RPM_BUILD_ROOT%{_libdir}/libdircmd.so.%{version}
install -s -m 755 .libs/libdircmd.a $RPM_BUILD_ROOT%{_libdir}/libdircmd.a
install -m 644 pkgconfig/dircmd.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/dircmd.pc
install -m 644 src/dircmd.h $RPM_BUILD_ROOT%{_includedir}/dircmd.h
ln -s libdircmd.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libdircmd.so.5
ln -s libdircmd.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libdircmd.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/libdircmd.so*

%files devel
%{_libdir}/pkgconfig/dircmd.pc
%{_includedir}/dircmd.h
%{_libdir}/libdircmd.a

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0
- Rebuilt for Fedora
* Wed Sep 26 2007 Chris Knight <chris@theknight.co.uk> 4.0.5-1
- Fixes to the build and distribution system.
