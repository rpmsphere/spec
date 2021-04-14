%undefine _debugsource_packages

Name: xgammon
Version: 0.98a
Release: 16.1
Summary: An X Window System based backgammon game
License: GPL
Group: Games/Boards
URL: http://fawn.unibw-hamburg.de/steuer/xgammon/downloads.html
Source0: http://fawn.unibw-hamburg.de/steuer/xgammon/Downloads/%name-%version.tar.bz2
Source1: %name
Source2: %{name}16.png
Source3: %{name}32.png
Source4: %{name}48.png
Patch: %name-Imakefile-patch
Patch1: %name-0.98a-alt-gcc3.3.patch
BuildRequires: imake libX11-devel flex-static libXpm-devel libXt-devel libXaw-devel

%description
Xgammon is an X Window System based backgammon game.
Xgammon allows you to play against the computer, or you can play against
another person. Xgammon also supports playing a game against another person
on a remote X terminal, and will display a second board there for their use.

%prep
%setup -q
%patch -p0
%patch1 -p1
sed -i 's|-lm|-lm -Wl,--allow-multiple-definition|' Imakefile

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS" BINDIR=%_bindir LIBDIR=%_datadir PATH=$PATH:. CFLAGS+=-Wno-format-security

%install
rm -rf $RPM_BUILD_ROOT
perl -pi -e "s@lib/%name.db@%_datadir/%name/%name.db@" %name.ad
%makeinstall DESTDIR=$RPM_BUILD_ROOT BINDIR=%_bindir LIBDIR=%_datadir XAPPLOADDIR=%_datadir/X11/app-defaults

install -Dm 644 xgammon.6 $RPM_BUILD_ROOT%_mandir/man6/xgammon.6
install -Dm 644 %SOURCE2 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%name.png
install -Dm 644 %SOURCE3 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%name.png
install -Dm 644 %SOURCE4 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%name.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/xgammon.desktop <<EOF
[Desktop Entry]
Name=XGammon
Type=Application
Description=Backgamoon
Exec=xgammon
Icon=xgammon
Categories=Game;BoardGame;
EOF

%files
%{_bindir}/*
%{_datadir}/app-defaults
%{_datadir}/X11/app-defaults/XGammon
%{_datadir}/%name
%{_mandir}/man?/*
%{_datadir}/applications/xgammon.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%doc COPYING Copyright README

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Sep 29 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.98a
- Rebuilt for Fedora
* Fri Jan 09 2004 Stanislav Ievlev <inger@altlinux.org> 0.98a-alt3
- rebuild with gcc3.3
* Thu Oct 31 2002 Stanislav Ievlev <inger@altlinux.ru> 0.98a-alt2
- rebuild with gcc3
* Thu Aug 15 2002 Stanislav Ievlev <inger@altlinux.ru> 0.98a-alt1
- Adopted for ALT
* Wed Jun 05 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.98a-1mdk
- 0.98a
- png icons
- menu in spec
- remove patch{0,1,2}
- add patch3 (stupid space in Imakefile)
- cleanup
- add %%doc
* Wed Aug 01 2001 Stefan van der Eijk <stefan@eijk.nu> 0.98-17mdk
- fix BuildRequires
- fix too long description
- s/Copyright/License/
* Fri Jan 19 2001 Etienne Faure  <etienne@mandrakesoft.com> 0.98-16mdk
- small fixes
* Sat Dec 16 2000 Etienne Faure  <etienne@mandraksoft.com> 0.98-15mdk
- macros
* Thu Aug 31 2000 Mark Walker <mwalker@mandrakesoft.com> 0.98-14mdk
- Release build
* Wed Aug 16 2000 David BAUDENS <baudens@mandrakesoft.com> 0.98-13mdk
- Fix menu entry
- %%update_menus %%clean_menus
* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.98-12mdk
- automatically added BuildRequires
* Wed May 03 2000 dam's <damien@mandrakesoft.com> 0.98-11mdk
- Corrected icons.
* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 0.98-10mdk
- Convert gif icon to xpm.
* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 0.98-9mdk
- Added menu entry.
* Mon Mar 27 2000 dam's <damien@mandrakesoft.com> 0.98-8mdk
- Release.
* Fri Nov 12 1999 dam's <damien@mandrakesoft.com>
- Mandrake release
* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS
* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 14)
* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0
* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root
* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig
* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
