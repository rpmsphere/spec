%global gdate   20190109

Name:           ticpp
Summary:        Completely new interface to TinyXML
Version:        0
Release:        0.git%gdate.1
License:        MIT
Group:          Development/Other
URL:            https://github.com/wxFormBuilder/ticpp
Source0:        ticpp-%{gdate}.tar.gz
Patch1:         ticpp-soversion.patch
Patch2:         ticpp-lib-install.patch
Patch3:         ticpp-headers-install.patch
Patch4:         ticpp-C++17.patch
BuildRequires:  cmake

%description
TiCPP is short for the official name TinyXML++. It is a completely new
interface to TinyXML that uses MANY of the C++ strengths. Templates,
exceptions, and much better error handling.

%package devel
Summary:        Development libraries and header files for TiCPP
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description devel
TiCPP is short for the official name TinyXML++. It is a completely new
interface to TinyXML that uses MANY of the C++ strengths. Templates,
exceptions, and much better error handling.

%prep
%autosetup -p1 -n ticpp-%{gdate}

%build
%cmake
%cmake_build

%install
%cmake_install
mv %buildroot/usr/lib %buildroot%_libdir

%files
%{_libdir}/libticpp.so.*

%files devel
%{_includedir}/ticpp/
%{_libdir}/libticpp.so

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0-0.git20190109.1
- Rebuilt for Fedora
* Sun Jan 03 2021 wally <wally> 0-0.git20190109.1.mga8
+ Revision: 1668417
- imported package ticpp
