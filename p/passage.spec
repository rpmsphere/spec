%global _name Passage

Name:           passage
Version:        4
Release:        7.1
Summary:        A Gamma256 video game by Jason Rohrer
Summary(fr):	Un jeu vidéo Gamma256 par Jason Rohrer
Group:          Amusements/Games/Other
License:        SUSE-Public-Domain
URL:            http://hcsoftware.sourceforge.net/passage/
Source0:        http://sourceforge.net/projects/hcsoftware/files/%{_name}_v%{version}_UnixSource.tar.gz
BuildRequires:  SDL-devel, gcc-c++, desktop-file-utils

%description
Passage is a 5-minute-long game which was selected for exhibition at
Kokoromi's Gamma256 event. It works on Mac, Windows and Linux.

%description -l fr
Passage est un jeu de cinq minutes qui a été présenté au salon Kokoromi
Gamma256. Il fonctionne sous Mac, Windows and Linux.

%prep
%setup -q -n %{_name}_v%{version}_UnixSource

%build
cd gamma256/gameSource
%__rm -f Makefile
%__cat Makefile.GnuLinux Makefile.all > Makefile
%__make
%__cp ../documentation/Readme.txt %_builddir/%{name}_v%{version}_UnixSource

%install
rm -rf %buildroot
%__mkdir %buildroot

%__mkdir_p %buildroot%{_datadir}/%{name}/graphics
%__mkdir_p %buildroot%{_datadir}/%{name}/music
%__mkdir_p %buildroot%{_datadir}/%{name}/settings
%__mkdir_p %buildroot%{_bindir}
%__mkdir_p %buildroot%{_mandir}/man6

%__install -m 755 gamma256/gameSource/Passage %buildroot%{_bindir}/Passage-exe
%__install -m 644 gamma256/gameSource/graphics/* %buildroot%{_datadir}/%{name}/graphics
%__install -m 644 gamma256/gameSource/music/*  %buildroot%{_datadir}/%{name}/music
%__install -m 644 gamma256/gameSource/settings/*  %buildroot%{_datadir}/%{name}/settings

echo -e '#!/bin/bash\ncd %{_datadir}/%{name}\n%{_bindir}/Passage-exe\nexit' > %buildroot%{_bindir}/Passage
%__chmod +x %buildroot%{_bindir}/Passage

# Man pages (added by packager, not present in source)
#__cp %_sourcedir/Passage.6 %buildroot%{_mandir}/man6
#__cp %_sourcedir/Passage-exe.6 %buildroot%{_mandir}/man6

%clean
rm -rf %buildroot

%files
%doc gamma256/documentation/*.txt
#{_mandir}/man6/Passage.6*
#{_mandir}/man6/Passage-exe.6*
%{_datadir}/%{name}
#{_datadir}/applications/passage.desktop
%{_bindir}/Passage-exe
%{_bindir}/Passage

%changelog
* Fri Feb 20 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 4
- Rebuilt for Fedora
* Fri Dec 28 2012 1Antoine1 <antoine.belvire@laposte.net> version 4
- Added .desktop file
* Tue Jun 12 2012 1Antoine1 <antoine.belvire@laposte.net> version 4
- Created rpm.
- Added man pages.
* Mon May 24 2010 Jason Rohrer <jasonrohrer@fastmail.fm>  version 4
- Fixed error in application of patch for older SDL versions.
- Fixed random number generation so that it works on 64-bit platforms (thanks
  to Kevin Fan).
- Fixed chest gem selection behavior on certain platforms (like iPhone).
- Fixed unsafe use of pointers into vector (triggered a bug with new shorter
  default vector size).
- Fixed string warnings that are caught by certain GCC versions.
* Thu Dec 13 2007 Jason Rohrer <jasonrohrer@fastmail.fm> version 3
- Switched to analog stick on 360 controller for much smoother play.
- Added patch for older SDL versions provided by Jarno van der Kolk.
- Added ESC in addition to Q to quit.
- Added settings files for controlling screen size and fullscreen mode.
* Tue Nov 13 2007 Jason Rohrer <jasonrohrer@fastmail.fm> version 2
- Added chiptune music soundtrack.
- Improved star sprite.
- Fixed bug with window sizing (manifested by title being set too low).
- Improved behavior of screen blow-up/blow-down keys.
- Fixed bug in game reset that can result in artifacts during subsequent plays.
- Fixed artifacts after screen blow-up factor change on double-buffered 
  platforms.
- Fixed problem with screen pitch.
- Now builds for MacOSX 10.2 and higher (using MinGW and SDL).
- Unix source distribution now available (compiles against SDL developer 
  library).
* Thu Nov 1 2007 Jason Rohrer <jasonrohrer@fastmail.fm> version 1
- Initial release (Gamma256 submission)
