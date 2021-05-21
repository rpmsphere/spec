Name:           marbles
BuildRequires:  SDL_mixer-devel 
#BuildRequires:	update-desktop-files
URL:            http://lgames.sourceforge.net/index.php?project=LMarbles
License:        GNU General Public License (GPL)
Group:          Amusements/Games/Action/Arcade
Version:        1.0.7
Release:        1
Summary:        Atomix-Like Game of Moving Marbles in Puzzles
Source0:        l%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

%description
Marbles is very similar to and was heavily inspired by Atomix. The goal
is to create a more or less complex figure out of single marbles within
a set time limit to reach the next level.

Sounds easy? Well, there is a problem: If a marble starts to move it
will not stop until it hits a wall or another marble. To make it even
more interesting, there are obstacles like arrows, crumbling walls, and
teleports.

Authors:
--------
    Michael Speck <kulkanie@gmx.net>

%prep
%setup -q -n l%{name}-%{version}

%build
cp /usr/share/automake-*/config.guess .
CFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=/usr --mandir=/usr/share/man \
            --localstatedir=/var/games/ \
            --datadir=/usr/share/games
make 

%install
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
#%suse_update_desktop_file -i %name Game X-SuSE-LogicGame

# Desktop
mkdir $RPM_BUILD_ROOT%{_datadir}/applications
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop 

# Icon
mkdir $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 0644 lmarbles32.gif $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%doc AUTHORS COPYING ChangeLog README
%attr(664,games,games) /var/games/lmarbles.prfs
%{_bindir}/lmarbles
%{_mandir}/man6/lmarbles.6.gz
%{_datadir}/games/lmarbles/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog -n marbles
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.7
- Rebuilt for Fedora
* Mon Oct 20 2008 - john@ossii.com.tw
- Rebuild for M6(OSSII)
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Sep 09 2005 - nadvornik@suse.cz
- added libmikmod to #neededforbuild
* Fri Jul 22 2005 - sndirsch@suse.de
- added SDL_mixer-devel to #neededforbuild
* Thu Jun 23 2005 - meissner@suse.de
- use RPM_OPT_FLAGS.
* Sat Mar 12 2005 - sndirsch@suse.de
- fixed data dir (Bug #72309)
* Fri Jul 16 2004 - sndirsch@suse.de
- updated to release 1.0.7
* Sat Jan 10 2004 - adrian@suse.de
- build as user
* Mon Aug 11 2003 - sndirsch@suse.de
- added desktop file
* Sun Dec 29 2002 - sndirsch@suse.de
- updated to release 1.0.6
* Sat Oct 26 2002 - sndirsch@suse.de
- created package
