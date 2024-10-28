%undefine _debugsource_packages
%define _disable_ld_no_undefined 1

Summary:        2D Fighting Game
Name:           paintown
Version:        3.6.0
Release:        1
License:        GPLv2+
Group:          Games/Arcade
URL:            https://paintown.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/paintown/paintown/%{version}/%{name}-%{version}.tar.bz2
Patch0:         paintown-3.6.0-static.patch
Patch1:         paintown-3.6.0-cmake-freetype.patch
BuildRequires:  cmake
BuildRequires:  ImageMagick
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
Requires: mpg123

%description
Paintown is a 2D engine for fighting games.
If you are looking for a side-scrolling, action packed game like you used
to play or if you are looking for an extensible engine to write your own game,
look no further. Paintown supports user created content through a mod system
and user defined functionality through scripting.

Warning! The game is buggy and requires some "magic moves" to play.
For example, with some langauges half of menu is blank...

Features
* Low CPU and GPU requirements
* Network play
* Dynamic lighting
* Joystick support
* mod/s3m/xm/it music modules
* Scripting with python
* M.U.G.E.N engine

%files
%doc README LEGAL LICENSE TODO scripting.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png

%prep
%setup -q
%patch 0 -p1
%patch 1 -p1
find data/ -type f -exec chmod 0644 {} \;
sed -i 's|-Wall|-Wall -fPIC -std=gnu++11|' CMakeLists.txt
sed -i '/TestForPythonEmbed/d' src/paintown-engine/script/CMakeLists.txt
sed -i '/error << /d' src/util/music-player.cpp

%build
LIBSUFFIX=$(echo "%{_lib}" | sed 's|^lib||')
mkdir build; cd build
cmake .. -DUSE_SDL=ON
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 build/bin/%{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -af data %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 data/menu/%{name}.png %{buildroot}%{_datadir}/pixmaps
convert data/menu/%{name}.png -resize 48x48 %{buildroot}%{_datadir}/pixmaps/%{name}.png

# wrapper script
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
exec %{_bindir}/paintown -d %{_datadir}/%{name}/data
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=PainTown
Comment=2D Fighting Game
Exec=%{name}
Icon=%{name}
Type=Application
Terminal=false
Categories=Game;ArcadeGame;
EOF

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.6.0
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3.6.0-5
- (d787b8e) MassBuild#1257: Increase release tag
