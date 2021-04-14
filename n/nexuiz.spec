%undefine _debugsource_packages

Summary: Multiplayer, deathmatch oriented first person shooter
Name: nexuiz
Version: 2.5.2
Release: 1
License: GPLv2+
Group: Amusements/Games
URL: http://www.nexuiz.com/
# Source is custom, obtained with :
# wget http://downloads.sourceforge.net/nexuiz/nexuiz-252.zip
# unzip -j nexuiz-252.zip Nexuiz/sources/enginesource20091001.zip
Source: enginesource20091001.zip
# For the .ico extraction
BuildRequires: libX11-devel, alsa-lib-devel, desktop-file-utils
BuildRequires: mesa-libGL-devel libXext-devel libXxf86dga-devel
BuildRequires: libXxf86vm-devel SDL-devel libXpm-devel
# This is necessary as these libraries are loaded during runtime
# and therefore it isn't picked up by RPM during build
Requires: zlib libvorbis libjpeg curl
Requires: desktop-file-utils >= 0.9
Requires: nexuiz-data = %{version}
Requires: opengl-games-utils
BuildRequires: desktop-file-utils

%description
Nexuiz is a fast-paced, chaotic, and intense multiplayer first person shooter, 
focused on providing basic, old style deathmatches.

%package server
Group: Amusements/Games
Summary: Dedicated server for the Nexuiz first person shooter
Requires: nexuiz-data = %{version}
# This is necessary as these libraries are loaded during runtime
# and therefore it isn't picked up by RPM during build
Requires: zlib curl

%description server
Nexuiz is a fast-paced, chaotic, and intense multiplayer first person shooter, 
focused on providing basic, old style deathmatches.

This is the nexuiz dedicated server required to host network games.

%prep
%setup -q -n darkplaces
%{__sed} -i 's/\r//' darkplaces.txt
%{__sed} -i 's,/usr/X11R6/,/usr/,g' makefile makefile.inc
%{__sed} -i 's,-Wall,-Wall -Wno-error,g' makefile.inc

%build
export DP_FS_BASEDIR=%{_datadir}/nexuiz
make cl-nexuiz sv-nexuiz sdl-nexuiz STRIP=:

%install
%{__rm} -rf %{buildroot}

# Install the main programs
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 0755 nexuiz-glx \
        %{buildroot}%{_bindir}/nexuiz-glx
%{__install} -m 0755 nexuiz-sdl \
        %{buildroot}%{_bindir}/nexuiz-sdl
%{__install} -m 0755 nexuiz-dedicated \
        %{buildroot}%{_bindir}/nexuiz-dedicated

# Create the desktop file
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Nexuiz
Comment=Multiplayer, deathmatch oriented first person shooter
Encoding=UTF-8
Icon=nexuiz
Exec=nexuiz-sdl-wrapper
Terminal=false
Type=Application
EOF

# Install the desktop file
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor=fedora \
    --dir %{buildroot}%{_datadir}/applications \
    --add-category ActionGame \
    --add-category Game \
    %{name}.desktop

%{__install} -D -m 0644 nexuiz.xpm %{buildroot}%{_datadir}/pixmaps/nexuiz.xpm

ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-sdl-wrapper

