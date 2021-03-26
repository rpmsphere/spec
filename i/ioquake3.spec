# Increase when packaging a newer snapshot
%define mainrel 12
%define date    20170428
# Increase when rebuilding the same snapshot
%define snaprel 3

Name:           ioquake3
Version:        1.36
Release:        %{mainrel}.%{date}.%{snaprel}
Summary:        Quake 3 Arena engine (ioquake3 version)
Group:          Games/Shooter
License:        GPLv2+
URL:            http://ioquake3.org/
# Snapshot from git repository: https://github.com/ioquake/ioq3
# - Strip thirdparty code:
# rm -rf code/{AL,jpeg-8c,libcurl-*,libogg-*,libspeex,libvorbis-*,opus-*,opusfile-*,SDL2,zlib}
# - Strip nonfree code (lcc) and binaries:
# rm -rf code/libs code/tools/lcc
Source0:        %{name}-%{date}.tar.xz
Source1:        %{name}-demo.sh
Source2:        %{name}.autodlrc
Source3:        %{name}.desktop
Source4:        %{name}.png
Source5:        %{name}-update.sh
Source6:        %{name}-update.autodlrc
Patch0: 	ioquake-1.36-CVE-2017-11721-buffer-overflow.patch

BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  nasm

# for quake3-update
Requires:       autodownloader 

%description
This package contains the enhanced opensource ioquake3 version of the Quake 3
Arena engine. This engine can be used to play a number of games based on this
engine, below is an (incomplete list):

* OpenArena, Free, Open Source Quake3 like game, recommended!
  (packagename: openarena)

* Urban Terror, gratis, but not Open Source FPS best be described as a
  Hollywood tactical shooter, a downloader and installer including an
  application menu entry is available in the urbanterror package.

* World of Padman, gratis, but not Open Source Comic FPS, a downloader and
  installer including an application menu entry is available in the
  worldofpadman package.

* Smokin' Guns, gratis, but not Open Source FPS, a semi-realistic simulation of 
  the "Old West's" great atmosphere, a downloader and installer including an
  application menu entry is available in the smokinguns package.

* Quake3 Arena, the original! A downloader and installer for the gratis, but
  not Open Source demo, including an application menu entry is available in
  the quake3-demo package.
  
  If you own a copy of quake 3, you will need to copy pak0.pk3 from the
  original CD-ROM and your q3key to /usr/libexec/quake3/baseq3 or ~/.q3a/baseq3.
  Also copy the pak?.pk3 files from the original 1.32 Quake 3 Arena point
  release there if you have them available or run quake3-update to download
  them for you.


%package demo
Summary:        Quake 3 Arena tournament 3D shooter game demo installer
Group:          Games/Shooter
Requires:       ioquake3 = %{version}-%{release}
Requires:       opengl-games-utils 
BuildArch:      noarch

%description demo
Quake 3 Arena tournament 3D shooter game demo installer. The Quake3 engine is
Open Source and as such is available as part of Mageia. The original Quake3
data files however are not Open Source and thus are not available as part of
Mageia. There is a gratis, but not Open Source demo available on the internet.

This package installs an application menu entry for playing the Quake3 Arena
demo. The first time you click this menu entry, it will offer to download and
install the Quake 3 demo datafiles for you.


%prep
%autosetup -p1 -n %{name}-%{date}

%build
%make_build \
  BUILD_CLIENT_SMP=1 \
  BUILD_GAME_SO=1 \
  BUILD_GAME_QVM=0 \
  DEFAULT_BASEDIR=%{_libexecdir}/%{name} \
  GENERATE_DEPENDENCIES=0 \
  OPTIMIZE="%{optflags}" \
  USE_CODEC_VORBIS=1 \
  USE_CODEC_OPUS=1 \
  USE_CURL=1 \
  USE_CURL_DLOPEN=0 \
  USE_INTERNAL_LIBS=0 \
  USE_LOCAL_HEADERS=0 \
  USE_OPENAL=1 \
  USE_OPENAL_DLOPEN=0 \
  VERSION="\\\"%{version} (git %{date}) [%{_vendor} %{release}]\\\""


%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_libexecdir}/%{name}/{baseq3,missionpack}

# ioquake3 binaries
pushd build/release-linux-*
install -m 755 %{name}.* %{buildroot}%{_bindir}/%{name}
install -m 755 ioq3ded.* %{buildroot}%{_bindir}/ioq3ded

