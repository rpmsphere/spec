# exclude plugin .so from provides
%global __provides_exclude_from %{_libdir}/%{name}/extensions/.*\\.so

# exclude plugin .so from requires
%global extensions lib(catalogs|edit_metadata|exiv2_tools|flicker_utils|gstreamer_utils|image_rotation|image_viewer|importer|jpeg_utils|oauth)\\.so
%global __requires_exclude %{extensions}

Name:           pix
Version:        2.6.5
Release:        1
Summary:        Image viewer and browser utility
License:        GPLv2+
Group:          Graphics/Viewers
Url:            https://github.com/linuxmint/pix
Source:         https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gnome-common
BuildRequires:  itstool
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:  pkgconfig(exiv2) >= 0.21
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.34.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libbrasero-burn3) >= 3.2.0
BuildRequires:  pkgconfig(libopenraw-0.1) >= 0.0.8
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.34.0
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-gnome-2.4) >= 2.36.0
BuildRequires:  pkgconfig(libwebp) >= 0.2.0
BuildRequires:  pkgconfig(sm) >= 1.0.0
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(glib-2.0)

%description
pix lets you browse your hard disk, showing you thumbnails of
image files.
It also lets you view single files (including GIF animations), add
comments to images, organise images in catalogs, print images, view
slide shows, set your desktop background, and more.

%package devel
Summary:        Image viewer and browser utility -- Development Files
Group:          System/Libraries
Requires:       %{name} = %{version}

%description devel
pix lets you browse your hard disk, showing you thumbnails of
image files.
It also lets you view single files (including GIF animations), add
comments to images, organise images in catalogs, print images, view
slide shows, set your desktop background, and more.

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=1 gnome-autogen.sh --add-missing
%configure \
  --disable-static       \
  --disable-silent-rules \
  --with-smclient=xsmp

%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING README debian/changelog
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/extensions/
%{_libdir}/%{name}/extensions/*.extension
%{_libdir}/%{name}/extensions/*.so
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_datadir}/glib-2.0/schemas/*%{name}*.gschema.xml
%{_datadir}/glib-2.0/schemas/*%{name}.enums.xml
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/%{name}-2.6/
%{_datadir}/aclocal/%{name}.m4
%{_libdir}/pkgconfig/%{name}-2.6.pc

%changelog
* Sun Sep 05 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.5
- Rebuilt for Fedora
* Wed Mar 10 2021 daviddavid <daviddavid> 2.6.3-1.mga9
+ Revision: 1701082
- new version: 2.6.3
* Fri Dec 11 2020 joequant <joequant> 2.6.1-1.mga8
+ Revision: 1655291
- update to 2.6.1
* Tue Dec 08 2020 joequant <joequant> 2.6.0-2.mga8
+ Revision: 1654570
- update to 2.6.0
* Thu Oct 08 2020 wally <wally> 2.4.8-2.mga8
+ Revision: 1632840
- filter plugin .so from provides and requires (mga#27373)
* Sat May 16 2020 joequant <joequant> 2.4.8-1.mga8
+ Revision: 1584309
- update to 2.4.8
* Tue Feb 18 2020 umeabot <umeabot> 2.4.0-2.mga8
+ Revision: 1539389
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%configure2_5x
* Wed Nov 27 2019 daviddavid <daviddavid> 2.4.0-1.mga8
+ Revision: 1463238
- new version: 2.4.0
* Thu Jul 11 2019 daviddavid <daviddavid> 2.2.0-1.mga8
+ Revision: 1419972
- new version: 2.2.0
* Thu May 16 2019 daviddavid <daviddavid> 2.0.3-2.mga7
+ Revision: 1398007
- rebuild for new exiv2 0.27.1
- use upstream patch to fix build with exiv2 >= 0.27
* Fri Jan 11 2019 daviddavid <daviddavid> 2.0.3-1.mga7
+ Revision: 1354904
- new version: 2.0.3
* Fri Jan 11 2019 daviddavid <daviddavid> 1.8.2-3.mga7
+ Revision: 1354836
- add patch to fix build with exiv2 >= 0.27
- rebuild for new exiv2 0.27
* Sun Sep 23 2018 umeabot <umeabot> 1.8.2-2.mga7
+ Revision: 1300291
- Mageia 7 Mass Rebuild
* Sat Jun 30 2018 joequant <joequant> 1.8.2-1.mga7
+ Revision: 1240996
- update to 1.8.2
* Sat Dec 16 2017 joequant <joequant> 1.6.2-1.mga7
+ Revision: 1182938
- upgrade to 1.6.2
* Tue Aug 08 2017 daviddavid <daviddavid> 1.0.5-3.mga7
+ Revision: 1138788
- rebuild for new libwebp 0.6.0
- fix for new %%find_lang
* Tue Jun 20 2017 neoclust <neoclust> 1.0.5-2.mga6
+ Revision: 1107989
- Rebuild against new exiv2
* Sun Jul 03 2016 joequant <joequant> 1.0.5-1.mga6
+ Revision: 1038393
- imported package pix