%post
update-desktop-database %{_datadir}/applications 2>/dev/null || :
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor 2>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications 2>/dev/null || :
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor 2>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%doc COPYING darkplaces.txt
%{_bindir}/nexuiz-glx
%{_bindir}/nexuiz-sdl
%{_bindir}/%{name}-sdl-wrapper
%{_datadir}/pixmaps/nexuiz.xpm
%{_datadir}/applications/*%{name}.desktop

%files server
%doc COPYING darkplaces.txt
%{_bindir}/nexuiz-dedicated

%changelog
* Fri Jul 15 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.2
- Rebuilt for Fedora
* Tue Sep 02 2008 Jon Ciesla <limb@jcomserv.net> - 2.4.2-3
- Fix .desktop category, BZ 460785.
* Mon Jul 07 2008 Jon Ciesla <limb@jcomserv.net> - 2.4.2-2
- Fix debuginfo, BZ 454141.
* Mon May 19 2008 Jon Ciesla <limb@jcomserv.net> - 2.4.2-1
- New upstream release.
* Tue Apr 29 2008 Jon Ciesla <limb@jcomserv.net> - 2.4-1
- New upstream release.
- Dropped nostrip patch.
- Added libXpm-devel BR.
* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> - 2.3-4
- GCC 4.3 rebuild.
* Wed Oct 24 2007 Jon Ciesla <limb@jcomserv.net> - 2.3-3
- Add support for opengl-games-utils.
- Dropped X-Fedora from .desktop install.
* Tue Aug 21 2007 Jon Ciesla <limb@jcomserv.net> - 2.3-2
- License tag correction.
- Rebuild for f8.
* Tue Jun 19 2007 Jon Ciesla <limb@jcomserv.net> - 2.3-1
- Updated to 2.3
* Thu Mar 01 2007 Adrian Reber <adrian@lisas.de> - 2.2.3-1
- updated to 2.2.3
* Mon Dec 18 2006 Adrian Reber <adrian@lisas.de> - 2.2.1-1
- updated to 2.2.1 (#220034)
- fix for CVE-2006-6609, CVE-2006-6610
* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.1-2
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21
* Sun Sep 24 2006 Adrian Reber <adrian@lisas.de> - 2.1-1
- updated to 2.1
- removed basedir patch; now using a environment variable
* Mon Sep 18 2006 Adrian Reber <adrian@lisas.de> - 2.0-3
- rebuilt
* Mon Jun 26 2006 Adrian Reber <adrian@lisas.de> - 2.0-2
- it looks like upstream changed the sources without increasing
  the version but now it works like it is supposed to
- added curl to the requires because the binaries are looking for it
* Sat Jun 17 2006 Adrian Reber <adrian@lisas.de> - 2.0-1
- updated to 2.0 (#195612)
- the binary has once again be renamed from darkplaces* to nexuiz*
- the desktop file now launches the sdl binary
* Sun Mar 19 2006 Adrian Reber <adrian@lisas.de> - 1.5-3
- rebuilt
* Sun Mar 19 2006 Adrian Reber <adrian@lisas.de> - 1.5-2
- rebuilt
* Thu Mar 16 2006 Adrian Reber <adrian@lisas.de> - 1.5-1
- updated to 1.5
- enabled sdl binary
* Wed Nov 30 2005 Adrian Reber <adrian@lisas.de> - 1.2.1-3
- changes for modular X
* Wed Nov 30 2005 Adrian Reber <adrian@lisas.de> - 1.2.1-2
- changed requires to make it work on 64 bit platforms
  (thanks thl)
* Mon Sep 19 2005 Adrian Reber <adrian@lisas.de> - 1.2.1-1
- updated to 1.2.1
- icons and binaries are now being renamed from darkplaces* to nexuiz*
* Fri Sep 02 2005 Adrian Reber <adrian@lisas.de> - 1.2-2
- another try without smp_mflags
* Fri Sep 02 2005 Adrian Reber <adrian@lisas.de> - 1.2-1
- updated to 1.2
* Tue Aug 16 2005 Adrian Reber <adrian@lisas.de> - 1.1-2
- support building on RHEL4 (#165522)
* Sat Jul 09 2005 Adrian Reber <adrian@lisas.de> - 1.1-1
- added gtk-update-icon-cache to %%post and %%postun
- added desktop-file-utils as Requires({post,postun})
* Fri Jul  8 2005 Matthias Saou <http://freshrpms.net/> 1.1-0
- Update to 1.1.
- Split off the huge data, unfortunately requires using custom sources.
- Major spec file changes.
* Thu Jun 09 2005 Adrian Reber <adrian@lisas.de> - 1.0-2
- comments concerning the requires added
- better(???) descriptions
* Thu Jun 09 2005 Adrian Reber <adrian@lisas.de> - 1.0-1
- initial version
