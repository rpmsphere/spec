Name:           scid
BuildRequires:  gcc-c++ tcl-devel libX11-devel
Summary:        A chess database application
License:        GPLv2
Group:          Amusements/Games
Requires:       tcl python2
Version:        4.7.0
Release:        1
URL:            https://scid.sourceforge.net/
Source:         https://sourceforge.net/projects/scid/files/Scid/Scid%204.7/%{name}-code-%{version}.zip
Source1:	%{name}.png
Source2:	%{name}.desktop 
Source3:	%{name}.6

%description 
Scid can perform many different searches, such as for particular
players, a certain opening position, material searches, and pattern
searches such as isolated pawns. It is very fast, because it uses its
own efficient format, but it can convert games to and from PGN, the
standard format for chess game files.

Scid can use a chess engine such as Crafty to analyze games and also
has a "tree" mode where it automatically shows all moves played from
the current position, their opening codes, success rates, etc.


Authors:
--------
	Shane Hudson <shane@cosc.canterbury.ac.nz> original scid up to 3.6.1
	pgeorges (at) users.sourceforge.net later versions
and
	Peter van Rossum <petervr@debian.org> (manual page)

%prep
%setup -q -n %{name}

%build
./configure --prefix=/usr\
	BINDIR=%{_bindir} \
	SHAREDIR=%{_datadir}/scid \
	OPTIMIZE="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -Wno-narrowing"
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
# install sound files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/scid/sounds/
install -m 644 sounds/* $RPM_BUILD_ROOT%{_datadir}/scid/sounds/
# install desktop file & icon
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/scid.png
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/scid.desktop
# install man page
install -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man6/scid.6

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING TODO ChangeLog
%{_datadir}/scid/
%{_datadir}/applications/scid.desktop
%{_datadir}/pixmaps/scid.png
%{_bindir}/*
%{_mandir}/man6/scid*

%changelog
* Tue Jan 07 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 4.7.0
- Rebuilt for Fedora
* Thu Apr 22 2010 mantel@suse.de
- fix language dependant bug in ECO browser
* Tue Mar  9 2010 packman@links2linux.de - 4.2.2
- changed installation location for included extra engines phalanx and togaII from /usr/share/scid/engines/ to /usr/bin
- renamed engine togaII to togaII-1.2.1a-scid to avoid potential conflicts with already installed togaII-engines
- removed obsolete rpmlintrc-file
* Wed Jan 20 2010 axel@links2linux.de - 4.2.2
- updated to version 4.2.2
  * Training -> Find best move : make it more user friendly :
    The next moves are automaticaly hidden in PGN window and in game info window
    Added buttons above the board to show solution, go to next / previous exercise
    Leave the training mode by unchecking the menu entry
  * updated swedish translation (thanks to Hans Eriksson)
  * updated spanish translation (thanks to Pedro Reina)
  * Scid Pocket : added Stockfish 1.6.2 ported to ARM (Windows Mobile)
  * FIDE changed the number of rating list per year. Add code to handle this properly.
    Maximum year for ratings added by spellchecker is _2010_. (Thanks to Joost 't Hart)
  * Searching for !me (own games) was broken
  * Xfcc passwords with XML entities were not handled correctly
- fixed building with RPM_OPT_FLAGS
* Wed Jan  6 2010 AxelKoellhofer@web.de
- updated to version 4.1
- removed obsolete patch to fix comments on last move (fixed upstream)
* Thu Sep 17 2009 AxelKoellhofer@web.de
- added upstream fix for entering comments on last move
* Wed Sep  2 2009 AxelKoellhofer@web.de
- updated to 4.0 (see /usr/share/doc/packages/scid/ChangeLog for all the new features)
- added desktop file and icon
- enabled sound
- added Obsoletes/Provides/Recommends
- patches refreshed
- added python to Requires
- changed License tag to GPL v2 (the file COPYING contains GPL v2 and no other version)
* Fri Aug 21 2009 AxelKoellhofer@web.de
- updated to 3.7.3
- patches refreshed
* Thu Feb  7 2008 detlef.steuer@gmx.de
- updated for 3.6.22
* Mon Jan 14 2008 detlef.steuer@gmx.de
- updated for 3.6.21
* Sat Nov 24 2007 detlef.steuer@gmx.de
- first try with pgeorges scid
* Sat Oct 28 2006 meissner@suse.de
- use RPM_OPT_FLAGS
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Mar  3 2004 mcihar@suse.cz
- update to 3.6.1
* Mon Feb 23 2004 mcihar@suse.cz
- update to 3.5
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Mon Sep 22 2003 ro@suse.de
- do not provuide phalanx
* Mon Jul 28 2003 ro@suse.de
- added tk-devel to neededforbuild
* Tue May 27 2003 mcihar@suse.cz
- move binaries to /usr/bin
* Thu Feb  6 2003 mcihar@suse.cz
- updated to 3.4
  * Scid now has its own built-in analysis engine called Scidlet;
  you can still use other WinBoard-compatible engines for
  analysis in Scid, of course.
  * New Player Finder window.
  * More improvements to the Tablebase window.
  * Moves on the main window chessboard are now animated.
  * Lots of small user interface improvements.
  * Added support for entering null (empty) moves in games.
* Mon Aug 19 2002 ro@suse.de
- add "-DUSE_NON_CONST" to cflags for new tcl
* Fri Jul 12 2002 max@suse.de
- Patching Makefile.conf and using configure instead of
  patching Makefile, so that the Tcl/Tk version can be
  detected at build time.
* Thu Jun 13 2002 mcihar@suse.cz
- updated to 3.3:
  * New "Piece Tracker" tool, new "Filter Graph" window
  * Maintenance window: new "Strip PGN tags" operation that finds
  extra PGN tags and allows the user to remove all instances of
  a particular unwanted tag.
  * Added "Load Random Game" menu command in the Game menu.
  * Extended search capabilities
  * Improved reading of annotations in PGN.
  * Removed limitation of game to 128 moves.
  * Improved the look of piece images in the chessboard.
* Wed Apr 24 2002 pmladek@suse.cz
- used macro %%%%{_lib} to fix for lib64
* Tue Jan 29 2002 pmladek@suse.cz
- updated to version 3.1
* Wed Dec  5 2001 pmladek@suse.cz
- updated on version 3.0:
  * new database format
  * new "Bookmarks" feature
  * new "Tip of the day" window
  * most window locations and sizes are now saved in the options file
  when "Save Options" is selected.
  * tree window: New "Best games" window
  * 12 new user-settable "flags" for marking games with various chess
  characteristics.
- added tk to Requires
- fixed to load spelling.ssp
* Mon Jun 25 2001 pblaha@suse.cz
- update on 2.5
* Wed May 30 2001 pblaha@suse.cz
- update on 2.4
- rewrite URL
* Wed May  9 2001 mfabian@suse.de
- bzip2 sources
* Tue Jan 16 2001 pblaha@suse.cz
- create this package
