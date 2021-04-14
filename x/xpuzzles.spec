Name:           xpuzzles
BuildRequires:  libX11-devel, libXt-devel
BuildRequires:  mesa-libGLU-devel
Version:        7.7.5
Release:        1.1
Summary:        Some games of skill under X11
License:        BSD-3-Clause
Group:          Amusements/Games/Board/Puzzle
URL:            http://www.tux.org/~bagleyd/puzzles.html
Source:         %{name}-%{version}.tar.bz2
%define progs barrel cubes dial dino hexagons mball mlink oct panex pyraminx rubik skewb threed triangles

%description
Use your wisdom and patience to solve these puzzles:
* xbarrel
* xcubes
* xdial
* xdino
* xhexagons
* xmball
* xmlink
* xoct
* xpanex
* xpyraminx
* xrubik
* xskewb
* xthreed
* xtriangles

%prep
%setup -q
sed -e 's/^#\(XT=${S.*G}\)$/\1/' -e 's/^\(XT=${R\)/#\1/' -i xpuzzles.Makefile

%build
export LIBS=-laudiofile
make -f xpuzzles.Makefile CFLAGS="$RPM_OPT_FLAGS"

%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man6/
for name in %{progs}; do
  install $name/x$name $RPM_BUILD_ROOT%{_bindir}
  if [ -f $name/x$name.man ]; then
    install -m 644 $name/x$name.man $RPM_BUILD_ROOT%{_mandir}/man6/x$name.6
  fi
done
# create score files
mkdir -p $RPM_BUILD_ROOT/var/games/xpuzzles
for dir in %{progs}; do
  touch $RPM_BUILD_ROOT/var/games/xpuzzles/$dir.scores
done

