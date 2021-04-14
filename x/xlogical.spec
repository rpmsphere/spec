Name:           xlogical
BuildRequires:  SDL_image-devel SDL_mixer-devel gcc-c++ 
License:        GPL
Group:          Amusements/Games/Logic
Summary:        Puzzle Game
Version:        1.0.8
Release:        1
URL:            http://changeling.ixionstudios.com/xlogical/
Source:         http://changeling.ixionstudios.com/xlogical/downloads/xlogical-1.0-8.tar.bz2
Source1:        %{name}_gfx.tar.bz2
Source2:        %{name}.desktop
Source3:        %{name}.png
Patch0:         %{name}-%{version}-destdir.patch
Patch1:         %{name}-%{version}-gcc43.patch

%description
XLogical is a puzzle game based on an Amiga game developed by Rainbow
Arts called Logical.

Authors:
--------
    Tom Warkentin <tom@changeling.dynip.com>
    Neil Brown <nbrown@changeling.dynip.com>
    Sloane Muscroft <sloane@changeling.dynip.com>
    Andrew Carpenter (graphics)

%prep
%setup -q -n %{name}-1.0-8
%patch0
%patch1
cd images
tar xfj %{S:1}

%build
autoreconf -f -i
export CXXFLAGS="$RPM_OPT_FLAGS"
%configure \
    --bindir=%{_prefix}/games \
    --datadir=%{_datadir}/games \
    --localstatedir=%{_localstatedir}/games
make %{?jobs:-j%jobs}

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -D -m 0644 %{S:3} $RPM_BUILD_ROOT%{_datadir}/pixmaps/xlogical.png

# Install Desktop
mkdir -p  $RPM_BUILD_ROOT%{_datadir}/applications
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog README TODO NEWS LICENSE
%verify(not mode) %attr(0755,games,games) %{_prefix}/games/%{name}
%{_datadir}/games/%{name}
%dir %{_localstatedir}/games/%{name}
%attr(664,games,games) %{_localstatedir}/games/%{name}/xlogical.scores
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.8
- Rebuilt for Fedora
* Wed Oct 22 2008 john@ossii.com.tw
- Rebuild for M6(OSSII)
* Mon Sep 22 2008 cmorve69@yahoo.es
- update to 1.0-8
- fixes for gcc 4.3
* Wed Jun  6 2007 pgajdos@suse.cz
- using fdupes
* Thu Mar  9 2006 bk@suse.de
- Use explicit gcc-c++ in BuildRequires (was implicit by SDL-devel)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Nov 14 2005 anicka@suse.cz
- fix last patch
* Mon Nov  7 2005 anicka@suse.cz
- fix build in gamelogic.cpp
* Wed Oct 12 2005 ro@suse.de
- remove gtk from neededforbuild (unused)
* Tue Aug 30 2005 anicka@suse.cz
- add desktop icon (#113922)
* Wed Mar 16 2005 mcihar@suse.cz
- fix permissions (fixes bug #73025)
* Mon Dec 15 2003 mcihar@suse.cz
- fix for automake
- little cleanup
* Wed Oct 29 2003 mcihar@suse.cz
- package according to permissions.secure and add %%run_permissions
- no root for build
* Tue Oct 14 2003 mcihar@suse.cz
- moved to /usr/games
- files under /usr/share/games are owned by root:root
* Sun Aug 10 2003 sndirsch@suse.de
- added desktop file
* Sun Aug  4 2002 ro@suse.de
- group name changed "game" -> "games"
* Wed Jul 17 2002 mcihar@suse.cz
- new graphics by Andrew Carpenter
- moved game data (sound/graphics/levels) into /usr/share/games
- new URL
* Tue Apr 16 2002 ro@suse.de
- always apply axp-patch (for gcc-3.1)
- use LANG=CPLUSPLUS when checking for SDL_mixer in configure
* Fri Feb  1 2002 ro@suse.de
- changed neededforbuild <libpng> to <libpng-devel-packages>
* Fri Oct 26 2001 ro@suse.de
- use neededforbuild aliases: SDL_devel-pakages, SDL_mixer-packages
* Thu Aug 16 2001 ro@suse.de
- changed neededforbuild <smpeg> to <smpeg smpeg-devel>
* Wed Aug 15 2001 cihlar@suse.cz
- update to version 1.0-7
* Wed Aug  8 2001 ro@suse.de
- changed neededforbuild <sdl> to <SDL>
- changed neededforbuild <sdl-devel> to <SDL-devel>
* Wed Jun 20 2001 cihlar@suse.cz
- added kdelibs and kdelibs-devel to neededforbuild
* Tue Apr 10 2001 cihlar@suse.cz
- update to version 1.0-6
* Thu Apr  5 2001 cihlar@suse.cz
- fixed to compile on axp
* Mon Mar 26 2001 ro@suse.de
- changed neededforbuild <sdl> to <sdl sdl-devel>
* Mon Mar 12 2001 cihlar@suse.cz
- update to version 1.0-5
- fixed neededforbuild
* Mon Mar  5 2001 cihlar@suse.cz
- include dir /usr/include/gtk-1.2
* Wed Feb 21 2001 cihlar@suse.cz
- added alsa, audiofile and esound to neededforbuild
* Tue Dec 19 2000 cihlar@suse.cz
- fixed file permissions to levels
* Fri Dec  1 2000 cihlar@suse.cz
- fixed file permissions
* Wed Nov 29 2000 cihlar@suse.cz
- package created
