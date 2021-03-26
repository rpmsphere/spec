Summary:	A set of Solitaire type games for the X Window System
Name:		xpat2
Version:	1.07
Release:    46.1
License:	GPLv2+
Group:		Games/Cards
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/solitaires/%{name}-%{version}-src.tar.bz2	
Source1:	xpat2.png
Patch0:		xpat2-fixes.patch
Patch1:		xpat2-1.07-lib64.patch
Patch2:		xpat2-1.07-gcc41.patch
Patch3:		xpat2-1.07-fix-str-fmt.patch
BuildRequires:	gcc-c++
BuildRequires:	imake
BuildRequires:	qt3-devel
BuildRequires:	perl
BuildRequires:	libXpm-devel

%description
Xpat2 is a generic patience or Solitaire game for the X Window System.
Xpat2 can be used with different rules sets, so it can be used to play
Spider, Klondike, and other card games.

%prep
%setup -q
%patch0 -p1 -b kk1
%patch1 -p1 -b .lib64
%patch2 -p0 -b .gcc41
%patch3 -p0

%build
make clean
%__rm -f src/moc*
%__rm -f src/mqmaskedit.cpp
%__rm -f src/mqhelpwin.cpp

export PATH=%{_bindir}/X11:$PATH

find -type f | xargs perl -pi -e "s|/var/games/|/var/lib/games/|g"
find -type f | xargs perl -pi -e "s|usr/games|usr|g"
perl -p -i -e "s|xmkmf &&||" Makefile
cd src
xmkmf
perl -p -i -e "s|CXXDEBUGFLAGS = .*|CXXDEBUGFLAGS = $RPM_OPT_FLAGS|" Makefile
perl -p -i -e "s|CDEBUGFLAGS = .*|CDEBUGFLAGS = $RPM_OPT_FLAGS|" Makefile
# 1.0.7-1
perl -p -i -e "s|chown.*||" Makefile
perl -p -i -e "s|-lqt|-lqt-mt -lstdc++|" Makefile
perl -p -i -e "s|LN = ln -s|LN = echo|" Makefile
make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT \
	XPATROOT=$RPM_BUILD_ROOT/usr/lib/xpat \
	XPATMANDIR=$RPM_BUILD_ROOT/usr/share/man/man6 \
	APPDEFSDIR=$RPM_BUILD_ROOT/usr/share/X11

mkdir -p $RPM_BUILD_ROOT/var/lib/games/
touch $RPM_BUILD_ROOT/var/lib/games/xpat.log
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=XPat2
Comment=A set of Solitaire type games for the X Window System
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Qt;Game;CardGame;
EOF
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %buildroot

%files
/usr/lib/xpat/*
%{_mandir}/man6/*
%{_bindir}/xpat2
%if %{fedora}<21
/usr/lib/X11/app-defaults/XPat
%else
%{_datadir}/X11/app-defaults/XPat
%endif
%{_datadir}/X11/*/app-defaults/XPat
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
/var/lib/games/xpat.log

%changelog
* Sun Sep 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.07
- Rebuild for Fedora
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.07-27mdv2011.0
+ Revision: 671354
- mass rebuild
* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.07-26mdv2011.0
+ Revision: 608227
- rebuild
* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.07-25mdv2010.1
+ Revision: 524459
- rebuilt for 2010.1
* Sun Mar 08 2009 Emmanuel Andry <eandry@mandriva.org> 1.07-24mdv2009.1
+ Revision: 352726
- diff p3 to fix string format not literal
- fix license
- uncompress patches
  + Antoine Ginies <aginies@mandriva.com>
    - rebuild
* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.07-23mdv2009.0
+ Revision: 218427
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.07-23mdv2008.1
+ Revision: 179479
- rebuild
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'
* Thu Aug 23 2007 Funda Wang <fwang@mandriva.org> 1.07-22mdv2008.0
+ Revision: 70724
- fix prerequires
- fix comment of desktop entry
  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension
