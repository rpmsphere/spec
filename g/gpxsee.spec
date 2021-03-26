Name:           gpxsee
Version:        2.15
Release:        4.3
Summary:        GPX visualizing and analyzing tool
License:        GPL-3.0
Group:          Productivity/Graphics/Visualization
URL:            http://tumic.wz.cz/gpxsee
Source0:        GPXSee-%{version}.tar.gz
Source1:        gpxsee.desktop
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  qt5-linguist

%description
GPXSee is a Qt based tool for visualizing and analyzing GPX files.

%prep
%setup -q -n GPXSee-%{version}

%build
lrelease-qt5 gpxsee.pro
qmake-qt5 gpxsee.pro
make %{?_smp_mflags}

%install
install -d 755 %{buildroot}/%{_bindir}
install -d 755 %{buildroot}/%{_datadir}/applications
install -d 755 %{buildroot}/%{_datadir}/pixmaps
install -d 755 %{buildroot}/%{_datadir}/%{name}
install -m 755 GPXSee %{buildroot}/%{_bindir}/%{name}
install -m 644 pkg/maps.txt %{buildroot}/%{_datadir}/%{name}
install -m 644 icons/gpxsee.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
if [ -x /usr/bin/update-desktop-database ]; then
	/usr/bin/update-desktop-database > /dev/null || :
fi

%postun
if [ -x /usr/bin/update-desktop-database ]; then
	/usr/bin/update-desktop-database > /dev/null || :
fi

%files
%dir %{_datadir}/gpxsee
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Fri Jun 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.15
- Rebuild for Fedora
* Sat May 28 2016 tumic@cbox.cz
- Update to version 2.14
  * Added print support.
  * Many fixes & improvements in PDF export (e.g. map support).
* Tue May  3 2016 tumic@cbox.cz
- Update to version 2.13
  * Fixed broken opening of non-ASCII named files as program arguments.
  * File info in window title.
  * Persistent program settings.
* Thu Apr 14 2016 tumic@cbox.cz
- Update to version 2.12
  * Added fullscreen mode.
  * Polished GUI.
* Sat Apr  2 2016 tumic@cbox.cz
- Update to version 2.11
  * Added "clear tile cache" option.
  * Lots of minor bug fixes and enhancements.
* Fri Mar 25 2016 tumic@cbox.cz
- Update to version 2.10
  * Added heart rate graphs.
  * Polished GUI.
  * Redesigned map/POI data sources handling.
  * Lots of minor bug fixes and enhancements.
* Sun Mar 20 2016 tumic@cbox.cz
- Update to version 2.9
  * Added support for displaying waypoints.
  * Minor bug fixes and enhancements.
* Sun Mar  6 2016 tumic@cbox.cz
- Update to version 2.8
  * Improved POI files control.
  * Minor bug fixes and enhancements.
* Sat Feb 13 2016 tumic@cbox.cz
- Update to version 2.7
  * Added default map sources (OSM, Thunderforest).
  * Added support for POIs in GPX format.
  * Added support for GPX files with multiple tracks.
* Wed Feb  3 2016 tumic@cbox.cz
- Update to version 2.6
  * Added map scale info.
  * Improved PDF export.
* Sun Dec 20 2015 tumic@cbox.cz
- Update to version 2.5
  * Added support for imperial units.
  * Fixed track view resizing issues.
