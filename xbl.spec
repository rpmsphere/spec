Name:           xbl
Version:        1.1.5
Release:        1
Summary:        3D Tetris
Group:          Amusements/Games/Logic
License:        GPL v2 or later
URL:            http://www710.univ-lyon1.fr/ftp/xbl/xbl.html
Source:         %{name}-%{version}.tar.bz2
Patch:          %{name}-%{version}-config.patch

%description
3D Tetris for X Window System.

%prep
%setup -q
%patch
sed -i -e 's|usr/local|usr|' -e 's|usr/man|usr/share/man|' -e 's|usr/lib/X11/app-defaults|usr/share/X11/app-defaults|' configure* Makefile*

%build
CFLAGS=$RPM_OPT_FLAGS \
./configure
make LIBS='-lm -lX11' %{?jobs:-j%jobs}

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/X11/app-defaults
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man6
mkdir -p $RPM_BUILD_ROOT/var/games/xbl
make DESTDIR=$RPM_BUILD_ROOT SCOREDIR=/var/games/xbl install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING INSTALL README xbl.html xbl-*
/usr/share/X11/app-defaults/Xbl
/usr/share/man/man6/xbl.6.gz
/usr/bin/xbl

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.5
- Rebuild for Fedora
* Tue Jun 23 2009 Kami <kami@ossii.com.tw>
- Build for OSSII
* Mon Apr 16 2007 - lmichnovic@suse.cz
- update to version 1.1.5
  * Added missing bloc: rrldb (thanks to N.Landys and M.Banguerski)
* Wed Jul 26 2006 - lmichnovic@suse.cz
- builds also with new X.org 7.x, checks the version of X.org.
* Thu Jun 22 2006 - lmichnovic@suse.cz
- update to version 1.1.4
  - some code improvements
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Jan 12 2006 - lmichnovic@suse.cz
- update to version 1.1.3
* Wed Oct 05 2005 - lmichnovic@suse.cz
- small adjustment of scoredir in makefile (#103762)
* Wed May 19 2004 - ro@suse.de
- try to fix compilation (broken by xvendorname changes)
* Sat Jan 10 2004 - adrian@suse.de
- build as user
* Mon Nov 03 2003 - ltinkl@suse.cz
- package according to permissions.secure and call run_permissions
* Mon Oct 27 2003 - ltinkl@suse.cz
- update to 1.1.2
- patches cleanup
- new patch to fix build
* Tue Sep 16 2003 - kukuk@suse.de
- Adjust permissions in filelist with /etc/permissions*
* Tue Jul 15 2003 - ltinkl@suse.cz
- fixed another buffer overflow [#27825]
* Wed Jul 09 2003 - ltinkl@suse.cz
- fixed potential buffer overflow [#27457]
* Wed Nov 27 2002 - pmladek@suse.cz
- updated to version 1.0k:
  * fix a missing block shape and a duplicate one
  * the default group install is the GID of "games"
  * realtime: less bugs, nicer, use less CPU, choose FPS
  * stereovision (You cross the eyes to see in 3D)
  * small delay before the start of a new game.
- fixed the usage of the varargs macros to compile with gcc-3.3
- fixed cast warnings on x64_64
- man page moved from mann to man6
* Sun Aug 04 2002 - ro@suse.de
- group name changed "game" -> "games"
* Fri Jun 29 2001 - pmladek@suse.cz
- bzipped sources
- added BuildRoot
- compiled with $RPM_OPT_FLAGS
- fixed rights of documentation files
* Mon Jan 17 2000 - freitag@suse.de
- new version V. 1.0j
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Mon May 17 1999 - ro@suse.de
- define __need___va_list before including varargs
* Fri Mar 06 1998 - ray@suse.de
- new package
- V. 1.0h
