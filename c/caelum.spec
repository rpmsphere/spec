Name:           caelum
Version:        0.6.1
Release:        14.1
License:        LGPL-3.0+
Summary:        Add-on for rendering atmospheric effects for OGRE
URL:            http://code.google.com/p/caelum/
Group:          Development/Libraries/Other
Source:         http://caelum.googlecode.com/files/caelum-%{version}.tar.gz
Patch0:         caelum-0.6.1-ogre18.patch
Patch1:         caelum-ogre-1.9.patch
#BuildRequires:  cg
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  ois-devel
BuildRequires:  ogre-devel < 1.9
BuildRequires:  ogre-pagedgeometry-devel
BuildRequires:  pkgconfig
BuildRequires:  libX11-devel

%description
Caelum is a plug-in/library for Ogre targeted to help create nice-looking
(photorealistic if possible) atmospheric effects such as sky colour,
clouds and weather phenomena such as rain or snow.

%package devel
Summary:        Caelum is an add-on for rendering atmospheric effects for OGRE
Requires:       caelum

%description devel
Caelum is a plug-in/library for Ogre targeted to help create nice-looking
(photorealistic if possible) atmospheric effects such as sky colour,
clouds and weather phenomena such as rain or snow.

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%prep
%setup -q
%patch0
%patch1 -p1

%build
export CFLAGS=-fpermissive
cmake -DLIB_INSTALL_DIR=%{_libdir} -DCMAKE_INSTALL_PREFIX=%{_prefix} .
make

%install
%make_install
mkdir -p %{buildroot}/%{_docdir}/%{name}
mv %{buildroot}%{_prefix}/doc/* %{buildroot}/%{_docdir}/%{name}/.
dos2unix %{buildroot}/%{_docdir}/%{name}/*
rmdir %{buildroot}%{_prefix}/doc

%files
%{_libdir}/*.so

%files devel
%{_includedir}/Caelum/
%{_libdir}/pkgconfig/Caelum.pc
%{_docdir}/%{name}/

%changelog
* Sun Apr 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuilt for Fedora
* Thu Nov  1 2012 reddwarf@opensuse.org
- Add caelum-0.6.1-ogre18.patch to fix build with Ogre 1.8
* Sat Mar  3 2012 joop.boonen@opensuse.org
- corrected the license
- correction in spec file for 32 bits systems
- cleaned up the spec file
* Fri Feb 24 2012 virus0025@gmail.com
- initial version
