Summary:   USB hubs and docking stations handling rules and scripts
Name:      sumu
Version:   3.0.38
Release:   1
URL:       http://code.google.com/p/otb-sources/wiki/SUMU
License:   MIT
Group:     System Environment/Base
Vendor:    Open Technologies Bulgaria, Ltd. <http://otb.bg>

# built by the `make tar' command
Source0:   sumu.tar.gz
BuildArch: noarch
Requires: sed
Requires: grep
Requires: mktemp
Requires: udev
Requires: util-linux
Requires: /bin/su
Requires: /usr/bin/X
Requires: /usr/bin/readlink
Requires: /usr/bin/gdmdynamic
Requires: /usr/bin/Xvnc
Requires(post): chkconfig
Requires(post): grubby
Requires(preun): chkconfig

%description
USB hubs and docking stations handling rules and scripts
which provide the ability to run multiple seats on a single computer.
This is based on upstream work from
http://libdlo.freedesktop.org/wiki/MultiSeatTerminal

%prep
%setup -q -c

%build
echo > /dev/null

%install
rm -rf %{buildroot}

cd sumu/

mkdir -p %{buildroot}/%{_sysconfdir}/logrotate.d
install -m 0644 src/logrotate.conf %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
install -m 0644 src/gdm.conf      %{buildroot}/%{_sysconfdir}/%{name}/
install -m 0644 src/xorg.conf.sed %{buildroot}/%{_sysconfdir}/%{name}/

mkdir -p %{buildroot}/%{_sysconfdir}/udev/rules.d
install -m 0644 src/50-usbseat.rules %{buildroot}/%{_sysconfdir}/udev/rules.d

mkdir -p %{buildroot}/%{_sysconfdir}/udev/scripts
install -m 0755 src/start-seat %{buildroot}/%{_sysconfdir}/udev/scripts
install -m 0755 src/stop-seat  %{buildroot}/%{_sysconfdir}/udev/scripts

mkdir -p %{buildroot}/etc/rc.d/init.d/
install -m 0755 src/init.d.sumu %{buildroot}/etc/rc.d/init.d/%{name}

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 src/sumu-hub-id %{buildroot}/%{_bindir}/
install -m 0755 src/disable-thumbnails.sh %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 doc/README  %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 doc/COPYING %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 doc/HOWTO   %{buildroot}/%{_docdir}/%{name}-%{version}

mkdir -p %{buildroot}/%{_var}/log/sumu

%clean
rm -rf %{buildroot}

%files
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/udev/rules.d/50-usbseat.rules
%{_sysconfdir}/udev/scripts/start-seat
%{_sysconfdir}/udev/scripts/stop-seat
/etc/rc.d/init.d/%{name}
%{_bindir}/sumu-hub-id
%{_bindir}/disable-thumbnails.sh
%doc %{_docdir}/%{name}-%{version}/
%dir %{_var}/log/sumu

%post
chkconfig --add %{name}
chkconfig %{name} on

# update bootloader configuration to remove the rhgb and quiet arguments
for k in `find /boot -name "vmlinuz*"`; do
    grubby --grub --update-kernel="$k" --remove-args="rhgb quiet"
done

# NOTE: sed will always make backups regardless if the file was updated
# and this will overwrite the original backup on the next update, rhbz#651905

# set the runlevel to 3 - text mode if we're in X11 mode
sed -i "s/id:5:initdefault:/id:3:initdefault:/" /etc/inittab

# set SELinux into permissive mode if in enforcing mode
sed -i "s/SELINUX=enforcing/SELINUX=permissive/" /etc/selinux/config

%preun
if [ $1 = 0 ]; then
    chkconfig --del %{name}
fi

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.38
- Rebuilt for Fedora

* Mon Oct 31 2011 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.38-1.el6otb
- Revert changes and requirements on never kmod-udlfb
- Updates were not released

