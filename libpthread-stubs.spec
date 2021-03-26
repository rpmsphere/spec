Name:          libpthread-stubs
Version:       0.2
Release:       5.1
Summary:       Weak aliases for pthread functions not provided in libc
Group:         System/Libraries
URL:           http://xcb.freedesktop.org
Source:        http://xcb.freedesktop.org/dist/libpthread-stubs-%{version}.tar.bz2
License:       MIT

%description
This library provides weak aliases for pthread functions not provided in libc
or otherwise available by default. Libraries like libxcb rely on pthread stubs
to use pthreads optionally, becoming thread-safe when linked to libpthread,
while avoiding any performance hit when running single-threaded.

libpthread-stubs supports this behavior even on platforms which do not supply
all the necessary pthread stubs. On platforms which already supply all the necessary
pthread stubs, this package ships only the pkg-config file pthread-stubs.pc,
to allow libraries to unconditionally express a dependency on pthread-stubs
and still obtain correct behavior.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
This library provides weak aliases for pthread functions not provided in libc
or otherwise available by default. Libraries like libxcb rely on pthread stubs
to use pthreads optionally, becoming thread-safe when linked to libpthread,
while avoiding any performance hit when running single-threaded.

libpthread-stubs supports this behavior even on platforms which do not supply
all the necessary pthread stubs. On platforms which already supply all the necessary
pthread stubs, this package ships only the pkg-config file pthread-stubs.pc,
to allow libraries to unconditionally express a dependency on pthread-stubs
and still obtain correct behavior.

This package contains static libraries and header files need for development.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/libpthread-stubs.so.*

%files devel
%{_libdir}/libpthread-stubs.a
%{_libdir}/libpthread-stubs.la
%{_libdir}/libpthread-stubs.so
%exclude %{_libdir}/pkgconfig/*.pc
%doc COPYING README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
* Sat Oct 10 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.2-2mamba
- devel package: don't obsolete main package
* Tue Sep 29 2009 Automatic Build System <autodist@mambasoft.it> 0.2-1mamba
- automatic update by autodist
* Sat Jun 21 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 0.1-3mamba
- correct obsolete for libpthread-stubs
* Fri Jun 20 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 0.1-2mamba
- specfile updated
- removed libpthread-stubs package and obsoleted by libpthread-stubs-devel
* Wed Feb 07 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 0.1-1qilnx
- package created by autospec
