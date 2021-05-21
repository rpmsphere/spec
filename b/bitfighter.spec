Name:           bitfighter
Version:        019f
Release:        1
Summary:        A a free multi-player 2-D space combat game with Robotron-like controls
License:        GPL-2.0
Group:          Amusements/Games/Action/Arcade
URL:            http://bitfighter.org/
Source:         %{name}-%{version}.tar.gz
Source2:        %{name}.desktop
Source3:        %{name}.png
BuildRequires:  gcc-c++
BuildRequires:  libpng10-devel
BuildRequires:  libvorbis-devel
BuildRequires:  ncurses-devel
BuildRequires:  openal-soft-devel
BuildRequires:  readline-devel
BuildRequires:  speex-devel
BuildRequires:  SDL-devel
BuildRequires:  desktop-file-utils

%description
Bitfighter is a a free multi-player 2-D space combat game with Robotron-like controls. It's a 
team-based strategy game featuring retro vector graphics and customizable ships. It's fast, 
fun, and frenetic.

%prep
%setup -q
sed -i 's/png\.h/libpng10\/png.h/' zap/ScreenShooter.h

%build
cd build
%cmake ..
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}

cd exe
cp -a %{name} %{buildroot}%{_libdir}/%{name}
cp -a joystick_presets.ini %{buildroot}%{_datadir}/%{name}
cd -

cd resource
cp -a levels %{buildroot}%{_datadir}/%{name}
cp -a music %{buildroot}%{_datadir}/%{name}
cp -a sfx %{buildroot}%{_datadir}/%{name}
cp -a robots %{buildroot}%{_datadir}/%{name}
cp -a scripts %{buildroot}%{_datadir}/%{name}
cp -a editor_plugins %{buildroot}%{_datadir}/%{name}

cp -a bficon.bmp %{buildroot}%{_libdir}/%{name}
cd -

# create start-up script
%__cat > %{name}.sh <<EOF
#!/bin/bash

datadir="%{_datadir}/%{name}"
userdatadir="\$HOME/.bitfighter"
screenshotdir="\$userdatadir/screenshots"

## First time run
# create settings dir in users home directory and copy resources
if [ ! -d "\$userdatadir" ]; then
  mkdir "\$userdatadir"
  mkdir "\$userdatadir/screenshots"
  mkdir "\$userdatadir/music"
  cp -a "\$datadir/levels" "\$userdatadir/"
  cp -a "\$datadir/robots" "\$userdatadir/"
  cp -a "\$datadir/scripts" "\$userdatadir/"
  cp -a "\$datadir/editor_plugins" "\$userdatadir/"
  cp -a "\$datadir/music" "\$userdatadir/"
fi

## Upgrade specifics
# 015a
if [ ! -f "\$userdatadir/robots/s_bot.bot" ]; then
  cp "\$datadir/robots/s_bot.bot" "\$userdatadir/robots/"
fi

# 016
if [ ! -d "\$userdatadir/scripts" ]; then
  cp -a "\$datadir/scripts" "\$userdatadir/"
fi
if [ ! -d "\$userdatadir/editor_plugins" ]; then
  cp -a "\$datadir/editor_plugins" "\$userdatadir/"
fi
if [ ! -f "\$userdatadir/joystick_presets.ini" ]; then
  cp "\$datadir/joystick_presets.ini" "\$userdatadir/"
fi
if [ ! -f "\$userdatadir/levels/core.level" ]; then
  cp -f "\$datadir/levels/"* "\$userdatadir/levels/"
fi

# 017
if [ ! -f "\$userdatadir/music/menu.ogg" -o ! -f "\$userdatadir/music/game.ogg" ]; then
  cp -a "\$datadir/music" "\$userdatadir/"
  # Just once upgrade s_bot
  cp -f "\$datadir/robots/s_bot.bot" "\$userdatadir/robots/"
fi

# Run the program
cd %{_libdir}/%{name}
./bitfighter -rootdatadir "\$userdatadir" "\$@"
EOF

install -D -m 0755 %{name}.sh %{buildroot}%{_libdir}/%{name}/%{name}.sh
install -D -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png

ln -sf %{_libdir}/%{name}/%{name}.sh %{buildroot}%{_bindir}/%{name}
ln -s %{_datadir}/%{name}/sfx %{buildroot}%{_libdir}/%{name}/sfx

install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc doc/README.txt LICENSE.txt
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 019f
- Rebuilt for Fedora
* Wed Aug 01 2012 Kevin Chen <kevin.chen@ossii.com.tw>
- Rebuild for OSSII
* Wed May  9 2012 dbuck@novell.com
- Update to version 017b
* Tue May  1 2012 dbuck@novell.com
- Fix crash on 32-bit systems when playing music
* Sat Mar 31 2012 dbuck@novell.com
- Update to version 017a
* Fri Mar 30 2012 dbuck@novell.com
- Update to version 017
  * Cores altered significantly
  * First achievement implemented (25 flags)
  * Better idle handling of players
  * High scores menu and better help menus
  * Lots of bug fixes
* Sun Feb  5 2012 dbuck@novell.com
- Add patch bitfighter-fix-resource-dirs.diff
* Tue Jan 31 2012 dbuck@novell.com
- Update to version 016
* Mon Nov 21 2011 jengelh@medozas.de
- Remove redundant/unwanted tags/section (cf. specfile guidelines)
* Sun Nov 20 2011 seife+obs@b1-systems.com
- add patch to fix missing NULL declaration
* Sat Nov 13 2010 dbuck@example.com
- update to 013f
* Sun Oct 24 2010 dbuck@example.com
- update to 013e
* Mon Oct  4 2010 dbuck@example.com
- initial package release at 013b
