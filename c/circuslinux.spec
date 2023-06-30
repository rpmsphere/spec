Name:         circuslinux
BuildRequires: SDL_image-devel SDL_mixer-devel desktop-file-utils
Summary:      A Clone of the Atari 2600 Game "Circus Atari"
Version:      1.0.3
Release:      1
License:      GPL
Group:        Amusements/Games/Action/Breakout
Source:       circuslinux-%{version}.tar.bz2
Source1:      %name.desktop
Patch:        circuslinux-%{version}.dif
URL:          https://www.newbreedsoftware.com/circus-linux/

%description
The object is to move a teeter-totter back and forth across the screen
to bounce clowns into the air. When they reach the top, they pop rows
of balloons, and then fall back down.

Authors:
--------
    Bill Kendrick <bill@newbreedsoftware.com>

%prep
%setup -q
%patch

%build
aclocal
automake --foreign -a
autoconf
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$CFLAGS" \
  ./configure --prefix=%{_prefix} i386-suse-linux
make

%install
%__rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install
find ${RPM_BUILD_ROOT}/%{_datadir}/%{name} -type f -exec chmod 644 {} \;
%__rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/circuslinux-*
%__mkdir_p $RPM_BUILD_ROOT/%{_datadir}/pixmaps
%__cp data/images/icon.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%name.png
%__mkdir_p %{buildroot}%{_datadir}/applications/
%__cp %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf ${RPM_BUILD_ROOT}

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%files
%{_bindir}/*
%{_datadir}/%{name}
%doc AUTHORS.txt COPYING.txt INSTALL.txt README.txt CHANGES.txt 
%doc FAQ.txt README-SDL.txt
%{_datadir}/applications/%name.desktop
%{_datadir}/pixmaps/%name.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuilt for Fedora
* Tue Oct 21 2008 Wind Win <yc.yan@ossii.com.tw>
- Rebuild for OSSII.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Sep  6 2005 nadvornik@suse.cz
- installed icon [#113919]
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Sun Aug 10 2003 sndirsch@suse.de
- added desktop file
* Tue May 27 2003 ro@suse.de
- remove unpackaged files from buildroot
* Tue Feb 26 2002 nadvornik@suse.cz
- fixed file pe%%__rmissions in /usr/share/circuslinux
* Fri Feb  1 2002 ro@suse.de
- changed neededforbuild <libpng> to <libpng-devel-packages>
* Tue Jan 22 2002 ro@suse.de
- changed neededforbuild <kdelibs-artsd> to <kdelibs3-artsd>
* Wed Nov  7 2001 nadvornik@suse.cz
- fixed to compile with new automake
- fixed neededforbuild for sound
* Wed Aug  8 2001 ro@suse.de
- changed neededforbuild <kdelibs kdelibs-devel> to <kdelibs-artsd>
* Wed Aug  8 2001 ro@suse.de
- changed neededforbuild <sdl> to <SDL>
- changed neededforbuild <sdl-devel> to <SDL-devel>
* Fri Jul 27 2001 nadvornik@suse.cz
- update to 1.0.3
* Wed Jun 20 2001 nadvornik@suse.cz
- added kdelibs and kdelibs-devel to neededforbuild
* Mon Mar 26 2001 ro@suse.de
- changed neededforbuild <sdl> to <sdl sdl-devel>
* Thu Mar 22 2001 nadvornik@suse.cz
- used suse_update_config
* Fri Mar  9 2001 ro@suse.de
- neededforbuild sdlmixer -> SDL_mixer
* Wed Feb 21 2001 nadvornik@suse.cz
- added alsa, alsa-devel to neededforbuild
* Fri Dec  1 2000 nadvornik@suse.cz
- new packages
