Name: earth3d
Version: 1.0.5
Release: 1
Summary: A program that visualizes the earth in realtime in a 3D view
License: GPL
Group: Amusements/Graphics
URL: http://www.earth3d.org/
Source0: http://prdownloads.sourceforge.net/earth3d/%{name}_client-%version-src.tar.bz2
Source1: %{name}.desktop
Patch: earth3d_client-1.0.4-alt-makefile.patch
# Automatically added by buildreq on Sun Jan 08 2006
BuildRequires: fontconfig-devel freetype-devel gcc-c++ libpng-devel libstdc++-devel libX11-devel zlib-devel libXmu-devel
Requires: fontconfig freetype libpng zlib libXmu
BuildRequires: qt3-devel

%description
Earth3D is a program that visualizes the earth in realtime in a
3D view. It uses data from NASA, USGS, the CIA and the city of
Osnabrück. I would like to thank these organisations to allow
me to use their data! The program is available as binary for
Linux, MacOS X and Windows under the GPL license. The program's
features are:

* viewing the earth as a whole
* zooming in until countries, cities and even single houses
  become visible (in areas where the necessary map resolution is
  available)
* embedding external data like current earthquake positions,
  cloud data or GPS points

You can also get some maps mirrored locally to speed up access:
http://venus.schunter.etc.tu-bs.de/~gunia/earthdata.zip
(~1.1->1.9Gb; doesn't include Landsat7 100m/pixel data)

PS: packaged experiencing frustration of Google Earth ;)

%prep
%setup -q -n %{name}
%patch -p1
echo "#include <gltest.h>" >> gltestwidget.h
sed -i '1i #include <cstdlib>' formview.ui.h listViewServiceItem.cpp network/*.cpp draw/*.cpp geometry/*.cpp
sed -i '/alloc\.h/d' network/urlDownload.cpp
sed -i -e '1i #include <cstring>' -e 's|png_voidp_NULL|NULL|' -e 's|png_infopp_NULL|NULL|' pngutils.cpp

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh ; PATH=$PATH:$QTDIR/bin
qmake earth3d.pro QMAKE_CXXFLAGS+=-fpermissive
%__make

%install
install -pD -m755 %{name}   %buildroot%{_bindir}/%{name}
install -pD -m644 %{name}.1 %buildroot%{_mandir}/man1/%{name}.1
install -pD -m644 %{SOURCE1} %buildroot%{_datadir}/applications/%{name}.desktop
install -pD -m644 images/webpres.png %buildroot%{_datadir}/pixmaps/%{name}.png

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%clean
%__rm -rf %buildroot

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.5
- Rebuilt for Fedora
* Thu Nov 09 2006 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- 1.0.5
* Tue Mar 07 2006 Michael Shigorin <mike@altlinux.org> 1.0.4-alt2
- fixed build with --as-needed; 
  thanks Dmitry Levin (ldv@) for rm -f /dev/brake
* Wed Feb 08 2006 Michael Shigorin <mike@altlinux.org> 1.0.4-alt1
- built for Sisyphus
- thanks Yuri Sedunov <aris@> for build fix suggestion
* Sun Jan 08 2006 Michael Shigorin <mike@altlinux.org> 1.0.4-alt0.M30.1
- built for M30
* Sun Jan 08 2006 Michael Shigorin <mike@altlinux.org> 1.0.4-alt1
- built for ALT Linux
