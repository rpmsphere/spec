Summary: 3D Viewer for LDraw models
Name: ldview
Group: Amesements
Version: 4.2
Release: 78.1
License: GPL
URL: http://ldview.sourceforge.net
Source0: LDView-4.2beta1.zip
Source1: FD_ZERO64.h
Source2: lib3ds-20080909.zip
BuildRequires: qt4-devel, boost-devel, mesa-libOSMesa-devel, gcc-c++, libpng-devel, tinyxml-devel, libjpeg-turbo-devel
BuildRequires: llvm-devel

%description
LDView is a real-time 3D viewer for displaying LDraw models using hardware-
accellerated 3D graphics. It was written using OpenGL, so should be accellerated
on any video card which provides full OpenGL 3D accelleration (so-called
mini-drivers are not likely to work). It should also work on other video cards
using OpenGL software rendering, albeit at a much slower speed. For information
on LDraw, please visit www.ldraw.org, the centralized LDraw information site. 

The program can read LDraw DAT files as well as MPD files. It then allows you to
rotate the model around to any angle with themouse. A fast computer or a video
card with T&L support (Transform & Lighting) is strongly recommended for
displaying complexmodels. 

%prep
%setup -q -c
cp %{SOURCE1} .
sed -i -e '/TCStlIncludes\.h/d' -e '5i #include <TCFoundation/TCStlIncludes.h>' LDLib/LDModelTree.h
sed -i '1i #include <string.h>\n#include <stdlib.h>' TCFoundation/TCArray.h
sed -i '1i #include <unistd.h>' TCFoundation/mystring.cpp
sed -i 's|TIME_UTC|TIME_UTC_|' LDLib/LDLibraryUpdater.cpp TCFoundation/TCWebClient.cpp TRE/TREMainModel.cpp
sed -i '212,213d' TRE/TREGLExtensions.cpp

unzip %{SOURCE2}
cd lib3ds-20080909
LIBS=-lm ./configure --build=x86_64
make
cp -f src/.libs/lib3ds.a ../lib/
cp src/.libs/lib3ds.a ../lib/lib3ds-64.a

%build
%define is_kde4 %(which kde4-config >/dev/null && echo 1 || echo 0)
%ifarch x86_64 aarch64
%define qplatform linux-g++-64
%ifarch aarch64
sed -i 's|-m32|-fPIC -fpermissive|' QT/LDView.pro OSMesa/Makefile Makefile.inc
%else
sed -i 's|-m32|-m64 -fPIC -fpermissive|' QT/LDView.pro OSMesa/Makefile Makefile.inc
%endif
sed -i 's|FD_ZERO|FD_ZERO64|' TCFoundation/TCWebClient.cpp
sed -i '14i #include "../FD_ZERO64.h"' TCFoundation/TCWebClient.cpp
%else
%define qplatform linux-g++-32
%endif
cd QT
qmake-qt4 -spec %{qplatform} QMAKE_CXXFLAGS+="-fPIC -fpermissive"
%ifarch aarch64
sed -i 's|-m64||' Makefile
%endif
make clean
make TESTING="%{optflags} -fpermissive"
lrelease-qt4 LDView.pro
strip LDView
cd ../OSMesa
make clean
make TESTING="%{optflags} -lGL -fpermissive"
cd ../QT/kde
if [ -d build ]; then rm -rf build ; fi
mkdir -p build
cd build
if cmake -DCMAKE_C_FLAGS_RELEASE="%{optflags} -fPIC -fpermissive" \
-DCMAKE_CXX_FLAGS_RELEASE="%{optflags} -fPIC -fpermissive" \
-DCMAKE_INSTALL_PREFIX=`kde4-config --prefix` .. ; then
make
fi

%install
cd QT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ldview
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/ldview
install -m 755 LDView $RPM_BUILD_ROOT%{_bindir}/LDView
install -m 755 ../OSMesa/ldview $RPM_BUILD_ROOT%{_bindir}/ldview
install -m 644 ../Textures/SansSerif.fnt \
$RPM_BUILD_ROOT%{_datadir}/ldview/SansSerif.fnt
install -m 644 ../Help.html $RPM_BUILD_ROOT%{_datadir}/ldview/Help.html
install -m 644 ../Readme.txt $RPM_BUILD_ROOT%{_datadir}/ldview/Readme.txt
install -m 644 ../ChangeHistory.html \
				$RPM_BUILD_ROOT%{_datadir}/ldview/ChangeHistory.html
install -m 644 ../license.txt \
				$RPM_BUILD_ROOT%{_datadir}/ldview/license.txt
install -m 644 ../m6459.ldr $RPM_BUILD_ROOT%{_datadir}/ldview/m6459.ldr
install -m 644 ../8464.mpd $RPM_BUILD_ROOT%{_datadir}/ldview/8464.mpd 
install -m 644 ../LDViewMessages.ini \
				$RPM_BUILD_ROOT%{_datadir}/ldview/LDViewMessages.ini
cat ../LDExporter/LDExportMessages.ini >> \
				$RPM_BUILD_ROOT%{_datadir}/ldview/LDViewMessages.ini
install -m 644 ../Translations/German/LDViewMessages.ini \
				$RPM_BUILD_ROOT%{_datadir}/ldview/LDViewMessages_de.ini
install -m 644 ../Translations/Italian/LDViewMessages.ini \
				$RPM_BUILD_ROOT%{_datadir}/ldview/LDViewMessages_it.ini
install -m 644 ../Translations/Czech/LDViewMessages.ini \
			    $RPM_BUILD_ROOT%{_datadir}/ldview/LDViewMessages_cz.ini
