Name:           shotcut
Version:        17.04
Release:        1
Summary:        A free, open source, cross-platform video editor
License:        GPLv3+
Group:          Applications/Multimedia
URL:            http://www.shotcut.org/
Source0:        https://github.com/mltframework/shotcut/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	shotcut.desktop
Patch:		mlt_path.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(mlt++)
BuildRequires:  pkgconfig(mlt-framework)
BuildRequires:	qt5-qtwebsockets-devel
BuildRequires:  x264-devel
Requires:	qt5-qtquickcontrols
Requires:	qt5-qtgraphicaleffects
Requires:	qt5-qtmultimedia
Requires:       frei0r-plugins
Requires:       ladspa
Requires:       mlt
Requires:       lame
Requires:       ffmpeg

%description
Shotcut is a free and open-source cross-platform video editing application for
Windows, OS X, and Linux. 

Shotcut supports many video, audio, and image formats via FFmpeg and screen, 
webcam, and audio capture. It uses a timeline for non-linear video editing of 
multiple tracks that may be composed of various file formats. Scrubbing and 
transport control are assisted by OpenGL GPU-based processing and a number of 
video and audio filters are available.

%prep
%setup -q
%patch -p0

%build
qmake-qt5 'CONFIG-=c++11' \
          QMAKE_STRIP="" \
          PREFIX=%{buildroot}%{_prefix} \
          QMAKE_CFLAGS+="%{optflags}" \
          QMAKE_CXXFLAGS+="%{optflags}"

make V=1 %{?_smp_mflags}

%install
%make_install V=1
install -D icons/%{name}-logo-64.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
install -D --mode=644 %{S:1} %{buildroot}/usr/share/applications/shotcut.desktop
chmod a+x %{buildroot}/usr/share/shotcut/qml/export-edl/rebuild.sh

%files
%{_bindir}/shotcut
%{_datadir}/shotcut/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Apr 05 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 17.04
- Rebuilt for Fedora
* Wed Aug 24 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 16.08-1
- Updated
* Tue Jul 12 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 16.07-1
- Initial build
