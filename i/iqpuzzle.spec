Name:           iqpuzzle
Version:        1.2.3
Release:        1
Summary:        A diverting I.Q. challenging pentomino puzzle
Group:          Games/Puzzles
License:        GPLv3
URL:            https://github.com/ElTh0r0/iqpuzzle
Source0:        https://github.com/ElTh0r0/iqpuzzle/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
iQPuzzle is a diverting I.Q. challenging pentomino puzzle.
Pentominos are used as puzzle pieces and more than 300 different board shapes
are available, which have to be filled with them.

%prep
%autosetup

%build
%qmake_qt5 PREFIX=%{buildroot}%{_prefix}
%make_build

%install
%make_install
%find_lang %{name} --with-man

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/com.github.elth0r0.iqpuzzle.desktop
%{_datadir}/icons/hicolor/*/apps/iqpuzzle.png
%{_datadir}/icons/hicolor/scalable/apps/iqpuzzle.svg
%{_datadir}/metainfo/com.github.elth0r0.iqpuzzle.metainfo.xml
%{_datadir}/%{name}/
%{_mandir}/man6/iqpuzzle.6.*

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.3
- Rebuilt for Fedora
* Sat Mar 06 2021 kekepower <kekepower> 1.2.2-1.mga9
+ Revision: 1700264
- Update to version 1.2.2
* Thu Dec 17 2020 umeabot <umeabot> 1.2.1-2.mga8
+ Revision: 1658592
- Rebuild for new Qt5
* Sun Nov 29 2020 kekepower <kekepower> 1.2.1-1.mga8
+ Revision: 1650304
- Update to version 1.2.1
* Thu Mar 19 2020 daviddavid <daviddavid> 1.2.0-1.mga8
+ Revision: 1557910
- new version: 1.2.0
* Mon Feb 17 2020 umeabot <umeabot> 1.1.5-2.mga8
+ Revision: 1537517
- Mageia 8 Mass Rebuild
* Sun Nov 03 2019 kekepower <kekepower> 1.1.5-1.mga8
+ Revision: 1457357
- Update to version 1.1.5
* Sun Oct 20 2019 kekepower <kekepower> 1.1.4-1.mga8
+ Revision: 1454658
- Update to version 1.1.4
* Mon Sep 30 2019 kekepower <kekepower> 1.1.3-1.mga8
+ Revision: 1448480
- Update to version 1.1.3
* Sun Aug 18 2019 kekepower <kekepower> 1.1.2-1.mga8
+ Revision: 1429890
- Update to version 1.1.2
* Sat Mar 30 2019 umeabot <umeabot> 1.1.1-4.mga7
+ Revision: 1381937
- Qt5 Rebuild
* Sun Sep 23 2018 umeabot <umeabot> 1.1.1-3.mga7
+ Revision: 1298320
- Mageia 7 Mass Rebuild
* Wed May 16 2018 daviddavid <daviddavid> 1.1.1-2.mga7
+ Revision: 1229834
- port to Qt5
* Sun May 06 2018 kekepower <kekepower> 1.1.1-1.mga7
+ Revision: 1226831
- Update to version 1.1.1
* Sun Feb 04 2018 kekepower <kekepower> 1.1.0-1.mga7
+ Revision: 1198928
- imported package iqpuzzle
