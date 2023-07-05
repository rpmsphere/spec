Name:			egoboo
Version:		2.7.7
Release:		1
Summary:		A top down graphical (3D) RPG in the spirit of Nethack
Group:			Amusements/Games/RPG
License:		GPL
URL:			https://home.no.net/egoboo/
Source0:		%{name}-source-%{version}.tar.gz
Source1:		%{name}.png
Patch0:		%{name}-shell.diff
BuildRequires:	mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf
BuildRequires:	enet-devel
BuildRequires:	desktop-file-utils
Requires:       %{name}-data = %{version}
Requires:		SDL_image
Requires:		SDL_mixer
Requires:		SDL_ttf

%description
Egoboo is a top down rpg in the spirit of Nethack and other games
of the Roguelike genre. It uses OpenGL graphics and will have
randomly generated maps and customizable characters. The objective
of the project is to bring the fun and depth of roguelike gameplay,
kicking and screaming, into the third dimension.

%prep
%setup -q -n %{name}-source-%{version}
%patch0 -p1
sed -i -e 's|enet_host_create( NULL, 1, 0, 0 )|enet_host_create( NULL, 1, 1, 0, 0 )|' -e 's|, NET_EGOBOO_NUM_CHANNELS|, 1, NET_EGOBOO_NUM_CHANNELS|' game/Client.c
sed -i 's|MAXPLAYER, 0, 0|MAXPLAYER, 1, 0, 0|' game/Server.c
sed -i 's/\r//g' game/change.log game/Egoboodoc.txt
iconv -f ISO-8859-1 -t UTF8 game/change.log > ChangeLog
sed -i -e 's|libexec/egoboo|egoboo/egoboo.bin|g' \
	game/%{name}.sh

%build
# We override ENET_OBJ and LDFLAGS to use the system enet
%__make -C game -f Makefile.unix \
	ENET_OBJ= \
	CFLAGS="$RPM_OPT_FLAGS `sdl-config --cflags` -DENET11 -Wno-format-security" \
	LDFLAGS="`sdl-config --libs` -lm -lSDL_ttf -lSDL_mixer -lSDL_image -lGL -lGLU -lenet -Wl,--allow-multiple-definition"

%install
%__install -dm 755 %{buildroot}%{_bindir}
%__install -m 755 game/%{name}.sh \
	%{buildroot}%{_bindir}/%{name}

%__install -dm 755 %{buildroot}%{_libdir}/%{name}
%__install -m 755 game/%{name} \
	%{buildroot}%{_libdir}/%{name}/%{name}.bin

%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE1} \
	%{buildroot}%{_datadir}/pixmaps

%__cat > %{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Egoboo
Name[zh_TW]=依葛堡傳說
Comment=A top down graphical (3D) RPG in the spirit of Nethack
Comment[zh_TW]=Egoboo 一個類似薩爾達傳說的3D立體RPG遊戲
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;RolePlaying;
EOF

desktop-file-install \
        --vendor fedora \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --add-category Game \
        --add-category RolePlaying \
        %{name}.desktop

%clean
%__rm -rf %{buildroot}

%files
%doc ChangeLog game/Egoboodoc.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/%{name}.bin
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.7
- Rebuilt for Fedora
* Fri Oct 31 2008 Wind <yc.yan@ossii.com.tw> - 2.7.7-0.1
- Rebuild for OSSII.
* Fri May 09 2008 Toni Graffy <toni@links2linux.de> - 2.7.7-0.pm.1
- update to 2.7.7
* Sat Dec 29 2007 Toni Graffy <toni@links2linux.de> - 2.7.5-0.pm.1
- update to 2.7.5
- new linux-patch from Hans de Goede
* Fri Oct 26 2007 Toni Graffy <toni@links2linux.de> - 2.4.4b-0.pm.1
- update to 2.4.4b
* Mon Oct 08 2007 Toni Graffy <toni@links2linux.de> - 2.4.3-0.pm.1
- initial build for packman
- spec adapted from Fedora package
* Sat Oct  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.4.3-1
- Initial Fedora package
