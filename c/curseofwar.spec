%define commit  47f7989
%define rel     3

Name:           curseofwar
Version:        1.2.0
Release:        1
Summary:        Fast-paced action strategy game with ncurses and SDL frontends
Group:          Games/Strategy
License:        GPLv3+
URL:            http://a-nikolaev.github.io/curseofwar/
Source0:        %{name}-%{version}-git%{commit}.tar.xz
Patch0:         curseofwar-1.2.0-mga-games-data-dir.patch
BuildRequires:  cmake
BuildRequires:  ImageMagick
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(sdl)

%description
Curse of War is a fast-paced action strategy game for Linux originally
implemented using a ncurses user interface. An SDL graphical version has
also been implemented more recently.

Unlike most RTS, you are not controlling units, but focus on high-level
strategic planning: Building infrastructure, securing resources,
and moving your armies.

%prep
%setup -q -n %{name}-%{version}-git%{commit}
%autopatch -p1

%build
%cmake
%make_build

%install
# Binaries
install -d %{buildroot}%{_bindir}
install -m755 %{name}* %{buildroot}%{_bindir}

# Tilesets for the SDL version
install -d %{buildroot}%{_datadir}/%{name}
cp -a images %{buildroot}%{_datadir}/%{name}/

# Man pages
install -d %{buildroot}%{_mandir}/man6
install -m644 %{name}.6     %{buildroot}%{_mandir}/man6/%{name}.6
install -m644 %{name}-sdl.6 %{buildroot}%{_mandir}/man6/%{name}-sdl.6

# Icons
install -d %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
convert pixmaps/%{name}-16x16.xpm %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
convert pixmaps/%{name}-32x32.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# Desktop entries
install -d %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Curse of War (ascii)
GenericName=Fast-paced action strategy game with ncurses frontend
Comment=Fast-paced action strategy game with ncurses frontend
Exec=%{name}
Icon=%{name}
Terminal=true
Type=Application
Categories=Game;StrategyGame;
EOF

cat << EOF > %{buildroot}%{_datadir}/applications/%{name}-sdl.desktop
[Desktop Entry]
Name=Curse of War (SDL)
GenericName=Fast-paced action strategy game with SDL frontend
Comment=Fast-paced action strategy game with SDL frontend
Exec=%{name}-sdl
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

%files
%doc CHANGELOG LICENSE README
%{_datadir}/applications/%{name}*.desktop
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}*.6*

%changelog
* Tue Nov 19 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora
* Sat Mar 19 2016 pterjan <pterjan> 1.2.0-1.47f7989.3.mga6
+ Revision: 992966
- Make it compatible with mass rebuild
* Fri Sep 11 2015 ovitters <ovitters> 1.2.0-1.47f7989.2.mga6
+ Revision: 877044
+ rebuild (emptylog)
* Sat Oct 04 2014 akien <akien> 1.2.0-1.47f7989.2.mga5
+ Revision: 736835
- Fix desktop file
- imported package curseofwar
