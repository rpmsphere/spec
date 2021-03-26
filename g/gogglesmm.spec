Summary:	Goggles Music Manager
Name:		gogglesmm
Version:	1.2.1
Release:	1
Group:		Sound
License:	GPLv3
URL:		https://github.com/%{name}
Source0:	https://github.com/%{name}/%{name}/archive/%{name}-%{version}.tar.gz
#Patch0:	%%{name}-%%{version}-fix-alsa-plugin-linking.patch
BuildRequires:	libgcrypt-devel
#BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(fox17) >= 1.7.50
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(sqlite3) >= 3.6.19
BuildRequires:	pkgconfig(taglib) >= 1.9.0
BuildRequires:	pkgconfig(taglib-extras)
# Output support
BuildRequires:	pkgconfig(alsa) >= 1.0
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse) >= 0.9.21
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glew) >= 2.0.0
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(x11)
# Input support
#BuildRequires:	cdda-devel
BuildRequires:	pkgconfig(smbclient)
# Codec support
#BuildRequires:	libfaad2-devel
BuildRequires:	pkgconfig(flac) >= 1.2
#BuildRequires:	pkgconfig(mad) >= 0.15
BuildRequires:	pkgconfig(ogg) >= 1.0
BuildRequires:	pkgconfig(vorbis) >= 1.2
BuildRequires:	pkgconfig(opus) >= 1.0
BuildRequires:	pkgconfig(wavpack)
#BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	libepoxy-devel

%description
Goggles Music Manager is a music collection manager and player that 
automatically categorizes your music files based on genre, artist, album and
song. It supports gapless playback and features easy tag editing.

%prep
%setup -q
sed -i 's|unescape|FXString::unescape|' gap/ap_http_response.cpp
sed -i '29s|name|key|' src/gmutils.h
sed -i 's|decompose|FXString::decompose|' src/GMFilename.cpp
sed -i 's|universalTime("%T GMT",time)|universalTime(time,"%T GMT")|' src/GMPodcastSource.cpp
sed -i 's|\.value|.data|' src/GMTrackDatabase.cpp src/GMDBus.cpp
sed -i 's|localTime("%b %d, %Y",date)|localTime(date,"%b %d, %Y")|' src/GMTrackItem.cpp

%build
%cmake -DWITH_CFOX=OFF
make

%install
%make_install
%find_lang %{name}
desktop-file-edit --set-key="Categories" --set-value="AudioVideo;Audio;Player;" \
		  %{buildroot}%{_datadir}/applications/%{name}.desktop
%ifarch x86_64 aarch64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files -f %{name}.lang
%doc README ChangeLog AUTHORS COPYING
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libgap_*.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Sep 04 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.1
- Rebuild for Fedora
* Sun Apr 12 2015 Giovanni Mariani <mc2374@mclink.it> 0.14.2-1
- (f194c7e) Dropped faad support: it breaks build on ABF
