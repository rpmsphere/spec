Summary:        An X Window System game of falling jewel blocks
Summary(de):    Game von der Art von Segas COLUMNS
Summary(fr):    Jeu du style Columns de Sega
Summary(pl):    Gra pod X Window System - spadające bloki
Summary(tr):    Sega'nýn columns'una benzer oyun
Name:           xjewel
Version:        1.6
Release:        33.1
License:        MIT
Group:          X11/Applications/Games
Source0:        ftp://ftp.x.org/R5contrib/%{name}-%{version}.tar.z
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         %{name}-imake.patch
Patch1:         %{name}-enhance.patch
Patch2:         %{name}-nobr.patch
Patch3:         %{name}-select.patch
BuildRequires: libX11-devel libXext-devel
BuildRequires: imake
Requires:   urw-fonts

%description
Xjewel is an X Window System game much like Domain/Jewelbox, Sega's
Columns and/or Tetris. The point of the game is to move or rotate the
blocks as they fall, to get jewels in patterns of three when they come
to rest.

%description -l de
Jewel hat große Ähnlichkeit mit Domain/Jewelbox, einem Puzzle-Game in
der Tetris-Manier. Die Aufgabe besteht darin, die Bewegung der Blöcke
zu steuern, die vom oberen Bildschirmrand nach unten fallen. Man kann
sie nach links und nach rechts bewegen und die Segmente drehen. Der
Spieler versucht, möglichst viele Punkte einzuheimsen, bevor sein
Lebensfaden abgezwackt wird.

%description -l fr
jewel est un jeu comme Domain/Jewelbox qui est un jeu de puzzle de
style Tetris.

On y joue en contrôlant le déplacement des blocs qui tombent du haut
de l'écran. On peut les déplacer ŕ droite et ŕ gauche et les faire
tourner. Le but est d'avoir le plus de points possible avant que la
Faucheuse n'y mette un terme.

%description -l pl
Xjewel jest grą pod X Window System podobną do Domain/Jewelbox,
Columns znanej z Segi lub Tetrisa. Celem gry jest przesuwanie lub
rotacja bloków podczas spadania, aby ułożyć składające się na nie
klejnoty w trójki w celu usunięcia.

%description -l tr
Jewel, Domain/Jewelbox ya da Tetris benzeri bir bulmaca oyunudur. Amaç
düţen bloklarý sađa/sola çevirerek ya da döndürerek uygun biçimde
yerleţtirmektir.

%prep
%setup -q
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p0

%build
xmkmf
%{__make} CDEBUGFLAGS="%{optflags}" \
        HSCORE_FILE=/var/games/xjewel.scores

%install
install -d $RPM_BUILD_ROOT{%{_datadir}/applications,%{_datadir}/pixmaps,/var/games}

%{__make} install install.man \
        DESTDIR=$RPM_BUILD_ROOT \
    MANDIR=/usr/share/man/man1
        HSCORE_FILE=/var/games/xjewel.scores

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

%files
%attr(2755,root,games) %{_bindir}/xjewel
%{_mandir}/man1/xjewel.1x*
%attr(664,root,games) %config(noreplace) %verify(not mtime size md5) /var/games/xjewel.scores
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Sun Sep 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Rebuilt for Fedora
* Sun Jan 04 2004 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.18.2.2  2004/01/04 12:48:36  ankry
- md5, updated .desktop, rel. 20
Revision 1.18.2.1  2003/07/11 12:04:53  eothane
- some pld.org.pl->pld-linux.org cosmetics
Revision 1.18  2002/05/30 10:22:54  kloczek
- desktop file moved to Games/Arcade/ and added using more macros.
Revision 1.17  2002/05/29 21:26:25  ankry
- applnk icon made transparent
- release 19
Revision 1.16  2002/02/23 05:29:54  kloczek
- adapterized.
Revision 1.15  2002/02/22 23:30:06  kloczek
- removed all Group fields translations (our rpm now can handle translating
  Group field using gettext).
Revision 1.14  2002/01/18 02:15:40  kloczek
perl -pi -e "s/pld-list\@pld.org.pl/feedback\@pld.org.pl/"
Revision 1.13  2001/11/02 23:17:02  qboosh
- fixed score file access (sgid games binary)
Revision 1.12  2001/10/31 23:48:10  qboosh
- changed imake patch (FHS 2.1/2.2): /var/lib/games -> /var/games
- pl description
- release 18
Revision 1.11  2001/05/28 23:56:00  kloczek
- release 17: new icon.
Revision 1.10  2001/05/03 01:14:07  qboosh
- adapterized and made spec %%debug ready or added using %%rpm*flags macros
Revision 1.9  2001/02/02 17:50:35  kloczek
- perl -pi -e "s/^\%\{_datadir\}\/pixmaps/\%\{_pixmapsdir\}/"
Revision 1.8  2000/06/09 07:24:22  kloczek
- added using %%{__make} macro.
Revision 1.7  2000/05/21 20:05:15  kloczek
- spec adapterized.
Revision 1.6  2000/05/03 23:45:31  kloczek
- release 14,
- added de, fr, tr translations from old Bero Linux spec file,
- wmconfig file replaced by desktop,
- added package icon,
- spec adapterized,
- added select patch from rawhide.
Revision 1.5  2000/04/25 16:16:49  baggins
- release++
- FHS 2.1, /var/state -> /var/lib
Revision 1.4  2000/04/10 17:06:18  baggins
- more spelling fixes
Revision 1.3  2000/04/01 11:16:02  zagrodzki
- changed all BuildRoot definitons
- removed all applnkdir defs
- changed some prereqs/requires
- removed duplicate empty lines
Revision 1.2  1999/11/02 13:30:21  baggins
- cleanup
- macros
- striping binaries
- gziping docs
- CVS tags
- FHS 2.0
Revision 1.1  1999/08/19 20:07:27  baggins
almost raw
