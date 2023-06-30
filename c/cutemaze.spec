Name:           cutemaze
Version:        1.3.0
Release:        1
Summary:        Top-down maze game
Group:          Games/Puzzles
License:        GPLv3+
URL:            https://gottcode.org/%{name}/
Source0:        https://gottcode.org/%{name}/%{name}-%{version}-src.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  qt5-qttools
BuildRequires:  qt5-linguist

%description
CuteMaze is a simple, top-down game in which mazes are randomly
generated using one of a choice of several different algorithms.
You move the character through the maze while hunting for targets
(cheese, by default)—the game is won once all of these targets
have been picked up.

%prep
%setup -q

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc COPYING CREDITS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
#%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man6/%{name}.6*

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0
- Rebuilt for Fedora
* Thu Oct 20 2016 akien <akien> 1.2.0-1.mga6
+ Revision: 1062586
- Version 1.2.0
* Tue Feb 09 2016 umeabot <umeabot> 1.1.1-2.mga6
+ Revision: 951335
- Mageia 6 Mass Rebuild
* Wed Dec 17 2014 akien <akien> 1.1.1-1.mga5
+ Revision: 803789
- imported package cutemaze