* Wed Oct 26 2011 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.37-1.el6otb
- require newer kmod-udlfb
- change the path to fbdev device (rhbz #726163)

* Thu Mar 17 2011 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.36-1.el6otb
- Added /usr/bin/disable-thumbnails.sh to disable thumbnails in GNOME and Nautilus

* Sun Mar 06 2011 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.35-1.el6otb
- set AlwaysRestartServer to false in gdm.conf. Solves issue with Xorg
  taking 100%% CPU after logout

* Tue Feb 22 2011 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.34-1.el6otb
- separate sumu-init.sh to sumu-audio-hooks package
- update udev rules for older UGA device to match the event mouse

* Fri Jan 14 2011 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.33-1.el6otb
- remove workarounds for issue #20. Fixed by latest udlfb
- make stop-seat accept arguments in the same format as start-seat but keep 
  backward compatibility
- add vnc screen at display :99 for teacher login - NB: iptables needs adjustment,
  see doc/HOWTO
- make udev link to event mouse (eventX) instead of input mouse (inputY) and
  make xorg.conf use evdev by default for mouse driver. This fixes scroll.

* Fri Nov 12 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.31-1.el6otb
- after `service sumu start' wait for 5 seconds and unblank all black screens.
  fixes http://code.google.com/p/otb-sources/issues/detail?id=20
- `service sumu status' is now more verbose

* Mon Nov 08 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.30-1.el6otb
- remove -novtswitch -sharevts from Xorg command line and add vt07. This fixes
  the issue where input is duplicated on tty1. 
- Add DontVTSwitch to xorg.conf to complement the tty1 fix.
- Add StandbyTime to xorg.conf to turn off monitors after 1 minite @ GDM login screen.
  This is a workaround for http://code.google.com/p/otb-sources/issues/detail?id=20
- Disable redundant options in xorg.conf - CoreKeyboard, CorePointer, Buttons, ZAxisMapping
  these options don't seem to have anny effect.

* Sat Nov 06 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.29-1.el6otb
- add more logging to start-seat and stop-seat
- in start-seat only run gdmdynamic -r after successfull add of display
- start gdm with our config file instead of modifying the default one
- copy all distro settings from gdm/defaults.conf to gdm.conf

* Tue Nov 02 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.28-2.el6otb
- use el6otb as dist tag

* Mon Nov 01 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.28-1
- adjust internal code structure
- add the HOWTO file 
- add logging to stop-seat

* Fri Oct 29 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.27-1
- Move the /etc/modprobe.d/udlfb.conf file to kmod-udlfb package
- add /etc/sumu and move config files under there
- log gdmdynamic output to /var/log/sumu/gdmdynamic.log
- add logrotate rules

* Mon Oct 25 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.26-1
- revert back to CorePointer/CoreKeyboard in xorg.conf. Fixes:
  http://code.google.com/p/otb-sources/issues/detail?id=19

* Fri Oct 22 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.25-2
- bump release field to compile a package for public distribution

* Fri Oct 22 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.25-1
- reduce code in start-seat and stop-seat to minimum,
  this makes those scripts thread-safe as much as possible without
  using blocking primitives
- call udevadm settle in the init script
- increase sleep to 2 sec and sleep between gdmdynamic invocations
  this slows down start-up but works around timing issues

* Thu Oct 21 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.24-1
- disable udev rules for old UD-160-A devices otherwise daisy chaining
  with new UGA-125-HUB devices breaks
- text console is now controlled by /etc/modprobe.d/udlfb.conf
- use SendCoreEvents instead of deprecated CorePointer
- split usbseat.sh into start-seat and stop-seat
- update udev rules to use the split scripts
- stop the seats in the init script
- produce verbose device names

* Mon Oct 11 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.23-1
- add the hub-id.sh script for busnum/devnum numbering
- update udev rules to use the new script
- add dependency on util-linux for the logger command

* Fri Oct 08 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.22-1
- use variable and quotes in init script when checking pid of gdm-binary
- use variable and quotes in usbseat.sh when checking pid of gdm-binary
- use separate test operators and variable quoting in usbseat.sh
- use static udev rules in 50-usbseat.rules
- get rid of find-parent-hub.sh which can lead to race conditions

* Tue Oct 07 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.21-1
- remove hard-coded binaries path in find-parent-hub.sh
- change NVR scheme, omit one 0

* Tue Sep 15 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.20-2
- configure some runtime parameters:
  o remove bootloader parameters rhgb and quiet
  o set default runlevel to 3 post install
  o set SELinux in permissive mode
  o turn sumu on by default
- add dependency on grubby
- fix typo in init script
- fix typos in usbseat.sh, convert tabs to spaces and remove extra variables

* Mon Sep 13 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.20-1
- GDM 2.16 can now be used - remove custom login manager and related files
- remove extra Requires and clean up the spec file
- simplify the usbseat.sh file to the original version + som eenhancements
- add the gdm.conf back in the package

* Sun Jul 04 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.19-1
- Use /tmp/xorg.conf.$SEAT_ID.XXXXXX as filename for temporary Xorg config
- add the find-parent-hub.sh file and use it in udev rules

* Sun Jun 13 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.18-1
- configure environment variables in sumu-init.sh
- Start /etc/X11/xinit/xinitrc which will start default session
- add the Last language option in the UI

* Sat Jun 12 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.17-1
- add support for language preference
- use gettext to translate UI and add Bulgarian translation

* Thu Jun 10 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.16-1
- export SEAT_ID variable and use it to display seat it at login prompt
- removed sumu-launch-session and replaced with gnome-session

* Wed Jun 09 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.15-1
- add logging for X, metacity and sumu-login-handler
- remove Module section from xorg.conf template - not needed anymore

* Mon Jun 07 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.14-1
- add the sumu-launch-session script
- update spec file to use macros for %%{_bindir} and %%{_datadir}
- center dialogs in the parent window, needs metacity
- start metacity during login window
- added Requires: /usr/bin/metacity

* Sun Jun 06 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.13-1
- add confirmation dialog for shutdown/reboot
- validate username/password against /etc/shadow
- get rid of subprocess module
- change order of functions/imports

* Fri Jun 04 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.12-1
- re-organize source code structure and adjust spec file to it
- add custom login-handler which will start gnome-session
- remove gdm.conf and Requires: gdm - not used in this version
- remove PRODUCT_VERSION from Makefile
- add requirements on pygtk and Glade

* Thu Jun 03 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.11-1
- enable X driver search in /usr/local/lib/xorg/modules. This is required 
  because customized Xorg driver will conflict with stock fbdev driver

* Sun May 30 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 3.0.0.10-1
- initial build for RHEL6
- remove VNC, awk, xdpyinfo dependency
- remove sysconfig file

* Sat Apr 10 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 2.1.0.9-1
- fix http://code.google.com/p/otb-sources/issues/detail?id=2
  use the BUS key instead of SUBSYSTEMS key which doesn't work on RHEL5.5
- bump version to make new release of the package

* Tue Mar 30 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 2.1.0.8-1
- rebuild for SUMU 2.1 release

* Sat Jan 23 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.8-1
- fix incorrect quote in udev rules file

* Sat Jan 23 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.7-2
- better detection of sound device using /dev/snd/controlC*
- this doesn't leave dangling symlinks and reduces code
- fix config files rpmlint warnings

* Mon Dec 14 2009 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.6-1
- add sysconfig file to remove hardcoded stuff

* Sat Dec 12 2009 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.5-1
- remove build-alsa-usb-id.sh
- use udev to create a link to the sound card device

* Fri Dec 11 2009 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.4-1
- fix broken handle-login.sh
- fix broken alsa-config-for-sumu.sh so users can login

* Thu Dec 10 2009 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.3-1
- store USB sound card id under /dev/usbseat/*/alsa-card-id
- add a script under /etc/profile.d which will configure the
  default sound card
- fix rpmlint warnings

* Mon Dec 7 2009 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.2-2
- resolved gdm/custom.conf conflict

* Mon Dec 7 2009 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.2-1
- Package name changed
- Added init.d script

* Sun Dec 6 2009 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.1-1
- Initial revision
