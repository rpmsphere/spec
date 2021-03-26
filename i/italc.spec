Name:           italc
Version:        2.0.0
Release:        4.1
Summary:        Didactical monitoring software for Linux-networks
License:        GPL
URL:            http://italc.sourceforge.net/
Group:          Productivity/Networking/Other
BuildRequires:  libjpeg-devel openssl-devel pkgconfig zlib-devel
BuildRequires:  gcc-c++ libstdc++-devel automake make openssl 
BuildRequires:  cmake pam-devel
##BuildRequires:  java-devel 
BuildRequires:  qt4-devel libXtst-devel 
BuildRequires:  qt-x11 qt-sqlite
#
# standard source and patch files
#
Source:         %{name}-%{version}.tar.bz2
Source2:        italc-start_ica
Source3:        italc.sysconfig
Source5:        ica-autostart.desktop
Source6:        italc-launcher
Source8:        italc.desktop
Source9:        italc-rpmlintrc
%define         italcgrp italc

%description
iTALC is a powerful software for Linux-networks, which was especially developed
for working with computers in school. But it can be also used in other
learning-environments. iTALC is a software for teachers using the computer
as didactical tool in their lessons. It aims to be a complete replacement for
expensive commercial software like MasterEye (tm).

iTALC makes it possible, to access and influence the pupils activities from the
computer of the teacher. This way iTALC supports the work with modern
equipment in school.
For example the teacher is able to see the content of the pupils screens on his
screen. If a student needs help, the teacher can access his desktop and
give support while sitting in front of his computer. The pupil can watch all
activities, the teacher is doing on his desktop. So the he can learn new
processes.

If you want to teach the pupils completely new stuff, you can switch into
demo-mode. Then all pupils see what the teacher is doing/demonstrating.
It's also possible to let a pupil demonstrate something by redirecting his
screen to all screens of the other pupils.
iTALC provides even more features for controlling the pupils computers.
For example you can lock all screens, so that the pupils can't continue their
work and are forced to turn their attention to the teacher. You can also kill
games or internet-browsers, if these things are not part of the lesson.

But there are also some nice features for administrators, making the
administration of the computers much easier and more comfortable. For example
you can execute one or more commands on every computer without sitting in front
of every computer and typing these comands. The execution of X-applications
(e.g. Star/OpenOffice-Setup) on all clients with redirection to the local
admin-computer is also part of iTALC's featurelist. Furthermore you can
shutdown and restart the computers per remote control. If the computers support
Wake-on-LAN, it's also possible to turn on all computers from a central place.


Author:
-------
    Tobias Doerfel


%package        client
Summary:        Software for iTALC-clients
Group:          Productivity/Networking/Other
Requires:       italc = %{version}

%description    client
This package contains the software, needed by iTALC-clients.

See /usr/share/italc/doc/INSTALL for details on how to install and setup iTALC
in your network.

Author:
-------
    Tobias Doerfel


%package        master
Summary:        Software for iTALC-masters
Group:          Productivity/Networking/Other
PreReq:         italc = %version
PreReq:         italc-client = %version
PreReq:         coreutils

%description    master
This package contains the software, needed by iTALC-master-computers.

See /usr/share/italc/doc/INSTALL for details on how to install and setup iTALC
in your network.


Author:
-------
    Tobias Doerfel


%prep
%setup -q

%build
##export SUSE_ASNEEDED=0
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="%{_prefix}" -DCMAKE_CXX_FLAGS="%{optflags} -fpie" ../

%install
cd build
make DESTDIR=$RPM_BUILD_ROOT install
cd ..
# create the directories containing the auth-keys
mkdir -p %buildroot%_sysconfdir/italc/keys/{private,public}/{teacher,admin,supporter,other}
# create pseudo key files so RPM can own them (ghost files)
for role in admin supporter teacher; do
	touch %buildroot%_sysconfdir/italc/keys/{private,public}/$role/key
