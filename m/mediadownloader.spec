Name:           mediadownloader
Version:        1.5.2
Release:        6.4
License:        GPL-3.0
Summary:        Google and YouTube Media Downloader
URL:            http://mediadownloader.cz.cc
Group:          Productivity/Networking/Web/Utilities
Source0:        http://download.sourceforge.net/googleimagedown/project/%{name}_%{version}-src.tar.gz
BuildRequires:  ghostscript-core ImageMagick
BuildRequires:  hicolor-icon-theme
BuildRequires:  libXtst-devel
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtNetwork)
BuildRequires:  pkgconfig(QtOpenGL)
BuildRequires:  pkgconfig(QtWebKit)
BuildRequires:  pkgconfig(QtXml)
BuildRequires:  pkgconfig(phonon)
Requires:       phonon-backend-gstreamer
#Recommends:     MPlayer
#Recommends:     ffmpeg
#Recommends:     libmp3lame
Provides:       google-image-downloader = %{version}
Obsoletes:      google-image-downloader < 1.3

%description
Mediadownloader is a software that lets you search, watch and download
items with Google Image and YouTube. Search results are displayed within
a mouse scrollable view, as well as mobile devices do.

%prep
%setup -q

%build
qmake-qt4 \
CONFIG+=release \
CONFIG-=debug \
QT+=phonon \
DEFINES+=PHONON_LIB \
QMAKE_CFLAGS+="%{optflags}" \
QMAKE_CXXFLAGS+="%{optflags}" \
QMAKE_STRIP=""
make %{?_smp_mflags}

%install
# Create correct desktop file.
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=mediadownloader
GenericName=Google and YouTube Media Downloader
GenericName[ru]=Загрузка картинок и видео из Google и YouTube
Type=Application
Exec=mediadownloader
Icon=mediadownloader
Categories=Network;FileTransfer;Qt;
Comment=Google Media and YouTube Downloader
Comment[ru]=Поиск и загрузка картинок и видео из Google и YouTube
Terminal=false
StartupNotify=true
EOF

make INSTALL_ROOT=%{buildroot} install

# Install CSSs and presets.
install -dm 0755 \
%{buildroot}%{_sysconfdir}/%{name}/{css,ffmpeg-presets}
install -m 0644 css/* \
%{buildroot}%{_sysconfdir}/%{name}/css
install -m 0644 ffmpeg-presets/* \
%{buildroot}%{_sysconfdir}/%{name}/ffmpeg-presets

# Install icons of various sizes.
install -Dm 644 icons/%{name}.png \
%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
for size in 96x96 64x64 48x48 32x32 22x22 16x16 ; do
install -dm 0755 \
%{buildroot}%{_datadir}/icons/hicolor/${size}/apps
convert -resize ${size} icons/%{name}.png \
%{buildroot}%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done

%files
%doc COPYING README.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%config %{_sysconfdir}/%{name}

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.2
- Rebuilt for Fedora
* Sun Apr 29 2012 lazy.kent@opensuse.org
- Use pkgconfig(*) as build dependencies.
- Removed check for unsupported openSUSE versions.
- Minor spec formatting.
* Tue Nov  1 2011 lazy.kent@opensuse.org
- Update to 1.5.2.
  + Now mplayer works as expected.
  + Added the option to download items within a directory named as
the item was searched with.
  + Added WebM Youtube video format support.
  + Fixed non fuctional changing video format while viewing video.
  + Fixed number of results when adding thumbs in most viewed, most
popular etc.
  + Fixed a crash using google suggest.
- Remove obsolete "clean" section.
* Sun Aug  7 2011 lazy.kent@opensuse.org
- update to 1.5.1
- install css and ffmpeg-presets
- requires phonon-backend
- recommends libmp3lame to extract audio
- corrected Summary and License tags
- use full URL for source
- added COPYING to docs
* Sun Feb 27 2011 lazy.kent@opensuse.org
- update to 1.5.0.1
- dropped obsolete patches
- requires phonon-backend-xine
* Sat Feb 26 2011 lazy.kent@opensuse.org
- update to 1.5.0
- removed qt44 patch - build requires Qt >= 4.5
- patch to disable check phonon capabilities (annoying window every
  program start)
- patch to fix not working file name parameter with spaces passed
  to ffmpeg
- build requires ImageMagick to convert and install different sizes
  of icons
- added optflags for qmake config
- don't strip binary
- recommends ffmpeg
* Mon Oct 25 2010 lazy.kent.suse@gmail.com
- update to 1.4.2
- added MPlayer to Recommends
* Wed Oct 13 2010 lazy.kent.suse@gmail.com
- update to 1.4.1.2
* Tue Sep 21 2010 lazy.kent.suse@gmail.com
- dropped translations patch (fixed upstream, no version change)
* Sun Sep 19 2010 lazy.kent.suse@gmail.com
- patch to fix missing Russian and Ukrainian translations
* Sat Sep 18 2010 lazy.kent.suse@gmail.com
- update to 1.4
- dropped phonon_include patch (fixed upstream)
- updated patch for Qt 4.4 compatibility
- new URL
* Sat Jul 24 2010 lazy.kent.suse@gmail.com
- update to 1.3.2
- corrected phonon include for different Qt versions compatibility
* Thu Jul  1 2010 lazy.kent.suse@gmail.com
- update to 1.3.1
* Wed Jun 30 2010 lazy.kent.suse@gmail.com
- update to 1.3
- package renamed from google-image-downloader to mediadownloader
- icon moved to icons/hicolor/128x128/apps
- added phonon-devel to BuildRequires
* Fri May  7 2010 lazy.kent.suse@gmail.com
- update to 1.2.3
* Mon Apr 12 2010 lazy.kent.suse@gmail.com
- update to 1.2.2
- dropped obsolete patches
- new icon
* Tue Mar 16 2010 lazy.kent.suse@gmail.com
- fixed search with Russian words
* Sat Mar 13 2010 lazy.kent.suse@gmail.com
- fixed compilation errors
* Sun Mar  7 2010 lazy.kent.suse@gmail.com
- initial package created
