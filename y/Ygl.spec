%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build

Summary: Run 2d-GL programs with standard X11 routines
Name: Ygl
Version: 4.2g
Release: 6.1
License: GPL
Group: X11/Libraries
Source: ftp://ftp.thp.uni-duisburg.de/pub/source/X11/%{name}-%{version}.tar.gz
URL: http://WWW.thp.Uni-Duisburg.DE/Ygl/ReadMe.html
BuildRequires: imake
BuildRequires: libX11-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: gcc-gfortran
BuildRequires: f2c

%description
Ygl is an X11 library that emulates the 2D routines of SGI's GL
(sometimes called IRIS GL). Please note that GL is different from OpenGL.
Ygl is very simple to use, and very fast. The 2D routines are built around
the standard X11 libraries and reported to be faster than GL itself.  SGI's
GL has 3D routines as well and Ygl tries to emulate these using OpenGL. 
However this does'nt work yet with Mesa and hence there is no 3D support in
this release.  This release will also work with FORTRAN code.

%package devel
Summary: Development files for the package Ygl

%description devel
Header files and examples for the library Ygl.

%prep
%setup -q -n %{name}-4.2
#sed -i 's|Has_GLX_SGI_video_sync 1|Has_GLX_SGI_video_sync 0|' Imakefile

%build
export FC=f95
xmkmf
make
cd examples
xmkmf
make
make smile_f77 smile_f2c

%install
rm -rf $RPM_BUILD_ROOT
%make_install
mkdir -p $RPM_BUILD_ROOT/usr/include/gl
ln -s ../X11/Ygl.h $RPM_BUILD_ROOT/usr/include/gl/gl.h
ln -s ../X11/Yfgl.h $RPM_BUILD_ROOT/usr/include/gl/fgl.h
ln -s ../X11/Ygl.h $RPM_BUILD_ROOT/usr/include/gl/device.h
ln -s ../X11/Yfgl.h $RPM_BUILD_ROOT/usr/include/gl/fdevice.h

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libYgl.so.*
%doc ReadMe.html FAQ.html Changes.html INSTALLATION
%doc LICENSE Smile.gif SharedLibs.txt

%files devel
%{_libdir}/libYgl.so
%{_includedir}/X11/Ygl.h
%{_includedir}/X11/Yfgl.h
%{_includedir}/X11/Ygltypes.h
%{_includedir}/gl/gl.h
%{_includedir}/gl/fgl.h
%{_includedir}/gl/device.h
%{_includedir}/gl/fdevice.h
%doc examples

%clean 
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Feb 06 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 4.2g
- Rebuilt for Fedora
* Sun Mar 21 1999 Prabhu Ramachandran <prabhu@aero.iitm.ernet.in> 4.0g
- I am the current maintainer
