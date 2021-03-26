%global _name QMPlay2

Name:           qmplay2
Version:        15.05.30
Release:        1
License:        GPL-3.0
Summary:        A Qt based media player, streamer and downloader
URL:            http://qt-apps.org/content/show.php/QMPlay2?content=153339
Group:          Productivity/Multimedia/Video/Players
Source:         http://kent.dl.sourceforge.net/project/zaps166/%{_name}/%{_name}-src-%{version}.tar.bz2
BuildRequires:  libXv-devel
BuildRequires:  portaudio-devel
BuildRequires:  pkgconfig(QtCore)
#BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libass)
BuildRequires:  ffmpeg-devel
BuildRequires:  libvdpau-devel
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(taglib)
Requires:       youtube-dl

%description
%{_name} is a video player, it can play and stream all formats supported by
ffmpeg and libmodplug (including J2B). It has an integrated Youtube browser.

%package        kde-integration
Summary:        %{_name} KDE integration subpackage
Requires:       %{name}
Requires:       kde-workspace
BuildArch:      noarch

%description    kde-integration
Media playing actions for removable devices in KDE.

%package        devel
Summary:        %{_name} development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description    devel
It's a development package for %{_name}.

%prep
%setup -q -n %{_name}-src
sed -i 's|headers|headers /usr/include/ffmpeg|' src/qmplay2/qmplay2.pro src/modules/*/*.pro

%build
NOTERM=1 SYSTEM_BUILD=1 ./compile_unix `echo "%{?_smp_mflags}" | grep -o '[0-9]*'`

%install
mkdir -p %{buildroot}%{_prefix}
cp -R app/* %{buildroot}%{_prefix}

# Setting libs to system libdir instead of 'lib'.
%if "%{_lib}" == "lib64"
mv %{buildroot}/%{_prefix}/{lib,lib64}
%endif

# Don't package binary modules in datadir.
mkdir -p %{buildroot}%{_libdir}/%{_name}
mv %{buildroot}/%{_datadir}/qmplay2/modules/*.so %{buildroot}%{_libdir}/%{_name}
rm -rf %{buildroot}/%{_datadir}/qmplay2/modules
ln -s %{_libdir}/%{_name} %{buildroot}/%{_datadir}/qmplay2/modules

# Deleting useless links.
rm -rf %{buildroot}/%{_datadir}/icons/hicolor
# Setting icon to 'pixmaps' instead of 'icons'.
mv %{buildroot}/%{_datadir}/{icons,pixmaps}


%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING TODO
%{_bindir}/%{_name}
%{_libdir}/%{_name}
%{_libdir}/libqmplay2.so.*
%{_datadir}/applications/%{_name}*.desktop
%{_datadir}/pixmaps/%{_name}.png
%{_datadir}/qmplay2

%files kde-integration
%{_datadir}/kde4/apps/solid/actions/*.desktop

%files devel
%{_libdir}/libqmplay2.so
%{_includedir}/%{_name}

%changelog
* Thu Jun 04 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 15.03.30
- Rebuild for Fedora
* Mon Dec 29 2014 dap.darkness@gmail.com
- Update to 14.12.28 (changes since 14.12.23):
  * fixed fonts loading from folders with subtitles
    (not recursively);
  * the main toolbar can be split out from the main window;
  * fixed crash if built with AVResample;
  * fixed names displaying at YouTube playlist;
  * minor bug fixing.
* Sat Dec 27 2014 dap.darkness@gmail.com
- Update to 14.12.23 (changes since 14.12.01):
  * fixed playing stopping during operation `youtube-dl`,
    as well as with protocols other than HTTP and HTTPS;
  * ability to rewind streams network without reconnecting to the server;
  * Support MPRIS2 songs titles, even if they do not contain a header;
  * removed the ability to upgrade in systems other than Windows;
  * automatic program updates `youtube-dl`;
  * minor fixes search in YouTube;
  * added cache for a class of parameters;
  * improved caching.
* Tue Dec  2 2014 dap.darkness@gmail.com
- Update to 14.12.01 (changes since 14.10.07):
  * subtitles fonts loading from the directory,
    that provides ASS/SSA subtitles;
  * added "User-Agent" for HTTP connections
    (ProstoPleer working again);
  * minor bug fixing.
* Tue Oct  7 2014 dap.darkness@gmail.com
- Update to 14.10.07 (changes since 14.07.27):
  * the action of ASS subtitles restoring
    from Matroska container in FFMpeg 2.4.x;
  * metadata changes support for using FFMpeg 2.4.x;
  * saving equalizer settings video;
  * added to the playlist directories sorting;
  * improved work with YouTube;
  * added support for pleer.com;
  * improved OpenGL operation;
  * bug fixes.
* Mon Jul 28 2014 dap.darkness@gmail.com
- Update to 14.07.27 (changes since 14.03.05):
  * icons can be loaded from the system icon set;
  * added new icons,
  * any video site support through via `youtube-dl`;
  * noise, sharpness, and levels of zoom filters support in VDPAU;
  * ability to block widgets
    (removes the header row and blocks the toolbar);
  * ability to load modules from a directory settings
    (about/.qmplay2/Modules);
  * ability to customize colors and Wallpaper (as in QMPlay1);
  * reading/recording-playing improvements;
  * changed the way to save window position;
  * thread switching was improved;
  * MPRIS2 support;
  * image files, OGG support;
  * minor fixes in HttpReader;
  * VDPAU improvement;
  * service HTTPS improvement;
  * other small changes;
  * bug fixes.
* Thu Mar  6 2014 dap.darkness@gmail.com
- Update to 14.03.05 (changes since 14.02.17):
  * Improvement of the functionality of the YouTube
    service in the framework of the program "youtube-dl"
    (the path must be entered in the options);
  * The name of the disk AudioCD appears as an album;
  * OSD update bug was fixed;
  * Tags editing bug was fixed.
* Mon Feb 17 2014 dap.darkness@gmail.com
- Update to 14.02.17 (changes since 14.01.10):
  * CDDB database support was added;
    (freedb.org, freedb.musicbrainz.org);
  * Tags could be edited via taglib library;
  * Various issues associated with VAApi were fixed;
  * Fast switching tracks in AudioCD was implemented;
  * Minor bugs in FFDecSW were fixed;
  * Echo effect was added;
  * Minor fixes.
* Thu Jan 16 2014 dap.darkness@gmail.com
- Update to 14.01.10 (changes since 14.01.05):
  * Added support for algorithms that eliminates
    Intel VAApi card (VAEntrypointVideoProc);
  * Fixed a lot of VAApi errors;
  * Minor fixes in the code.
* Mon Jan  6 2014 dap.darkness@gmail.com
- Update to 14.01.05 (changes since 14.01.03):
  * Optional possibility of preview decoding through VDPAU;
  * Fixed building with the old version of alsa-lib;
  * The ability to playback in random order in the group;
  * Improved VAApi performance and stability;
  * Minor fixes in "VDPAU Writer.
* Fri Jan  3 2014 dap.darkness@gmail.com
- Update to 14.01.03 (changes since 13.12.15):
  * Method processParams () from "PrepareForHWBobDeint" was fixed;
  * Automatic search for the correct settings for sound;
  * Ability to add your own radio stations;
  * Improved modules ALSA and PortAudio;
  * Fixed a bug in ALSA plugin because of bad sound cards;
  * Added German translation (Daniel Meiß-Wilhelm);
  * "Playback setting" menu was fixed;
  * Possibility to save the skin;
  * Minor code fixes.
- pkgconfig(alsa) >= 1.0.26 became required to prevent build issue.
* Sun Dec 15 2013 dap.darkness@gmail.com
- Update to 13.12.15 (changes since 13.12.07):
  * Added ability to set the tabs at the top of the main window;
  * Added ability to select the audio channel in the Playback menu;
  * Restoration of validity HWAccel with FFMpeg 1.2;
  * Minor Bug fixes.
* Sun Dec  8 2013 dap.darkness@gmail.com
- Update to 13.12.07 (changes since 13.10.24):
  * Window will be opened automatically when the movie opens;
  * Shuffles play songs without repetitions;
  * Allows only one instance;
  * Bug fixes.
* Wed Oct 30 2013 dap.darkness@gmail.com
- Update to 13.10.24 (changes since 13.09.08):
  * actual number of frames per second representation;
  * OSD in DirectDraw improved;
  * LastFM support;
  * connections through a proxy server support;
  * display OSD in XVideo and DirectDraw improved;
  * hardware decoding via VDPAU added;
  * OSD display optimization;
  * ALSA module improved;
  * bug fixes.
- Spec-file was fixed up via `spec-cleaner`.
- KDE integration subpackage was added.
* Wed Sep 11 2013 fisiu@opensuse.org
- Update to 13.09.08 (changes since 13.08.18):
  * support SHOUTcast titles
  * ALSA output support
  * allow to setup decoders priority
  * new sound filter - phase reverse
  * fix WMA audio playback
  * fix video display using openGL and XVideo
  * many minor fixes
* Tue Sep  3 2013 obs@botter.cc
- add kdebase4-workspace to buildrequires to add KDE default action
* Sun Sep  1 2013 dap.darkness@gmail.com
- Initial build.
