# This should be pushed to nonfree because atomiks reuses the level design and graphics
# of the original Atomix game (with permission of the authors but not under a FLOSS license).
%undefine _debugsource_packages

Name:           atomiks
Version:        1.0.4.1
Release:        3
Summary:        A remake of the classic Atomix game for modern platforms
Group:          Games/Puzzles
License:        GPLv3+ and Nonfree
URL:            http://atomiks.sourceforge.net/
Source0:        https://downloads.sf.net/atomiks/%{name}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  icoutils
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(zlib)

%description
Atomiks is a faithful remake of, and a tribute to, Atomix, a classic puzzle
game created by Softtouch & RoSt and published in 1990 by the Thalion
Software company. Atomiks is free software, and shares no code with
the original Atomix game.

The Atomiks engine is released under the GNU GPL license, altough this
license does NOT apply to level design and graphics used by Atomiks, since
these remain the intellectual property of their authors, Softtouch & RoSt.

%prep
%setup -q
dos2unix readme.txt license.txt history.txt

# fix empty debugsourcefiles
sed -i 's|CFLAGS =|CFLAGS+=|' Makefile

%build
%make_build

%install
install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}

# Icon
install -d %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
icotool -x %{name}.ico -o %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Menu entry
install -d %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Atomiks
Comment=Remake and tribute to Atomix
Exec=%{name}
Icon=%{name}
Type=Application
Categories=Game;LogicGame;
EOF

%files
%doc readme.txt license.txt history.txt "atomiks-softtouch agreement.png"
%{_bindir}/atomiks
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%changelog
* Thu Sep 20 2018 umeabot <umeabot> 1.0.4.1-3.mga7
  (not released yet)
+ Revision: 1280099
- Mageia 7 Mass Rebuild
* Fri Apr 15 2016 akien <akien> 1.0.4.1-2.mga6.nonfree
+ Revision: 1002650
- Rebuild for Mageia 6
* Thu Feb 19 2015 akien <akien> 1.0.4.1-1.mga5.nonfree
+ Revision: 815942
- Version 1.0.4.1
* Wed Oct 15 2014 umeabot <umeabot> 1.03-3.mga5.nonfree
+ Revision: 744305
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 1.03-2.mga5.nonfree
+ Revision: 678027
- Mageia 5 Mass Rebuild
* Tue Jul 01 2014 akien <akien> 1.03-1.mga5.nonfree
+ Revision: 641710
- imported package atomiks
