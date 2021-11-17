Name:		navit
Summary:	Car navigation system with routing engine
Version:	0.5.6
Release:	1
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	http://www.navit-project.org/maps/osm_bbox_11.3,47.9,11.7,48.2.osm.bz2
Source2:	%{name}-0.2.0.zh_TW.po
Source3:        taiwan.navit.zip
Source4:	navit-fix-icons.zip
Patch0:         navit-0.2.0-freetype2.patch
Patch1:         navit-0.2.0-gpsd3.patch
Patch2:         navit-0.1.2-static_sample.patch
Group:		Applications/Productivity
License:	GPLv2
BuildRequires:	zlib-devel
BuildRequires:	gtk2-devel
BuildRequires:	fontconfig-devel
BuildRequires:	SDL_image-devel
BuildRequires:	libpq-devel
BuildRequires:	imlib2-devel
BuildRequires:	libXmu-devel
BuildRequires:	freeglut-devel
BuildRequires:	quesoglc-devel
BuildRequires:	python2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gd-devel
BuildRequires:	speech-dispatcher-devel
BuildRequires:	gpsd-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtsensors-devel
BuildRequires:	shapelib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	desktop-file-utils
# autopoint requires cvs to work
BuildRequires:	cvs
#Requires:	dejavu-sans-fonts
URL:		http://www.navit-project.org/

%description
Navit is a car navigation system with routing engine. Its modular
design is capable of using vector maps of various formats for routing
and rendering of the displayed map. It's even possible to use multiple
maps at a time.

The GTK+ or SDL user interfaces are designed to work well with touch
screen displays. Points of Interest of various formats are displayed
on the map.

The current vehicle position is either read from gpsd or directly from
NMEA GPS sensors.

The routing engine not only calculates an optimal route to your
destination, but also generates directions and even speaks to you.

%package graphics-qt
Summary:	Qt graphics renderer for Navit navigation system
Group:		Applications/Productivity
Requires:	%{name} = %{version}-%{release}

%description graphics-qt
Navit is a car navigation system with routing engine. This package
contains the Qt-QPainter graphics renderer for Navit. You need to
enable this renderer in /etc/navit/navit.xml or ~/.navit/navit.xml
to use it.

%package graphics-sdl
Summary:	SDL graphics renderer for Navit navigation system
Group:		Applications/Productivity
Requires:	%{name} = %{version}-%{release}

%description graphics-sdl
Navit is a car navigation system with routing engine. This package
contains the SDL graphics renderer for Navit. You need to enable
this renderer in /etc/navit/navit.xml or ~/.navit/navit.xml to use it.

%prep
%setup -q
#patch0 -p1
#patch1 -p1
#patch2 -p1 -b .static_sample
install -m 0644 %{SOURCE1} navit/maps
cp %{SOURCE2} po/zh_TW.po.in
unzip -o %{SOURCE4} -d navit/icons
sed -i 's/Liberation Sans/AR PL New Kai/' navit/navit_shipped.xml
sed -i 's/4808 N 1134 E/2503 N 12133 E/' navit/navit_shipped.xml
sed -i 's|gps_read(priv->gps);|gps_read(priv->gps,NULL,0);|' navit/vehicle/gpsd/vehicle_gpsd.c

%build
export LDFLAGS=-Wl,--allow-multiple-definition
#autoreconf -i
%cmake .
#configure --disable-gui-clutter --enable-graphics-gd --disable-graphics-qt-qpainter
%cmake_build 

%install
rm -rf %{buildroot}
#makeinstall
%cmake_install

# Don't need the README here
rm -f %{buildroot}%{_datadir}/%{name}/README

# Put the config file in /etc: upstream likes it in /usr to be
# relocatable, but that doesn't concern us. The code does check
# in /etc, so we don't need a patch - AdamW 2009/01
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/%{name}.xml %{buildroot}%{_sysconfdir}/%{name}/%{name}.xml

# Create a README.Fedora - AdamW 2009/01
cat > README.Fedora << EOF 
Navit comes with a sample map of Munich, but if you live (or drive!)
anywhere else, you'll need to add another map set. These are not
available as packages because they're rather large and the data changes
on a daily basis, so the packages would have to be refreshed very
often. For instructions on downloading or generating, and installing,
different types of map sets, see these Navit Wiki pages:

http://wiki.navit-project.org/index.php/OpenStreetMaps

http://wiki.navit-project.org/index.php/European_maps

http://wiki.navit-project.org/index.php/Garmin_maps

You should either add the appropriate configuration elements to
/etc/navit/navit.xml, or copy /etc/navit/navit.xml to
~/.navit/navit.xml and edit it there. You may have to remove or comment
out the section for the sample map set, also.
EOF

# validate the .desktop file
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

unzip %{SOURCE3} -d %{buildroot}/%{_datadir}/%{name}/maps

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS README*
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/dbus-1/services/*.service
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.xml
%{_datadir}/man/man1/*

#files graphics-qt
#{_libdir}/%{name}/graphics/libgraphics_qt*

%files graphics-sdl
%{_libdir}/%{name}/graphics/libgraphics_sdl*

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.6
- Rebuilt for Fedora
* Fri Sep 25 2009 Adam Williamson <awilliam@redhat.com> - 0.1.2-0.2.20090918svn2578
- spec clean:
+ add svn snapshot source creation comment
+ use make install DESTDIR=buildroot, not makeinstall
* Fri Sep 18 2009 Adam Williamson <awilliam@redhat.com> - 0.1.2-0.1.20090918svn2578
- update to latest SVN, bump version to 0.1.2 as upstream released a 0.1.1
- change evr to match policy (per review)
- add a comment on static_sample.patch's upstream status (per review)
- update static_sample.patch for 0.1.2
- add icon cache update snippets (per review)
- validate the .desktop file in install (per review)
- drop the warning about GPS from the README as it works even without
  gpsd running, now
* Tue Aug 04 2009 Adam Williamson <awilliam@redhat.com> - 0.1.1-0.1.2431
- initial package (not really, but begin changelog) based on MDV spec
