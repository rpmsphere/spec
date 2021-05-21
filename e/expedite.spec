Summary:	Expedite Evas benchmark/test suite
Name:		expedite
Version:	0.7.2
Release:	1
License: 	BSD
Group: 		Graphical desktop/Enlightenment
Source:		http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
Source1:	%name.desktop
URL:		http://www.enlightenment.org/
BuildRequires: 	evas-devel >= 0.9.9.063
BuildRequires:	xcb-util
BuildRequires:	SDL-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXrender-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils

%description
Expedite Evas benchmark/test suite

%prep
%setup -qn %{name}-%{version}
sed -i -e 's/Evas_Engine_Software_X11.h/Evas_Legacy.h/' -e 's/Evas_Engine_Info_Software_X11/Evas_Engine_Info/' src/bin/engine_software_xlib.c

%build
%configure
make

%install
rm -fr %buildroot
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cp -vf %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/

mkdir -p %buildroot{%{_datadir}/icons/hicolor/64x64/apps,%{_datadir}/icons/hicolor/32x32/apps,%{_datadir}/icons/hicolor/16x16/apps}
install -m 644 data/e.png %buildroot%{_datadir}/icons/hicolor/64x64/apps/%name.png
convert -resize 32x32 data/e.png %buildroot%{_datadir}/icons/hicolor/32x32/apps/%name.png
convert -resize 16x16 data/e.png %buildroot%{_datadir}/icons/hicolor/16x16/apps/%name.png

mkdir -p %buildroot%{_datadir}/pixmaps
cp data/e.png %buildroot%{_datadir}/pixmaps/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING* README
%{_bindir}/%name
%{_bindir}/expedite-cmp
%{_datadir}/%name
%{_datadir}/icons/*.png
%{_datadir}/icons/*/*.png
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu Oct 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> 0.7.2-1.ossii
- Rebuild for OSSII

* Sat Dec 18 2010 Funda Wang <fwang@mandriva.org> 0.7.2-1mdv2011.0
+ Revision: 622840
- new version 0.7.2

* Tue Nov 16 2010 Funda Wang <fwang@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 597999
- new version 0.7.1
- BR xrender
- new snapshot

* Sun Dec 13 2009 Funda Wang <fwang@mandriva.org> 0.6.0-8.20091130.1mdv2010.1
+ Revision: 478143
- bump rel
- New snapshot

* Sat Aug 08 2009 Funda Wang <fwang@mandriva.org> 0.6.0-8.20090808.1mdv2010.0
+ Revision: 411698
- renew tarball to build with latest evas

* Wed Jul 08 2009 Funda Wang <fwang@mandriva.org> 0.6.0-8.20090503.2mdv2010.0
+ Revision: 393395
- fix xcb
- rebuild

* Sun May 03 2009 Funda Wang <fwang@mandriva.org> 0.6.0-8.20090503.1mdv2010.0
+ Revision: 370871
- New snapshot

* Mon Mar 02 2009 Antoine Ginies <aginies@mandriva.com> 0.6.0-7mdv2009.1
+ Revision: 346965
- add missing binairies
- SVN SNAPSHOT 20090227, release 0.6.0

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sun Oct 19 2008 Funda Wang <fwang@mandriva.org> 0.6.0-6mdv2009.1
+ Revision: 295182
- simplify BR

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-5mdv2009.0
+ Revision: 266746
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 0.6.0-4mdv2009.0
+ Revision: 214080
- clean spec

  + Antoine Ginies <aginies@mandriva.com>
    - update buildrequires

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu May 31 2007 Antoine Ginies <aginies@mandriva.com> 0.6.0-3mdv2008.0
+ Revision: 33097
- fix expedite.desktop

* Wed May 30 2007 Antoine Ginies <aginies@mandriva.com> 0.6.0-2mdv2008.0
+ Revision: 32865
- rebuild to enable evas_gl

* Tue May 29 2007 Antoine Ginies <aginies@mandriva.com> 0.6.0-1mdv2008.0
+ Revision: 32581
- adjust buildrequires
- few adjustement to fix menu entry
- first release
- Import expedite
