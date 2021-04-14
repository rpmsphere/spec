Name:           sdl-ball
Version:        1.01
Release:        11.4
Summary:        A Free/OpenSource brick-breaking game with pretty graphics
License:        GPL-3.0
Group:          Amusements/Games/Action/Breakout
URL:            http://sdl-ball.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         %{name}-makefile.patch
Patch1:         %{name}-dontstrip.patch
Patch2:         %{name}-gcc47.patch
BuildRequires:  mesa-libGL-devel
BuildRequires:  gcc-c++
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel

%description
SDL-Ball is a Free/OpenSource brick-breaking game with pretty graphics.
It is written in C++ using SDL and OpenGL. Features:
* 50 levels.
* OpenGL eye candy. (Nice graphics, really)
* Lots of powerups and powerdowns.
* Powerup Shop - You get special coins for collecting powerups, you can spend
  them on more powerups.
* Highscores.
* Sound.
* Easy to use level editor.
* Themes - Selectable from options menu. Themes support loading new gfx, snd
  and levels. A theme can be partial, if a file is missing, it will be loaded
  from the default theme. You can even mix between gfx,snd and level themes!
* Controllable with Mouse/Keyboard/Joystick and WiiMote.
* Save and Load games
* Cool Introscreen
* Screenshot function

%prep
%setup -q -n %{name}
%patch0
%patch1 -p1
%patch2 -p1
sed -i 's|cr,cg,cb,|cr,cg,cb|' main.cpp

%build
make clean
rm *.bin
export CFLAGS="%{optflags}"
make %{?_smp_mflags} PREFIX=%{_prefix} BINDIR=%{_bindir} DATADIR=%{_datadir}/%{name}/

%install
make DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} BINDIR=%{_bindir} DATADIR=%{_datadir}/%{name}/ install
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%doc README LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat Sep 29 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.01
- Rebuilt for Fedora
* Thu May 24 2012 joop.boonen@opensuse.org
- Created a gcc47 patch and a don't strip for debug patch
- Cleaned spec file up
* Sun Mar 25 2012 jengelh@medozas.de
- Parallel build with %%_smp_mflags; strip redundant spec sections
- Avoid service downloading a new tarball
* Tue Jul 14 2009 PVince81@yahoo.fr
- Changed installation paths
* Fri Jul  3 2009 PVince81@yahoo.fr
- Moved binary from /usr/bin to /usr/games
* Fri Jun 19 2009 PVince81@yahoo.fr
- Fixed libSDL build dependency
* Thu May 21 2009 PVince81@yahoo.fr
- fixed rpm description to be displayed properly in yast
* Sat May  9 2009 PVince81@yahoo.fr
- added missing RPM_OPT_FLAGS
* Wed May  6 2009 PVince81@yahoo.fr
- created package (version 1.01)
