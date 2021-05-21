Name: bombehunter
Summary: A powerfull 2D game engine
Version: 1.5.4
Release: 1
Group: Amusements/Games
License: GPLv3
URL: http://congelli.eu/prog_info_bombehunter.html
Source0: http://congelli.eu/download/bombehunter/%{name}-%{version}.tar.gz
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: boost-devel
BuildRequires: compat-SFML16-devel
BuildRequires: lua-devel
BuildRequires: compat-lua-devel

%description
This game is made for two or one player(s). You are a super demining team.
The goal is to bring the bomb that the players transport to the exit of the
building. The bomb is launched between the players to progress in the levels
(warning, if the bomb hits a wall, you have to restart the level !

The two players go throw the level by exchanging their roles. Each player
chose a character and keeps its control during the game. The players exchange
the mouse (which need to be put between the two players) when they exchange
their roles.

%prep
%setup -q
cat > sfml.pc <<EOF
prefix=/usr
exec_prefix=\${prefix}
libdir=\${exec_prefix}/%{_lib}
includedir=\${prefix}/include/sfml1

Name: SFML
Description: Simple and Fast Multimedia Library
Version: 1.6
Requires: gl
Libs: -L\${libdir} -lsfml-graphics-1.6 -lsfml-system-1.6 -lsfml-window-1.6 -lsfml-network-1.6 -lsfml-audio-1.6 -lGLU -lGL
Cflags: -I\${includedir}
EOF
sed -i 's|LUA_GLOBALSINDEX|(-10002)|' src/luabind/include/luabind/object.hpp src/luabind/include/luabind/detail/call_function.hpp

%build
export PKG_CONFIG_PATH=.
ln -s /usr/include/sfml1/SFML src/SFML
%configure
make

%install
%make_install

%files
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/doc/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-icon.png

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.4
- Rebuilt for Fedora
