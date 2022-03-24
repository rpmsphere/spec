Summary: An attractive astronomical ephemeris program for X Window
Name: xephem
Version: 4.1.0
Release: 1
License: Distributable, see Copyright file for details. NOT GPL!
Group: Applications/Scientific
Source: http://www.clearskyinstitute.com/xephem/XEphem-%{version}.tar.gz
Source1: XEphem.desktop
Source2: XEphem.kdelnk
Source3: XEphem.png
Source4: XEphem.xpm
Source5: mini-XEphem.xpm
Source6: v3.7-catalogs.tar.bz2
Source7: hubble-1.0.tar.gz
URL: http://www.clearskyinstitute.com/xephem/xephem.html
BuildRequires: motif-devel libjpeg-devel libpng-devel libXmu-devel

%description
XEphem is an interactive astronomical ephemeris program for X Window
system with OpenMotif. It provides many graphical views as well as
quantitative heliocentric, geocentric and topocentric information for
Earth satellites, solar system and deep-sky objects.

%prep
%setup -a6 -a7 -q -n XEphem-%{version}

%build
cd GUI/xephem
make
cd tools/lx200xed
make
cd ../simpleINDI
make
cd ../xedb
make
cd ../xephemdbd
make
cd ..

%install
XS=GUI/xephem
XL=$RPM_BUILD_ROOT/usr/share/xephem

mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/xephem
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/share/X11/app-defaults
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
#mkdir -p $RPM_BUILD_ROOT/usr/share/applnk/Astro
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
#mkdir -p $RPM_BUILD_ROOT/usr/share/icons/mini
mkdir -p $RPM_BUILD_ROOT/usr/share/xephem/tools/lx200xed
mkdir -p $RPM_BUILD_ROOT/usr/share/xephem/tools/xephemdbd
mkdir -p $RPM_BUILD_ROOT/usr/share/xephem/tools/xedb
mkdir -p $RPM_BUILD_ROOT/usr/share/xephem/tools/simpleINDI

cp $RPM_SOURCE_DIR/XEphem.desktop $RPM_BUILD_ROOT/usr/share/applications/.
#cp $RPM_SOURCE_DIR/XEphem.kdelnk $RPM_BUILD_ROOT/usr/share/applnk/Astro/.
cp $RPM_SOURCE_DIR/XEphem.png $RPM_BUILD_ROOT/usr/share/pixmaps/.
cp $RPM_SOURCE_DIR/XEphem.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/.
cp $RPM_SOURCE_DIR/mini-XEphem.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/.
cp *.edb $XS/catalogs/
cp ./gallery/* $XS/gallery/.

install -m 755 $XS/xephem $RPM_BUILD_ROOT/usr/bin/xephem
install -m 755 $XS/tools/lx200xed/lx200xed $XL/tools/lx200xed
install -m 755 $XS/tools/xedb/xedb $XL/tools/xedb
install -m 755 $XS/tools/xephemdbd/xephemdbd $XL/tools/xephemdbd
install -m 755 $XS/tools/xephemdbd/*.pl $XL/tools/xephemdbd
install -m 755 $XS/tools/simpleINDI/simpleINDI $XL/tools/simpleINDI/simpleINDI

cd $XS/tools
find . -name "*.[coh]" -exec rm \{\} \;
cd -

install -m 644 $XS/xephem.man $RPM_BUILD_ROOT/usr/share/man/man1/xephem.1x
gzip -v $RPM_BUILD_ROOT/usr/share/man/man1/xephem.1x

install -d -m 755 $XL/auxil
install -d -m 755 $XL/catalogs
install -d -m 755 $XL/fifos
install -d -m 755 $XL/fits
install -d -m 755 $XL/help
install -d -m 755 $XL/help/png
install -d -m 755 $XL/tools
install -d -m 755 $XL/tools/xephemdbd
install -d -m 755 $XL/tools/lx200xed
install -d -m 755 $XL/tools/xedb
install -m 644 $XS/auxil/*		$XL/auxil
install -m 644 $XS/catalogs/*		$XL/catalogs
install -m 644 $XS/fifos/*		$XL/fifos
install -m 644 $XS/help/xephem.html	$XL/help
install -m 644 $XS/help/png/*		$XL/help/png
install -m 644 $XS/tools/xedb/README	$XL/tools/xedb
install -m 644 $XS/tools/xedb/sample.res	$XL/tools/xedb
install -m 644 $XS/tools/lx200xed/README	$XL/tools/lx200xed
install -m 644 $XS/tools/xephemdbd/*	$XL/tools/xephemdbd

echo "XEphem.ShareDir: /usr/share/xephem" > $RPM_BUILD_ROOT/usr/share/X11/app-defaults/XEphem

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE README.md
/usr/bin/xephem
/usr/share/man/man1/xephem.1x.gz
/usr/share/xephem
/usr/share/X11/app-defaults/XEphem
/usr/share/applications/XEphem.desktop
/usr/share/pixmaps/*

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.0
- Rebuilt for Fedora
* Fri Jul 16 2010 <tom@mmto.org>
- move the X resource: "XEphem" to /usr/share/X11/app-defaults
- move the "stuff" from /usr/lib/xephem to /usr/share/xephem
* Thu Jul 15 2010 <tom@mmto.org>
- link against dynamic openmotif and make
- this package depend on openmotif
- allow for 64 bit build
* Sat Aug 9 2008 <ckulesa@as.arizona.edu>
- added hipparchos, IC, new NGC catalogs from dpkiel
- added NASA/ESA gallery images from dpkiel
* Fri Aug 8 2008 <ckulesa@as.arizona.edu>
- updated to 3.7.3
- removed jpeg,png,z, motif libs from build
* Thu Feb 16 2006 <ckulesa@as.arizona.edu>
- updated to 3.7.1
* Wed Oct 5 2005 <ckulesa@as.arizona.edu>
- updated to 3.7
- removed previous patches, now unnecessary
- added help directory in install
* Sat Jun 4 2005 <ckulesa@as.arizona.edu>
- updated to 3.6.4
- had to patch tools/indi Makefile for missing waitINDI
* Thu Jan 13 2005 <ckulesa@as.arizona.edu>
- New version 3.6.3
- Small SPEC file tweaks
- Added new XEphem tools
- Removed XEphem's inline Motif stubs in favor of OpenMotif 
- Built for Fedora Core (1 and 3)
* Sun Oct 21 2001 <ckulesa@as.arizona.edu>
- New version 3.5
* Thu Dec 7 2000 <ckulesa@as.arizona.edu>
- New version 3.4
- Redhat 7.0 and 6.x support
- Built dynamically against OpenMotif 2.1.30 (Redhat 7.0 Powertools)
- Discontinued use of wmconfig in favor of GNOME and KDE desktop links
- New PNG and XPM icons for GNOME and KDE
- Now shares "Astro" desktop folder with Tim Pickering's IRAF packages
* Thu Apr 13 2000 <ckulesa@as.arizona.edu>
- Linked against Lesstif 0.89.9
- Redhat 6.2 version
- Uses wmconfig for automatic desktop entries
* Mon Nov 1 1999 <ckulesa@as.arizona.edu>
- RPM-ification
- Statically linked against Lesstif 0.86
