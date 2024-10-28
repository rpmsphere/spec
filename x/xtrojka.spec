Summary:        An X Window System falling blocks game
Name:           xtrojka
Version:        1.2.3
Release:        12.1
License:        Distributable
Group:          Games/Arcade
BuildRequires:  libX11-devel libXaw-devel Xaw3d-devel libXpm-devel
Source0:        ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/xtrojka123.tar.bz2
URL:            ftp://ftp.funet.fi/pub/unix/games/
Source2:        %{name}-16.png.bz2
Source3:        %{name}-32.png.bz2
Source4:        %{name}-48.png.bz2
Patch0:         xtrojka-1.2.3-make.patch.bz2
Patch1:         xtrojka-errno.patch.bz2

%description
The xtrojka game is an X Window System game of falling blocks, like Xjewel or
Tetris.

%prep
%setup -q -n xtrojka123
%patch 0 -p1
%patch 1 -p1

%build
cp XTrojka.uk XTrojka
./resgen
make CFLAGS="$RPM_OPT_FLAGS -DXPM -DLINUX -DSCOREFILE='\"/var/lib/games/xtrojka.scores\"'"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man6
mkdir -p $RPM_BUILD_ROOT/var/lib/games

make    TARGET_DIR=$RPM_BUILD_ROOT/usr/bin \
        MANDIR=$RPM_BUILD_ROOT/usr/share/man/man6 \
        HSFILE=$RPM_BUILD_ROOT/var/lib/games/xtrojka.score \
        install
sed -i 's|'$RPM_BUILD_ROOT'||' $RPM_BUILD_ROOT/usr/share/man/man6/xtrojka.6
chmod 0666 $RPM_BUILD_ROOT/var/lib/games/xtrojka.score

install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
bzcat %{SOURCE2} >$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
bzcat %{SOURCE3} >$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
bzcat %{SOURCE4} >$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=XTrojka
Comment=A tetris game
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Categories=Game;ArcadeGame;
EOF

%files
%doc AUTHOR COPYRIGHT MANIFEST README YIKES
%{_bindir}/xtrojka
%{_mandir}/man6/xtrojka.6*
%{_datadir}/applications/%{name}.desktop
/var/lib/games/xtrojka.score
%{_datadir}/icons/hicolor/16x16/apps/*.png
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png

%changelog
* Sun Sep 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.3
- Rebuilt for Fedora
* Wed Sep 13 2006 Nicolas Lécureuil <neoclust@zarb.org> 1.2.3-5plf2007.0
- Rebuild
* Sun Apr 23 2006 Michael Scherer <misc@zarb.org> 1.2.3-4plf
- use mkrel
* Sat Sep 25 2004 Michael Scherer <misc@zarb.org> 1.2.3-3plf 
- rebuild
* Wed Jul 23 2003 Michael Scherer <scherer.michael@free.fr> 1.2.3-2plf 
- fix compilation ( patch #1 )
* Wed Jun 05 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2.3-1plf
- mdk => plf (see COPYRIGHT)
* Tue Jun 04 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2.3-17mdk
- xpm icons ( out xpm!)
- menu file in spec
- add %%doc files
* Thu Aug 23 2001 Etienne Faure <etienne@mandrakesoft.com> 1.2.3-16mdk
- rebuild
* Tue Mar  6 2001  Daouda Lo <daouda@mandrakesoft.com> 1.2.3-15mdk
- spec cleanup 
- rebuild 
* Fri Sep 15 2000 David BAUDENS <baudens@mandrakesoft.com> 1.2.3-14mdk
- Fix Title in Menu entry
- Macros
- %%{update_menus} & %%{clean_menus}
- Remove stupid hard coded PATH for icon in menu entry
* Fri Sep 01 2000 Alexis Younes <ayounes@mandrakesoft.com> 1.2.3-13mdk
- Release
* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2.3-12mdk
- automatically added BuildRequires
* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 1.2.3-11mdk
- Convert gif icon to xpm.
* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 1.2.3-10mdk
- Added menu entry.
* Mon Mar 27 2000 dam's <damien@mandrakesoft.com> 1.2.3-9mdk
- Release.
* Fri Nov 5 1999 dam's <damien@mandrakesoft.com>
- Mandrake release
* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS
* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)
* Mon Dec 21 1998 Michael Maher <mike@redhat.com>
- built package for 6.0
* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root
* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new version
- wmconfig
* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
