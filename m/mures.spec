Name:           mures
BuildRequires:  SDL_image-devel SDL_net-devel SDL_ttf-devel 
URL:            http://mures.sourceforge.net/
License:        GPL v2 or later
Group:          Amusements/Games/Logic
AutoReqProv:    on
Version:        0.5
Release:        1
Summary:        A Multiplayer Puzzle Game
Source:         %{name}-%{version}.tar.bz2
Source1:        mures.desktop
Source2:        mures.png
Patch:          %{name}-%{version}.dif
Patch1:         %{name}-%{version}-gcc-warning.patch

%description
Mures is a cross-platform clone of Sega's "Chu Chu Rocket," a
multiplayer puzzle game. It is written in C using SDL. Multiplayer is
handled through a client-server design that supports multiple players
per client.

Authors:
--------
    Adam D'Angelo <dangelo@ntplx.net>

%prep
%setup -q
%patch
%patch1

%build
export LDFLAGS=-Wl,--allow-multiple-definition
CFLAGS="$RPM_OPT_FLAGS -lm" ./configure --prefix=/usr
make 

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
DATADIR=$RPM_BUILD_ROOT/usr/share/games/mures
rm -fr $DATADIR
install -d -m 755 $DATADIR
install -d -m 755 $DATADIR/images
install -d -m 755 $DATADIR/maps
install -d -m 755 $DATADIR/gui
install -d -m 755 $DATADIR/sounds
cp -a src/maps/[a-z]* $DATADIR/maps
rm -f $DATADIR/maps/*/Makefile*
cp -a src/images/*.ttf src/images/*.png src/images/*.ani src/images/*.Fonts $DATADIR/images
cp -a src/gui/*.png $DATADIR/gui
cp -a src/sounds/*.wav $DATADIR/sounds
cp -p src/*.lua $DATADIR
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/pixmaps/
install -m 0644 $RPM_SOURCE_DIR/mures.png $RPM_BUILD_ROOT/usr/share/pixmaps/mures.png
#%suse_update_desktop_file -i %name
mkdir %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
/usr/bin/mures
/usr/share/applications/*.desktop
/usr/share/games/mures
/usr/share/pixmaps/mures.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuild for Fedora
* Mon Oct 20 2008 - john@ossii.com.tw
- Rebuild for M6(OSSII)
* Sun Jul 15 2007 - coolo@suse.de
- BuildRequires SDL_ttf-devel
* Thu Jun 07 2007 - sbrabec@suse.cz
- Removed invalid desktop Category "Application" (#254654).
* Mon Mar 05 2007 - ssommer@suse.de
- BuildRequires SDL_net-devel
* Thu Feb 16 2006 - stbinner@suse.de
- fix XGD category .desktop file
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Jan 18 2006 - pnemec@suse.cz
- added desktop file and custom icon, fixed some gcc complains
* Sat Jan 10 2004 - adrian@suse.de
- build as user
* Sat Aug 16 2003 - adrian@suse.de
- install desktop file from kappfinder
* Mon Jun 16 2003 - coolo@suse.de
- use BuildRoot
* Wed Jun 12 2002 - uli@suse.de
- update -> 0.5 (fixes, better joystick support, more maps)
* Fri Feb 01 2002 - ro@suse.de
- changed neededforbuild <libpng> to <libpng-devel-packages>
* Tue Jan 22 2002 - ro@suse.de
- changed neededforbuild <kdelibs-artsd> to <kdelibs3-artsd>
* Fri Jan 11 2002 - ro@suse.de
- no subdirs in /usr/games
* Mon Aug 27 2001 - uli@suse.de
- update -> 0.4
  Added animation support.
  Altered collision detection to be compatible with dreamcast/gba
  puzzles.
  Altered cat speed/mouse speed ratio to be compatible with dreamcast/gba
  puzzles. Cat speed is now 2/3 mouse speed.
  Added puzzle mode.
  Added joystick support.
  Added support for wrapping from top to bottom / left to right in maps.
  Added directional creature images.
  Added a clock percentage bar.
* Tue Aug 07 2001 - uli@suse.de
- initial package
