Summary:        A program that allows visualization of huge graphs
Name:           tulip
Version:        5.4.0
Release:        1
URL:            https://sourceforge.net/projects/auber/
Source0:        https://downloads.sourceforge.net/project/auber/%{name}/%{name}-%{version}/%{name}-%{version}_src.tar.xz
License:        GPLv2+
Group:          Graphics
#BuildRequires: qt4-devel qt-assistant-adp-devel qt4-assistant qtwebkit-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  cmake
BuildRequires:  pkgconfig(glew) >= 2.0.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  xmltex doxygen graphviz libxml2-devel
BuildRequires:  libgomp
#BuildRequires: python-devel python-sphinx
BuildRequires:  python3-devel python3-sphinx
BuildRequires:  environment-modules sip
BuildRequires:  doxygen
BuildRequires:  docbook-style-xsl
BuildRequires:  ftgl-devel
BuildRequires:  java-devel-openjdk lua
BuildRequires:  netpbm

%description
Tulip software is a system dedicated to the visualization of huge graphs.
It manages graphs with a number of elements (node and edges) up to 500.000 
on a personal computer (PIII 600, with 256mo). Its SuperGraph technology 
architecture enables to do the following things :

  * 3D visualizations
  * 3D modifications
  * Plug-in support for easy evolution
  * Building of clusters and navigation into it
  * Automatic drawing of graphs
  * Automatic clustering of graphs
  * Automatic selection of elements
  * Automatic Metric coloration of graphs

%package devel
Summary:        A library for handling large graphs
Group:          Development/Other
Requires:       %{name} = %version-%release

%description devel
A library for handling large graphs.
You need this package if you plan to build apps using
tulip libraries.

%package doc
Summary:        Tulip user documentation and developer Handbook
License:        LGPLv2
BuildArch:      noarch

%description doc
This package contains Tulip user documentation and developer Handbook in HTML.

%prep
%setup -q
sed -i -e '217d' -e '321d' library/tulip-python/src/ConsoleUtilsModule.cpp

%build
%cmake -DBUILD_DOC=on -DCMAKE_CXX_FLAGS="-fpermissive -fPIC" .
%cmake_build

%install
%cmake_install

%files
%{_bindir}/tulip
%{_bindir}/tulip_perspective
%{_datadir}/%{name}/apiFiles
%{_libdir}/lib*.so.*
%{_libdir}/tulip
#{_libdir}/python
%{_datadir}/tulip/bitmaps
%{_datadir}/applications/Tulip-5.4.0.desktop
%{_datadir}/icons/*.png
%{_datadir}/pixmaps/*.png
%{_datadir}/mime/packages/*.xml

%files devel
%{_includedir}/%{name}
%{_includedir}/%{name}2ogdf
%{_libdir}/cmake/TULIP
#{_datadir}/tulip/wizards
%{_bindir}/tulip-config
%{_libdir}/lib*.so

%files doc
%{_datadir}/doc/tulip
%{_datadir}/tulip/AUTHORS
%{_datadir}/tulip/COPYING.LESSER

%changelog
* Mon Aug 31 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 5.4.0
- Rebuilt for Fedora
* Mon Apr 02 2012 Alexandre Lissy <alissy@mandriva.com> 3.7.0-3
+ Revision: 788761
- Fixing installation path of python modules
- pushing release
- Putting platform-independant bitmaps in separate and platform-independant package
- Using %%{name} for python package name and not %%lib%%{name} -> python-lib64tulip0 becomes python-tulip
- fix: rpmlint flags useless provide on python-lib64tulip0
* Mon Apr 02 2012 Alexandre Lissy <alissy@mandriva.com> 3.7.0-1
+ Revision: 788719
- Fixing remote references to XSL with local ones.
- Adding java buildrequires for documentation building
- Adding buildrequires against python-sip
- Tulip 3.7.0 building
  Using icons and desktop file provided
  Building as "Ubuntu PPA" (correct install paths)
- Updating to tulip 3.7.0
  Introducing python binding
  Splitting doc in separate package
  Building doc from sources
  Managing .desktop file as source file
  Removing useless patches
  Adding gcc 4.7 specific patch
  Adding new buildrequires to follow those changes (qt4-assistant, python-devel, python-sphinx, doxygen, docbook-style-xsl, texlive-passivetex)
* Thu Oct 28 2010 Funda Wang <fwang@mandriva.org> 3.4.1-2mdv2011.0
+ Revision: 589709
- rebuild
* Thu Sep 30 2010 Funda Wang <fwang@mandriva.org> 3.4.1-1mdv2011.0
+ Revision: 582130
- should be 3.4.1
- new version 3.4.1
- BR qt-assistant-adp
* Sat Mar 13 2010 Funda Wang <fwang@mandriva.org> 3.3.1-1mdv2010.1
+ Revision: 518688
- new version 3.3.1
- add BR
* Sat Feb 27 2010 Funda Wang <fwang@mandriva.org> 3.3.0-1mdv2010.1
+ Revision: 512269
- New version 3.3.0
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
* Fri Jan 23 2009 Funda Wang <fwang@mandriva.org> 3.1.1-1mdv2009.1
+ Revision: 333094
- New version 3.1.1
* Fri Dec 26 2008 Olivier Thauvin <nanardon@mandriva.org> 3.1.0-1mdv2009.1
+ Revision: 319257
- install the pdf documentation
- 3.1.0
* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 3.0.1-2mdv2009.0
+ Revision: 269440
- rebuild early 2009.0 package (before pixel changes)
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
* Sat May 31 2008 Funda Wang <fwang@mandriva.org> 3.0.1-1mdv2009.0
+ Revision: 213663
- add conflicts with old packages
- move plugin manager to qt package
- clean file list
- more patches
- New version 3.0.1
  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Sun Jul 15 2007 Funda Wang <fwang@mandriva.org> 3.0.0-0.B6.1mdv2008.0
+ Revision: 52198
- fix file list
- use xdg menu
- BR qt4
- New version
