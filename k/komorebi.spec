Name: komorebi
Summary: A beautiful and customizable wallpapers manager for Linux
Version: 2.2.1
Release: 1
Group: system
License: Free Software
URL: https://github.com/cheesecakeufo/komorebi
Source0: https://github.com/Komorebi-Fork/komorebi/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gtk3-devel
BuildRequires: webkitgtk4-devel
BuildRequires: libgee-devel
BuildRequires: clutter-gtk-devel
BuildRequires: clutter-devel
BuildRequires: clutter-gst3-devel
BuildRequires: vala-devel
Requires: lato-fonts
Requires: vt323-fonts
Requires: gstreamer1-libav

%description
Komorebi is an awesome desktop manager for all Linux platforms. It provides
fully customizeable image and video wallpapers that can be tweaked at any time!

%prep
%setup -q
#sed -i -e 's|/System/Applications|/usr/bin|' -e 's|/System/Resources|/usr/share|' `find -type f`

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/fonts/AmaticSC-Regular.ttf
%{_datadir}/fonts/Bangers-Regular.ttf
%{_datadir}/fonts/BubblerOne-Regular.ttf
%{_datadir}/pixmaps/%{name}
%{_datadir}/metainfo/*
%exclude %{_datadir}/fonts/Lato-Hairline.ttf
%exclude %{_datadir}/fonts/Lato-Light.ttf
%exclude %{_datadir}/fonts/VT323-Regular.ttf

%changelog
* Sun Jun 26 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.1
- Rebuilt for Fedora