install -m 644 ../Translations/Hungarian/LDViewMessages.ini \
				$RPM_BUILD_ROOT%{_datadir}/ldview/LDViewMessages_hu.ini
install -m 644 todo.txt $RPM_BUILD_ROOT%{_datadir}/ldview/todo.txt
install -m 644 ldview_en.qm $RPM_BUILD_ROOT%{_datadir}/ldview/ldview_en.qm
install -m 644 ldview_de.qm $RPM_BUILD_ROOT%{_datadir}/ldview/ldview_de.qm
install -m 644 ldview_it.qm $RPM_BUILD_ROOT%{_datadir}/ldview/ldview_it.qm
install -m 644 ldview_cz.qm $RPM_BUILD_ROOT%{_datadir}/ldview/ldview_cz.qm
install -m 644 ../LDExporter/LGEO.xml \
			   $RPM_BUILD_ROOT%{_datadir}/ldview/LGEO.xml
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime-info/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/application-registry/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/gnome/32x32/mimetypes
mkdir -p $RPM_BUILD_ROOT/etc/gconf/schemas
install -m 644 desktop/ldraw.mime $RPM_BUILD_ROOT%{_datadir}/mime-info/ldraw.mime
install -m 644 desktop/ldraw.xml  \
				$RPM_BUILD_ROOT%{_datadir}/mime/packages/ldraw.xml
install -m 644 desktop/ldraw.keys $RPM_BUILD_ROOT%{_datadir}/mime-info/ldraw.keys
##install -m 644 desktop/ldview.applications \
##			$RPM_BUILD_ROOT%{_datadir}/application-registry/ldview.applications
sed -i -e 's|/usr/local/bin/||' -e 's|Application;|Game;BlocksGame;|' desktop/ldraw.desktop
install -m 644 desktop/ldraw.desktop \
				$RPM_BUILD_ROOT%{_datadir}/applications/ldview.desktop
install -m 755 desktop/ldraw-thumbnailer \
				$RPM_BUILD_ROOT%{_bindir}/ldraw-thumbnailer
install -m 644 images/LDViewIcon.png \
				$RPM_BUILD_ROOT%{_datadir}/pixmaps/gnome-ldraw.png
install -m 644 images/LDViewIcon.png $RPM_BUILD_ROOT%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-x-ldraw.png
install -m 644 images/LDViewIcon.png $RPM_BUILD_ROOT%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-x-multipart-ldraw.png
install -m 644 desktop/ldraw.schemas \
			$RPM_BUILD_ROOT/etc/gconf/schemas/ldraw.schemas
mkdir -p $RPM_BUILD_ROOT%{_datadir}/kde4/services
install -m 644 kde/ldviewthumbnailcreator.desktop \
		$RPM_BUILD_ROOT%{_datadir}/kde4/services/ldviewthumbnailcreator.desktop
if [ -f kde/build/lib/ldviewthumbnail.so ] ; then
mkdir -p $RPM_BUILD_ROOT%{_libdir}/kde4
install -m 644 kde/build/lib/ldviewthumbnail.so \
				$RPM_BUILD_ROOT%{_libdir}/kde4/ldviewthumbnail.so
fi

%files
%{_bindir}/LDView
%{_datadir}/ldview/SansSerif.fnt
%{_datadir}/ldview/Help.html
%{_datadir}/ldview/license.txt
%{_datadir}/ldview/ChangeHistory.html
%{_datadir}/ldview/m6459.ldr
%{_datadir}/ldview/8464.mpd
%{_datadir}/ldview/Readme.txt
%{_datadir}/ldview/LDViewMessages.ini
%{_datadir}/ldview/LDViewMessages_de.ini
%{_datadir}/ldview/LDViewMessages_it.ini
%{_datadir}/ldview/LDViewMessages_cz.ini
%{_datadir}/ldview/LDViewMessages_hu.ini
%{_datadir}/ldview/todo.txt
%{_datadir}/ldview/ldview_en.qm
%{_datadir}/ldview/ldview_de.qm
%{_datadir}/ldview/ldview_it.qm
%{_datadir}/ldview/ldview_cz.qm
%{_datadir}/ldview/LGEO.xml
%if %{is_kde4}
%{_libdir}/kde4/ldviewthumbnail.so
%endif
%{_datadir}/kde4/services/ldviewthumbnailcreator.desktop
%{_datadir}/mime-info/ldraw.mime
%{_datadir}/mime/packages/ldraw.xml
%{_datadir}/mime-info/ldraw.keys
##%{_datadir}/application-registry/ldview.applications
%{_datadir}/applications/ldview.desktop
%{_bindir}/ldraw-thumbnailer
%{_datadir}/pixmaps/gnome-ldraw.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-x-ldraw.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-x-multipart-ldraw.png
/etc/gconf/schemas/ldraw.schemas

%clean
rm -rf $RPM_BUILD_ROOT

%post
update-mime-database  %{_datadir}/mime >/dev/null
update-desktop-database
cd /etc/gconf/schemas
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` \
gconftool-2 --makefile-install-rule ldraw.schemas >/dev/null

%postun
update-mime-database  %{_datadir}/mime >/dev/null
update-desktop-database

%preun
cd /etc/gconf/schemas
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` \
gconftool-2 --makefile-uninstall-rule ldraw.schemas >/dev/null

%package osmesa
Summary: OSMesa port of LDView for servers without X11
Group: Applications/Multimedia
%description osmesa
OSMesa port of LDView for servers without X11

%files osmesa
%{_bindir}/ldview

%changelog
* Tue May 22 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 4.2beta1
- Rebuilt for Fedora
* Mon May 14 2012 Peter Bartfai <pbartfai@stardust.hu>
- Initial package