done
# create the initial config
mkdir -p "%buildroot/%_sysconfdir/qt4/iTALC Solutions"
cat > "%buildroot/%_sysconfdir/qt4/iTALC Solutions/iTALC.conf" << EOF
[keypathsprivate]
admin=%_sysconfdir/italc/keys/private/admin/key
supporter=%_sysconfdir/italc/keys/private/supporter/key
teacher=%_sysconfdir/italc/keys/private/teacher/key

[keypathspublic]
admin=%_sysconfdir/italc/keys/public/admin/key
supporter=%_sysconfdir/italc/keys/public/supporter/key
teacher=%_sysconfdir/italc/keys/public/teacher/key
EOF
# install manpages
mkdir -p %{buildroot}%{_mandir}/man1
install -m644 ./ica/ica.1 %{buildroot}%{_mandir}/man1/
install -m644 ./ima/italc.1 %{buildroot}%{_mandir}/man1/
# install start script for ica client
install -D -m755 %{SOURCE2} %buildroot/%_bindir/start-ica
install -D -m644 %{SOURCE5} %buildroot/%_sysconfdir/xdg/autostart/ica-autostart.desktop
install -D -m755 %{SOURCE6} %buildroot/%_bindir/italc-launcher
# icon for the desktop file
install -Dm644 ima/data/italc.png %buildroot/%{_datadir}/pixmaps/italc.png
#
# Distribution specific
#
# configuration for ica
install -D -m644 %{SOURCE3} %buildroot/%_sysconfdir/sysconfig/ica
install -Dm644 %{SOURCE8} %{buildroot}/%{_datadir}/applications/%{name}.desktop 

%clean
rm -rf %{buildroot}

%post
if
    getent group %italcgrp >/dev/null
then
    : OK group %italcgrp already present
else
    groupadd -r %italcgrp 2>/dev/null || :
fi

%post master
# dont run scripts on update
if [ ${1:-0} -lt 2 ]; then
  for role in admin supporter teacher; do
	if [ ! -f "%_sysconfdir/italc/keys/private/$role/key" ]; then
		/usr/bin/ica -role $role -createkeypair 1>/dev/null
		chgrp %italcgrp "%_sysconfdir/italc/keys/private/$role/key"
		chmod 0440 "%_sysconfdir/italc/keys/private/$role/key"
	fi
  done
fi


%files
%doc contrib doc/* AUTHORS ChangeLog COPYING README* TODO
##%{_datadir}/italc/
%dir %_sysconfdir/italc
%dir %_sysconfdir/italc/keys
%dir %_sysconfdir/italc/keys/public
%dir %_sysconfdir/italc/keys/public/teacher
%dir %_sysconfdir/italc/keys/public/admin
%dir %_sysconfdir/italc/keys/public/supporter
%dir %_sysconfdir/italc/keys/public/other
%dir %_sysconfdir/qt4
%dir "%_sysconfdir/qt4/iTALC Solutions"
%ghost %config(missingok,noreplace) %_sysconfdir/italc/keys/public/*/key
%config(missingok,noreplace) "%_sysconfdir/qt4/iTALC Solutions/iTALC.conf"

%files 	client
%doc %{_mandir}/man1/ica.1*
%{_bindir}/ica
%_bindir/start-ica
%{_bindir}/imc
%{_bindir}/italc_auth_helper
%{_libdir}/libItalcCore.so
%config %_sysconfdir/xdg/autostart/ica-autostart.desktop
%config(noreplace) %_sysconfdir/sysconfig/ica

