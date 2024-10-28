Name:           madbomber
BuildRequires:  SDL_image-devel SDL_mixer-devel gcc-c++
#BuildRequires:  update-desktop-files
License:        GPL v2 or later
Group:          Amusements/Games/Action/Arcade
Summary:        A Clone of the Atari Game Kaboom!
Version:        0.2.5
Release:        1
URL:            https://www.newbreedsoftware.com/madbomber/
Source0:        madbomber-%{version}.tar.bz2
Source1:        %name.desktop
Patch0:         madbomber-%{version}-makefile.diff
Patch1:         %{name}-%{version}-permissions.diff
Patch2:         %{name}-%{version}-invalid-operation.diff

%description
Mad Bomber is a clone of Activision's classic Atari 2600 console game,
Kaboom!, by Larry Kaplan. It has spruced-up graphics, sound effects,
and music.

Authors:
--------
    Bill Kendrick <bill@newbreedsoftware.com>

%prep
%setup -q
%patch 0
%patch 1
%patch 2

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps 
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m 0644 data/images/icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc *.txt
/usr/bin/madbomber
/usr/share/games/madbomber
/usr/share/applications/%name.desktop
/usr/share/pixmaps/%name.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.5
- Rebuilt for Fedora
* Mon Oct 20 2008 john@ossii.com.tw
- Rebuild for M6(OSSII)
* Fri Dec 08 2006 anicka@suse.cz
- fix invalid operation
- build with $RPM_OPT_FLAGS
* Fri Jan 27 2006 nadvornik@suse.cz
- fixed BuildRequires
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Aug 29 2005 anicka@suse.cz
- add icon to desktop menu (#113657)
* Wed Jun 23 2004 hmacht@suse.de
- added # norootforbuild in specfile
- removed chown -R root command in Makefile
* Sun Jan 18 2004 ro@suse.de
- fix for chown syntax
* Sun Aug 10 2003 sndirsch@suse.de
- added desktop file
* Mon May 05 2003 mcihar@suse.cz
- updated to 0.2.5:
  * Now takes advantage of SDL_mixer's left/right stereo panning
  support.(For splashes and explosions.)
* Thu Feb 06 2003 mcihar@suse.cz
- updated to 0.2.4 (mostly small bugfixes add embdeded version)
* Tue Apr 16 2002 ro@suse.de
- link using g++ (for SDL_mixer)
* Fri Feb 01 2002 ro@suse.de
- changed neededforbuild <libpng> to <libpng-devel-packages>
* Fri Oct 26 2001 cihlar@suse.cz
- use neededforbuild aliases: SDL_devel-pakages, SDL_mixer-packages
* Thu Aug 16 2001 ro@suse.de
- changed neededforbuild <smpeg> to <smpeg smpeg-devel>
* Wed Aug 08 2001 ro@suse.de
- changed neededforbuild <sdl> to <SDL>
- changed neededforbuild <sdl-devel> to <SDL-devel>
* Wed Jun 20 2001 cihlar@suse.cz
- added kdelibs and kdelibs-devel to neededforbuild
* Mon Mar 26 2001 ro@suse.de
- changed neededforbuild <sdl> to <sdl sdl-devel>
* Mon Mar 12 2001 cihlar@suse.cz
- fixed neededforbuild
* Fri Mar 09 2001 ro@suse.de
- neededforbuild sdlmixer -> SDL_mixer
* Wed Feb 21 2001 cihlar@suse.cz
- added alsa, audiofile and esound to neededforbuild
* Mon Dec 04 2000 cihlar@suse.cz
- package created
