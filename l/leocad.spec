Name:    leocad
Version: 19.07.1
Release: 1
Summary: Visual brick construction tool for kids
Summary(ru_RU): Детский конструктор, использующий блоки с шипами
License: GPLV2+
URL:     http://www.leocad.org
Source0: https://codeload.github.com/leozide/leocad/tar.gz/v%{version}#/%{name}-%{version}.tar.gz
Group:   Games/Puzzles
BuildRequires: qt4-devel
Requires: leocad-data

%description 
LeoCAD is a CAD program that uses bricks similar to those found in many toys
(but they don't represent any particular brand). Currently it has a library
of more than 1000 different pieces. LEGO is a trademark of the LEGO Group of
companies which does not sponsor, authorize or endorse this software.

%description -l ru_RU
LeoCAD -- программа для конструирования чего
угодно из блоков с шипами. В прилагаемой
библиотеке таких блоков содержится более
1000 различных видов. Блоки похожи на те,
что используются некоторыми фирмами,
производящими разборные игрушки. LEGO --
торговая марка группы компаний LEGO, которые
не спонсируют и не курируют LeoCAD, а также
не имеют авторских прав на эту программу.

%prep
%setup -q

%build
%qmake_qt4
make

%install
make install INSTALL_ROOT=%{buildroot}

%files
%_bindir/*
%_datadir/pixmaps/%name.png
%_mandir/man1/%name.*
%_datadir/applications/%name.desktop
%_datadir/doc/%name
%_datadir/icons/hicolor/scalable/mimetypes/application-vnd.%name.svg
%_datadir/mime/packages/%name.xml
%_datadir/metainfo/leocad.appdata.xml

%changelog
* Wed Sep 11 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 19.07.1
- Rebuilt for Fedora
* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.75-alt5.2
- Rebuilt with libpng15
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.75-alt5.1
- Fixed build
* Wed May 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.75-alt5
- fixed build:  added libGL-devel to BR:
- .desktop file cleanup
* Sun Mar 27 2011 Igor Vlasenko <viy@altlinux.ru> 0.75-alt4.1
- completely useless work (thanks to at@)
* Mon Mar 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.75-alt4
- added libpng-devel to BuildRequires: (thanks to at@)
* Tue Sep 21 2010 Fr. Br. George <george@altlinux.ru> 0.75-alt3
- [Igor Vlasenko] updated source from 0.75 branch (closes #22831)
* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.75-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for leocad
  * postclean-05-filetriggers for spec file
* Mon May 25 2009 Fr. Br. George <george@altlinux.ru> 0.75-alt2
- GCC4.4 build fixup
* Sun Oct 07 2007 Fr. Br. George <george@altlinux.ru> 0.75-alt1
- Initial build for ALT
