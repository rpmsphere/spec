%global debug_package %{nil}

Name:           chessx
Version:        1.5.0
Release:        1
Summary:        An Open Source chess database
License:        GPLv2
Group:          Games/Boards
URL:            http://chessx.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
BuildRequires:  gcc-c++
BuildRequires:  qt5-devel qt5-qttools
BuildRequires:	icoutils

%description
ChessX is an Open Source chess database. With ChessX you can operate on your
collection of chess games in many ways: browse, edit, add, organize, analyze, etc.

%prep
%setup -q
#sed -i '1i #include <QMetaType>' src/database/threadedguess.cpp
#sed -i -e 's|~4,|251,|' -e 's|~5,|250,|' -e 's|~1,|254,|' -e 's|~8,|247,|' -e 's|~10,|245,|' -e 's|~2|153|' src/database/bitboard.cpp
sed -i '27i #include <QButtonGroup>' src/dialogs/savedialog.cpp
sed -i '36i #include <QAction>' src/dialogs/preferences.cpp
sed -i '12i #include <QAction>' src/gui/gamewindow.cpp

%build
lrelease-qt5 %{name}.pro
qmake-qt5 %{name}.pro
make

%install
mkdir -p %{buildroot}%{_bindir}
install -m0755 release/chessx %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r data/* %{buildroot}%{_datadir}/%{name}
cp i18n/*.qm %{buildroot}%{_datadir}/%{name}/lang/

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
cp data/images/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=ChessX
Comment=Open Source chess database
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

%files
%doc COPYING ChangeLog
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Tue Jan 07 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.0
- Rebuild for Fedora
* Thu Dec 20 2012 dams <dams> 0.9.4-2.mga3
+ Revision: 332984
- add back icon (broken by last update)
* Mon Dec 17 2012 kamil <kamil> 0.9.4-1.mga3
+ Revision: 332147
- new version 0.9.4
* Sat Dec 01 2012 kamil <kamil> 0.9.2-2.mga3
+ Revision: 324365
- clean a bit .spec
* Fri Nov 16 2012 dams <dams> 0.9.2-1.mga3
+ Revision: 318925
- new version 0.9.2
- update buildrequire
- now use project icon instead of generic icon
- update specfile to enable i18n translations
* Mon Sep 19 2011 obgr_seneca <obgr_seneca> 0.8-1.mga2
+ Revision: 145389
- imported package chessx
* Sun Sep 18 2011 Kamil Rytarowski <n54@gmx.com> 0.8-1
- initial package for Mageia
- thanks to some guys at pacman for the inspiration taken from their spec file
