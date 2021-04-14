Name: xscavenger
Summary: Cool arcade/thinking game very much like Lode Runner
Version: 1.4.4
Release: 17.1
Source: http://www.xdr.com/dash/%{name}-%{version}.tar.bz2
Source10: %{name}.16.png.bz2
Source11: %{name}.32.png.bz2
Source12: %{name}.48.png.bz2
Patch0: xscavenger-1.4.4-link.patch
URL: http://www.xdr.com/dash/scavenger.html
License: GPL
Group: Games/Arcade
BuildRequires: libX11-devel
BuildRequires: imake

%description
Scavenger is a cool arcade/thinking game very much like Lode Runner.
You've got to run around and collect objects while avoiding enemies. Some
objects are buried and you've got to dig down to get at them. It's an
addictive game and some of the levels are devilishly (cruelly) complicated
to solve.

%prep
%setup -q
%patch0 -p0

%build
cd src
perl -pi -e 's,^LIBNAME.*,LIBNAME = %{_datadir}/%{name},' Imakefile
xmkmf
touch scavenger.man
make CDEBUGFLAGS="%optflags" EXTRA_LDOPTIONS="%optflags"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/%{name}
cp src/scavenger $RPM_BUILD_ROOT%{_bindir}
cp -a data/* $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
cp src/scavenger.6 $RPM_BUILD_ROOT%{_mandir}/man6

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat << EOF > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=scavenger
Icon=%{name}
Categories=Game;ArcadeGame;
Name=X-Scavenger
Comment=Cool arcade/thinking game very much like Lode Runner
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
bzcat %{SOURCE10} > $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
bzcat %{SOURCE11} > $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
bzcat %{SOURCE12} > $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README DOC copyright
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_mandir}/*/*

%changelog
* Sat Sep 29 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.4
- Rebuilt for Fedora
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.4.4-10mdv2011.0
+ Revision: 634914
- simplify BR
* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.4.4-9mdv2010.0
+ Revision: 435275
- rebuild
* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 1.4.4-8mdv2009.0
+ Revision: 262704
- rebuild
* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.4.4-7mdv2009.0
+ Revision: 257710
- rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 1.4.4-5mdv2008.1
+ Revision: 135571
- BR imake
- auto-convert XDG menu entry
- kill re-definition of %$RPM_BUILD_ROOT on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import xscavenger
* Sun Oct 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4.4-5mdk
- BuildRequires fix
* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4.4-4mdk
- Rebuild
* Fri Feb 27 2004 Guillaume Cottenceau <gc@mandrakesoft.com> 1.4.4-3mdk
- rebuild
* Tue Jan 14 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.4.4-2mdk
- rebuild
* Sun Jan 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.4.4-1mdk
- 1.4.4
* Wed Jun 12 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 143-2mdk
- png icons (out xpm!)
* Tue Mar 12 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 143-1mdk
- new version
* Mon Oct 15 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 142-3mdk
- fix obsolete-tag Copyright
* Thu Jul  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 142-2mdk
- rebuild
- add man page
* Thu Mar 22 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 142-1mdk
- first mdk release
