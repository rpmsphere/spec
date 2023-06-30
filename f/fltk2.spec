%define svn r8518

Summary: 	Fast Light Tool Kit (FLTK)
Name: 		fltk2
Version: 	2.0.x.%{svn}
Release: 	36.1
License: 	LGPL
Group: 		System/Libraries
Source: 	ftp://ftp.fltk.org/pub/fltk/%{version}/fltk-2.0.x-%{svn}.tar.bz2
URL: 		https://www.fltk.org
# use BuildRoot so as not to disturb the version already installed
BuildRequires:  gcc-c++ pkgconfig libpng-devel libjpeg-devel
BuildRequires: 	libX11-devel xorg-x11-proto-devel libXft-devel
BuildRequires: 	mesa-libGLU-devel mesa-libGL-devel libXext-devel
BuildRequires:  desktop-file-utils makedepend
BuildRequires:  zlib-devel libXi-devel freetype-devel 

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a
cross-platform C++ GUI toolkit for UNIX(r)/Linux(r) (X11),
Microsoft(r) Windows(r), and MacOS(r) X.  FLTK provides modern
GUI functionality without the bloat and supports 3D graphics via
OpenGL(r) and its built-in GLUT emulation.

%package devel
Summary: FLTK - development environment
Group: Development/Libraries/Other

%description devel
Install fltk-devel if you need to develop FLTK applications. 
You'll need to install the fltk package if you plan to run
dynamically linked applications.

%prep
%setup -q -n fltk-2.0.x-%{svn}
sed -i '1i #include <cstring>' images/fl_png.cxx
sed -i "s|0xAA|'\xAA'|g" src/UpBox.cxx

%build
CFLAGS="$RPM_OPT_FLAGS -Wno-error -fpermissive" CXXFLAGS="$RPM_OPT_FLAGS -Wno-error -fpermissive" LDFLAGS="$RPM_OPT_FLAGS" LIBS="-lstdc++ -lXrender -lfontconfig -lfreetype" ./configure  \
--prefix=/usr \
--mandir=%{_mandir} \
--enable-shared \
--enable-xft \
--enable-xdbe \
--enable-png \
--enable-jpeg \
--enable-zlib

# If we got this far, all prerequisite libraries must be here.
make

%install
%{__mkdir_p} $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README* COPYING CREDITS CHANGES TODO documentation

%files devel
%{_bindir}/*
%dir %{_includedir}/fltk
%{_includedir}/fltk/*
%{_libdir}/libfltk2*
%exclude %{_mandir}/*

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.x.%%{svn}
- Rebuilt for Fedora
* Mon Mar 21 2011 Agnelo de la Crotche <agnelo@unixversal.com>
- version  2.0.x r8518 packaged for openSUSE 11.3, 11.4
