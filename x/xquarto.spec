Name:           xquarto
BuildRequires:  libX11-devel, libXt-devel, libXpm-devel, libXaw-devel, imake
License:        GPLv2+
Group:          Amusements/Games/Board/Puzzle
Version:        2.5
Release:        1599.1
Source:         xquarto-2.5.tar.bz2
Patch:          xquarto-2.5-imake_font.patch
URL:            ftp://ftp.ac-grenoble.fr/ge/educational_games/xquarto-2.5.tgz
Summary:        A board game designed for the X

%description
The game is a two-player game. Player 1 chooses one of the 16 pieces.
Player 2 then places this piece on one of the 16 squares of the board
and chooses a piece out of the remaining 15 pieces which he gives to
player 1, who places this piece on one of the remaining 15 squares on
the board, etc...

Xquarto supports three different player combinations: human vs
computer, computer vs human and human vs human (possibly through the
local network in the latter case). The default combination is human vs
computer, i.e. the human player starts the game against the computer.
This can be changed by clicking on the "Actions" menu (see below for
more details).

%prep
%setup -q
%patch

%build
xmkmf -a
make %{?jobs:-j%jobs} CCOPTIONS="$RPM_OPT_FLAGS"

%install
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT/usr/games/* $RPM_BUILD_ROOT%{_bindir}
%if %{fedora}<21
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mv $RPM_BUILD_ROOT/usr/man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/xquarto
%{_mandir}/man1/xquarto.1x.gz

%changelog
* Thu Sep 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5
- Rebuild for Fedora
* Mon Nov  8 2010 coolo@novell.com
- remove support for pre-9.1
* Thu Oct  4 2007 bg@suse.de
- don't use hpux environment
* Tue Aug  8 2006 lmichnovic@suse.cz
- compiling with RPM_OPT_FLAGS
- patch renamed to xquarto-2.5-imake_font.patch
* Fri Jul 28 2006 lmichnovic@suse.cz
- builds also with new X.org 7.x, detecting prefix in X.org
- building with icecream
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Nov  2 2005 dmueller@suse.de
- don't build as root
* Wed Oct 30 2002 ro@suse.de
- fix build on alpha
* Thu Feb  7 2002 tcrhak@suse.cz
- fix buildroot
* Thu Jan 10 2002 ro@suse.de
- no subdirs in /usr/games
* Fri Oct 26 2001 tcrhak@suse.cz
- New package: initial version 2.5
