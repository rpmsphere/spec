Name:           xclass
BuildRequires:  gcc-c++ libX11-devel libXpm-devel libXext-devel
License:        GPL v2 or later; LGPL v2.1 or later
Group:          System/Libraries
Version:        0.9.2
Release:        344.1
Summary:        Library for Uniform Presentation of fvwm95 Programs
URL:            https://xclass.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-configs.patch
Patch1:         %{name}-%{version}-gcc-3.1.patch
Patch2:         %{name}-%{version}-gcc-4.0.patch
Patch3:         %{name}-%{version}-gcc-4.1.patch

%description
This package contains a library for uniform presentation of fvwm95
programs.

Authors:
--------
    Hector Peraza <peraza@mitac11.uia.ac.be>

%package devel
License:        LGPL v2.1 or later
Summary:        Library for Uniform Presentation of fvwm95 Programs - development files
Group:          System/Libraries
Requires:       %{name} = %{version}

%description devel
This package contains development files for xclass library.

Authors:
--------
    Hector Peraza <peraza@mitac11.uia.ac.be>

%prep
%setup -q
%patch 0 -p1
%patch 1 -p1
%patch 2
%patch 3
sed -i 's/max/std::max/g' lib/libxclass/OXGLFrame.cc
sed -i 's|packages/xclass|xclass-%{version}|' doc/Makefile*
sed -i '1i #include <cmath>' lib/libxclass/OXFrame.cc
sed -i 's/abs(/fabs(/g' lib/libxclass/OGifImage.cc lib/libxclass/OXFrame.cc

%build
cp -f /usr/lib/rpm/redhat/config.* .
autoconf
CXXFLAGS="$RPM_OPT_FLAGS -Wno-narrowing" \
./configure --prefix=%{_prefix} \
        --libdir=%{_libdir} \
    --sysconfdir=/etc \
    --enable-debug=no
make shared
make all

%install
rm -rf $RPM_BUILD_ROOT
mv lib/libxclass/icons/*.xpm icons/
make DESTDIR=$RPM_BUILD_ROOT install 
make DESTDIR=$RPM_BUILD_ROOT install_shared
install -m 644 include/xclass/XCconfig.h $RPM_BUILD_ROOT%{_prefix}/include/XCconfig.h

%files
%{_datadir}/doc/%{name}-%{version}
%config /etc/xclassrc
%{_datadir}/xclass/
%{_libdir}/libxclass.so.*

%files devel
%{_prefix}/bin/xc-config
%{_prefix}/include/XCconfig.h
%{_prefix}/include/xclass/
%{_libdir}/libxclass.a
%{_libdir}/libxclass.so

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.2
- Rebuilt for Fedora
* Mon May 28 2007 anosek@suse.cz
- split off devel package
* Tue Sep 12 2006 anosek@suse.cz
- updated to version 0.9.2
  * this version includes OpenGL support
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Dec  6 2005 mmarek@suse.cz
- fix undefined operation warning in OXHtmlIndex.cc
* Tue Nov 29 2005 mmarek@suse.cz
- fix strict aliasing with gcc-4.1
* Tue Nov 15 2005 mmarek@suse.cz
- don't build as root
* Wed Oct  5 2005 mmarek@suse.cz
- fixed build with gcc-4.1
* Mon Apr 11 2005 pmladek@suse.cz
- fixed pointer to int casts for gcc-4.0 on 64-bit architectures
* Mon Feb  7 2005 pmladek@suse.cz
- updated to version 0.9.1:
  * added OXToolBarButton
  * implemented html-based help system
  * added support for viewing rgb images
  * some more compiled in pixmaps
  * and more fixes and improvements, see the package documentation
- removed obsolete gcc-3.3.patch and warnings.patch
- updated gcc-3.1.patch (still necessary to compile rfb package)
- installed symlinks, so the dynamic library is usable out of box
* Fri Apr 16 2004 pmladek@suse.cz
- fixed compiler warnings (control reaches end of non-void function)
* Fri Jun  6 2003 ltinkl@suse.cz
- updated sources to version 0.8.2
  * new HTML widget
- redid the patches
* Thu Nov 21 2002 pmladek@suse.cz
- updated to the version 0.7.4
- removed obsolete patch which fixes OIniFile::PutItem to use
  a const char* as second arg
- removed obsolete patch which fixes iterators
- fixed to build with gcc-3.3
- used the instaled documentation
- moved all icons from /usr/lib to /usr/share
* Sat Apr 13 2002 ro@suse.de
- make it compile with gcc-3.1
* Tue Jan 29 2002 pmladek@suse.cz
- prefix changed from /usr/X11R6 to /usr [#12954]
- fixed xc-config for lib64
* Fri Jan 18 2002 pmladek@suse.cz
- updated to version 0.6.2
- fixed URL
* Wed Jan  9 2002 pmladek@suse.cz
- used macro %%{_lib} to fix for lib64
* Mon Jan  7 2002 schwab@suse.de
- Properly use iterators.
* Wed Oct 31 2001 pmladek@suse.cz
- updated to version 0.5.8
- removed obsolete textentry patch
- added URL
* Sun Apr 29 2001 pmladek@suse.cz
- removed fvwm95 from requires
* Thu Apr  5 2001 pmladek@suse.cz
- fixed bug with text entry
- reorganized patches
* Wed Mar  7 2001 cihlar@suse.cz
- fixed neededforbuild
* Thu Dec 28 2000 sf@suse.de
- added -fPIC for shared libs
* Mon Nov 27 2000 cihlar@suse.cz
- added /etc/xclassrc to file list
* Mon Nov 27 2000 ro@suse.de
- fixed build-root (DESTDIR) in Makefiles
* Mon Nov 27 2000 ro@suse.de
- added xc-config to filelist
* Tue Nov 21 2000 cihlar@suse.cz
- update to version 0.5.4. Applications are not
  part of this package
- removed ancient tutorial
* Mon Aug 21 2000 cihlar@suse.cz
- update to version 981004
- added BuildRoot
- bzipped sources
* Mon Jun  5 2000 ro@suse.de
- doc relocation
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Jan 21 1999 ro@suse.de
- modified patch-style
- OScrollBar.h : give sb_width a type : int
- cleaned up OIniFile::PutItem to use a const char* as second arg
- copy const char * to char * using strdup in OXFileDialog
- chmod 755 libxclass.so
* Tue Oct  7 1997 maddin@suse.de
- first S.u.S.E. version
- integrated xclass and xclass-tutorial into one package