%files
%{_bindir}/*
%{_mandir}/man6/*
%dir /var/games/xpuzzles
%verify(not md5 size mtime) %config(noreplace) %attr(664,games,games) /var/games/xpuzzles/*.scores

%changelog
* Wed Dec 17 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 7.7.5
- Rebuilt for Fedora
* Sat May 12 2012 opensuse@dstoecker.de
- update to version 7.6.3
* Fri Aug 22 2008 lmichnovic@suse.cz
- update to version 7.4.1:
  * Strange character at end of help title removed.
  * pyraminx: Fixed a possible timing auto-solve problem.
* Fri Jul 18 2008 lmichnovic@suse.cz
- update to version 7.4
  * Leading function names in lowercase.
  * panex: Fixed background color problem.
  * pyraminx: Fixed turning bug when selecting face 2 then face 1
  when horizontal.
  * rubik, skewb, dino: Extra callback was causing 2d to go out of
  sync.
  * rubik: Mouse release sometimes was using wrong face.
* Thu Feb 28 2008 lmichnovic@suse.cz
- update to version 7.3.3
  * Constants changed.
  * Windows error fix for cubes, hexagons, mlink, rubik when
  changing size.
  * Added 3D look to frame for cubes, triangles, hexagons, panex.
  * rubik bug found when changing size while GL puzzle rotating.
  * rubik randomizes to a maximum of 100 moves.
  * Fixed drawing errors on mlink and barrel rotation.
  * barrel: 1B had and extra move in solution.
  * Updated action codes and sync'd Java and C code.
  * Various small changes.
* Thu Jul 26 2007 lmichnovic@suse.cz
- update to version 7.3.1 - obsoletes *strict_aliasing.patch
    Sound added for mball, pyraminx, oct, dino, skewb, rubik.
    barrel: Auto-solve.
    barrel: Fixes for get and write.
    mlink: Fix for get.
* Tue Jun 12 2007 lmichnovic@suse.cz
- fixed strict aliasing (*strict_aliasing.patch)
* Tue Jun 12 2007 lmichnovic@suse.cz
- update to version 7.3  Changes from last update:
  Html no longer corrupted.
  reverseVideo update.
  New bump.au sound, db lowered, and bumpdat.au removed, thanks
    to  http://audacity.sourceforge.net to help clean the sound up.
  Changed default so that practice is true for puzzles that have
    it:  xrubik, xskewb, xdino, xpyraminx, xoct, xmball, xmlink,
    xbarrel.
  Now use http://netpbm.sf.net to generate images from xpm.
  xdino: Fix some orient line OpenGL problems.
  xdino: Fix Period 2 OpenGL problems.
  wrubik, wskewb, wdino: Windows OpenGL stuff now ported.
  wcubes, wmlink, wpanex, wpyraminx, wrubik: Windows version
    interruptable on auto-solve.
  xpyraminx, xoct: Drag and drop between adjacent faces.
  xpyraminx: Fixed minor drawing errors for orient lines.
  xpyraminx: Fixed bug when changing to Period 2.
  xrubik, xskewb, xdino: drag and drop between adjacent faces.
  xdino: OpenGL for xdino added.
  xskewb, xdino: Orienting faces for OpenGL added.
  skewb: Control-Alt was not working right for OpenGL.
  xrubik, xskewb, xdino: added view option for OpenGL, "v".
  Fixed menu to assure the ok part of queries is handled correctly.
    (Bug fixed from redo change in xpanex, xmlink, xbarrel, xmball,
    xpyraminx, xoct, xrubik, xskewb, xdino).
* Wed Sep  6 2006 lmichnovic@suse.cz
- update to version 7.2.3
  cubes: Should now always work for all arrangements.
* Mon Aug  7 2006 lmichnovic@suse.cz
- fixed build with new X.org 7.x, detecting prefix in X.org
- using RPM_OPT_FLAGS
* Mon Aug  7 2006 lmichnovic@suse.cz
- update to version 7.2.2
  Changes:
    Fixed assorted memory leaks and uninitialized memory access reads.
    r is now for redo.  z is now the character for randomize.
    triangles: no more fully random positions, a starting position is
    made by randomly turning puzzle CCW or CW (+-120 degrees).
    hexagons (corners): shifting them down by 2's work.
    x=1 and y=n top and bottom pieces are always trapped.
    There are some positions that are weird...  x=1 y=3 and x=2 y=2 in
    particular and  and these cases have to have special handling.
    hexagons (no corners): shifted by 1, actually always solvable from
    EVERY position, except x=n y=1 this case is easily handled.
    cubes: Starting position instead of random
    Tried shifting by one and all reversed but made solutions too trivial.
    Starting pattern is ordered going down columns.
    Special case of 2x2x1 is handled (or else its solved already).
    Nx1x1 to be handled also.
    Some patterns require the last numbers to be swapped in order for the
    puzzle to be solvable.
* Tue Jun 20 2006 lmichnovic@suse.cz
- update to version 7.2.1
  * xrubik: undo needed debouncing on own window.
  * Recognize solved when doing undo where practice option exists.
  * xpanex: scan instant and undo at double speed.
  * xpanex: fixed drawing errors.
  * Made usage string compatible with versions of Motif and screen.
  * More defensive code in case getlogin fails.
  * panex: in hanoi mode illegal moves are handled better.
  * xmlink: solve fix for swapping left most middle tiles.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 23 2006 schwab@suse.de
- Don't strip binaries.
* Mon Jan  2 2006 lmichnovic@suse.cz
- update to version 7.1.5
- created scorefiles
* Sun Jan 11 2004 adrian@suse.de
- add %%defattr
* Fri Dec  5 2003 ltinkl@suse.cz
- update to version 7.0
* Thu Oct 23 2003 ltinkl@suse.cz
- updated to 5.7.3
* Wed Jun 11 2003 ltinkl@suse.cz
- clean the build root before install
* Mon Jun  9 2003 ltinkl@suse.cz
- updated sources to version 5.6.2
- created a patch to make xmball compile
* Tue Oct  9 2001 tcrhak@suse.cz
- update to 5.5.4.1
* Tue Apr 10 2001 vinil@suse.cz
- update to 5.5.3
- specfile cleanup
- source bzip2ed
* Sat Nov 18 2000 kukuk@suse.de
- Remove lesstif, no program need it
* Thu Apr 27 2000 vinil@suse.cz
- buildroot added
* Wed Jan 26 2000 ro@suse.de
- update to 5.5.2
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Mon Jul 12 1999 uli@suse.de
- now builds with lesstif
* Thu May  7 1998 fehr@suse.de
- add library -lXp for Motif 2.1
* Tue Dec  9 1997 ro@suse.de
- build static and dynamic versions
* Tue Oct 21 1997 ro@suse.de
- ready for autobuild
