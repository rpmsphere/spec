%undefine _debugsource_packages
%global _version 22-273

Summary: Another blooming C utility library
Name: cimfomfa
Version: 22.273
Release: 1
License: GPL
Group: Applications
Source0: http://micans.org/cimfomfa/src/cimfomfa-%{_version}.tar.gz
URL: https://github.com/micans/cimfomfa
BuildRequires: automake
Provides: tingea

%description
C utility library libtingea for MCL and zoem.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Provides: tingea-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{_version}
#sed -i 's|-O2|-O2 -fPIC -fPIE|' configure

%build
%{configure}
%{make_build}

%install
%{make_install}

%files
%doc COPYING LICENSE AUTHORS NEWS ChangeLog README TODO THANKS
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/tingea

%changelog
* Sun Apr 21 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 22.273
- Rebuilt for Fedora
