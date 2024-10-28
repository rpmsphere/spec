%undefine _debugsource_packages

Name: uxtank
Version: 2.3
Release: 14.4
Summary: A game of tank
Summary(de): uxTank ist ein Spiel bei dem man auf Panzer schießt, für Xwindow
Group: Games/Arcade
License: GPL
URL: https://ux.tank.googlepages.com/home
Source: https://ux.tank.googlepages.com/uxtank%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-core ImageMagick
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires: desktop-file-utils
BuildRequires: libX11-devel
BuildRequires: libXpm-devel

%description
uxTank is a game of tank shooting for X window.

%description -l de
uxTank ist ein Spiel bei dem man auf Panzer schießt, für Xwindow.

%prep
%setup -q -n %{name}%{version}
sed -i 's|-lSDL_mixer|-lSDL -lSDL_mixer|' Makefile

%build
make

%install
rm -rf %{buildroot}
%make_install
mv %{buildroot}/usr/games %{buildroot}/%{_bindir}

# icon
install -dm 755 %{buildroot}%{_datadir}/pixmaps
convert icons/uxTankIcon50.xpm -resize 48x48 %{name}.png
install -m 644 %{name}.png %{buildroot}%{_datadir}/pixmaps

# menu-entry
install -dm 755 %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=uxTank
Comment=uxTank is a game of tank shooting for Xwindows
Comment[de]=uxTank ist ein Spiel bei dem man auf Panzer schießt, für Xwindows
Exec=%{name}
Icon=%{name}
Categories=Game;ArcadeGame;
EOF

%files
%doc COPYING.TXT 
%{_bindir}/%{name}
%{_datadir}/%{name}*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}*.desktop

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3
- Rebuilt for Fedora
* Thu Feb 23 2012 Neal <nealbrks0 at gmail dot com> 2.3-1pclos2012
- process
* Thu Feb 23 2012 ghostbunny <hmhaase at pclinuxosusers dot de> 2.3-1pclos2012
- 2.3
- added german summary, description and comment in desktop file section
- added xz compression
- renamed spec file to pclos-uxtank.spec
* Mon Aug 18 2008 Slick50 <slick50@linuxgator.org> 2.0-1pclos2007
- Initial build