%files 	master
%{_bindir}/italc
%{_bindir}/italc-launcher
%doc %{_mandir}/man1/italc.1*
%{_datadir}/applications/italc.desktop
#{_datadir}/icons/italc.*
%{_datadir}/pixmaps/italc.*
%dir %_sysconfdir/italc/keys/private
%defattr(0440,root,%italcgrp,0750)
%dir %_sysconfdir/italc/keys/private/teacher
%dir %_sysconfdir/italc/keys/private/admin
%dir %_sysconfdir/italc/keys/private/supporter
%dir %_sysconfdir/italc/keys/private/other
%ghost %config(missingok,noreplace) %_sysconfdir/italc/keys/private/*/key

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Oct 19 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Tue Aug 30 2011 lars@linux-schulserver.de
- update to 2.0.0
- removed unneeded patches
- moved generic iTALC.conf from '/etc/settings/iTALC Solutions'
  to '/etc/qt4/iTALC Solutions' according to the wiki documentation
  for version 2
* Mon Aug  1 2011 lars@linux-schulserver.de
- just require avahi on SLED 11 (fix bnc #709338)
* Wed Mar 30 2011 lars@linux-schulserver.de
- update to 1.0.13:
  + fixes serious memory leak when running iTALC master
* Sat Jul 31 2010 lars@linux-schulserver.de
- update to 1.0.10:
  * Added NSIS script for building an iTALC installer
  * Added support for languages written right-to-left
  * IMA: rewrote top level UI and added new toolbar style
  * IMA: updated and improved splash screen
  * IMA: Implemented Toggle Autoview
  * IMA/ClassroomManager: sort items numerically where appropriate
  * ICA/Linux/x11vnc: synced with libvncserver Git repository
  * Updated localization files:
  - Czech
  - French
  - German
  - Norwegian
  - Slovakian
  - Ukrainian
  - Spanish
  * Added localization files
  - Catalan
  - Hebrew
  - Turkish
  * Localization files: merged all translations of each language
    into one file
  + Bugfixes:
  * Allow remote login without password
  * Include stdint.h for compiling with GCC >= 4.4
  * Setup/Makefile.am: do not fail linking when using
  - -as-needed linker flag
  * IsdServer: fixed running multiple program
  * IMA/Client: do not paint screen if window is too small
- added patch from Frank Schuett to italc-launcher, so the keys
  mentioned in /etc/settings/iTALC Solutions/iTALC.conf are
  honored
- fixed deprecated md5 module usage in italc-launcher
* Sat Jun 26 2010 cyberorg@opensuse.org
- use gcc43 to enable building on 11.3
* Fri Nov 20 2009 cyberorg@opensuse.org
- add export SUSE_ASNEEDED=0 to enable building on 11.2
* Thu Oct  1 2009 cyberorg@opensuse.org
- Fix source6 defined twice
- add italc-add-missing-include-gcc4.4.patch to fix build on new gcc
* Mon Mar 30 2009 lars@linux-schulserver.de
- fix italc-launcher again to save/re-use system lang for ifconfig
  (thanks again to Ciro Iriarte for the patch)
* Tue Mar 24 2009 lars@linux-schulserver.de
- fix italc-launcher not finding ifconfig
  (thanks to Ciro Iriarte for the patch)
* Thu Sep 25 2008 lars@linux-schulserver.de
- moved to Education base repository
* Thu Sep 18 2008 lrupp@suse.de
- write logfiles to /var/tmp as files in this directory are stored
  longer than in /tmp
* Mon Sep  1 2008 lars@linux-schulserver.de
- fix ica launch script
* Fri Aug 15 2008 lars@linux-schulserver.de
- added wvstreams-devel to BuildRequires
* Mon Aug 11 2008 cyberorg@opensuse.org
- Add italc-launcher and new ica launch scripts from stgraber@ubuntu.com
  +Autodetection of all the clients using avahi
* Thu Jul 24 2008 lars@linux-schulserver.de
- update to 1.0.9:
  + switched back to Qt 4.3.5 - finally "fixes" demo-crash
  + fixed endless loop when initializing keys
  + add date and time to logfiles
  + updated miniLZO-library to version 2.03
  + increased timeouts in socket-read-function in order to minimize
    lost connections
  + made Linux-version compile with libc 2.8
  + Linux: integrated latest x11vnc-version which fixes
    ICA-crashes when isconnecting during internal speed-estimations
  + added option for making toolbar buttons only display icon
  + fixed tooltip flicker issue
  + made visibility of individual sidebar-buttons configurable
    via context-menu
  + when selecting multiple clients (<ctrl>+left click) perform
    context-menu action on all selected clients
  + added support for controlling master-application via
    system-tray-icon
* Mon Jul  7 2008 lars@linux-schulserver.de
- update to 1.0.9-rc4:
  + integrated latest x11vnc-version which fixes ICA-crahes when
    disconnecting in certain situations
  + do not update GUI outside GUI-thread - fixes crashes of master
* Fri Jun 13 2008 lars@linux-schulserver.de
- update to 1.0.9-rc3:
  + made visibility of individual sidebar-buttons configurable
    via context-menu
  + when selecting multiple clients (<ctrl>+left click) process
    selected action in context menu on all clients
  + fixed possibility to escape locked mode
  + finally fixed huge-logfile problem under win32
  + made Linux-version compile on latest systems
  + in case of failed connections, sleep longer for not immediately
    hitting WinXP SP2 connection limit
* Thu Jun 12 2008 lars@linux-schulserver.de
- prefix ICA variables to aviod name clashes
- package the script and desktop file in other distributions, too
- enable post script for italc and italc-master on other dists
- new pathname: Applications/iTALC in sysconfig
* Wed Jun 11 2008 lars@linux-schulserver.de
- allow additional options in /etc/sysconfig/ica for ica
- allow really to disable ica in /etc/sysconfig/ica
* Tue Jun 10 2008 lars@linux-schulserver.de
- enhanced documentation in README and sysconfig
- firewall settings should be in the italc package
* Mon Jun  9 2008 lars@linux-schulserver.de
- /etc/X11/xinit/xinitrc.d/ is to early
  use /etc/xdg/autostart now
* Thu Jun  5 2008 lars@linux-schulserver.de
- the sysconfig script is called italc not ica (set manually)
- complete reconstruction of the ica start. Using an adapted script
  from Skolelinux now
- start ica using /etc/X11/xinit/xinitrc.d/
* Mon May 26 2008 lars@linux-schulserver.de
- update to 1.0.9-rc2 (1.0.8.992):
  + Qt 4.4-compatibility fixes
  + fixed mode-buttons in toolbar (demo, locked ...)
  + fixed tray-menu-actions when main-window is minimized
  + updated localizations
* Tue May 20 2008 lars@linux-schulserver.de
- the private keys and directories should belong to the
  italc-master package
- don't pay attention for 'other' role
* Fri May 16 2008 lars@linux-schulserver.de
- fix renamed italc init script in activation code
* Sun May 11 2008 lars@linux-schulserver.de
- update to 1.0.9-rc1 (1.0.8.99 to make updates easier):
  + fixed demo-mode on Linux
  + fixed endless loop when initializing keys
  + add date and time to logfiles
    (italc-1.0.8-logging.patch removed)
  + added option for making toolbar buttons only display icon
  + fixed tooltip flicker issue
  + updated miniLZO-library to version 2.03
  + added support for controlling master-application via
    system-tray-icon
  + increased timeouts in socket-read-function in order to minimize
    lost connections
* Wed Apr 23 2008 lars@linux-schulserver.de
- added italc-1.0.8-logging.patch
- don't call --with-qtdir on fedora and centos
* Mon Apr 21 2008 lars@linux-schulserver.de
- update to 1.0.8:
  - disabled MMX-optimized image-scaler on x86_64 as
    it's currently buggy
  - added zoom-feature: holding mouse-button on a client-window
    makes it zoom
  - display hostname in client-windows when "show user" is
    not checked
  - removed support-tab and added a button in toolbar instead
  - improved sidebar
  - visibility of individual toolbar-buttons can be configured
    via the toolbar-contextmenu
  - fixed several issues with scaling in remote-control-window
  - always try to run demo-server on default-port 5858 to allow
    easier and more secure firewall-configuration
  - drag'n drop support in classroom manager
  - fixed confirmation-dialog when closing setup-window
    via Alt+F4/close-button
  - added timeout-recognition in isdConnection::readFromServer()-function
    which makes iTALC-master not hang when quitting if a connection
    is somehow blocked
  - the name-field of a client is now optional - if you do not
    specify it, the hostname/IP is used for displaying
    the client's name
  - network-interface for demo-modes doesn't need to be configured
    anymore - it's auto-detected by clients
  - improved stability of demo-server
- added Port 5858 to the SuSEfirewall2
- removed upstreamed italc-1.0.7-fix-x64_64-compilation.patch
- fix some duplicated buildrequires
- prereq pwdutils
* Mon Mar 10 2008 lars@linux-schulserver.de
- update to 1.0.7:
  - improved overall usability by adding new icons and reworking
    look of overview-mode
  - added new image-scaling algorithm with (optional)
    MMX-optimizations in order to use less CPU-time on master-computer
    when monitoring a lot of clients with short update-intervals
  - thanks to fast image-scaler, remote-control and demo-mode now
    scale screen in real-time instead of having the user to scroll
  - removed user-list and added ability to display user-name instead
    of IP-address in classroom-manager instead
  - removed remote-IP-property as not used anymore
  - fixed logon-feature from classroom-action-menu
  - in case user accidently changed role but no keys exist for this
    role try teacher-role as fallback in order to make iTALC still
    usable in such cases (Closes #1866440)
  - added Polish localization-files
  - made power-down, reboot and logoff work under Linux
    if no user is logged in
  - fixed various crashes
- use the rcitalc script in /etc/X11/xdm/Xsetup (italc-setup.sh)
- rcitalc just starts, if third parameter is given
* Fri Mar  7 2008 lars@linux-schulserver.de
- created italc-setup.sh to be able to stop and start italc even
  if the package is not (de-)installed
- added README.SuSE for italc-client
* Tue Mar  4 2008 lars@linux-schulserver.de
- added service definition for SuSEfirewall2 (> 1020)
* Fri Feb 22 2008 lars@linux-schulserver.de
- update to 1.0.6:
  + many 64bit fixes
  + added possibility to set parameters such as -ivsport and -isdport
    using settings in /etc/settings/iTALC Solutions/iTALC.conf
  + added setting for client-double-click-action
  + added "-v" and "--version"-parameter
  + added support for trapping Alt+Space (closes italc#1704091)
  + also print log-messages to stdout
  + correct titlebar caption (closes italc#1700553)
  + set widget-cursor for vncView to according remote-cursor
    instead of drawing it - speeds thing a bit up
  + complete redesign of toolbar and buttons
  + made all code in common-dir a shared library which all
    components are linked against
  + do not reload clients if remote-control is active
  + do not resize to desktop-geometry in window-mode
  + lot of cleanups
  + use "halt" rather than "poweroff" for halting Linux-systems
  + when copying file add absolute paths to source-file-names
    (closes italc#1704173)
  + display user-name in toolbar (closes italc#1711333)
  + updated localizations
  + implemented "lock student"-functionality in remote-control
  + highlight current classroom in classroom-menu
  + added "hide teacher-clients"-feature
  + added key for loglevel: 0 silent, 2 fatal, 4 critical,
    6 warning, 9 debug, default is 6
  + changed log-directory to /tmp
  + added fullscreen-functionality via F11
  + stop demo on clients after student showed demo
  + also accepting keys that were generated using ssh-keygen
  + added "-screen"-argument which makes it possible to specify
    which screen the remote-control-window should be displayed on
  + fixed host-based authentication in such a way that it works for
    ThinClient-environments as well as when ports other than 5900
    are used for IVS (i.e. -ivsport has been used) - fixes
    non-working-demo in these scenarios
  + make Backtab (i.e. Shift+Tab) work properly in remote-control
    (closes italc#1889307)
- fix permissions of the generated keys
- added sysconfig file and init script
- start ica automatically via /etc/X11/xdm/Xsetup for clients
* Tue Jan 15 2008 lars@linux-schulserver.de
- add italc group automatically
- generate italc keys automatically
* Wed May  2 2007 lars@linux-schulserver.de
- update to 1.0.2
* Tue Dec 12 2006 lars@linux-schulserver.de
- initial package 1.0.0.0-rc2
