%undefine _debugsource_packages

Name:           falconseye
Requires:       timidity++
Version:        1.9.3
Release:        925.1
Source:         %{name}-%{version}.tar.bz2
Source1:        %name.desktop
Patch:          %{name}-%{version}.diff
Patch1:         %{name}-libs.patch
Patch2:         %{name}-tinfo.patch
URL:            https://www.hut.fi/~jtpelto2/nethack.html
Summary:        A Mouse-Driven interface for NetHack
License:        NGPL
Group:          Amusements/Games/RPG
BuildRequires:  SDL-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  cpp
BuildRequires:  flex
BuildRequires:  gdbm-devel
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  slang-devel
BuildRequires:  libX11-devel
BuildRequires:  zlib-devel
BuildRequires:  ghostscript-core ImageMagick

%description
Falcon's Eye is a mouse-driven interface for NetHack that enhances the
visuals, audio, and accessibility of the game, yet retains all the
original gameplay and game features.

Falcon's Eye needs to be installed together with nh_data and is run as
nethack.

%prep
%setup -q
%patch
%patch1
%patch2

%build
sh sys/unix/setup.sh links
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wno-format-security"
make

%install
make DESTDIR="$RPM_BUILD_ROOT" install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
#mv $RPM_BUILD_ROOT%{_datadir}/games/falconseye \
#  $RPM_BUILD_ROOT%{_datadir}/falconseye
mv $RPM_BUILD_ROOT/usr/falconseye \
  $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_datadir}/falconseye/falconseye \
  $RPM_BUILD_ROOT%{_bindir}/falconseye.bin
ln -snf %{_bindir}/falconseye.bin \
  $RPM_BUILD_ROOT%{_datadir}/falconseye/falconseye
rmdir $RPM_BUILD_ROOT%{_datadir}/falconseye/save
mkdir -p $RPM_BUILD_ROOT/var/games/falconseye/save
ln -s /var/games/falconseye/save $RPM_BUILD_ROOT%{_datadir}/falconseye/save
touch $RPM_BUILD_ROOT/var/games/falconseye/jtp_log.txt
ln -s /var/games/falconseye/jtp_log.txt $RPM_BUILD_ROOT%{_datadir}/falconseye/jtp_log.txt
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/falconseye.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert $RPM_BUILD_ROOT%{_datadir}/falconseye/nethack.ico $RPM_BUILD_ROOT%{_datadir}/pixmaps/falconseye.png

%files
%{_datadir}/falconseye
%{_bindir}/falconseye
%{_bindir}/falconseye.bin
%{_datadir}/applications/%name.desktop
/var/games/falconseye
%{_datadir}/pixmaps/falconseye.png

%changelog
* Wed Feb 25 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.3
- Rebuilt for Fedora
* Sun Jun 30 2013 seife+obs@b1-systems.com
- fix license field, it's NGPL (Nethack General Public License)
* Wed Nov 23 2011 jengelh@medozas.de
- Remove redundant/unwanted tags/section (cf. specfile guidelines)
* Wed Nov 23 2011 jreidinger@suse.com
- add libs patch to compile on newer distros
- clean up buildrequires
- add tinfo patch for ncurses separation on newer distros
* Wed Sep 13 2006 gerberb@zenez.com
- setup and fixed to build on OBS
* Tue Sep 21 2004 sbrabec@suse.cz
- Moved variable files to /var.
- Fixed save dir permission (#45723).
* Mon May 17 2004 ro@suse.de
- fix some compiler warnings
* Tue Feb 24 2004 stepan@suse.de
- use gzip instead of compress for save files. This fixes saving
  games.
* Mon Feb 23 2004 sndirsch@suse.de
- changed desktop category to X-SuSE-AdventureGame
* Tue Feb 17 2004 adrian@suse.de
- fix Categories
* Tue Nov  4 2003 ro@suse.de
- package according to permissions.secure and add run_permissions
- don't build as root
* Tue Aug 12 2003 sndirsch@suse.de
- added desktop file
* Mon Mar 10 2003 sndirsch@suse.de
- moved falconseye binary from /usr/share/games/falconseye to
  /usr/games/ (falconseye.bin)
* Sat Mar  8 2003 sndirsch@suse.de
- use old NH data files again (Bug #24399)
* Mon Feb 17 2003 sbrabec@suse.cz
- Removed -mminimal-toc from spec file for PPC, since it is now RPM
  default (bug #23266).
* Mon Nov 11 2002 ro@suse.de
- changed neededforbuild <xshared> to <x-devel-packages>
* Tue Aug  6 2002 kukuk@suse.de
- Add fileutils to PreRequires
- Fix Provides: nh_binary -> nethack_binary
* Mon Aug  5 2002 kukuk@suse.de
- Fix requires (nh_data -> nethack_data)
* Sun Aug  4 2002 ro@suse.de
- group name changed "game" -> "games"
* Mon Jul  1 2002 olh@suse.de
- hack to build with RPM_OPT_FLAGS, use -mminimal-toc on ppc64
* Thu Feb 14 2002 ro@suse.de
- changed neededforbuild <kdelibs3-artsd> to <arts arts-devel>
* Fri Feb  1 2002 tcrhak@suse.cz
- fixed hackdir path and path to timidity, added Requires timidity
- compile staff in util with -DTIMED_DELAY to be nh_data compatible
* Tue Jan 22 2002 ro@suse.de
- changed neededforbuild <kdelibs-artsd> to <kdelibs3-artsd>
* Tue Jan 15 2002 tcrhak@suse.cz
- singled out nh_binary related data, package now works as a frontend
- to nh_data
- moved files from /usr/share/games/nethackdir to
- /usr/share/games/nethack
* Mon Jan 14 2002 ro@suse.de
- moved files to /usr/share/games/nethackdir
* Tue Nov 20 2001 tcrhak@suse.cz
- initial version 1.9.3
