Name:           between
Version:        6
Release:        6.1
Summary:        A game about consciousness and isolation
Group:          Amusements/Games/Other
License:        SUSE-Public-Domain
URL:            https://www.esquire.com/features/best-and-brightest-2008/rohrer-game
Source0:        https://sourceforge.net/projects/hcsoftware/files/Between_v%{version}_UnixSource.tar.gz
BuildRequires:  SDL-devel, gcc-c++, desktop-file-utils

%description
You know exactly what you need to do -- you can see it shimmering right there
in front of you. You can see it while dreaming, too, and the difference has
become subtle. Dreams wake into dreams, and people blend in and out:
real characters and dream characters, all woven into the same script. Finally,
they fade completely, and you're alone in the expanse with the construction.
With time, you feel something growing, a pinhole that eventually yawns into
a deep ravine of longing. The construction languishes, though the expanse
seems indifferent.

One night, in a dream, they appear: things that you clearly could not have
conjured on your own. Not snowflakes. Not the self-similar forms of leaves.
Not distant planets' erosion networks as viewed through telescopes. Not those
things that are beautifully external but lack the signatures of consciousness.
These things that appear are ugly and non-procedural: indecipherable
transmissions bubbling up through static, faded messages floating in bottles,
and charcoal handprints on cave walls. Evidence has reached you through time
of unknown duration and distance of unknown magnitude, but stale evidence is
still evidence.

Somewhere, across whatever barriers stand between, is an other.

-- Jason Rohrer, November 4, 2008

%prep
%setup -q -n Between_v%{version}_UnixSource

%build
# Configure
cd game7
%__rm -f Makefile
%__cat Makefile.GnuLinux Makefile.common ../minorGems/build/Makefile.minorGems gameSource/Makefile.all ../minorGems/build/Makefile.minorGems_targets > gameSource/Makefile

# Make
cd gameSource
%__make

# Doc
%__cp ../documentation/Readme.txt %_builddir/%{name}_v%{version}_UnixSource

%install
rm -rf %buildroot
%__mkdir %buildroot

%__mkdir_p %buildroot%{_datadir}/%{name}/graphics
%__mkdir_p %buildroot%{_datadir}/%{name}/music
%__mkdir_p %buildroot%{_datadir}/%{name}/settings
%__mkdir_p %buildroot%{_datadir}/%{name}/languages
%__mkdir_p %buildroot%{_bindir}
%__mkdir_p %buildroot%{_mandir}/man6

%__install -m 755 game7/gameSource/Between %buildroot%{_bindir}/between-exe
%__install -m 644 game7/gameSource/graphics/* %buildroot%{_datadir}/%{name}/graphics
%__install -m 644 game7/gameSource/music/*  %buildroot%{_datadir}/%{name}/music
%__install -m 644 game7/gameSource/settings/*  %buildroot%{_datadir}/%{name}/settings
%__install -m 644 game7/gameSource/languages/*  %buildroot%{_datadir}/%{name}/languages
%__install -m 644 game7/gameSource/language.txt  %buildroot%{_datadir}/%{name}

echo -e '#!/bin/bash\ncd %{_datadir}/%{name}\n%{_bindir}/between-exe\nexit' > %buildroot%{_bindir}/between
%__chmod +x %buildroot%{_bindir}/between

# Man pages (added by packager, not present in source)
#__cp %_sourcedir/Between.6 %buildroot%{_mandir}/man6/between.6
#__cp %_sourcedir/Between-exe.6 %buildroot%{_mandir}/man6/between-exe.6

%clean
rm -rf %buildroot

%files
%doc game7/documentation/*.txt
#{_mandir}/man6/between.6*
#{_mandir}/man6/between-exe.6*
%{_datadir}/%{name}
#{_datadir}/applications/between.desktop
%{_bindir}/between-exe
%{_bindir}/between

%changelog
* Tue Feb 03 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 6
- Rebuilt for Fedora
* Fri Dec 28 2012 1Antoine1 <antoine.belvire@laposte.net> version 6
- Added .desktop file
* Sun Jun 24 2012 1Antoine1 <antoine.belvire@laposte.net> version 6
- Created rpm.
- Added man pages.
* Thu Aug 26 2010  Jason Rohrer <jasonrohrer@fastmail.fm>  version 5 (probably wrong release date)
- Fixed pointer arithmetic in WebRequest code to work on 64-bit platforms 
  (thanks to David Turner).
- Got working against latest minorGems code.
- Fixed string warnings triggered by newer GCC versions.
* Wed Nov 12 2008 Jason Rohrer <jasonrohrer@fastmail.fm>  version 5
- Fixed scaling and position of text strings to avoid aliasing artifacts.
- Disabled compiler optimizations to avoid GCC 4.0 bug.
- Set windowed mode as default (so that you can use other apps to give your
  friend a game code).
- Fixed bug that allowed blocks to be added floating in air if selector moved
  up just as block added.
- Fixed window title.
* Mon Nov 10 2008 Jason Rohrer <jasonrohrer@fastmail.fm>  version 4, changes to make block constructor's function more clear
- Added ghosted block grid template inside constructor.
- Added "W" hint that appears when constructor full.
* Tue Nov 4 2008 Jason Rohrer <jasonrohrer@fastmail.fm>  version 3
- Initial release for private beta testing.
