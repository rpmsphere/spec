Name:           gigi
Version:        0.8.0
Release:        6
Summary:        A C++ OpenGL GUI library
License:        LGPL
URL:            http://gigi.sourceforge.net/
Source0:	    lib%{name}-9999.tar.xz
Patch0:         gigi-938-link.patch
#from https://build.opensuse.org/package/files?package=gigi&project=home%3Adbuck
#Patch1:         gigi-vector.patch
#Patch2:         gigi-adobe-cmath.patch
#Patch3:         gigi-cmake-tests.patch
#Patch4:		gigi_insert.patch
BuildRequires:  ogre-devel
BuildRequires:  boost-devel SDL-devel doxygen libtiff-devel
BuildRequires:  freetype-devel libstdc++-devel gcc-c++ glibc-headers glibc-devel
BuildRequires:  ois-devel DevIL-devel libpng-devel libjpeg-devel cmake

%package devel
Requires:       %{name} = %{version}
Summary:        Development files for libgigi (GiGi/GG)

%package ogre
Requires:       %{name} =  %{version} ogre
Summary:        Ogre plugin for libgigi (GiGi/GG)

%package SDL
Requires:       %{name} =  %{version}
Summary:        SDL plugin for libgigi (GiGi/GG)

%package SDL-devel
Requires:       %{name}-SDL = %{version}
Summary:        Development files for libgigi(GiGi/GG) SDL plugin

%package ogre-devel
Requires:       %{name}-ogre = %{version}
Summary:        Development files for libgigi(GiGi/GG) Ogre plugin

%description
GiGi (aka GG) is a C++ OpenGL GUI library. It has drivers that work with SDL 
(http://www.libsdl.org) and Ogre (http://www.ogre3d.org).

%description devel
Development files for libgigi (GiGi/GG)

%description SDL
SDL plugin for libgigi (GiGi/GG)

%description ogre
Ogre plugin for libgigi (GiGi/GG)

%description SDL-devel
Development files libgigi(GiGi/GG) SDL plugin

%description ogre-devel
Development files for libgigi(GiGi/GG) Ogre plugin

%prep
%setup -q -n GG
%patch0 -p1 
#%patch1 -p1 
#%patch2 -p1 
#%patch3 -p1 
#%patch4 -p1 
sed -i 's|!defined(ADOBE_NO_DOCUMENTATION)|defined(ADOBE_NO_DOCUMENTATION)|' GG/adobe/eve.hpp

%build
#export CFLAGS="-fPIC -std=gnu11"
%cmake
make
#cd doc
#doxygen 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/GG

%files
%doc README INSTALLING PACKAGING COPYING
%{_libdir}/libGiGi.so

%files SDL
%{_libdir}/libGiGiSDL.so

%files ogre
%{_libdir}/libGiGiOgre.so
%{_libdir}/libGiGiOgrePlugin_OIS.so

%files devel
%doc doc/GG/*
%{_includedir}/GG/*.h
%{_includedir}/GG/*.py*
%{_includedir}/GG/adobe/*
%{_includedir}/GG/dialogs/*
%{_includedir}/GG/utf8/*
%{_libdir}/pkgconfig/GiGi.pc

%files SDL-devel
%{_includedir}/GG/SDL/SDLGUI.h
%{_libdir}/pkgconfig/GiGiSDL.pc

%files ogre-devel
%{_includedir}/GG/Ogre/*
%{_libdir}/pkgconfig/GiGiOgre.pc

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.0
- Rebuilt for Fedora
* Sat Feb 16 2013 josef radinger <cheese@nosuchhost.net> - 0.8.0-6
- extract libgigi from freeorion
  therefore we no longer have a valid svnrev  
* Fri Nov  9 2012 josef radinger <cheese@nosuchhost.net> - 0.8.0-5
- add patch4 for compile error
- fix install-section
- fix doc-section
* Wed Nov  7 2012 josef radinger <cheese@nosuchhost.net> - 0.8.0-4
- update for new ogre-library
* Mon Aug  1 2011 Алексей <alex@alex-desktop> - 0.8.0-3.R
- update for new ogre-library
* Thu Jul 28 2011 Alexei Panov <elemc AT atisserv DOT ru> - 0.8.0-2.R
- added missing build requires (libpng, DevIL, libjpeg)
* Wed Jul 27 2011 Alexei Panov <elemc AT atisserv DOT ru> - 0.8.0-1
- Initial build
