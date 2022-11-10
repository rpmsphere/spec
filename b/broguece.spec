Name:           brogue
Version:        1.7.5
Release:        1
Summary:        Roguelike game that favors simplicity over complexity
Group:          Games/Arcade
License:        AGPL
URL:            https://sites.google.com/site/broguegame/
# Repacked from https://sites.google.com/site/broguegame/brogue-1.7.4-linux-amd64.tbz2
# without binaries: `rm -f brogue bin/brogue bin/libtcod.so.1`
# and fixed permissions: `find -type f -exec chmod 644 {} \;`
Source0:        %{name}-%{version}-repacked.tar.xz
Source1:        brogue-wrapper.sh
#Patch0:         brogue-1.7.4-mga-system-libtcod.patch
Patch1:         brogue-1.7.4-mga-hardcode-data-path.patch
Patch2:         brogue-1.7.5-compile-flags.patch
#Patch3:         brogue-1.7.4-libtcod-1.6.2.patch
Patch4:         brogue-1.7.5-static-libtcod-1.5.2.patch
# Current libtcod uses SDL2 and is not compatible with old brogue 1.7.4
# Used bundled libtcod 1.5.2 for now.
#BuildRequires:  pkgconfig(libtcod)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  unrtf
Provides:       bundled(libtcod) == 1.5.2

%description
Brogue is a direct descendant of Rogue, unlike other popular modern
roguelikes, and it favors simplicity over complexity, while trying
to ensure that the interactions between components will be interesting
and varied.

It is possible to play entirely with the keyboard or entirely with
the mouse or a combination of the two as the player chooses.

Brogue can be played either with a libtcod/SDL or a ncurses interface.
See `brogue --help' for more information.

%prep
%setup -q
%autopatch -p1

# sed -i \
#   -e 's,uint8,Uint8,g' \
#   -e 's,uint32,Uint32,g' \
#   src/platform/tcod-platform.c

%build
pushd src/libtcod-1.5.2
mkdir -p build/libtcod/release/png
%make_build libtcod.a
popd
%make_build both PREFIX=%{_prefix} LIBDIR=%{_libdir} OPTFLAGS="%{optflags}" LDFLAGS="%{optflags} -Wl,--allow-multiple-definition"

%install
# Launch game via a wrapper script and install binary in %%_libexecdir
install -D -m755 bin/%{name} %{buildroot}%{_libexecdir}/%{name}/%{name}
install -D -m755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# Install data files
install -d %{buildroot}%{_datadir}/%{name}
cp -a bin/fonts/ \
      bin/icon.bmp \
      bin/keymap \
      %{buildroot}%{_datadir}/%{name}/

# Icon and desktop entry
install -D -m644 bin/brogue-icon.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

install -d %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Brogue
GenericName=Roguelike
Comment=Brave the Dungeons of Doom!
Exec=%{name}
Icon=%{name}
Type=Application
Categories=Game;RolePlaying;
Terminal=false
EOF

# Prepare documentation
unrtf Readme.rtf > readme.html
mv readme readme.linux

%files
%doc readme.html readme.linux "Brogue seed catalog.txt"
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.5
- Rebuilt for Fedora
* Mon Oct 01 2018 akien <akien> 1.7.5-1.mga7
  (not released yet)
+ Revision: 1314060
- Version 1.7.5
- Build against bundled libtcod-1.5.2, not compatible with newer SDL2-based versions (mga#23471)
* Sat Sep 22 2018 umeabot <umeabot> 1.7.4-9.mga7
+ Revision: 1295682
- Mageia 7 Mass Rebuild
* Mon Jun 18 2018 wally <wally> 1.7.4-8.mga7
+ Revision: 1237890
- build using our compile flags
* Mon Jun 18 2018 wally <wally> 1.7.4-7.mga7
+ Revision: 1237885
- fix build
* Sun Jan 08 2017 akien <akien> 1.7.4-6.mga6
+ Revision: 1080639
- Patch 3: Fix build against libtcod 1.6.2
* Sat Oct 29 2016 akien <akien> 1.7.4-5.mga6
+ Revision: 1063939
- BR sdl even though libtcod itself uses sdl2
- Rebuild for libtcod 1.6.1
* Sat Apr 02 2016 pterjan <pterjan> 1.7.4-4.mga6
+ Revision: 997676
- Remove march=i586 from the Makefile
* Tue Feb 09 2016 umeabot <umeabot> 1.7.4-3.mga6
+ Revision: 950974
- Mageia 6 Mass Rebuild
* Thu Nov 27 2014 akien <akien> 1.7.4-2.mga5
+ Revision: 799583
- Brogue seed catalog.txt is a documentation file
* Thu Nov 27 2014 akien <akien> 1.7.4-1.mga5
+ Revision: 799562
- Add documentation
- imported package brogue
