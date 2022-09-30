Name:           ogre-caelum
Version:        0.6.3
Release:        4.58
Summary:        Add-on for rendering atmospheric effects for OGRE
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/RigsOfRods/ogre-caelum
Source0:        https://github.com/RigsOfRods/ogre-caelum/archive/v%{version}/ogre-caelum-%{version}.tar.gz
Patch0:         cmake-fix-linking.patch
Patch1:         cmake-fix-doc.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
#BuildRequires:  libboost_date_time-devel
#BuildRequires:  libboost_filesystem-devel
#BuildRequires:  libboost_system-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OGRE)
BuildRequires:  pkgconfig(OIS)

%description
Caelum is a plug-in/library for Ogre targeted to help create nice-looking
(photorealistic if possible) atmospheric effects such as sky colour,
clouds and weather phenomena such as rain or snow.

%package doc
Summary:        Developer documentation for Caelum
Group:          Documentation/HTML
Enhances:       %{name}-devel = %{version}

%description doc
This package contains the doxygen developer documentation for Cealum.

%package devel
Summary:        Development files for Caelum
Group:          Development/Libraries/C and C++
Requires:       libCaelum%{sover} = %{version}
Recommends:     OGRE-%{name} = %{version}
Suggests:       %{name}-doc = %{version}

%description devel
This package contains the development files needed for Caelum.
So it contains pkgconfig-file, headers and some documentation.

%prep
%setup -q -n ogre-caelum-%{version}
%patch0 -p1
%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# Correct .so version
mv %{buildroot}%{_libdir}/libCaelum.so %{buildroot}%{_libdir}/libCaelum.so.%{version}
ln -s libCaelum.so.%{version} %{buildroot}%{_libdir}/libCaelum.so

# Create symlink in OGRE plugin directory, most programs will load this as plugin and therefor search there
mkdir -p %{buildroot}%{_libdir}/OGRE
ln -s ../libCaelum.so.%{version} %{buildroot}%{_libdir}/OGRE/libCaelum.so

# We install it manually
rm -rvf %{buildroot}%{_datadir}/doc/*
mkdir -p %{buildroot}%{_docdir}/%{name}
#cp -R */doc/html/* %{buildroot}%{_docdir}/%{name}

%files
%license lgpl.txt Contributors.txt
%{_libdir}/libCaelum.so.*
%{_libdir}/OGRE/libCaelum.so

%files devel
%doc ReadMe.txt
%{_includedir}/Caelum/
%{_libdir}/libCaelum.so
%{_libdir}/pkgconfig/Caelum.pc

#files doc
#doc %{_docdir}/%{name}

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.3
- Rebuilt for Fedora
* Thu Jun  7 2018 dliw@posteo.net
- fixed build on Tumbleweed and Leap 15.0
- cleaned up spec file
* Mon Jan 11 2016 mailaender@opensuse.org
- Update to version 0.6.3
  * updated for Ogre 1.9
  * implemented physically correct moon phases
  * set finite AABB for starfield in order to avoid infection of parent AABB
  * fixed problem when only one light source is allowed but sun and moon were both active
  * fixed clang build
- Removed caelum-0.6.1-ogre18.patch
- Removed caelum-0.6.1-ogre19.patch
- Removed caelum-0.6.1-disable-script-support.patch
- Removed caelum-pkgconfig-cmake.patch
* Sat May 17 2014 adam@mizerski.pl
- fixed devel package dependency
- fixed rpm groups
* Wed May 14 2014 adam@mizerski.pl
- added patches caelum-0.6.1-ogre19.patch,
  caelum-0.6.1-disable-script-support.patch and
  caelum-pkgconfig-cmake.patch
- removed unneeded BuildRequires
- renamed library package to follow shared library packaging policy
- cleaned up the spec file
* Thu Nov  1 2012 reddwarf@opensuse.org
- Add caelum-0.6.1-ogre18.patch to fix build with Ogre 1.8
* Sat Mar  3 2012 joop.boonen@opensuse.org
- corrected the license
- correction in spec file for 32 bits systems
- cleaned up the spec file
* Fri Feb 24 2012 virus0025@gmail.com
- initial version
