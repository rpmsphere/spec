%define _default_patch_fuzz 2

Name:           siren
Version:        0.9
Release:        1
Summary:        Text-Based Audio Player
License:        ISC
Group:          Productivity/Multimedia/Sound/Players
Patch1:         siren-ncurses.patch
URL:            http://www.kariliq.nl/siren/
Source:         http://www.kariliq.nl/siren/dist/siren-%{version}.tar.gz
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libao-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libmad-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  wavpack-devel

%description
Siren is a text-based audio player for UNIX-like operating systems. Various
aspects of Siren have been inspired by cmus. Siren is distributed under the ISC
licence.

Siren supports Ogg Vorbis, MP3, FLAC, WavPack, WAVE, AIFF and a few other file
formats. Playback is possible through sndio, PulseAudio, OSS, Sun audio and
libao. Siren has been tested on OpenBSD, NetBSD, FreeBSD and Linux.

%prep
%setup -q
%patch1 -p1

%build
CFLAGS="%{optflags}" \
./configure \
    prefix="%{_prefix}" \
    bindir="%{_bindir}" \
    mandir="%{_mandir}" \
    plugindir="%{_libdir}/%{name}" \
    debug=no \
    flac=yes \
    mad=yes \
    sndfile=yes \
    vorbis=yes \
    wavpack=yes \
    ao=yes \
    oss=yes \
    pulse=yes \
    sndio=no \
    sun=no

make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%doc CHANGES
%{_bindir}/siren
%{_mandir}/man1/siren.1*
%{_libdir}/siren

%changelog
* Thu Aug 08 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9
- Rebuild for Fedora
* Sat Oct  8 2016 aloisio@gmx.com
- Update to version 0.7
  * Add the ffmpeg input plug-in.
  * Add the pwd and reopen-output-plugin commands.
  * Add the library-format-alt, player-track-format-alt,
    playlist-format-alt and
    queue*format-alt options.
  * Add the filename format variable.
  * Add OpenBSD pledge(2) support.
  * Bind "i" to select-active-entry by default.
  * Support the (less standard) totaldiscs and totaltracks
    Vorbis comments.
  * Handle the "n/m" format in the discnumber and
    tracknumber Vorbis comments
    where "n" is the disc/track number and "m" is total
    number of discs/tracks.
  * Remove support for ao file output drivers. These are not
    very useful.
  * Fix various minor bugs.
  Siren 0.6 (2015*09-01):
  * Support bit depths other than 16.
  * Add the aac input plug-in.
  * Add the portaudio output plug-in.
  * Add the albumartist, comment, discnumber, disctotal and
    tracktotal metadata
    fields.
  * Update the metadata cache on start-up if the metadata
    cache file uses an
    older format.
  * Allow relative paths in playlists.
  * Handle CRLF newlines in playlists.
  * Remove the confirm command. It is not very useful.
    Instead let the delete-entry and quit commands ask for
    confirmation directly.
  * Remove the -p option of the command-prompt and
    search-prompt commands. It is
    not very useful.
  * Fix various minor bugs.
  Siren 0.5 (2015*03-04):
  * Add 256-colour support.
  * Add the mpg123 input plug-in.
  * Add the opus input plug-in.
  * Add the source command.
  * Build on OS X.
  * Fix various minor bugs.
  Siren 0.4 (2014*07-16):
  * Add the playlist view.
  * Add the load-playlist command.
  * Allow continued playback of all audio files in the
    browser view.
  * Add the -d flag to the update-metadata command to delete
    the metadata of non-existent tracks.
  * Remove the clear-history command and the
    max-history-entries and
    show*dirs-before-files options as they were not very
    useful.
  * Significantly reduce the time needed to load the library
    on start-up.
  * Do not silently remove unsupported and non-existent
    tracks from the library.
  * Let changes to output plug-in options take effect
    immediately.
  * Change the default key bindings that display views.
  * Fix various minor bugs.
  Siren 0.3.1 (2013*07-08):
  * Accommodate the build to flac 1.3.0.
  Siren 0.3 (2013*06-04):
  * Add the ALSA output plug-in.
  * Add the update-metadata command.
  * Rename the save-cache command to save-metadata for
    consistency.
  * Remove the clear-cache command. It is no longer possible
    to clear the metadata cache while Siren is running.
    To clear the metadata cache, remove the ~/.siren/metadata
    file.
  * Fix a buffer overflow in the format-string parser.
  * Fix a mutex deadlock.
  * Fix various minor bugs.
- Spec cleanup
- Refreshed siren-ncurses.patch
* Wed Nov  7 2012 pascal.bleser@opensuse.org
- fix ncurses patch for the feature detection to work properly,
  namely enabling screen resizing and proper background color in
  xterms; thanks to Tim van der Molen for the fix and the heads up
* Thu Oct 25 2012 pascal.bleser@opensuse.org
- initial version (0.2)
