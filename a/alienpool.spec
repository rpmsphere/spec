Name:			alienpool
Summary:		Arcade-style mix of asteroids and pool
Version:		0.2.0
Release:		14.4
Source:			%{name}-%{version}.tar.bz2
URL:			https://mkorman.org/alienpool/
Group:          	Amusements/Games/Action/Arcade
License:		GPLv2
BuildRequires:		desktop-file-utils
BuildRequires:		gcc-c++
BuildRequires:			pkgconfig
BuildRequires:			SDL-devel
BuildRequires:			SDL_image-devel
BuildRequires:			SDL_mixer-devel
BuildRequires:			SDL_ttf-devel

%description
Alienpool is a space-shooter that is similar to both asteroids
and pool. Move a spaceship around the screen and shoot at aliens.
Aliens that have been shot bounce around the screen and hit other
aliens.

%prep
%setup -q
sed -i 's|games/%{name}|%{name}|' src/Makefile* data/Makefile*

%build
%configure
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -D -m 2755 src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 644 data/%{name}-48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}-48.png
install -D -m 644 data/%{name}.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.xpm
install -D -m 644 doc/%{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6

mkdir -p $RPM_BUILD_ROOT/var/games
install -m 664 %{name}.scores $RPM_BUILD_ROOT/var/games

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
install -m 644 data/sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
install -m 644 data/sounds/*.ogg $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds

for i in alien alienbullet bullet dumbalien healthbonus hyperbonus ship shootbonus thrustship
do
 mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/$i
 install -m 644 data/sprites/$i/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/$i
 install -m 644 data/sprites/$i/info $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/$i
done

for i in h.png s.png starscape.png alienpool.xpm mainmenu.png VeraBI.ttf
do
 install -m 644 data/$i $RPM_BUILD_ROOT%{_datadir}/%{name}/$i
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m 644 %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

desktop-file-install                                    \
 --delete-original                                      \
 --vendor ""                                            \
 --dir $RPM_BUILD_ROOT%{_datadir}/applications          \
 --add-category Game                                    \
 --add-category ArcadeGame                              \
 $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%files
%{_datadir}/pixmaps/%{name}*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man6/%{name}*
%doc README NEWS COPYING AUTHORS
%{_bindir}/%{name}
/var/games/%{name}.scores

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
* Thu Dec 13 2007 David Bolt <davjam@davjam.org>
- Updated the spec file.
-  Now follows package naming conventions for Mandriva,
-  Fedora and openSUSE.
* Sun Oct 16 2005 David Bolt <davjam@davjam.org>
- first ported to SuSE 9.3
- repacked source using bzip2
- added a .desktop file
* Sat Mar 27 2004 Michael J. Korman <mike@taequin.org>
- Version 0.2.0.
- Added spaceship inertia for realism and challenge.
- Fixed bug that caused input events to be buffered during "Level" screen.
- Fixed bug that caused input events to be buffered during "Game Over" screen.
- Added icons that indicate which bonuses are currently active.
- Changed shapeship image to show when engines are being thrust.
- Added notification on game over if a high score has been achieved.
- Fixed bug that caused bonuses to carry over into a new game.
* Fri Jan 01 2004 Michael J. Korman <mike@taequin.org>
- Initial release.
- Put something in the README and AUTHORS files.
