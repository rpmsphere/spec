Name: maxishoot2
Summary: Kill as many enemies as you can
Version: 1.0.2
Release: 1
Group: Amusements/Games
License: GPLv3
URL: http://congelli.eu/prog_info_maxishoot2.html
Source0: http://congelli.eu/download/maxishoot2/%{name}-%{version}.tar.gz
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: compat-SFML16-devel
BuildRequires: boost-devel
BuildRequires: lua-devel

%description
Maxishoot2 is an improved rewrite of Maxishoot, a game that I published a
long time ago. Maxishoot2 is the same type of game as Maxishoot : that's a
"shoot them up" game in which the goal is to protect your base against enemy
missiles.

On the other hand, this new game doesn't share much with its ancestors. Indeed,
this new version contains a new design, some beautiful special effects based on
particles and new weapons and missiles. Moreover, Maxishoot2 uses a new type of
gameplay : now, you have to chose what part of your equipment you want to improve
(more life, new weapons, faster reload...). You choose !

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
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuild for Fedora
