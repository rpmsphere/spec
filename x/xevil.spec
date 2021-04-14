# $Revision: 1.26 $, $Date: 2007-02-12 22:09:22 $
Summary:	A fast-action violent game for the X Window System
Summary(cs):	Hra podobná hře Pac-Man pro X Window System
Summary(da):	Et Pacman-lignende spil til X-vinduessystemet
Summary(de):	Ein schnelles, extrem gewalttätiges Actionspiel für X
Summary(fr):	Un jeu d'action rapide et très violent sous X
Summary(it):	Un violento gioco di azione per X Window
Summary(nb):	Et hurtig voldelig spill for X-vindussytemet
Summary(pl):	Brutalna gra o szybkiej akcji pod X Window System
Summary(sk):	Rýchla násilná hra pre X Window Systém
Summary(tr):	Hızlı ve şiddet yüklü bir X oyunu
Summary(zh_TW):	快打暴力遊戲
Name:		xevil
Version:	2.02r2
Release:	1
License:	GPL
Group:		Amusements/Games
#Source0:	http://www.xevil.com/download/stable/%{name}src%{version}.zip
Source0:	%{name}_2.02r2.orig.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:         %{name}_2.02r2.patch
URL:		http://www.xevil.com/
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
BuildRequires:	libX11-devel
BuildRequires:	libXpm-devel

%description
XEvil is an X Window System based game with a side view display
reminiscent of LodeRunner. The object of the game is to run around
killing everything in sight and exploring the different levels. XEvil
can be played against the computer or against other people.

%description -l cs
XEvil je hra pro X Window System s podobným bočním pohledem na hru
připomínající hru LodeRunner. Cílem hry je projít celou úroveň a zabít
všechno v dohledu a dostat se do další úrovně. XEvil můžete hrát proti
počítači nebo proti jiným hráčům.

%description -l de
Ein Action/Adventure-Spiel für X Window, in dem Sie als Ninja alles
niedermachen und dann die Gegend erkunden - wenn Sie überleben.

%description -l fr
XEvil est un jeu sous X Window avec une vue de côté à la Lode Runner.
Il faut explorer les différents niveaux en tuant tout ce qui bouge. On
peut jouer contre un autre être humain ou contre l'ordinateur.

%description -l it
Un gioco per X11 con una vista dall'utente stile LodeRunner.
L'obbiettivo del gioco e' quello di andare in giro ed uccidere tutti
esplorando i vari livelli.

%description -l pl
xevil jest grą pod X Window System bazującą na LodeRunnerze. Celem gry
jest zabijanie wszystkiego w zasięgu wzroku oraz przechodzenie
kolejnych poziomów. W xevil można grać przeciwko komputerowi albo
innym graczom.

%description -l sk
XEvil je hra pre X Window systém s bočným pohľadom, pripomínajúca
LodeRunner. Cieľom hry je pohybovať sa po hre, zabíjať všetko v
dohľade a skúmať rozličné úrovne. XEvil môže byť hraný proti počítaču,
alebo proti iným hráčom.

%description -l tr
X Window altında oynanan bir action/macera oyunu. Sizin rolünüz, bir
Ninja savaşçısı olarak karşınıza çıkan her şeyi öldürmek.

%prep
%setup -q -n %{name}-2.02r2.orig
%patch0 -p1
sed -i 's|-static||' config.mk
sed -i -e 's|const char\* cs,int c|char* cs,int c|g' \
       -e 's|const char\* cs,const char\* ct|char* cs,char* ct|' cmn/utils.h

%build
%{__make} \
	HOSTTYPE=i386 \
	DEBUG_OPT="%{optflags} -fno-exceptions" \
	LINK_FLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/applications,%{_datadir}/pixmaps}
install x11/REDHAT_LINUX/xevil $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications
echo -e 'Name[zh_TW]=極限邪惡\nComment[zh_TW]=Xevil 快打暴力遊戲' >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc readme.txt instructions
%attr(755,root,root) %{_bindir}/xevil
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.02r2
- Rebuilt for Fedora

* Thu Jun 06 2011 Chris Lin <chris.lin@ossii.com.tw>
- Fix types in cmn/utils.h

* Mon Nov 17 2008 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for CentOS5

* Mon Feb 12 2007 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: xevil.spec,v $
Revision 1.26  2007-02-12 22:09:22  glen
- tabs in preamble

Revision 1.25  2007/02/12 01:06:38  baggins
- converted to UTF-8

Revision 1.24  2006/10/23 15:31:11  qboosh
- updated config patch, switched to modular xorg
- added c++ patch (fixes needed by gcc 4)
- release 3

Revision 1.23  2004/08/01 22:28:32  qboosh
- fixed build on amd64, release 2

Revision 1.22  2004/02/18 15:25:16  qboosh
- moved to /usr, switched to desktopdir

Revision 1.21  2004/02/18 15:16:12  qboosh
- s/no/nb/ in Summary langs

Revision 1.20  2003/11/11 01:33:24  ankry
- caps unification, other cosmetics

Revision 1.19  2003/08/02 09:28:04  gotar
- fixed X Window System spelling

Revision 1.18  2003/06/30 20:12:27  qboosh
- up to 2.02r2
- removed obsolete c++ patch, gcc3 patch replaced by new one for gcc 3.3

Revision 1.17  2003/06/23 12:22:40  ankry
- use URL
NOTE: 2.02r2 with gcc3 fixes available

Revision 1.16  2003/06/23 12:20:11  ankry
- md5

Revision 1.15  2003/05/25 06:28:15  misi3k
- massive attack s/pld.org.pl/pld-linux.org/

Revision 1.14  2002/12/08 21:03:58  ankry
- merge translations from RH

Revision 1.13  2002/12/08 11:53:21  blues
- spelling fixes by Tomasz "Witek" Wittner <wittt_@poczta.onet.pl>

Revision 1.12  2002/11/21 21:05:07  wolf
- fixed install
- BR: compress

Revision 1.11  2002/11/21 20:35:18  ankry
- added icon based on icon from the package
- desktop moved to Games/Arcade/
- release 3

Revision 1.10  2002/10/13 23:02:27  ankry
- added -const_float patch to fix build

Revision 1.9  2002/10/13 10:55:48  qboosh
- added gcc3 patch with C++ fixes, enabled rtti (it's needed)
- new %%doc, release 2

Revision 1.8  2002/04/02 18:36:15  kloczek
- removed using %%{__install} macro.

Revision 1.7  2002/02/23 05:29:54  kloczek
- adapterized.

Revision 1.6  2002/02/22 23:30:05  kloczek
- removed all Group fields translations (our rpm now can handle translating
  Group field using gettext).

Revision 1.5  2002/01/18 02:15:39  kloczek
perl -pi -e "s/pld-list\@pld.org.pl/feedback\@pld.org.pl/"

Revision 1.4  2001/07/03 07:45:35  kloczek
- added "-fno-exceptions -fno-rtti" to DEBUG_OPT (smaller executable).

Revision 1.3  2001/07/03 06:54:34  kloczek
- merge old Bero Linux de, fr, tr translations,
- desktop file move to separated file (more translations added),
- cut %%changelog.

Revision 1.2  2001/07/02 21:25:36  qboosh
- updated to 2.02, updated config patch
- added c++ patch with fixes for current C++

Revision 1.1  2001/06/07 16:07:04  qboosh
- taken from RH PowerTools

Based on RedHat spec file.
