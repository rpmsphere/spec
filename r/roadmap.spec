%undefine _debugsource_packages

Name:		roadmap
Version:	1.2.1
Release:	1
Group:		Sciences/Geosciences
License:	GPL
Summary:	GPS Tracker
URL:		https://roadmap.sourceforge.net/download.html
Source0:	https://downloads.sourceforge.net/roadmap/%{name}-%{version}-src.tar.gz
Source1:	https://downloads.sourceforge.net/roadmap/roadmap-1.2.0-wince-arm.cab
Source2:	demo_maps.tar.gz
Patch2:		roadmap-1.2.1-fix-paths.patch
Requires:	gpsd
BuildRequires:	shapelib-devel 
BuildRequires:	expat-devel
BuildRequires:  gtk2-devel
BuildRequires:  popt-devel

%description 
A navigation system that displays US street maps (from the US Census Bureau)
and tracks a vehicle using GPS. Specific areas can be displayed by selecting
a street address (street number & name, city, and state).
RoadMap can run on iPAQ and Zaurus.

%prep
%setup -q
%patch2 -p1 -b .paths
sed -i 's/VectorGraphics;Graphics;Viewer;/Utility;Geography;/' src/%{name}.desktop
tar zxvf %{SOURCE2}

%build
export LDFLAGS=-Wl,--allow-multiple-definition
cd src
make DESKTOP=GTK2 MODECFLAGS="$RPM_OPT_FLAGS -ffast-math -W -Wall -Wno-unused-parameter -DROADMAP_USE_SHAPEFILES -I%{_includedir}/libshp"

%install
rm -rf %{buildroot}
%makeinstall -C src \
    DESKTOP=GTK2 \
    DESTDIR=%{buildroot} \
    INSTALLDIR=/usr \
    desktopdir=%{buildroot}%{_datadir}/applications

install -m755 src/gtk2/gtkroadgps -D %{buildroot}%{_bindir}/roadgps
install -m755 src/gtk2/gtkroadmap -D %{buildroot}%{_bindir}/roadmap

install -m644 src/icons/roadmap-16.png -D %{buildroot}%{_datadir}/icons/mini/%{name}.png
install -m644 src/icons/roadmap-32.png -D %{buildroot}%{_datadir}/icons/%{name}.png
install -m644 src/icons/roadmap-48.png -D %{buildroot}%{_datadir}/icons/large/%{name}.png

cp demo_maps/* %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%doc README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/mini/%{name}.png
%{_datadir}/icons/%{name}.png
%{_datadir}/icons/large/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.1
- Rebuilt for Fedora
* Tue Sep 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-3mdv2010.0
+ Revision: 442804
- drop tautologic references to README in package description
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2.1-2mdv2010.0
+ Revision: 442754
- rebuild
* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 355117
- new version
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
  + Thierry Vignaud <tvignaud@mandriva.com>
    - auto convert menu to XDG
    - kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Pascal Terjan <pterjan@mandriva.org>
    - Import roadmap
* Thu Feb 16 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.10-5mdk
- Fix Group (thanks plg)
* Sat Dec 17 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.10-4mdk
- Add BuildRequires : popt-devel
* Thu Jun 16 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0.10-3mdk
- fix buildrequires
* Thu Jun 16 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0.10-2mdk
- fix hardcoded paths (P2)
- add usdir.rdm file
- require gpsd in stead of gps3d
* Thu Jun 16 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0.10-1mdk
- initial release (club request :)