install -m 755 renderer_opengl*.so %{buildroot}%{_libexecdir}/%{name}/
install -m 755 baseq3/*.so %{buildroot}%{_libexecdir}/%{name}/baseq3/
install -m 755 missionpack/*.so %{buildroot}%{_libexecdir}/%{name}/missionpack/
popd

# script to download the demo
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/ioquake3-demo
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}/

# script to install the latest patch
install -m 755 %{SOURCE5} %{buildroot}%{_bindir}/ioquake3-update
install -m 644 %{SOURCE6} %{buildroot}%{_datadir}/%{name}/

# desktop file and icons
install -D -m 644 misc/setup/%{name}.desktop \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 644 misc/quake3.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/quake3.svg
install -D -m 644 misc/quake3.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/quake3.png

%files
%doc md4-readme.txt opengl2-readme.md README.md voip-readme.txt
%license COPYING.txt id-readme.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-update
%{_bindir}/ioq3ded
%{_datadir}/%{name}/%{name}-update.autodlrc
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/quake3.png
%{_datadir}/icons/hicolor/scalable/apps/quake3.svg
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/baseq3/
%{_libexecdir}/%{name}/missionpack/
%{_libexecdir}/%{name}/renderer_opengl*.so

%files demo
%{_bindir}/%{name}-demo
%{_datadir}/%{name}/%{name}.autodlrc

%changelog
* Wed Mar 06 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.36-12.20170428.3
- Rebuild for Fedora
* Wed Oct 03 2018 pterjan <pterjan> 1.36-12.20170428.3.mga7
  (not released yet)
+ Revision: 1316246
- Mageia 7 Mass Rebuild
* Sat Jan 13 2018 mrambo3501 <mrambo3501> 1.36-12.20170428.2.mga7
+ Revision: 1192666
- added debian patch which fixes CVE-2017-11721 mga#21580
* Tue May 09 2017 akien <akien> 1.36-12.20170428.1.mga6
+ Revision: 1099843
- Git snapshot 20170428
  o Upstreams P2 and P3, also drop P1 and P4 which are Debian-specific
  o Fixes a crtical security vulnerability:
    https://ioquake3.org/2017/03/13/important-security-update-please-update-ioquake3-immediately/
- Build the game .so libraries, and put them in /usr/libexec/quake3
  o The .pk3 will now also be expected there, or in ~/.q3a as usual
- Now builds against SDL2 and Opus, removes Speex
- Cleanup build options, define meaningful version string
* Mon Feb 15 2016 umeabot <umeabot> 1.36-11.svn2102.5.mga6
+ Revision: 960693
- Mageia 6 Mass Rebuild
* Thu Oct 29 2015 tv <tv> 1.36-11.svn2102.4.mga6
+ Revision: 896519
- BR pkgconfig(speexdsp)
* Wed Oct 15 2014 umeabot <umeabot> 1.36-11.svn2102.3.mga5
+ Revision: 744275
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 1.36-11.svn2102.2.mga5
+ Revision: 680531
- Mageia 5 Mass Rebuild
* Sun Jun 22 2014 wally <wally> 1.36-11.svn2102.1.mga5
+ Revision: 638658
- rebuild for mga5
* Wed Jan 09 2013 malo <malo> 1.36-11.svn2102.mga3
+ Revision: 343797
- updated RPM group
* Fri Nov 16 2012 juancho <juancho> 1.36-10.svn2102.mga3
+ Revision: 318404
- Change group to new Games/Shooter
* Fri Mar 02 2012 juancho <juancho> 1.36-9.svn2102.mga2
+ Revision: 216696
- Removed Suggests for urbanterror, quake3-demo and worldofpadman
* Thu Dec 08 2011 juancho <juancho> 1.36-8.svn2102.mga2
+ Revision: 178837
- Added Smokin' Guns to the description.
- Removed unneeded patch
* Wed Dec 07 2011 juancho <juancho> 1.36-7.svn2102.mga2
+ Revision: 178420
- Fixed group for ioquake3-demo
- Added missing BuildRequires: desktop-file-utils
- Fixed group
- Replaced current spec with latest from Fedora (quake3-1.36-12.svn2102.fc17) and adapted it for Mageia to be used with other ioquake3 based games.
- Replaced current spec with latest from Fedora (quake3-1.36-12.svn2102.fc17) and adapted it for Mageia to be used with other ioquake3 based games.
* Sun Apr 17 2011 stormi <stormi> 1.36-6.mga1
+ Revision: 87417
- fix RPM group
* Thu Apr 14 2011 pterjan <pterjan> 1.36-5.mga1
+ Revision: 84816
- Re-upload after upload bug
* Wed Apr 13 2011 juancho <juancho> 1.36-4.mga1
+ Revision: 84716
- Fixed format of some lines, fixed group tags, removed BuildRoot and removed remaining Authors: lines
* Wed Apr 13 2011 tv <tv> 1.36-3.mga1
+ Revision: 84650
- description != authors file
* Wed Apr 13 2011 juancho <juancho> 1.36-2.mga1
+ Revision: 84450
- imported package ioquake3
