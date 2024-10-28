Name:           audio-recorder
Version:        2.2.3
Release:        1
Summary:        Audio recorder application for the GNOME 3
License:        GPLv3+
Group:          Sound/Utilities
URL:            https://launchpad.net/audio-recorder
Source0:        %{name}_%{version}.tar.xz
Patch0:         audio-recorder-correct-desktop-menu.patch
BuildRequires:  intltool
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libpulse)
Requires:       gstreamer1-plugins-bad-free
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good

%description
Audio-recorder allows you to record your favourite music or audio to
a file. It can record audio from your system's soundcard,
microphones, browsers, webcams & more. Put simply: if it plays out of
your loudspeakers you can record it.

%prep
%setup -q -n %{name}
%patch 0 -p1

%build
%configure
make

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/*/%{name}*.svg
%{_datadir}/glib-2.0/schemas/org.gnome.audio-recorder.gschema.xml
%{_mandir}/man1/%{name}.*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.3
- Rebuilt for Fedora
* Sun Jun 21 2015 daviddavid <daviddavid> 1.6-1.mga6
+ Revision: 838275
- new version: 1.6-2
- add BuildRequires appindicator3-0.1 and gstreamer-pbutils-1.0
* Wed Oct 15 2014 umeabot <umeabot> 1.4-3.mga5
+ Revision: 744383
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 1.4-2.mga5
+ Revision: 678043
- Mageia 5 Mass Rebuild
  + tv <tv>
    - s/uggests:/Recommends:/
* Fri Jul 11 2014 daviddavid <daviddavid> 1.4-1.mga5
+ Revision: 651347
- imported package audio-recorder
