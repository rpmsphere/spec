%global debug_package %{nil}

Summary: A tool to manipulate and create images of Earth
Name: xrmap
Version: 2.33
Release: 21.1
License: GPLv2+
Group: Sciences/Geosciences
Source: ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/%{name}-%{version}.tar.bz2
Patch0: xrmap-2.33-fix-str-fmt.patch
URL: http://frmas.free.fr/li_1.htm
BuildRequires:	imake
BuildRequires:	libX11-devel
BuildRequires:	bzip2-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXext-devel

%description
The Xrmap package is derived from the rmap package by Reza Naima.
It provides a user-friendly X client for manipulating the CIA
World data bank II global vector information and for generating images 
of the Earth. The images can be very accurately zoomed in, up to a 
factor of 100 or more.
Xrmap does have many more features than the original command line program
'rmap', especially it implements Rectangular, Mercator and Miller 
projections in addition to the Spherical projection, as well as reverse 
search of coordinates.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch0 -p1 -b .strfmt
perl -pi -e "s,/usr/X11R6/lib ,%{_libdir} ," earthview/Makefile
sed -i '23i #include <zlib.h>' image.c
sed -i 's|gzFile \*gzd|gzFile gzd|' earthview/earthview.c

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
make install DESTDIR=$RPM_BUILD_ROOT/usr
mv $RPM_BUILD_ROOT/usr/X11R6/* $RPM_BUILD_ROOT/usr
make install.man DESTDIR=$RPM_BUILD_ROOT/usr
mv $RPM_BUILD_ROOT/usr/X11R6/* $RPM_BUILD_ROOT/usr/share
mv $RPM_BUILD_ROOT/usr/man/man1/* $RPM_BUILD_ROOT/usr/share/man/man1

mkdir -p $RPM_BUILD_ROOT%_datadir/pixmaps
install xrmap.xpm -m 644 $RPM_BUILD_ROOT%_datadir/pixmaps/xrmap.xpm
install editkit/emx $RPM_BUILD_ROOT%{_prefix}/bin

#mkdir -p $RPM_BUILD_ROOT%_datadir/rmap/{anthems,examples,extra}
#install anthems/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/anthems
#install examples/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/examples
#install extra/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/extra

#mkdir -p $RPM_BUILD_ROOT%_datadir/rmap/factbook/{extra,text}
#install factbook/extra/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/factbook/extra
#install factbook/text/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/factbook/text

#mkdir -p $RPM_BUILD_ROOT%_datadir/rmap/flags/{big,small}
#install flags/big/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/flags/big
#install flags/small/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/flags/small

#mkdir -p $RPM_BUILD_ROOT/usr/share/rmap/hymns
#install hymns/* -m 644 $RPM_BUILD_ROOT/usr/share/rmap/hymns

mkdir -p $RPM_BUILD_ROOT/usr/share/rmap/tools/{anthems,cbd2else,factbook,jpd2else,locutils,rez2else,upgrade}
install tools/anthems/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/anthems
install tools/cbd2else/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/cbd2else
install tools/factbook/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/factbook
install tools/jpd2else/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/jpd2else
install tools/locutils/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/locutils
install tools/rez2else/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/rez2else
install tools/upgrade/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/upgrade

mkdir -p %buildroot%{_datadir}/applications
cat << EOF > %buildroot%{_datadir}/applications/%name.desktop
[Desktop Entry]
Type=Application
Categories=Education;Science;Geology;        
Name=Xrmap        
Comment=Manipulate and create images of Earth        
Exec=%{name}        
Icon=%{name}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGES INSTALL midi_cfg/* tools/README.tools LICENSE MAPEDIT README TODO VECTORMAP
%{_datadir}/pixmaps/xrmap.xpm
%{_datadir}/rmap
%{_datadir}/editkit
%{_prefix}/bin/earthview
%{_prefix}/bin/emx
%{_prefix}/bin/xrmap
%{_prefix}/share/man/man1/*
%{_datadir}/applications/*.desktop

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.33
- Rebuild for Fedora
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.33-8mdv2011.0
+ Revision: 615735
- the mass rebuild of 2010.1 packages
* Thu Feb 04 2010 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 2.33-7mdv2010.1
+ Revision: 500926
- fix str fmt
- disable parallel make
- fix License tag
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.33-4mdv2009.0
+ Revision: 257691
- rebuild
- kill re-definition of %%buildroot on Pixel's request
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Fri Dec 14 2007 Thierry Vignaud <tv@mandriva.org> 2.33-2mdv2008.1
+ Revision: 120008
- auto convert menu to XDG
- partially adapt to new X11 layout
- do not hardcode spec-helper
- buildrequires imake
- kill bogus buildrequires on X11
* Mon Apr 10 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.33-2mdk
- Add BuildRequires
* Tue Jan 31 2006 Jerome Soyer <saispo@mandriva.org> 2.33-1mdk
- New release 2.33
* Thu Jan 19 2006 Anssi Hannula <anssi@mandriva.org> 2.32-3mdk
- fix BuildRequires bzip2-devel
* Sun Jan 08 2006 Anssi Hannula <anssi@mandriva.org> 2.32-2mdk
- fix x86_64 build
* Thu Sep 15 2005 Franck Villaume <fvill@mandriva.org> 2.32-1mdk
- new version 2.32
- fix source url
* Thu Aug 25 2005 Franck Villaume <fvill@mandriva.org> 2.31-1mdk
- new version 2.31
* Sat Apr 23 2005 Franck Villaume <fvill@mandriva.org> 2.30-2mdk
- buildrequires again
* Mon Apr 18 2005 Franck Villaume <fvill@mandriva.org> 2.30-1mdk
- new release
- buildrequires
* Thu Sep 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.29-1mdk
- new
