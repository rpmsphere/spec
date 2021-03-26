%define srcname Phalanx
%define srcver  XXV

Name:           phalanx
URL:            http://sourceforge.net/projects/phalanx
Version:        25
Release:        1
Source:         http://downloads.sourceforge.net/project/phalanx/Version%20%{srcver}/%{name}-%{srcver}-source.tgz
Patch0:         Phalanx-XXII.diff
# PATCH-FIX-UPSTREAM phalanx-castling-broken.patch bnc#819525 mike.catanzaro@gmail.com -- fix castling always treated as illegal move
Patch1:         phalanx-castling-broken.patch
Summary:        A Chess Program
License:        GPL-2.0+
Group:          Amusements/Games/Board/Chess

%description
A smart chess playing program which uses opening book.

Authors:
--------
    Dusan Dobes <dobes@math.muni.cz>

%prep
%setup -q -n %{srcname}-%{srcver}
%patch0 -p1
%patch1 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
install -d $RPM_BUILD_ROOT/usr/bin/
install -d $RPM_BUILD_ROOT/usr/share/phalanx/
install -m 0755 {x,}phalanx $RPM_BUILD_ROOT/usr/bin/
install -m 0644 eco.phalanx pbook.phalanx sbook.phalanx $RPM_BUILD_ROOT/usr/share/phalanx

%files
%doc COPYING HISTORY README
%{_datadir}/phalanx
%{_bindir}/*

%changelog
* Fri Dec 28 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 25
- Rebuild for Fedora
* Mon May 11 2015 pgajdos@suse.com
- updated to XXIV
  * Xboard protocol - 'memory' command support.
  * New file phalanx.eng to support the new Xboard automatic engine
    load.
  * More log messages.
  * Late move reductions with move count based pruning.
  * Small but important changes in the static evaluation that improve
    endgame play: Passed pawn, rook mobility, knight mobility.
  * Default contempt factor changed from -20 to -10.
  * Fixed tournament timecontrols.
  * Positional  learning is now off by default.
  * Tweaked polling input timeslice to better handle rapid changes
    in analyze mode.
  * Fixed GCC warnings.
* Wed Nov 19 2014 pgajdos@suse.com
- updated to XXIII final
  * Xboard protocol version 2 compatibility.
  * New -n commandline option to limit nodes per second.
  * New -z commandline option to randomize root moves.
  * Easy levels now don't play instantly, but use time.
  * DrawScore (contempt factor) adjusted in endgames towards
    positive values to avoid playing dead draws like KRKR.
  * Minor engine fixes.
  * see HISTORY for details
* Sat May 18 2013 mike.catanzaro@gmail.com
- Add phalanx-castling-broken.patch to fix castling (bnc#819525)
* Tue Aug  7 2012 pgajdos@suse.com
- updated to XXIII-beta
* Fri Mar 23 2012 jengelh@medozas.de
- Parallel build with %%_smp_mflags; strip redundant sections/tags
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Jun 16 2005 meissner@suse.de
- use RPM_OPT_FLAGS
* Mon Apr 18 2005 mcihar@suse.de
- fix for current gcc
* Mon Jan 12 2004 adrian@suse.de
- let rpm strip
* Mon Sep 15 2003 adrian@suse.de
- Provide general "chess_backend" alias
* Tue May 13 2003 mcihar@suse.cz
- added %%defattr(-,root,root)
* Thu Nov 21 2002 mcihar@suse.cz
- bzipped sources
- fixed multiline string
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Mon Nov 20 2000 pblaha@suse.cz
- create this pakage
