%global debug_package %{nil}

Name:		crosti
Summary:	Tool to create cross stitch scheme from custom image
Version:	1.14.0
Release:	1
License:	GPLv3+
Group:		Applications/Editors
URL:		https://sites.google.com/site/crostiapp/
Source0:	http://downloads.sourceforge.net/project/crosti/%{name}-%{version}-source.zip
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	dos2unix
BuildRequires:	unzip
BuildRequires:	gcc-c++

%description
This tool allows you to make your own unique cross stitch scheme from custom
image. You can resize and rotate image, reduce the number of colors, change
image palette, make cross stitch scheme, preview it, save and print. Cross
stitch scheme edition available: colors and icons changing, new color addition,
color fill, scheme pixel draw, lines and half-stitches.

Features:
* Convert custom image to cross stitch scheme.
* Edit cross stitch scheme.
* Save and print the scheme that you created.
* Input images: BMP, GIF, ICO, JPEG, JPG, MNG, PBM, PGM, PNG, PPM, SVG, TIF,
  TIFF, XBM, XPM.
* Output cross stitch scheme: BMP, ICO, JPEG, JPG, PNG, PPM, TIF, TIFF, XBM,
  XPM, PDF, CST (crosti scheme text file).

%prep
%setup -q -c

%build
qmake-qt4
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/*/*.png

%changelog
* Tue Sep 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.14.0
- Rebuild for Fedora
* Sun Apr 8 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.7.0-1
- update to 1.7.0
- mime type text/x-cst
* Fri Mar 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.6.0-4
- Fedora and openSUSE support
* Tue Mar 06 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.6.0-3
+ Revision: 782423
- move icons to iconsdir
* Tue Mar 06 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.6.0-2
+ Revision: 782379
- fix desktop file
- use home directory instead /usr/share
* Fri Mar 02 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.6.0-1
+ Revision: 781742
- imported package crosti