* Mon Apr 30 2007 Crispin Boylan <crisb@mandriva.org> 1.07-21mdv2008.0
+ Revision: 19451
- Fix menu name
* Mon Apr 30 2007 Crispin Boylan <crisb@mandriva.org> 1.07-20mdv2008.0
+ Revision: 19422
- XDG menu
- Fix buildRequires
- Rebuild, add gcc4.1 patch
- Import xpat2
* Fri Sep  9 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.07-19mdk
- menudir
* Fri Jun  4 2004  <lmontel@n2.mandrakesoft.com> 1.07-18mdk
- Rebuild
* Sun Dec 21 2003 Stefan van der Eijk <stefan@eijk.nu> 1.07-17mdk
- BuildRequires
- Add %%{_prefix}/X11R6/lib/X11/app-defaults symlink
- PreReq on rpm-helper
* Fri Sep 26 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.07-16mdk
- lib64 fixes
* Tue Sep 02 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.07-15mdk
- Fix compile with amd64
* Thu Aug 28 2003 Aurelien Lemaire <alemaire@mandrakesoft.com> 1.07-14mdk
- Add DIRM /usr/games/lib/xpat/
- Spec file permission fix to 644
- PreReq on rpm-helper
- Add Url on Source path
- Get out the 3 obsolete patch :
	xpat2-1.03-fsstnd.patch.bz2
	xpat2-1.04-xpm.patch.bz2
	xpat2-1.04-nobr.patch.bz2
* Thu Jul 17 2003 David BAUDENS <baudens@mandrakesoft.com> 1.07-13mdk
- Rebuild
* Tue Aug 27 2002 David BAUDENS <baudens@mandrakesoft.com> 1.07-12mdk
- Fix icon (menu)
* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.07-11mdk
- Automated rebuild with gcc 3.2-0.3mdk
* Tue Jul 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.07-10mdk
- use -lqt-mt (thx Laurent)
- png icons
- from Quel Qun <kelk1@hotmail.com> :
	- rebuild with qt3 and gcc3.2
* Thu Feb 28 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.07-9mdk
- fix path and perms for /var files, use a ghost file
* Tue Jan 22 2002 Stefan van der Eijk <stefan@eijk.nu> 1.07-8mdk
- BuildRequires
* Fri Dec 13 2001 Stefan van der Eijk <stefan@eijk.nu> 1.07-7mdk
- fix duplicate files in %%files section
* Thu Oct 11 2001 Etienne Faure <etienne@mandrakesoft.com> 1.07-6mdk
- Requires libpng2 ->libpng3
* Wed Sep 19 2001 Frederic Lepied <flepied@mandrakesoft.com> 1.07-5mdk
- fix path (Quel Qun).
* Thu Aug 30 2001 David BAUDENS <baudens@mandrakesoft.com> 1.07-4mdk
- Use new icons
* Tue Jul 17 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 1.07-3mdk
- Remove %%ifarch x86 section, it applies to all ports
* Sat Jul 07 2001 Stefan van der Eijk <stefan@eijk.nu> 1.07-2mdk
- BuildRequires:	qt2-devel
* Sat Jun 30 2001 Etienne Faure  <etienne@mandrakesoft.com> 1.07-1mdk
- version 1.07
* Sat Jan 20 2001 Etienne Faure  <etienne@mandrakesoft.com> 1.04-23mdk
- fixed menu entry
* Fri Dec  8 2000 Etienne Faure  <etienne@mandraksoft.com> 1.04-22mdk
- Rebuilt for ppc
- Macros
* Thu Aug 31 2000 Mark Walker <mwalker@mandrakesoft.com> 1.04-21mdk
- Release build
* Wed Aug 26 2000 David BAUDENS <baudens@mandrakesoft.com> 1.04-20mdk
- Fix menu entry
- Human readable spec
* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.04-19mdk
- automatically added BuildRequires
* Sun Jul 23 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.04-18mdk
- macroszifications
- update menus and clean menus macro
- BM
* Mon May 15 2000 David BAUDENS <baudens@mandrakesoft.com> 1.04-17mdk
- Fix build for i486
- Use %%{_tmppath} for BuildRoot
* Wed May 03 2000 dam's <damien@mandrakesoft.com> 1.04-16mdk
- Corrected icons.
* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 1.04-15mdk
- Convert gif icon to xpm.
* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 1.04-14mdk
- Added menu entry.
* Thu Mar 30 2000 dam's <damien@mandrakesoft.com> 1.04-13mdk
- Release.
* Wed Jan 12 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.04-12mdk
- Use bz2 sources.
* Thu Nov 6 1999 dam's <damien@mandrakesoft.com>
- Mandrake adaptation
* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 10)
* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0
* Thu Sep 17 1998 Jeff Johnson <jbj@redhat.com>
- use "mkdir -p" rather than mkdirhier to avoid IFS problem with bash-2.02.
* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root
* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig
* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
