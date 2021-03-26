Name		: crimson-fields
Version		: 0.5.3
Release		: 1
License		: GPLv2+
Group		: Amusements/Games
URL		: http://crimson.seul.org/
Source		: http://crimson.seul.org/files/crimson-%{version}.tar.bz2
Summary		: A hex-based tactical war game
BuildRequires   : SDL-devel >= 1.1.5, SDL_ttf-devel
BuildRequires   : gawk, zlib-devel

%description
Crimson Fields is a tactical war game in the tradition of Battle Isle for
one or two players.

The outcome of the war lies in your hands. You decide which units are
sent to the front lines, and when to unleash the reserves. Your mission
objectives range from defending strategically vital locations to simply
destroying all enemy forces in the area. Protect supply convoys or raid
enemy facilities to uncover technological secrets or fill your storage
bays so you can repair damaged units or build new ones in your own
factories. Lead your troops to victory!

Tools are available to create custom maps and campaigns. You can also play
the original Battle Isle maps if you have a copy of the game.

%prep
%setup -q -n crimson-%{version}

%build
LDFLAGS="-Wl,--as-needed" \
CFLAGS="$RPM_OPT_FLAGS" \
CXXFLAGS="$RPM_OPT_FLAGS" %configure \
	--enable-cfed --enable-bi2cf --enable-comet
%{__make} %{?_smp_flags}

%install
rm -rf "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf "$RPM_BUILD_ROOT"

%files 
%doc COPYING NEWS README* THANKS TODO music/COPYING.MUSIC
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/crimson
%{_datadir}/pixmaps/*
%{_mandir}/man6/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.3
- Rebuild for Fedora
* Sat Jul  4 2009 Peter Hanecak <hany@hany.sk> 0.5.3-1
- updated to 0.5.3
* Sun May 11 2008 Peter Hanecak <hany@hany.sk> 0.5.2-1
- updated to 0.5.2
* Fri Oct 12 2007 Peter Hanecak <hany@hany.sk> 0.5.1-1
- adapted to Doors 11.0 (Fedora 7)
* Thu Mar 10 2005 Jens Granseuer <jensgr@gmx.net>
- remove unused prefix definition
- add desktop file
* Tue Apr 20 2004 Jens Granseuer <jensgr@gmx.net>
- include COPYING.MUSIC
* Sun Feb 22 2004 Jens Granseuer <jensgr@gmx.net>
- require SDL_ttf
* Sat Sep 20 2003 Jens Granseuer <jensgr@gmx.net>
- distribute icon
- use system directories
* Fri Aug 22 2003 Jens Granseuer <jensgr@gmx.net>
- updated URLs
* Sat Dec 7 2002 Jens Granseuer <jensgr@gmx.net>
- update for 0.3.0
- build and install the new bi2cf tool by default
* Fri Jun 28 2002 Jens Granseuer <jensgr@gmx.net>
- renamed ChangeLog to NEWS
* Wed Apr 24 2002 Jens Granseuer <jensgr@gmx.net>
- added THANKS and TODO files to docs
* Sun Jul 22 2001 Jens Granseuer <jensgr@gmx.net>
- use CXXFLAGS instead of CFLAGS
* Thu May 17 2001 Jens Granseuer <jensgr@gmx.net>
- include manual pages
* Sun Apr 22 2001 Jens Granseuer <jensgr@gmx.net>
- require SDL 1.1.5
* Wed Mar 7 2001 Jens Granseuer <jensgr@gmx.net>
- updated to 0.1.1
- set Group to Amusements/Games
* Thu Mar 1 2001 Jens Granseuer <jensgr@gmx.net>
- initial public release
