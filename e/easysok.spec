Summary: sokoban game
Name: easysok
Version: 0.3.5
Release: 3
License: GPL
Group: Amusements/Games
URL: http://easysok.sourceforge.net/
Vendor: Ralf Schmelter
Source: http://dl.sf.net/easysok/%{name}-%{version}-kde3.tar.bz2
Source1: %{name}-%{version}.zh_TW.po
Patch: assert-include.patch
BuildRequires: gettext, libjpeg-devel
BuildRequires: libpng-devel, zlib-devel
BuildRequires: kdelibs3-devel, gcc-c++
BuildRequires: fam-devel
%{?el4:BuildRequires: libselinux-devel}
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}
Requires: kdelibs3

# Screenshot: http://easysok.sourceforge.net/snapshot1.png
# ScreenshotURL: http://easysok.sourceforge.net/screenshots.html

%description
Easysok is a sokoban game for KDE3. In sokoban you are a warehouse keeper
which has to push gems on their goals. The problem is, that the keeper can
only push one gem and there are walls which stand in his way. Sokoban was
originally invented in 1982 by Hiroyuki Imabayashi at the Japanese company
Thinking Rabbit, Inc.

%description -l nl
Easysok is een sokoban spel voor KDE3. In sokoban bent u een winkelier die
stenen moet duwen naar bepaalde plaatsen. U kan slechts 1 steen
tegelijkertijd bewegen en er zijn muren die in de weg staan. Sokoban is
uitgevonden door in 1982 door Hiroyuki Imabayashi in het Japans bedrijf
Thinking Rabbit, Inc.

%prep
%setup -q
sed -i 's|assert(index >= 0);|//assert(index >= 0);|' src/bookmarks.cpp
##%patch -p 1

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%{__make} install-strip DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_datadir}/applnk/Games/TacticStrategy/easysok.desktop %{buildroot}%{_datadir}/applications/easysok.desktop
echo -e 'Categories=Game;\nName[zh_TW]=KDE 倉庫番\nComment[zh_TW]=EasySok 倉庫番遊戲' >> %{buildroot}%{_datadir}/applications/easysok.desktop
mkdir -p %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES
msgfmt %{SOURCE1} -o %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES/easysok.mo
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/easysok.png %{buildroot}%{_datadir}/pixmaps/easysok.png

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS README THANKS TODO VERSION
%{_bindir}/easysok
%{_libdir}/easysok.*
%{_datadir}/applications/easysok.desktop
%{_datadir}/apps/easysok
%{_datadir}/doc/HTML/en/easysok
%{_datadir}/icons/*/*/apps/easysok.png
%{_datadir}/pixmaps/easysok.png
%{_datadir}/wallpapers/GreenBallThemeBackground.jpg
%{_datadir}/wallpapers/KSokobanThemeBackground.jpg
%{_datadir}/wallpapers/SpaceThemeBackground.png
%{_datadir}/wallpapers/WarehouseKeeperThemeBackground.jpg

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.5
- Rebuilt for Fedora
* Wed Jun  5 2011 Chris Lin <chris.lin@ossii.com.tw> 0.3.5-3.ossii
- Rename kdelibs to kdelibs3
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.5-2 - 4264/dries
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel
* Sat Jun 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.5-1
- Update to release 0.3.5.
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.3.3-1
- cleanup of spec file
- update to 0.3.3
* Sun Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 0.3.2-2
- completion of the spec file
* Sun Dec 7 2003 Dries Verachtert <dries@ulyssis.org> 0.3.2-1
- first packaging for Fedora Core 1
