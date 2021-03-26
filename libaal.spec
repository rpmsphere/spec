%global debug_package %{nil}

Name:          libaal
Version:       1.0.5
Release:       8.1
Summary:       A library that provides application abstraction mechanism
Group:         System/Libraries
URL:           http://www.kernel.org
Source:        http://www.kernel.org/pub/linux/utils/fs/reiser4/libaal/libaal-%{version}.tar.bz2
License:       GPL
BuildRequires: gcc-c++

%description
This is a library that provides application abstraction mechanism.
It includes device abstraction, libc independence code, etc.

%package devel
Group:         Development/Libraries
Summary:       Static libraries and headers for %{name}
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
This is a library that provides application abstraction mechanism.
It includes device abstraction, libc independence code, etc.
This package contains static libraries and header files need for development.

%prep
%setup -q
sed -i 's|long long|long|' include/aal/types.h

%build
autoreconf -ifv
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/*.so.*
%doc AUTHORS BUGS COPYING CREDITS ChangeLog README THANKS TODO

%files devel
%dir %{_includedir}/aal
%{_includedir}/aal/*.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_datadir}/aclocal/libaal.m4

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.5
- Rebuild for Fedora
* Wed May 20 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.5-1mamba
- package created by autospec
