Summary: The sophisticated clock for the X Window system
Name: sunclock
Version: 3.56
Release: 7.1
License: GPL
Group: Sciences/Astronomy
Source: ftp://ftp.ac-grenoble.fr/ge/geosciences/%{name}-%{version}.tar.bz2
Patch0: sunclock-3.56-fix-str-fmt.patch
URL: http://freshmeat.net/projects/sunclock/
BuildRequires: imake libX11-devel libjpeg-devel libpng-devel libXpm-devel libXext-devel

%description
Sunclock displays a map of the Earth and shows which portion is illuminated
by the sun. It can commute between two states, the "clock window" and
the "map window". The clock window displays a small map of the Earth
and therefore occupies little space on the screen, while the "map window" 
displays a large map and offers more advanced functions. 

%prep
%setup -q
%patch0 -p0
sed -i 's|gzFile \* fd|gzFile fd|' readvmf.c

%build
xmkmf
make CDEBUGFLAGS="%{optflags}" CXXDEBUGFLAGS="%{optflags}"

%install
make install DESTDIR=$RPM_BUILD_ROOT%{_prefix} BINDIR=/bin MANDIR=/share/man/man1
make install.man DESTDIR=$RPM_BUILD_ROOT%{_prefix} BINDIR=/bin MANDIR=/share/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
install wm_icons/sunclock2.xpm -m 644 $RPM_BUILD_ROOT/usr/share/pixmaps/sunclock2.xpm

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Categories=Amusement;
Name=Sunclock
Comment=Sophisticated clock for the X Window system
Exec=%{name}
Icon=%{name}2
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGES coordinates.txt COPYING INSTALL README TODO VMF.txt
%{_datadir}/%name
%{_bindir}/sunclock
%{_mandir}/man1/*
%{_datadir}/pixmaps/sunclock2.xpm
%{_datadir}/applications/*.desktop

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.56
- Rebuilt for Fedora
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 3.56-4mdv2011.0
+ Revision: 615040
- the mass rebuild of 2010.1 packages
* Sun Jan 24 2010 Funda Wang <fwang@mandriva.org> 3.56-3mdv2010.1
+ Revision: 495378
- fix str fmt
- use standard file location
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 3.56-2mdv2009.0
+ Revision: 269395
- rebuild early 2009.0 package (before pixel changes)
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Sat May 17 2008 Funda Wang <fwang@mandriva.org> 3.56-1mdv2009.0
+ Revision: 208511
- New version 3.56
  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - auto convert menu to XDG
    - do not reinvent spec-helper
    - BR png-devel
    - BR jpeg-devel
    - BR X11-devel
    - BR imake
    - kill re-definition of %%buildroot on Pixel's request
    - import sunclock
* Thu Aug 18 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.54.1-2mdk
- Add Conflict
* Wed Aug 17 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.54.1-1mdk
- New release 3.54.1
* Thu Feb 03 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.53-1mdk
- 3.53
* Mon Oct 11 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.52-1mdk
- 3.52
* Wed Sep 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.51-1mdk
- new
* Thu Aug 30 2001 Francois Massonneau <frmas@free.fr>
- Add files needed for K Menu entries
* Tue Aug 14 2001 Francois Massonneau <frmas@free.fr>
- Change the spec file to match the 3.5x serie
* Tue Jun 26 2001 Francois Massonneau <frmas@free.fr>
- Add the Sunclock icon during the install
* Tue Mar 06 2001 Francois Massonneau <frmas@free.fr>
- First spec file
