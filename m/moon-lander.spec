Name:           moon-lander
BuildRequires:  SDL_image-devel SDL_mixer-devel gcc-c++ 
BuildRequires:	mesa-libGL-devel
URL:            http://magigames.org/moonlander.html
License:        BSD 3-Clause
Group:          Amusements/Games/Action/Arcade
Version:        1.0
Release:        1
Summary:        A 2D Game of Gravity
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}-autopilot.tar.bz2
Source2:	%{name}.png
Patch0:         %{name}.dif
Patch1:         %{name}-destdir.patch
Patch2:         %{name}-overflow.patch
Patch3:         %{name}-makefile.patch
Patch4:         %{name}-autopilot.dif
Patch5:         %{name}-readme.patch

%description
Moon Lander is a 2D game of gravity.  Land your ship on the landing
pad. Do not go too fast or you will crash.

Authors:
--------
    David J. Blood <geekd@yahoo.com>
    Mike Heckman <mike@heckman.net>
    Ryan Daniels <pacmanfever@hotmail.com>
    Brian "Mo" Degenhardt <bmd@mp3.com>
    Garrett Banuk <mongoose@wpi.edu>

%prep
%setup -qn %{name} -b0 -a1
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3
%patch4 -p1
%patch5

%build
export RPM_OPT_FLAGS
make

%install
rm -rf $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
make install
pushd $RPM_BUILD_ROOT/usr/share/games/moon-lander
for file in `ls -1d *`; do
	if test "$file" != moon-lander.bin && test -f $file; then
		rm $file
	fi
done
popd

#Desktop
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF

[Desktop Entry]
Name=%{name}
Name[zh_TW]=登月者
Comment=Moon Lander is a 2D game of gravity. Land your ship on the landing pad. Do not go too fast or you will crash.
Comment[zh_TW]=降落太空船的速度如果太快，你就會炸死!請小心操作。
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Game;Amusements;Games;
EOF

#Icon
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.txt
%{_datadir}/games/moon-lander
%{_bindir}/moon-lander
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Mon Oct 20 2008 - john@ossii.com.tw
- Rebuild for M6(OSSII)
* Mon Sep 04 2006 - anosek@suse.cz
- added a flight director and simplified autopilot [#183259]
  (autopilot.tar.bz2, autopilot.dif, readme.patch)
* Wed Aug 23 2006 - anosek@suse.cz
- changed prefix /usr/X11R6 -> /usr
* Fri Jan 27 2006 - nadvornik@suse.cz
- fixed BuildRequires
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Oct 25 2005 - pnemec@suse.cz
- fixed makefile
* Tue May 10 2005 - meissner@suse.de
- fixed buffer overflow.
* Mon Jan 12 2004 - adrian@suse.de
- added %%defattr
* Mon Jun 16 2003 - coolo@suse.de
- use BuildRoot
* Tue Apr 16 2002 - ro@suse.de
- link using g++ (for SDL_mixer)
* Fri Feb 01 2002 - ro@suse.de
- changed neededforbuild <libpng> to <libpng-devel-packages>
* Fri Oct 26 2001 - ro@suse.de
- use neededforbuild aliases: SDL_devel-pakages, SDL_mixer-packages
* Thu Aug 23 2001 - uli@suse.de
- initial package
