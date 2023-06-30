%undefine _missing_build_ids_terminate_build

Name:			libcwd
Version:		1.1.2
Release:		1
Summary:		Debugging Library for C++
Source:			https://prdownloads.sourceforge.net/libcwd/libcwd-%{version}.tar.gz
URL:			https://libcwd.sourceforge.net
Group:			System/Libraries
License:		Q Public License (QPL)
BuildRequires:	gcc-c++ libstdc++-devel make glibc-devel procps
BuildRequires:	autoconf automake libtool
Requires:		libcwd-config >= %{version}
Requires:		/bin/ps

%description
Libcwd is a thread-safe, full-featured debugging support library for C++
developers.  It includes ostream-based debug output with custom debug channels
and devices, powerful memory allocation debugging support, as well as run-time
support for printing source file:line number information and demangled type
names.

Authors:
--------
    Carlo Wood <carlo@alinoe.com>

%package config
Summary:		Configuration for the libcwd Debugging Library for C++
Group:			System/Libraries
Requires:		%{name} = %{version}-%{release}

%description config
Libcwd is a thread-safe, full-featured debugging support library for C++
developers.  It includes ostream-based debug output with custom debug channels
and devices, powerful memory allocation debugging support, as well as run-time
support for printing source file:line number information and demangled type
names.

This package contains the configuration file for libcwd:
    %{_datadir}/libcwd/libcwdrc

Authors:
--------
    Carlo Wood <carlo@alinoe.com>

%package devel
Summary:		Development Environment for the libcwd Debugging Library for C++
Group:			Development/Libraries/C and C++
Requires:		%{name} = %{version}-%{release}
Requires:		libstdc++-devel

%description devel
Libcwd is a thread-safe, full-featured debugging support library for C++
developers.  It includes ostream-based debug output with custom debug channels
and devices, powerful memory allocation debugging support, as well as run-time
support for printing source file:line number information and demangled type
names.

This package contains the development environment needed to compile and
link software against libcwd.

Authors:
--------
    Carlo Wood <carlo@alinoe.com>

%prep
%setup -q
#sed -i 's|-Werror//|-Werror /-fpermissive /|' configure

%build
%configure
#sed -i 's|^typedef .*|typedef unsigned int getgroups_t;|' include/sys.h
sed -i 's|-Wall|-Wall -fpermissive|' Makefile
make

%install
rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%doc LICENSE.QPL NEWS README*
%{_libdir}/libcwd.so.*
%{_libdir}/libcwd_r.so.*

%files config
%dir %{_datadir}/libcwd
%config(noreplace) %{_datadir}/libcwd/libcwdrc

%files devel
%{_includedir}/libcwd
%{_libdir}/libcwd.so
%{_libdir}/libcwd_r.so
%{_libdir}/pkgconfig/libcwd.pc
%{_libdir}/pkgconfig/libcwd_r.pc

%changelog
* Sun Apr 2 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.2
- Rebuilt for Fedora
* Sun Jul 27 2008 Pascal Bleser <guru@unixtech.be> 1.0.0
- new package
