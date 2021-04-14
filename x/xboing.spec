Summary:	A Breakout style X Window System based game
Summary(pl):	Gra pod X podobna do Breakout
Name:		xboing
Version:	2.4
Release:	24.1
License:	MIT
Group:		X11/Applications/Games
Source0:	http://www.techrescue.org/xboing/%{name}%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}.patch
Patch1:		%{name}-Imakefile.patch
Patch2:		%{name}-sparc.patch
Patch3:		%{name}-visualfix.patch
URL:		http://www.techrescue.org/xboing/
BuildRequires:	imake, libX11-devel, libXpm-devel, libXext-devel

%description
Xboing is an X Window System based game like the Breakout arcade game.
The object of the game is to keep a ball bouncing on the bricks until
you've broken through all of them.

%description -l pl
Xboing jest grą pod X Window System podobną do klasycznej gry
Breakout. Celem gry jest utrzymanie piłki odbijającej się od cegieł aż
do przebicia się przez wszystkie.

%prep
%setup -q -n xboing
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i 's|-lm|-lm -Wl,--allow-multiple-definition|' Imakefile

%build
xmkmf
%{__make} \
	CC=%{__cc} \
	CDEBUGFLAGS="%{optflags}" \
	XBOING_DIR=%{_datadir}/xboing \
	HIGH_SCORE_FILE=/var/games/xboing.score

%install
install -d $RPM_BUILD_ROOT{/var/games,%{_datadir}/xboing,%{_datadir}/applications,%{_datadir}/pixmaps,%{_bindir},%{_mandir}/man1}

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	XBOING_DIR=$RPM_BUILD_ROOT%{_datadir}/xboing \
	HIGH_SCORE_FILE=$RPM_BUILD_ROOT/var/games/xboing.score \
	install install.man

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

%files
%doc COPYRIGHT README docs/*.doc
%attr(2755,root,games) %{_bindir}/xboing
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/xboing.score
%{_datadir}/xboing
%{_mandir}/man1/xboing.1x*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Sun Sep 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuilt for Fedora

* Fri Jul 09 2004 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.21  2004/07/09 16:59:56  havner
- ugly hack to build this "game"
- what kind of smoker invented imake?

Revision 1.20  2004/07/04 21:42:05  adamg
- applnk -> vfolders; release 12

Revision 1.19  2004/07/04 21:39:04  adamg
- removed two lines with define (I allways wanted to commit that)

Revision 1.18  2004/04/26 19:25:32  adamg
- release 11 for Ac (10 is for Ra)

Revision 1.17  2003/05/28 13:03:03  malekith
- massive attack: source-md5

Revision 1.16  2003/05/25 06:28:07  misi3k
- massive attack s/pld.org.pl/pld-linux.org/

Revision 1.15  2002/11/30 23:00:30  juandon
- new %%doc

Revision 1.14  2002/02/22 23:30:01  kloczek
- removed all Group fields translations (oure rpm now can handle translating
  Group field using gettext).

Revision 1.13  2002/01/18 02:15:28  kloczek
perl -pi -e "s/pld-list\@pld.org.pl/feedback\@pld.org.pl/"

Revision 1.12  2002/01/11 08:44:48  kloczek
- release 10: added missing Icon in desktop file.

Revision 1.11  2002/01/10 22:58:34  kloczek
- renamed patches,
- separate desktop file and added Icon,
- move desktop file to Games/Arcade/,
- updated URL and Source url,
- more macros.

Revision 1.10  2001/11/03 22:11:38  qboosh
- BuildRequires: XFree86-devel

Revision 1.9  2001/11/03 17:45:36  qboosh
- changed -2.4 patch - FHS 2.1/2.2: /var/lib/games -> /var/games
- visualfix - fix for BadMatch error if not using default colourmap
- made score files work (sgid games binary)
- changed .wmconfig file to .desktop file
- pl description
- release 9

Revision 1.8  2001/05/03 01:14:06  qboosh
- adapterized and made spec %%debug ready or added using %%rpm*flags macros

Revision 1.7  2000/06/09 07:24:14  kloczek
- added using %%{__make} macro.

Revision 1.6  2000/05/21 20:05:15  kloczek
- spec adapterized.

Revision 1.5  2000/04/25 16:16:49  baggins
- release++
- FHS 2.1, /var/state -> /var/lib

Revision 1.4  2000/04/10 17:06:18  baggins
- more spelling fixes

Revision 1.3  2000/04/01 11:16:00  zagrodzki
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
