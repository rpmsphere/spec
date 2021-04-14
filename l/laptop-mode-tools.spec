Name:           laptop-mode-tools
Version:        1.67
Release:        6.1
Summary:        The Laptop Mode Tools
License:        GPL-2.0+
Group:          System/Base
URL:            http://www.samwel.tk/laptop_mode/
Source:         http://samwel.tk/laptop_mode/tools/downloads/%{name}_%{version}.tar.gz
##Source1:        laptop-mode-tools.pm-utils-hook
Source2:        README.%{name}
##Requires:  pm-utils
BuildRequires:  udev
BuildArch:      noarch

%description
Laptop Mode Tools is a laptop power saving package for Linux systems.
It allows you to extend the battery life of your laptop, in several
ways. It is the primary way to enable the Laptop Mode feature of the
Linux kernel, which lets your hard drive spin down. In addition, it
allows you to tweak a number of other power-related settings using a
simple configuration file.

%prep
%setup -q -n %{name}_%{version}
cp %{SOURCE2} README

%build

%install
DESTDIR=%{buildroot} MAN_D=%{_mandir} INSTALL=install INIT_D=none LIB_D=%{_libdir} UDEV_D=%{_udevrulesdir} SYSTEMD_UNIT_D=%{_unitdir} ACPI=DISABLED PMU=disabled APM=disabled ./install.sh
##install -D -m 0755 %{SOURCE1} %{buildroot}%{_libexecdir}/pm-utils/power.d/laptop-mode-tools
chmod 644 %{buildroot}/%{_mandir}/man8/*
# Don't ship sysvinit script
#rm -r %{buildroot}%{_sysconfdir}/init.d
# Fix a weird issue...
mv %{buildroot}%{_udevrulesdir}/rules.d/99-laptop-mode.rules %{buildroot}%{_udevrulesdir}/99-laptop-mode.rules
# Hack to remove sysvinit script link in usr/sbin
ln -s service %{buildroot}/%{_sbindir}/rclaptop-mode

%files
%dir %{_sysconfdir}/laptop-mode
%config %{_sysconfdir}/laptop-mode/*
%{_datadir}/%{name}
##{_libexecdir}/pm-utils/power.d/laptop-mode-tools
%{_sbindir}/*
%{_udevrulesdir}/lmt-udev
%{_udevrulesdir}/99-laptop-mode.rules
/usr/lib/pm-utils/sleep.d/01laptop-mode
%{_mandir}/man8/*
%doc README
%{_tmpfilesdir}/laptop-mode.conf
%{_unitdir}/laptop-mode.service

%changelog
* Thu Jul 09 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.67
- Rebuilt for Fedora
* Fri Jun 19 2015 tchvatal@suse.com
- Clean up all various rpmlint warnings
* Wed Dec 18 2013 p.drouand@gmail.com
- Update to version 1.64
  + Don't touch USB Controller power settings. The individual devices,
    when plugged in, while on battery, inherit the power settings
    from the USB controller
  + start-stop-programs: add support for systemd.
  + Replace hardcoded path to udevadm with "which udevadm".
  + Honor .conf files only.
  + Make '/usr/lib' path configurable. This is especially useful for
    systems that use /usr/lib64, or /lib64 directly
  + Don't call killall with the -g argument.
  + Fix RPM Spec file build errors
- Changes from 1.63
  + Kick the power savings back in, as soon as the stick is unplugged
  + Release lock descriptors in start-stop-programs module.
  + Add option to disable alarm level check. This is helpful if
    you have a broken battery reporting incorrect states
  + Check for external helper application's presence. And if not
    available, handle it.
  + Added PCIe ASPM module.
  + Do not ship the board-specific/ folder in default installs
- Remove AUTHORS section
- Remove laptop-mode-1.49-initscript.diff and
  laptop-mode-1.62-customize-installation-of-udev-systemd-files.patch;
  fixed on upstream release
- Switch to systemd
* Sun Aug 11 2013 seife+obs@b1-systems.com
- own all directories in /usr/lib/pm-utils/* to prevent build
  failure in case the pm-utils packaging changes again
* Fri Mar  8 2013 rmilasan@suse.com
- laptop-mode-1.62-customize-installation-of-udev-systemd-files.patch:
  introduce $LIB_D in install.sh so we can customize the installation
  of systemd/udev files.
- drop laptop-mode-1.60-local-can-only-be-used-in-a-function.patch:
  not need it anymore as 1.62 version has the fix.
* Mon Feb  4 2013 wstephenson@suse.com
- update to 1.62:
  * Add systemd support
  * Be specific on what file systems we want to handle. Given the
    wide range of file systems Linux has, we don't want to consider
    them all as not all of them fall under the power saving scenarios.
  * Factor out some common code
  * Do not touch autonegotiation settings. Fiddling with
    auto-negotiation settings can cause more problems and the
    standards expect them to be always on
  * Trim mount point display
  * Organize state/STATE tracking so that we get actual results.
  * cleaner output when asking status.
  * Append to stdout/stderr to avoid truncating file logs
  * Fix spec file for RPM syntax
- fix some rpmlint warnings
* Wed Jul 25 2012 rmilasan@suse.com
- Local variables can only be used in a function.
  add: laptop-mode-1.60-local-can-only-be-used-in-a-function.patch
* Fri Apr 13 2012 rmilasan@suse.com
- update to 1.60:
  * Check for block device's existence. Thanks to Simon Que.
  * Add suspend/resume helper tools: pm-helper, pm-suspend, pm-hibernate.
  * What laptop-mode-tools is stopped from init, also kill polling daemon.
  * Reliable and much better locking mechanics.
  * Make polling dameon lock safe.
  * Make lmt-udev distro neutral. Thanks to Simon Que.
  * Change Intel HDA Audio's default power save timeout to 2 seconds.
* Thu Sep 15 2011 hmacht@suse.de
- update to 1.59 (excerpt):
  - add support for kernel 3.x (this makes
    laptop-mode-tools-1.57-kernel3.0.patch superfluous)
  - add USB auto-suspend whitelist
  - Check for files instead of kernel version numbers
  - Enable new in-kernel polling mechanism for block devices
    (Debian BTS: #617705, #574867)
  - Add new module nmi-watchdog to handle NMI Watchdog related power
    savings. Thanks to Quentin Denis for the report
  - More minor fixes...
* Wed Jul 20 2011 aj@suse.de
- Support kernel 3.0
- Remove dependency on haldaemon since hal is an optional
  requirement, the package can work without it just fine.
- Update to 1.57:
  * many fixes
  * support for newer kernels
  * Add a new "exec-commands" module
  * Updated manpages
* Tue Dec  7 2010 coolo@novell.com
- prereq init script haldaemon
* Thu Feb 25 2010 ro@suse.de
- drop laptop-mode-1.49-moblin-disable-control-hd-powermgmt.patch
  again which was just changin a setting from another patch
  (laptop-mode-1.49_conf.diff).
  upstream has CONTROL_HD_POWERMGMT="auto" now
- update to 1.53
  * Add global enable/disable switch for laptop-mode-tools
  * Add scheduler power saving module for SMT processors. Thanks to John
    Reilly.
  * Add a new "Auto Modules" mode which enables all modules whitelisted as
    auto with a single configuration setting, ENABLE_AUTO_MODULES.
  * Add LM/NOLM option for Intel SATA Power Management
  * Do a check before trying to write to the SuperHE Control File
- update to 1.52
  * Initialize DEBUG to 0 by default. THanks to Matthijs Kooijman for pointing
    it out.
  * Add an option to completely disable ethernet devices when on battery.
  * Introduce hooks to enable debug mode for individual modules
  * Use iwconfig to determine device type for iwlwifi devices also
  * Collect the correct exit code for iwconfig execution.
  * Use iwconfig in wireless-iwl-power. Thanks to Darren Hoo for spotting it
  * Handle spaces in mount point names. Thanks to Louis Simard for the patch
  * Clarify about Global Debug mode and Module Specific Debug mode.
  * Fix incorrect variable reference in video-out module. Thanks to Hans Werner
    for noticing that.
- update to 1.51
  * Add option to blacklist usb devices by their device id.
    Thanks to ich@phuk.ath.cx for the patch
  * Trigger timer change for power mgmt by doing a device open/close
    The open/close operation can fail if the audio device is busy.
    Since this failure is non-fatal (worst case is that the timer changes
    don't get activated), we don't bother if it was successful or not.
  * Add support for EeePC FSB Control. Thanks to James Rayner
  * Update iwlwifi power modes. Thanks to Clemens Buchacher
    See Debian BTS: #540639
  * Use the standard pm-hibernate script from pm-utils for hibernation
    See Debian BTS: #541447
  * Check if wireless device is disabled before attempting to power configure it
    Thanks to Clemens Buchacher. See Debian BTS: #541997
  * On speed change, an ethernet device can lose connectivity. Document that in
    the config file
- update to 1.50
  * Ship pm-utils hooks in /usr/lib/ and not in /etc/pm/
    Distributions will always want to have customized settings in /etc
    and default upstream settings in /usr/lib. See LP: #384875
  * Fix incorrect explanation of Intel HDA Power Savings. See Debian
    BTS: #532733
  * Don't clutter screen with print messages.
  * Add patch from Mulyadi Santosa that adds ability to lm-profiler to show
    read/write frequency of each collected program. Thank you.
  * Enhance usb-autosuspend module to be executed under conditions. Also explain
    the weirdness of broken usb drivers. Fixes Debian Bug #535051
  * Do the test comparision of integeres using string operators. Fixes Debian
    Bug #535650
  * Run pidof with the -x Script Mode switch. Thanks Matthijs Kooijman
  * Disconnect descriptors when backgrounding a script. Thanks Matthijs Kooijman
  * Add option to run in shell debug mode
  * Add a spec file to generate an RPM package
* Fri Dec  4 2009 jlee@novell.com
- Add laptop-mode-1.49-moblin-enable-intel-hda-powersave.patch for
  enable audio power saving even using ac-power.
* Thu Nov 19 2009 jlee@novell.com
- Add laptop-mode-1.49-moblin-disable-control-hd-powermgmt.patch to
  disable the APM level setup to harddrive. (bug #545681)
* Mon Oct  5 2009 seife@opensuse.org
- fix/workaround laptop-mode-tools causing garbage in the pm-utils
  suspend / hibernate logfile
* Fri Jun 26 2009 seife@suse.de
- update to 1.49. Notable changes:
  - use syslog
  - better diagnostic messages
  - most of the other changes are unused in this package, see the
    changelog for more information
- adjust dirty_ratio defaults to new kernel's defaults
* Fri Jan 23 2009 seife@suse.de
- fix udevadm version check (bnc#468848), remove old patches
* Thu Jan 15 2009 seife@suse.de
- update to 1.45
  - various improvements, most are not used in this package
  - removed bashisms
  - AC adapter fixes
  - minor optimizations
  - manpage fixes
* Fri Dec 12 2008 hmacht@suse.de
- fix enabling of laptop-mode by default:
  Use %%insserv_force_if_yast instead of %%insserv_and_fillup to
  enable laptop-mode-tools by default (fate#304737)
* Wed Sep 24 2008 ro@suse.de
- use udevadm info instead of udevinfo
* Tue Sep 16 2008 hmacht@suse.de
- fate#304737
  start laptop-mode-tools by default
  remount devices with relatime when on battery
  set hard dist power management to 128 when on battery
* Tue Aug 19 2008 seife@suse.de
- Add "Default-Start:" and "Default-Stop:" to initscript
* Thu May  8 2008 seife@suse.de
- build fix
- add README.SUSE
- enhance the init script
- pm-utils integration
* Wed May  7 2008 seife@suse.de
- initial submission, version 1.41
