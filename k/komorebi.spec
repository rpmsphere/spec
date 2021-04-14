Name: komorebi
Summary: A beautiful and customizable wallpapers manager for Linux
Version: 2.1
Release: 1
Group: system
License: Free Software
URL: https://github.com/cheesecakeufo/komorebi
Source0: https://github.com/iabem97/komorebi/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
sed -i -e 's|/System/Applications|/usr/bin|' -e 's|/System/Resources|/usr/share|' `find -type f`

%build
%cmake
make %{?_smp_mflags}

%install
%make_install

%files
%doc LICENSE README.md
%{_bindir}/*
%{_datadir}/Komorebi
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/wallpapercreator.desktop
%{_datadir}/fonts/AmaticSC-Regular.ttf
%{_datadir}/fonts/Bangers-Regular.ttf
%{_datadir}/fonts/BubblerOne-Regular.ttf
%exclude %{_datadir}/fonts/Lato-Hairline.ttf
%exclude %{_datadir}/fonts/Lato-Light.ttf
%exclude %{_datadir}/fonts/VT323-Regular.ttf

%changelog
* Mon Dec 23 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuilt for Fedora
