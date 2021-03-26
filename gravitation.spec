%global _name Gravitation

Name:           gravitation
Version:        3
Release:        8.1
Summary:       	A video game about mania, melancholia, and the creative process
Group:          Amusements/Games/Other
License:        SUSE-Public-Domain
URL:            http://hcsoftware.sourceforge.net/gravitation/
Source0:        http://sourceforge.net/projects/hcsoftware/files/%{_name}_v%{version}_UnixSource.tar.gz
Patch0:			Gravitation_v3_UnixSource-lpthread_issue.patch
BuildRequires:  SDL-devel, desktop-file-utils

%description
Gravitation is a 8-minute-long video game dealing with mania, melancholia,
and the creative process. It is the fourth game created by Jason Rohrer.

%prep
%setup -q -n %{_name}_v%{version}_UnixSource
%patch0 -p1 -b .lpthread_issue

%build
cd game5/gameSource
%__rm -f Makefile
%__cat Makefile.GnuLinux Makefile.all > Makefile
%__make
%__cp ../documentation/Readme.txt ../documentation/toDo.txt %_builddir/%{_name}_v%{version}_UnixSource

%install
rm -rf %buildroot
%__mkdir %buildroot

%__mkdir_p %buildroot%{_datadir}/%{name}/graphics
%__mkdir_p %buildroot%{_datadir}/%{name}/music
%__mkdir_p %buildroot%{_datadir}/%{name}/settings
%__mkdir_p %buildroot%{_bindir}
%__mkdir_p %buildroot%{_mandir}/man6

%__install -m 755 game5/gameSource/Gravitation %buildroot%{_bindir}/Gravitation-exe
%__install -m 644 game5/gameSource/graphics/* %buildroot%{_datadir}/%{name}/graphics
%__install -m 644 game5/gameSource/music/*  %buildroot%{_datadir}/%{name}/music
%__install -m 644 game5/gameSource/settings/*  %buildroot%{_datadir}/%{name}/settings

echo -e '#!/bin/bash\ncd %{_datadir}/%{name}\n%{_bindir}/Gravitation-exe\nexit' > %buildroot%{_bindir}/gravitation
%__chmod +x %buildroot%{_bindir}/gravitation

# Man pages (added by packager, not present in source)
#__cp %_sourcedir/Gravitation.6 %buildroot%{_mandir}/man6/gravitation.6
#__cp %_sourcedir/Gravitation-exe.6 %buildroot%{_mandir}/man6/Gravitation-exe.6

%clean
rm -rf %buildroot

%files
%doc Readme.txt
#{_mandir}/man6/gravitation.6*
#{_mandir}/man6/Gravitation-exe.6*
%{_datadir}/%{name}
#{_datadir}/applications/gravitation.desktop
%{_bindir}/Gravitation-exe
%{_bindir}/gravitation

%changelog
* Tue Feb 17 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 3
- Rebuild for Fedora
* Fri Dec 28 2012 1Antoine1 <antoine.belvire@laposte.net> version 3
- Added .desktop file
* Mon Jun 25 2012 1Antoine1 <antoine.belvire@laposte.net> version 3
- Created rpm.
- Added man pages.
* Sat Mar 1 2008 Jason Rohrer <jasonrohrer@fastmail.fm> version 3 
- (Thanks to Chris Hecker for pointing out that player-freeze during fade-out
felt weird.)
- Re-enabled player motion during game-end fade-out.
- Added a 3-second title-screen freeze after fade-out to ensure that the player knows that the game is really over (so that key presses during the fade-out do not trigger a new game instantly).
- Kiln now stops melting blocks (because fire is gone) during fade-out
* Fri Feb 29 2008 Jason Rohrer <jasonrohrer@fastmail.fm> version 2
- Increased fade-out time at end of game.
- Froze player during game-over fade-out.
* Fri Feb 29 2008 Jason Rohrer <jasonrohrer@fastmail.fm> version 1
- Initial release.
