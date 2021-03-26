Name:           hwinfo
BuildRequires:  doxygen flex perl-XML-Parser udev
BuildRequires:  perl-XML-Writer
BuildRequires:  libx86emu-devel
License:        GPL-2.0+
Group:          Hardware/Other
Provides:       libhd
Obsoletes:      libhd
Summary:        Hardware Library
Version:        21.29
Release:        3.1
URL:            https://github.com/openSUSE/hwinfo
Source:         %{name}-%{version}.tar.gz

%description
A simple program that lists results from the hardware detection
library.

%package      devel
License:        GPL-2.0+
Summary:        Hardware Detection Library
Group:          Development/Libraries/C and C++
Provides:       libhddev
Obsoletes:      libhddev
Requires:       %name = %version perl-XML-Parser udev wireless-tools
Requires:       perl-XML-Writer 
Requires:       expat-devel

%description devel
This library collects information about the hardware installed on a
system.

%prep
%setup -q
echo %{version} > VERSION
rm git2log

%build
make static
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}
install -m 644 src/libhd.a $RPM_BUILD_ROOT%{_libdir}
make clean
make LIBDIR=%{_libdir}
make doc
gzip -9c doc/hwinfo.8 >hwinfo.8.gz

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir}
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 hwinfo.8.gz $RPM_BUILD_ROOT%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT/var/lib/hardware/udi

%clean 
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/sbin/hwinfo
/usr/sbin/mk_isdnhwdb
/usr/sbin/getsysinfo
%{_libdir}/libhd.so.*
%doc README*
%doc %{_mandir}/man8/hwinfo.8.gz
%dir /var/lib/hardware
%dir /var/lib/hardware/udi
%dir /usr/share/hwinfo
/usr/share/hwinfo/*

%files devel
/usr/sbin/check_hd
/usr/sbin/convert_hd
%{_libdir}/libhd.so
%{_libdir}/pkgconfig/hwinfo.pc
/usr/include/hd.h
%doc doc/libhd/html

%changelog
* Sun Jul 17 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 21.29
- Rebuild for Fedora
* Mon Oct  7 2013 snwint@suse.de
- AArch64 support
- Add support for AArch64
- Add a new CPU Arch Type, AArch64, and properly
- parse the /proc/cpuinfo (that is quite similar to ARM 32bit)
- Remove various unused variables
- Fix sizing error in memset() call
* Fri Oct  7 2011 snwint@suse.de
- fix network detection if several interfaces are attached to a single pci function (bnc #693090)
- fixed typo
- USB joystick fixes
- replace USB details by joystick details
- set unix_dev_name2 to /dev/input/jsX
- added Gameport bus, detect gameport joysticks
- cleanup - removed unused variables
- added NULL checks
- joystick: detect and report number of axes and buttons
- added support for detecting USB joysticks
- updated .gitignore
- added .gitignore files
- show disk capacity in GB
* Fri Mar 11 2011 snwint@suse.de
- check for battery, too, to decide on notebook (bnc #678456)
* Tue Mar  8 2011 snwint@suse.de
- avoid potential NULL pointer reference (bnc #677686)
* Wed Feb 16 2011 snwint@suse.de
- support Draytech miniVigor 128 ISDN (bnc #663288)
* Wed Feb 16 2011 snwint@suse.de
- support Validity fingerprint sensor (bnc #644149)
- add vmbus storage controllers (bnc #654959)
- fix SPARC compile fixes
* Wed Sep 15 2010 kkaempf@novell.com
- Fix build on non-SUSE distros
* Wed Aug 25 2010 snwint@suse.de
- added more fingerprint sensors
* Tue Aug 17 2010 snwint@suse.de
- parse id files in /var/lib/hardware/ids
- added fingerprint sensor (bnc #528596)
* Tue Jun 22 2010 snwint@suse.de
- assume notebook if there's a track point or touch pad (bnc #591703)
* Mon Jun  7 2010 snwint@suse.de
- fix NULL pointer bug (bnc #610454)
* Fri May 21 2010 snwint@suse.de
- detect formfactor without hal (bnc #591703)
* Wed Mar 17 2010 snwint@suse.de
- remove hal dependency
- removed VERSION
* Mon Mar 15 2010 snwint@suse.de
- fix memory size detection (bnc #588028)
- create VERSION and changelog from git repo
- fix compile on non-suse systems
* Fri Feb 12 2010 snwint@suse.de
- fix device renaming detection (bnc #574442)
- more cpu features (bnc #578994)
- recognize agere modem lines (bnc #578286)
* Fri Oct  9 2009 snwint@suse.de
- made kernel log parser aware of time stamps (bnc #544269)
* Wed Sep 30 2009 snwint@suse.de
- map video memory writable (bnc #539227)
- fix memory leak when run as non-root (bnc #519015)
- updated dvb & tv card info (bnc #465139)
- updated pci ids
- fix video memory mapping (bnc #539227)
- recognize usb auto & smartcard devices (bnc #290279)
* Wed Sep 16 2009 snwint@suse.de
- check for ddc capabilities before issuing a ddc call (suggested by Anssi Hannula)
* Mon Aug  3 2009 snwint@suse.de
- revert --log patch from v16.3; leads to all kinds of
  problems (bnc #525223)
* Wed Jul 29 2009 snwint@suse.de
- support NPIV (bnc #501312)
- added some ISDN devices (bnc #234529)
* Wed Jun 24 2009 snwint@suse.de
- --log without other options assumes --all (bnc #243103)
- rewrote man page, help text & README (bnc #178662)
* Fri Jun 19 2009 coolo@novell.com
- disable as-needed for this package as it fails to build with it
* Mon Jun 15 2009 snwint@suse.de
- fix build on non-x86 archs
* Tue Jun  9 2009 snwint@suse.de
- rewrite monitor detection to use libx86emu
* Thu May 14 2009 snwint@suse.de
- setup dummy int 0x15 for BIOS emulation (bnc #469863)
- fix memory size detection (bnc #500410)
- 'hwprobe' variables can now have values (int, string, list) instead of
  being just flags
- fix some compiler warnings
* Thu Jan 22 2009 snwint@suse.de
- make ehea look more ordinary (bnc #467033)
* Fri Jan 16 2009 snwint@suse.de
- added HP LCD size (bnc #465858)
* Tue Jan 13 2009 uli@suse.de
- determine unix_dev_name for IUCV interfaces (bnc #457537)
* Mon Jan 12 2009 snwint@suse.de
- avoid segfault with broken sysfs data (bnc #461161)
* Fri Jan  9 2009 snwint@suse.de
- fix input device detection (bnc #457834)
* Thu Dec 11 2008 snwint@suse.de
- add some more instructions to the x86 emulation (bnc #406804)
* Mon Nov 24 2008 snwint@suse.de
- more ibm displays (bnc #446699)
* Fri Nov 21 2008 snwint@suse.de
- updated pci ids from latest pciutils-ids
* Fri Nov 21 2008 snwint@suse.de
- another ibm display (bnc #446699)
* Wed Nov 19 2008 snwint@suse.de
- only avoid mouse/modem detection on usb->serial adapter (bnc #408715)
* Tue Nov 18 2008 snwint@suse.de
- map video memory for vbe calls (bnc #441802)
* Mon Nov 17 2008 snwint@suse.de
- fix wlan detection (bnc #441778)
* Fri Nov 14 2008 snwint@suse.de
- more display sizes (bnc #441796)
* Fri Nov  7 2008 snwint@suse.de
- ibm kiosk system display sizes (bnc #441796)
* Wed Nov  5 2008 snwint@suse.de
- fix ehea detection (bnc #436954)
* Wed Oct 15 2008 snwint@suse.de
- removed ancient refs to ide-generic (bnc #433105)
* Wed Oct  8 2008 uli@suse.de
- s390: dual port OSA Express devices are not detectable; fixing
  dualport flag to 1 (fate #304080)
- s390: adapt to change in sysfs symlink structure (bnc #431533)
* Mon Oct  6 2008 snwint@suse.de
- one more fingerprint sensor
* Mon Oct  6 2008 snwint@suse.de
- re-reverse hardware item lists (bnc #388754, #414717)
- new fingerprint readers (bnc #429533)
* Fri Sep 26 2008 snwint@suse.de
- dump network card eeprom to log (bnc #430170)
* Thu Sep 25 2008 uli@suse.de
- s390: dual port OSA Express devices are not detectable; fixing
  dualport flag to 1 (fate #304080)
* Mon Sep 22 2008 uli@suse.de
- s390: added dualport flag for OSA devices (currently unused until
  we know what devices support it; fate #304080)
* Mon Sep 15 2008 snwint@suse.de
- use udevadm instead of udevinfo
* Tue Sep  9 2008 ro@suse.de
- fix build on x86 with 2.6.67 kernel includes
* Fri Aug  8 2008 olh@suse.de
- add inital POWER6 ibmebus support for ehea network (bnc#394602 -LTC44938)
* Tue Jul 22 2008 snwint@suse.de
- fixed compiling on s390
* Mon Jul 21 2008 snwint@suse.de
- skip T-Balancer BigNG (bnc #408715)
* Mon Jul 21 2008 snwint@suse.de
- support virtio devices (bnc #404803)
- detect virtio mouse
* Wed Jul 16 2008 snwint@suse.de
- updated X11 data
- add fibre channel resource
* Mon Jun  2 2008 snwint@suse.de
- fix macbook keyboard detection (bnc #374101)
* Mon May 26 2008 snwint@suse.de
- ppc: report usb controller properly (bnc #368234)
* Mon May 19 2008 snwint@suse.de
- braille: ht detection needs longer timeouts
- adjusted panel size (bnc #373997)
* Fri May  9 2008 snwint@suse.de
- fixed typo in recent braille code change
* Fri May  9 2008 snwint@suse.de
- another go at mv643xx (bnc #359867)
* Fri May  9 2008 snwint@suse.de
- read up to 4 ddc records from sysfs tree (bnc #387064)
- not everything is a mouse (bnc #373177)
- updated X11 data (bnc #387880)
- detect more braille devices
* Mon Apr 28 2008 snwint@suse.de
- add some more fingerprint sensors (bnc #382273)
- monitors added (bnc #373997)
* Mon Apr 14 2008 snwint@suse.de
- disable old isa isdn card detection (bnc #359175)
* Thu Mar 20 2008 snwint@suse.de
- fix mv643xx fix (bnc #359867)
* Wed Mar 19 2008 snwint@suse.de
- fix bios id assignment with multipath disks
* Mon Mar 17 2008 snwint@suse.de
- fix mv643xx detection (bnc #359867)
- updated ps3 network card detection (bnc #370850)
* Fri Mar 14 2008 snwint@suse.de
- wlan detection sometimes missed network cards (bnc #368442)
- ide-cd module name changed
- make hwprobe=+udev work again
- support MS virtual network devs (bnc #359261)
* Thu Mar  6 2008 snwint@suse.de
- fix compilation on x86_64
* Thu Mar  6 2008 snwint@suse.de
- try a bit harder to find matching card for an interface (bnc #356405)
- fix segfault in new mouse code (bnc #367457)
* Tue Mar  4 2008 snwint@suse.de
- detect vmware mouse (bnc #358460)
* Mon Mar  3 2008 snwint@suse.de
- hal: info.bus -> info.subsystem
- detect virtualbox mouse (bnc #358460)
* Fri Feb 29 2008 snwint@suse.de
- adjust mouse detection to work with mice that do not use
  /dev/input/mice but work via event dev (bnc #266002)
- change input device code to use kernel device ids for input devices
- adjust to latest sysfs changes
- work around some strange pci subdevice names (bnc #183188)
- update pci device name database
* Tue Feb  5 2008 snwint@suse.de
- updated X11 data
- even better BIOS disk id handling
* Fri Feb  1 2008 snwint@suse.de
- need to increase major version (due to changes in introduced in v13.59)
* Mon Jan 28 2008 snwint@suse.de
- more braille devices
* Mon Jan 28 2008 snwint@suse.de
- look at ancient unique-keys directory, too
- rewrote BIOS disk id assignment
- updated X11 data
* Thu Dec 27 2007 crrodriguez@suse.de
- fix library-without-ldconfig-post* errors
* Tue Sep 25 2007 snwint@suse.de
- braille: fix el2d detection; wait longer in ht code
- fix mv643xx detection (#300613)
* Mon Sep 24 2007 snwint@suse.de
- updated X11 data (#326503)
* Mon Sep 24 2007 snwint@suse.de
- updated X11 data (#327568)
* Tue Sep 18 2007 snwint@suse.de
- updated X11 data
* Mon Sep 17 2007 snwint@suse.de
- updated pci & usb ids
* Tue Sep 11 2007 snwint@suse.de
- look for old config files in udi subdir, too (#308198, #309051)
* Mon Sep 10 2007 snwint@suse.de
- updated X11 data (#307218)
* Tue Sep  4 2007 snwint@suse.de
- some more dir -> link sysfs changes (#303978)
* Mon Sep  3 2007 snwint@suse.de
- slusb: make it a modem (#94155)
- rework mv643xx detection (#300613)
* Wed Aug 29 2007 snwint@suse.de
- fix wlan detection (#302045)
- detect ps3 sound card (#305913)
* Mon Aug 27 2007 snwint@suse.de
- rework iseries handling (#302667)
- handle ahci/ata_piix issue (#304134)
- update forcedeth info (#297606)
- change subclass id for wlan cards (#288450)
* Wed Aug 22 2007 snwint@suse.de
- prepare for upcoming sysfs change (#299685)
- updated X11 data
- monitor detection: handle >1 detailed timing info block
* Mon Aug 20 2007 snwint@suse.de
- deprecate sk98in (#298724)
- fix ppc buffer overrun (#301752)
- updated X11 data
* Wed Aug 15 2007 snwint@suse.de
- olh: generate fake EDID for known powermacs (#299202)
- adjusted help text (#299770)
- get wlan interfaces right (#298365)
- ppc: support ttyPSC0 console (#259923)
- ppc: EFIKA support (#263773)
- updated X11 data
* Wed Aug  8 2007 uli@suse.de
- s390: handle missing CCW device attributes
* Mon Jul 30 2007 snwint@suse.de
- olh: add ppc sound card (#295614)
* Mon Jul 30 2007 snwint@suse.de
- ps3: new disk & cdrom code (#294789, #295097)
* Wed Jul 25 2007 snwint@suse.de
- more wlan drivers (#291131)
- fixed framebuffer color depth calculation (#294334)
* Mon Jul 16 2007 snwint@suse.de
- add fingerprint reader support
* Thu Jul 12 2007 snwint@suse.de
- updated X11 data
* Fri Jun 22 2007 snwint@suse.de
- hschaa: fix wpa issue (#168971)
- removed slamr data (#284287)
* Wed May 16 2007 snwint@suse.de
- corrected ps3 patch
* Fri May 11 2007 snwint@suse.de
- sassmann: added ps3 support (#273135)
* Thu May  3 2007 snwint@suse.de
- braille detection can no longer block libhd (#266163)
- get network interface link state from sysfs
* Thu May  3 2007 prusnak@suse.cz
- changed expat to libexpat-devel in Requires of devel subpackage
* Thu Apr 12 2007 snwint@suse.de
- resolving symlinks in sysfs did not work properly
- updated X11 data
* Thu Mar 29 2007 snwint@suse.de
- added flex to BuildRequires
* Wed Mar 28 2007 snwint@suse.de
- changed network detection to work with latest sysfs
* Tue Mar 27 2007 snwint@suse.de
- changed getsysinfo to avoid 'cp'
- load ide-disk, too (#250241)
* Fri Mar 16 2007 snwint@suse.de
- better cpu detection (#252183)
* Thu Mar  8 2007 snwint@suse.de
- updated X11 data
* Thu Mar  1 2007 snwint@suse.de
- perfer libata modules over ide
* Wed Feb 28 2007 snwint@suse.de
- map only disks
* Tue Feb 27 2007 snwint@suse.de
- new xen code broke non-x86 archs
- rewrote '--map' option
* Wed Feb 21 2007 snwint@suse.de
- removed most of prom parsing code (#220762)
- detect new xen stuff (#241564)
* Mon Feb 19 2007 snwint@suse.de
- provide a bit more xen device info (#241564)
- sysfs: 'bus' is now called 'subsystem'
- support ehea devices (#243710)
* Fri Feb  9 2007 snwint@suse.de
- use dpt_i2o, not i2o (#176735)
* Fri Feb  9 2007 snwint@suse.de
- be careful reading MP config table to make Xen happy (#154681)
- ensure network/hardware sysfs ID consistency (bug #168492)
* Fri Jan 26 2007 snwint@suse.de
- there are usb tapes (#222978)
- apple vs. pc kbd layout issue solved for ppc (#233968)
* Mon Nov 27 2006 snwint@suse.de
- updated X11 data
* Fri Nov 24 2006 snwint@suse.de
- updated X11 data
* Fri Nov 24 2006 snwint@suse.de
- updated X11 data
- fix xen network detection (#220817)
* Mon Nov 20 2006 snwint@suse.de
- sometimes usb mice were missed (#216091)
* Tue Nov 14 2006 snwint@suse.de
- read modalias entry for macio devices (#220762)
- fixed modalias matching
* Mon Nov 13 2006 snwint@suse.de
- updated X11 data (#220171)
* Fri Nov 10 2006 snwint@suse.de
- updated X11 data (#213029)
* Fri Oct 27 2006 snwint@suse.de
- resolved piix vs. ata_piix (#214992)
* Wed Oct 25 2006 snwint@suse.de
- sometimes it's not really an usb mouse (#208745)
- give all apple usb keyboards a 'macintosh' layout (#213294)
* Fri Oct 20 2006 snwint@suse.de
- more checks for obviously broken monitor sizes (#213630)
* Thu Oct 19 2006 snwint@suse.de
- thoenig: do not close shared connection to the D-Bus system bus
- added hd_update_driver_data() that updates just the driver
  information for an hardware item
* Mon Oct 16 2006 thoenig@suse.de
- add patch hwinfo-do-not-close-shared-connection-thoenig-01.patch:
  Do not close shared connection to the D-Bus system bus.
* Wed Oct 11 2006 snwint@suse.de
- added magic for pata_* modules (libata based ide modules)
* Tue Oct 10 2006 snwint@suse.de
- scan 3 ports on all notebooks with nvidia cards for monitor data
- print detailed monitor timings
- report driver module name
* Wed Sep 27 2006 snwint@suse.de
- revert TIOCGDEV removal accidentally introduced in v13.0 (#201741)
- remove adb code (#206648)
- provide bogo mips value (#206649)
- no edd unless x86 or x86_64 (#206654)
- always use cpu emulation for BIOS calls (#207112)
- on dell notebooks, scan 3 ports for monitor data (#162973)
- include ACPI dump in log (#143090)
- drop tiny lib
* Mon Sep 18 2006 snwint@suse.de
- acx_pci is now acx (#164992)
- updated X11 data
* Mon Sep 11 2006 snwint@suse.de
- fixed minor bug
- use RPM_OPT_FLAGS
* Mon Sep  4 2006 snwint@suse.de
- more general modalias matching (#199112)
- more device files (#159405)
- mvidner: add pkgconfig file
* Tue Aug 29 2006 snwint@suse.de
- updated X11 data
- x86 emulation was not turned on for broken BIOSes (#188839)
- use dbus_connection_close, not dbus_connection_disconnect
- removed libsysfs
* Thu Aug 24 2006 thoenig@suse.de
- revert duplication of dbus_connection_unref as libdbus is now
  fixed
* Mon Aug 21 2006 ro@suse.de
- duplicate dbus_connection_unref to avoid dbus crash
* Mon Aug 14 2006 thoenig@suse.de
- Add patch hwinfo-dbus-api-fix-thoenig-01.patch: Use
  dbus_connection_close, not dbus_connection_disconnect
* Thu Jun 29 2006 snwint@suse.de
- add another sanity check to ddc parser (#186096)
- updated X11 data (#176929, #186055)
- glogow@fbihome.de: major documentation update
* Fri Jun  9 2006 snwint@suse.de
- internal monitor db can override fsc data
- add --nowpa option (#168971)
- parse monitor timing information
- updated X11 data
- don't strip binaries
* Mon May 22 2006 schwab@suse.de
- Don't strip binaries.
* Mon May  8 2006 snwint@suse.de
- fix some memory leaks (#148043)
- jdelvare: last 240 bytes of ROM were not scanned for SMBIOS
  entry point (#171640)
- jdelvare: support legacy DMI entry points (#17164)
- get vio devices from sysfs, not prom (#161684)
- don't load st module (#160304)
- fixed really big memory leak in s390 code (bug #148043)
* Tue May  2 2006 snwint@suse.de
- updated X11 data
* Thu Apr 27 2006 snwint@suse.de
- updated X11 data
- added dvb card (#169693)
* Tue Apr 25 2006 snwint@suse.de
- report monitor bandwidth
- remove obsolete megaraid info (#168325)
* Fri Apr 21 2006 snwint@suse.de
- iseries network driver was renamed to iseries_veth (#162209)
* Tue Apr 18 2006 snwint@suse.de
- removed references to kernel-nongpl (#155357)
* Wed Apr 12 2006 snwint@suse.de
- updated X11 data
* Tue Apr 11 2006 snwint@suse.de
- s390: storage controller need sysfs id (#162961)
* Tue Apr 11 2006 snwint@suse.de
- updated X11 data
* Mon Apr 10 2006 snwint@suse.de
- add module info ('ctc') for ficon channels (#162961)
* Mon Apr 10 2006 snwint@suse.de
- updated X11 data
* Fri Apr  7 2006 snwint@suse.de
- updated X11 data
* Mon Apr  3 2006 snwint@suse.de
- updated X11 data
* Thu Mar 30 2006 snwint@suse.de
- updated X11 data
- fixed minor bug in X11 CDB access script
* Mon Mar 27 2006 snwint@suse.de
- updated X11 data
- cleaned up network module data
- updated pci ids
- more macio devices (#115845, #117639)
* Fri Mar 17 2006 snwint@suse.de
- support mv643xx_eth (#117053)
- jg: fix WPA capabilities detection (#154725)
- updated X11 data
- support macio wireless (#104300)
* Tue Mar 14 2006 snwint@suse.de
- limit monitor detection to 2 ports (#155018)
* Tue Mar 14 2006 snwint@suse.de
- assigning to HAL udi could go wrong
- added 'hotpluggable' flag for external drives (#150744)
- suport more DVD types
* Mon Mar 13 2006 snwint@suse.de
- added LCD data (#157587)
- updated X11 data
* Thu Mar  9 2006 snwint@suse.de
- don't map video bios ram - not really necessary; added hwprobe=bios.nvram
  option to turn it back on, in case it causes trouble (#155132)
- remove remaining perror()s so we don't write to stderr (#155132)
* Wed Mar  8 2006 snwint@suse.de
- don't report hp-officeJet package (#155973)
- add sanity check for monitor size data (#155096)
- ppc monitor detection modernized (#156075)
* Mon Feb 27 2006 snwint@suse.de
- fix libhd bug detecting mice on older 2.6 kernels
* Mon Feb 20 2006 snwint@suse.de
- another LCD added (#151867)
- ms: detect more than one monitor
* Thu Feb 16 2006 snwint@suse.de
- removed avm_fcdsl (#151148)
- more compact LCD data set
* Tue Feb 14 2006 snwint@suse.de
- added LCD size
- s390 dasd code conflicted with iSeries (#148346)
* Mon Feb 13 2006 snwint@suse.de
- better DDC parser
- compact ibm notebook list
- updated X11 data
* Fri Feb 10 2006 snwint@suse.de
- ms: report LCD size
- updated ibm notebook list
* Wed Feb  8 2006 snwint@suse.de
- added --hddb-dir option to hwinfo (#120079)
- new wlan driver (#145190)
- remove dep on wireless-tools
- some LCDs added (#147516)
* Mon Jan 30 2006 snwint@suse.de
- updated X11 data
* Fri Jan 27 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Jan 25 2006 snwint@suse.de
- fixed serial device detection problem on Dell PowerEdge (#145051)
- report system type (e.g. laptop) (#145485), resulting in:
- upgraded major version to reflect api change
* Mon Jan 23 2006 snwint@suse.de
- better monitor detection
- updated X11 data
- qla* modules require qlogic-firmware
* Mon Jan 16 2006 snwint@suse.de
- added qla4xxx workaround (#141069)
* Mon Jan  9 2006 snwint@suse.de
- adjusted i2o driver info (#129301)
* Mon Jan  9 2006 snwint@suse.de
- jg: wlan update
* Fri Dec  9 2005 snwint@suse.de
- add VirtualIron network cards (#135309)
- updated X11 data
* Wed Dec  7 2005 snwint@suse.de
- report ide-generic for non-pci ide interfaces
* Tue Dec  6 2005 snwint@suse.de
- s390: make sysfs reading more robust
- s390: fixed stack corruption on exotic hw setups (bug #128453)
- s390: detect OSN devices as QETH interfaces (bug #120724)
- s390: add module entry for P/390 LCS device (bug #81207)
- adjust input device detection to new sysfs layout (#134032)
* Fri Oct 28 2005 snwint@suse.de
- added Dell Notebook LCD size (#130180)
- another Notebook added (#130208)
* Fri Oct 14 2005 snwint@suse.de
- find xen ethernet cards
- remove old hardware entries (#118673)
- better support for virtual i/o hardware on ppc (#119592)
- added r8180 to wlan list (#115268)
- jg: fix wlan includes
* Thu Oct 13 2005 jg@suse.de
- fixed includes
* Tue Sep 20 2005 snwint@suse.de
- don't assume mp records start below 1MB (#112699)
- fix unaligned accesses (#97838)
- gcc 4.1 fixes
* Wed Sep 14 2005 snwint@suse.de
- fix forcedeth, again (#116394)
* Tue Sep 13 2005 snwint@suse.de
- better pcmcia module detection (#104517)
* Mon Sep 12 2005 snwint@suse.de
- update forcedeth driver info (#116394)
* Fri Sep  9 2005 snwint@suse.de
- fix vmware check (broke in UML) (#115424)
- toshiba notebooks need ial (#113714)
* Tue Sep  6 2005 snwint@suse.de
- toshiba notebooks don't need fnfx (#113714)
* Mon Sep  5 2005 snwint@suse.de
- ppc: read 'LCD,EDID', too (#115085)
- module renamed: skystar2 -> b2c2-flexcop-pci (#115262)
- dto, dmasound -> snd-powermac (#112919)
* Fri Sep  2 2005 snwint@suse.de
- report more ivtv cards, and make them (analog) tv cards (#113195)
* Thu Sep  1 2005 snwint@suse.de
- fixed udev parser bug (#113766)
- use new 'udevinfo -e' option (#113766)
- add PowerBook LCD to db (#113795)
- cardbus device detection fixed (#113708)
* Tue Aug 30 2005 snwint@suse.de
- jg: added support for WPA Wireless Extension in WLAN probing
  (fixes faulty probing of ipw2x00 and hostap devices)
- jg: added rt2570 & zd1201 driver to list of WLAN adapters (#105623)
* Mon Aug 29 2005 snwint@suse.de
- fix alps touchpad detection (#98947, #103075)
- drop ltmodem support (#113336)
- don't make too many floppies (#113571)
- updated X11 data
- updated pci ids
- added WinTV PVR-350 as dvb card
* Wed Aug 24 2005 snwint@suse.de
- fix pppoe detection (#106836)
* Mon Aug 22 2005 snwint@suse.de
- fix pcmcia controller detection
* Fri Aug 19 2005 snwint@suse.de
- rip out all special tulip-related module info (#105730)
- load lp module (#104874)
- pcmcia probing works again (#103740)
- support 'modalias' sysfs entries (#103740, #103978)
- getsysinfo collects a bit more info
- drop pci.handmap code (after talking to zoz)
* Tue Aug 16 2005 snwint@suse.de
- fixed evil bug when hal is running (#104654)
* Mon Aug 15 2005 snwint@suse.de
- added hdtv cards (#102933)
- find input device udi (#102575)
- fixed usb device udi matching (#102575)
- read modules.alias, not modules.pcimap
- updated X11 data
* Wed Aug 10 2005 snwint@suse.de
- drop special ADB input device scanning (#98324)
- internal db function rework continued (#102575)
- add udi when possible (#102575)
- updated X11 data
* Mon Aug  1 2005 snwint@suse.de
- updated X11 data
- implement compat wrapper to keep old db functions working
- kkeil: AVM now suports 64 bit drivers
- hwinfo-devel no longer requires hal-devel & dbus-1-devel
* Mon Jul 25 2005 snwint@suse.de
- updated X11 data
- static mpt fusion pci id data removed (#97665)
* Thu Jul 21 2005 snwint@suse.de
- read/write udi-based persitent properties works
* Mon Jul 18 2005 snwint@suse.de
- rip out remaining old db access methods
* Wed Jul  6 2005 snwint@suse.de
- pci devs basically work
- use giant ibm notebook database
- added 'hwclass' entry to db format
* Tue Jul  5 2005 snwint@suse.de
- make C++ happy
* Mon Jul  4 2005 snwint@suse.de
- removed special ppc driver info (#91437)
- skip Video BIOS checksum test
- move libhd back to /usr
- use hal/dbus
* Tue Jun 14 2005 ro@suse.de
- added sysfsutils to nfb
* Thu Jun  9 2005 snwint@suse.de
- getsysinfo collects more info
- some more ibm notebooks
- don't use de4x5
- acpi: always load thermal & fan modules (#72146)
* Mon Apr 11 2005 snwint@suse.de
- smbios detection: don't assume dmi records start below 1MB
- fixed kernel header include
* Fri Apr  1 2005 snwint@suse.de
- removed hwscan*
* Wed Mar 30 2005 coolo@suse.de
- make it build with gcc4
* Tue Mar 22 2005 snwint@suse.de
- updated X11 data (#74130)
* Mon Mar 21 2005 snwint@suse.de
- mls: faster hwscand
* Mon Mar 21 2005 snwint@suse.de
- updated X11 data (#74022)
* Sat Mar 19 2005 snwint@suse.de
- fix wrong entry for Fritz!Card DSL SL USB and
  make ppp mode detection safer (#71995)
- adjusted ltmodem info (#71979)
* Fri Mar 18 2005 snwint@suse.de
- updated nongpl info
- reverting slamr patch (#72301)
- pcmcia info updated (#73057)
- pci dev names updated
- read /proc/modules less often
- updated X11 data
- aic7xxx/aic79xx driver info update
- fix Fritz!Box Fon entry in database
* Thu Mar 17 2005 snwint@suse.de
- another notebook (#67412)
- do wlan detection for --netcard (#73077)
- remove Eicon cards from 64 bit archs, the driver does not support
  64 bit yet (#55722)
* Wed Mar 16 2005 snwint@suse.de
- updated notebook display data
- fix udev db reading
- updated X11 data
- ltmodem device id update
- no check for gfx card changes (#72907)
* Mon Mar 14 2005 snwint@suse.de
- hardware detection for ISDN PCMCIA cards (#71208)
- updated ISDN data
- updated X11 data
- better network type detection (#70991, #71231, #67325)
- load some acpi modules on hp notebook (#72146)
- fixed isapnp sound card detection (#67303)
- slamr: ttySL0 -> ttyLT0 (#72301)
* Mon Mar  7 2005 snwint@suse.de
- updated X11 data
* Fri Mar  4 2005 snwint@suse.de
- s390: made ccwgroup walking more robust
- fixed bios base mem detection
- allow device class in 'hwinfo --db' request
- updated X11 data
* Mon Feb 28 2005 snwint@suse.de
- jg: improved wlan patch (no dependency on libiw)
* Mon Feb 28 2005 snwint@suse.de
- fixed model name for some SGI hardware (#63973)
- fix Fritz!Card DSL SL USB ID (#66674)
- better heuristics to assign BIOS driver numbers (#66669)
- removed ahci vs. ata_piix hack (#65218)
* Fri Feb 25 2005 snwint@suse.de
- reworked pcmcia code to give cardbus devices sysfs ids
- report pci class 0x403 as audio devices (#66466)
- load ahci *and* ata_piix (#65218)
- symlink /dev/fb might be missing; trying fb0, too (#66501)
- reorder modules.pcimap entries so that more specific matches are
  considered first (#66594)
- ensure nvida network cards are network cards (#65852)
- updated X11 data
* Mon Feb 21 2005 snwint@suse.de
- jg: added wlan feature detection
* Thu Feb 17 2005 snwint@suse.de
- notebook lcd data update
- build shared tiny lib
* Tue Feb 15 2005 snwint@suse.de
- libhd interface changes: geometry values
- prepare for wlan feature detection
- x11 db update
- better disk geometry handling
* Tue Feb  8 2005 snwint@suse.de
- added '--kernel-version' option
* Mon Jan 31 2005 snwint@suse.de
- updated X11 data
* Tue Dec 14 2004 snwint@suse.de
- fixed access to undefined memory (#39238)
- fix segfault when using 'x11=foo' boot option (#46367)
- add additional check to catch broken BIOSes (#48665)
- abort BIOS code execution if it takes too long (#48665)
- find usb serial lines
* Thu Dec  2 2004 snwint@suse.de
- report network interfaces correctly even though udev lists them
- s390: identify new CU types 2107, 1750 as DASD
- fixed some dvb entries (#47057)
- s390: added new prog_if ID pif_dasd_fba to identify FBA DASDs
  (reqd. by fehr)
- less agressively assume scsi devs are disks (#47654)
- fixed external hardware db parser (#47606, comment 6)
- ibm notebook data updated
- avoid libsysfs accidentally reading pci config space
- fixed parsing of scsi serial id (#48757)
- look at /sys/class/net/*/type, too (#48812)
* Tue Oct 12 2004 snwint@suse.de
- report usb host-to-host links as network devs (#22739)
* Mon Oct 11 2004 snwint@suse.de
- find ide devices != cdrom & disk (#39911, #45229)
- return special ids for synaptics touchpad (#46649)
* Thu Oct  7 2004 snwint@suse.de
- fixed segfault with large /proc/interrupt entries (e.g. 512 cpus) (#46582)
* Fri Oct  1 2004 snwint@suse.de
- list bluetooth isdn box as bt device, too (#46626)
* Fri Oct  1 2004 snwint@suse.de
- smartlink-softmodem is back (#46594)
- added some dvb cards (#46612)
* Thu Sep 30 2004 snwint@suse.de
- updated X11 data (#45870)
* Wed Sep 29 2004 snwint@suse.de
- removed obsolete module info; reworked pcmcia info
* Wed Sep 29 2004 snwint@suse.de
- updated pcmcia & usb network data (#33647)
- updated pci device names
* Wed Sep 29 2004 snwint@suse.de
- use SG_IO for SCSI device accesses (#46058)
* Tue Sep 28 2004 snwint@suse.de
- added gen-hwcfg-disk.sh (#46311)
* Mon Sep 27 2004 snwint@suse.de
- updated ancient audio info (#46096)
- add ipw/atmel firmware packages (#45960)
- updated X11 data
- added new isdn cards to database
* Mon Sep 27 2004 snwint@suse.de
- report bluetooth devices (#45893)
* Fri Sep 24 2004 snwint@suse.de
- return package info for sony notebooks, too (35245)
* Thu Sep 23 2004 snwint@suse.de
- added --pcmcia option to hwscanqueue (#44290)
- return package info in system entry (#35245)
* Wed Sep 22 2004 snwint@suse.de
- updated X11 data
* Tue Sep 21 2004 snwint@suse.de
- drop workaround for multiple hotplug events by broken kernel
* Tue Sep 21 2004 snwint@suse.de
- replaced raiddetect with dmraid
* Mon Sep 20 2004 snwint@suse.de
- sata info update (#45551)
- look at smbios data for smp detection, too
* Fri Sep 17 2004 snwint@suse.de
- added some epson scanners (#45074)
- adaptec module info update
* Mon Sep 13 2004 snwint@suse.de
- kernel-nongpl stuff only for i386 (#45099)
- updated megaraid module info
- ibm notebook info update (#45038)
* Mon Sep 13 2004 snwint@suse.de
- sata driver seems to generate a dummy scsi vendor name (#44286)
- clear hd_data struct after it has been released (#44855)
- updated X11 data
- changed sata vendor name handling a bit
- isdn: remove old bluetooth packages from database
* Mon Sep  6 2004 snwint@suse.de
- updated tv-card info
* Mon Sep  6 2004 snwint@suse.de
- win modem dev name change (#44253)
- added nongpl module info
- fixed /tmp file handling (#44538)
- removed ancient function hd_has_special_eide()
- use edd module to get extended BIOS features (#44649)
- 'hwinfo --map' includes a hardware scan
* Mon Aug 30 2004 snwint@suse.de
- changed hwbootscan to use bash (#44199)
- fixed hd.ids parser bug
- updated X11 data
- moved libhd to /lib
* Mon Aug 23 2004 snwint@suse.de
- updated X11 data
- added display sizes for a number of IBM notebooks
* Wed Aug 18 2004 snwint@suse.de
- new wlan data (#42759, #39481, #43921)
- hwscan now really moved to /sbin
* Mon Aug 16 2004 ro@suse.de
- complete sbin move
* Mon Aug 16 2004 snwint@suse.de
- now really install to /sbin
* Mon Aug 16 2004 snwint@suse.de
- move hwscan* to /sbin (#43601)
* Thu Aug 12 2004 ro@suse.de
- added libpng to neededforbuild (for doxygen)
* Thu Aug  5 2004 snwint@suse.de
- push/pop don't work with 32bit regs on amd64 (#43531)
* Wed Aug  4 2004 snwint@suse.de
- get netcard link state via ethtool ioctl
* Tue Jul  6 2004 snwint@suse.de
- joined changes up to 8.60 from 9.1 branch
* Fri Jun 18 2004 bg@suse.de
- add hppa defines
* Wed Jun  2 2004 ro@suse.de
- avoid inclusion of linux/audit.h
* Mon May 10 2004 snwint@suse.de
- updated to 9.1 version to make yast happy
* Mon May 10 2004 snwint@suse.de
- added functions necessary to build a model name to tiny version;
  this is needed by linuxrc (#39092)
* Thu May  6 2004 snwint@suse.de
- detect IUCV pseudodevices (bug #39456)
- added hd_busid_to_hwcfg() (bug #39456)
- updated X11 data (#39767)
- fixed strange side effect of UML detection (#39946)
* Thu Apr 29 2004 snwint@suse.de
- s390: enhance grouped channel detection using ccwgroup bus
- use *last* console parameter for serial console
- look for usb network cards (#37870)
- network class id cleanup (#39456)
* Wed Apr 28 2004 snwint@suse.de
- add bus.name for bus.id == bus_ccw
- avoid unspecific network types (#38874)
- fixed memory size detection (#34895, #38758)
- report UML network (#39521)
* Tue Apr 27 2004 snwint@suse.de
- 'hwinfo --map' returns mapping new -> old block
  device names (#39437)
* Mon Apr 26 2004 snwint@suse.de
- s390: set is.notready flag on unformatted DASDs (bug #39174)
- rewrote serial console handling (#39029, #23322, #35824)
- updated X11 data (#39282)
- subclass 0x83 for xpnet card (#35867)
- add UML keyboard (#38922)
* Tue Apr 20 2004 uli@suse.de
- s390: add bus id bus_ccw
- s390: set bus.id, sysfs_bus_id and sysfs_device_link for all devices
- s390: do not do pr_s390disks by default, and run it after pr_s390
  to keep already detected non-disk devices from being deleted
- s390: implement rw/ro info properly
- s390: fake geometry and size of unformatted DASDs to most likely
  values
* Mon Apr 19 2004 snwint@suse.de
- fixed bug in modules.alias conversion script (#38800)
- fixed linmodem data (#38800)
- handle veth devices on iSeries (#38696, #37981)
- another de4x5 vs. tulip case (#39127)
- fixed cdrom config segfault (might happen while reading inconsistent
  cdrom config data)
- support pSeries vscsi (#36029)
* Fri Apr 16 2004 snwint@suse.de
- bcm5700, not tg3 on ppc* (#38647)
- add Acer TravelMate 660 & Asus S5200N LCD sizes (#38149)
- make SGI IOC4 known as storage controller (#38628)
- support SGI XPNET (#35867)
* Sat Apr 10 2004 aj@suse.de
- hwinfo does not need kernel-source.  Remove dependency.
* Tue Apr  6 2004 snwint@suse.de
- do call --partion with --fast in hwscand polling code
* Tue Apr  6 2004 snwint@suse.de
- fixed unique ids for pci devs (#37570)
* Tue Apr  6 2004 snwint@suse.de
- run raiddetect only on x86-like archs (#36157)
- don't run raiddetect if we didn't find any disks
* Mon Apr  5 2004 snwint@suse.de
- don't run raiddetect if --fast option is used
* Mon Apr  5 2004 snwint@suse.de
- make --only accept device names, too (#38265)
- make it more resistant against strange libsysfs data (#38259)
- tg3 vs bcm5700 again (#38268)
* Sun Apr  4 2004 adrian@suse.de
- disable --only usage in hwscand, since it is broken in hwscan atm.
* Sun Apr  4 2004 kkaempf@suse.de
- check return value from hd_sysfs_id() (#38266)
* Fri Apr  2 2004 snwint@suse.de
- another wlan card (#38119)
* Fri Apr  2 2004 snwint@suse.de
- store driver list & sysfs info in hardware config files
* Fri Apr  2 2004 snwint@suse.de
- add Fritz!Card DSL SL USB in database
- hwbootscan: move icon creation from coldplug
- lt modem (#36552)
- fixed some module names (#37285, #37518)
- added dvb cards (#32730)
- use old bios disk assign code if there's no edd info
* Thu Apr  1 2004 snwint@suse.de
- wlan card detection fix (#37872)
- updated X11 data
- read isapnp from sysfs (#35157)
* Wed Mar 31 2004 adrian@suse.de
- make hwscand pid file locking atomar
- ignore same events after 10 seconds to prevent loops due to
  invalid events by some drivers
* Wed Mar 31 2004 snwint@suse.de
- changed bios probing to do less things
- added duplicate DASD detection code from the late dasd.c
  to block.c (bug #37068)
- changed bios probing to do less things
- another winmodem (#37335)
- rewrote input device handling
- load ide-cd, sd_mod, sr_mod before looking for block devs (#37558)
- fixed usb printer detection
- run 'raiddetect' to tag ide soft raid devices
- minor vbe bios fixes
* Mon Mar 29 2004 snwint@suse.de
- don't run modprobe if it doesn't exist
* Mon Mar 29 2004 snwint@suse.de
- add edd support (#27807, #36876)
* Sun Mar 28 2004 snwint@suse.de
- added hwscand hwscanqueue
- use sysfs for usb devices
- scsi tapes detected again
- added hardware class 'tape'
- added getsysinfo script (collect data to debug hw detection)
* Thu Mar 25 2004 snwint@suse.de
- added hd_is_uml() to report if we're running in an UM kernel
- b44 vs. bcm4400 (#36763)
- fix inconsitency in device name list
- allow device names in 'hwscan --show'
* Mon Mar 22 2004 snwint@suse.de
- removed Intel-v92ham support (#36667)
- worked on new sysfs block code
* Sun Mar 21 2004 snwint@suse.de
- use sysfs for block devices
* Sat Mar 20 2004 adrian@suse.de
- make it possible to give a unix device name instead of the
  unique id to hwscan
* Mon Mar 15 2004 snwint@suse.de
- fixed 8139cp/too module info (#36028)
* Mon Mar 15 2004 snwint@suse.de
- do not reverse sysfs order (libsysfs does it)
- updated X11 data
- return real device name, not udev symlink
- DSL hardware detection for none pppoe (kkeil)
* Sun Mar 14 2004 snwint@suse.de
- s390: added two missing DASD device types
- added '--root' option (for testing)
- added '--db' option for database queries
- fixed 'x11i' parameter handling
- read pci.handmap
* Tue Mar  9 2004 snwint@suse.de
- udevinfo moved to /usr/bin
* Mon Mar  8 2004 snwint@suse.de
- added host info for s390 SCSI devices
- added disk-only probing method for s390
- added WWPN, FCP LUN for s390 SCSI devices
- updated X11 data
* Thu Mar  4 2004 snwint@suse.de
- s390: added LCSS info to ccw_t
- link libhd against libsysfs
- added hw item for quick DASD rescanning
- updated digital camera ids.
- pci from sysfs finished
- network interfaces from sysfs
* Tue Mar  2 2004 adrian@suse.de
- link against libsysfs
- add %%defattr macros
* Mon Mar  1 2004 snwint@suse.de
- fix smp detection on ia32e (#34742)
- store some new fields in unique-id files
- better error logging for vbios init
- disable all BIOS related things on ia64 (#34550)
- updated X11 data
- use sysfs for pci data (not default)
- removed uClibc from neededforbuild
* Tue Feb 24 2004 snwint@suse.de
- include x86emu into libhd.so
- don't segfault if we couldn't get a shared memory segment
* Tue Feb 24 2004 kkaempf@suse.de
- try to include x86emu library in libhd
* Mon Feb 23 2004 snwint@suse.de
- fixed Makefile
* Mon Feb 23 2004 snwint@suse.de
- added '--version' (#31925)
* Mon Feb 23 2004 snwint@suse.de
- check for hyperthreading on amd64 (#34742)
- removed last references to ataraid from hardware db
- added new x86 emulator (#34545)
- return MacRISC<n> (#34591)
* Tue Feb 17 2004 snwint@suse.de
- handle '-' vs. '_' in module names
* Tue Feb 17 2004 snwint@suse.de
- isdn database optional read from /usr/share/hwinfo/ISDN.CDB.hwdb
- mk_isdnhwdb tool to convert CDB data to ISDN.CDB.hwdb
- fixed Makefile
* Mon Feb 16 2004 snwint@suse.de
- disable uClibc build; it's not used anyway
* Mon Feb 16 2004 snwint@suse.de
- fixed ia64 unaligned access (#32396)
- use modprobe for tulip (#32911)
* Thu Feb 12 2004 uli@suse.de
- fixed segfault on s390*
- removed special ia64 hardware data: new kernel, new game
* Mon Feb  9 2004 snwint@suse.de
- nvnet -> forcedeth (#25531)
- sata module data updated
- moved psaux mice to input/mice
- make convert_hd understand modules.alias files
* Fri Feb  6 2004 snwint@suse.de
- sysfs includes moved
- usb modules renamed
- really basic udev & sysfs support for block devs
* Fri Dec  5 2003 snwint@suse.de
- proper multichannel device detection (finally...)
- identify virtual reader/punch/printer
* Tue Dec  2 2003 snwint@suse.de
- build with "-pipe"
- accommodated to changes in format of /proc/dasd/devices
- ditched storage subclass dasd, introduced s390disk prog_if instead
- ditched fake CTC controller generation
- deal with unsorted bus trees in multichannel device detection
* Tue Nov 18 2003 snwint@suse.de
- converted s390 HW detection to sysfs
- moved CU/device models to separate data structure
- added more s390 devices
- rewrote parsing of SMBIOS data structures
* Thu Nov  6 2003 ro@suse.de
- build uclibc version again
* Tue Oct 28 2003 snwint@suse.de
- get pci config type from kernel log (#30704)
- add new flag 'cpuemu' to use cpu emulation on i386
- no uClibc version
* Mon Sep 22 2003 snwint@suse.de
- updated usb scanner & webcam data
- updated X11 data
- hwbootscan: split 'hwscan --pci --disk' call to avoid
  wrong unique ids for some pci devices (#31545)
* Sun Sep 21 2003 snwint@suse.de
- updated X11 data
* Thu Sep 18 2003 snwint@suse.de
- set ATA RAID bus type to 'RAID' (#31235)
* Wed Sep 17 2003 snwint@suse.de
- don't make every parport into a printer (#31161)
- some driver data updated
* Tue Sep 16 2003 snwint@suse.de
- default to 'printer' if a class tag is missing in parport
  autoprobe data (#30982)
- fixed serial console detection (#30936)
* Mon Sep 15 2003 snwint@suse.de
- pcmcia data update
* Mon Sep 15 2003 snwint@suse.de
- report pci modems (#30887)
- don't get fooled by removed pcmcia cards
- wlan data update (#30886, #30823, #30501)
- driver data update (#30384, #29468, #30745)
* Mon Sep 15 2003 snwint@suse.de
- ignore alternative usb interface settings
* Sun Sep 14 2003 snwint@suse.de
- updated X11 data
- don't read from cd drives that don't exist (#23248)
* Wed Sep 10 2003 snwint@suse.de
- fixed monitor data interpretation bug (#29718)
* Tue Sep  9 2003 snwint@suse.de
- more ltmodem ids
- uli: implementation of S/390 hardware detection
* Mon Sep  8 2003 snwint@suse.de
- updated driver info (#25457, #29481, #25531)
- updated X11 data
- added --combine option to check_hd to assist in creating driver data
- fixed minor typos
* Mon Sep  8 2003 snwint@suse.de
- updated usb mouse data (#29719)
- better touch pad/track point reporting for notebooks
- fork() for serial mouse & modem detection (#25843, #26513)
- fixed hwbootscan (#29959)
- don't load imm.o module (#14175)
* Tue Sep  2 2003 snwint@suse.de
- catch more vm86() faults (#28381)
- added 'active' status flag (not modified by libhd)
* Mon Sep  1 2003 snwint@suse.de
- update ISDN CDB data
- catch faults inside vm86() code (#29571)
- give wlan cards their own subclass (#29506)
- updated X11 data
* Thu Aug 28 2003 snwint@suse.de
- iopl() may fail even if we're root (#29494)
* Wed Aug 27 2003 snwint@suse.de
- probe for multiple hardware classes at a time
* Tue Aug 26 2003 kkeil@suse.de
- updated ISDN CDB data
- ISDN data default for all archs
* Tue Aug 26 2003 snwint@suse.de
- updated X11 data (#29316)
- fix minor warnings
- add ISDN CDB database for IA64
* Mon Aug 25 2003 kkeil@suse.de
- create missing directories in buildroot
* Mon Aug 25 2003 snwint@suse.de
- don't try BIOS things on SGI Altix (#28663)
* Mon Aug 25 2003 snwint@suse.de
- added lots of new camera ids.
- new isdn data taken from cdb
- updated X11 data
- fixed spec (#28796, #29224)
* Mon Aug 18 2003 snwint@suse.de
- add ChildIDs field (reverse of ParentID)
* Tue Aug 12 2003 snwint@suse.de
- better internal hwclass handling
* Mon Aug 11 2003 snwint@suse.de
- define HARDWARE_DIR in hd.h
* Fri Aug  8 2003 snwint@suse.de
- hp officejet scanner gets package info & own subclass
- ltmodem is back
- parent id, again
- use modprobe instead of insmod for scsi modules
* Fri Aug  1 2003 snwint@suse.de
- reworked usb things
* Fri Jul 18 2003 snwint@suse.de
- changed disk size reading for 2.6
- more 2.6 header fixes
* Thu Jul 17 2003 snwint@suse.de
- store parent id (#27508) and hotplug field
- new attempt to work around broken cciss_ioctl.h inclue file
* Wed Jul 16 2003 snwint@suse.de
- fixed megaraid info (#26325)
- detect pcmcia cards
- updated x11 data
* Tue Jun 10 2003 ro@suse.de
- prefer includes from kernel-source
* Mon Mar 17 2003 snwint@suse.de
- updated X11 data (#23847)
- workaround for ps/2 mouse detection inconsistency (#25331)
* Thu Mar 13 2003 snwint@suse.de
- ltmodem stuff makes trouble, removed (#25309)
* Thu Mar 13 2003 snwint@suse.de
- updated X11 data (#25217)
* Wed Mar 12 2003 snwint@suse.de
- be more careful when joining feature flags of
  ide-scsi handled devices (#25169)
* Wed Mar 12 2003 snwint@suse.de
- limit the maximum amount of data we expect looking
  for serial mice (#25153)
* Tue Mar 11 2003 snwint@suse.de
- updated ide raid info (#25010)
* Mon Mar 10 2003 snwint@suse.de
- added more notebook data
* Sat Mar  8 2003 snwint@suse.de
- fixed ide-scsi detection bug (device names mixed up if more than
  one device is handled by ide-scsi)
* Sat Mar  8 2003 snwint@suse.de
- updated data from pci utils
* Sat Mar  8 2003 snwint@suse.de
- detect wlan cards (#23491)
* Fri Mar  7 2003 snwint@suse.de
- usb multiple interfaces again: only for HID devices (#24824)
- add monitor vendor & device name
- allow hwscan to be disabled at boot time via 'hwprobe=-scan'
* Thu Mar  6 2003 snwint@suse.de
- updated X11 data
- added '--dsl' option to hwscan
* Thu Mar  6 2003 snwint@suse.de
- write ff to /dev/lp0 if imm.o didn't load (#14175)
- probe for scsi cache even in fast mode, else we miss scsi cd writers
- better Epson scanner detection (#20837)
- fixed stupid '\0'-missing-at-end-of-buffer bug
- added '--slient' option to hwscan (don't show ids)
- cleaned up notebook lcd detection and added more data
* Tue Mar  4 2003 snwint@suse.de
- fixed floppy detection (#24283)
* Tue Mar  4 2003 snwint@suse.de
- fixed ataraid detection (format of /proc/ide/ide?/config
  changed, #23057, #24528)
* Mon Mar  3 2003 snwint@suse.de
- bcm instead of tg3 (request by ak)
- reenable mouse probing, but without serial mice and no dialog (#20309)
- support some winmodems
- updated X11 data
* Wed Feb 26 2003 snwint@suse.de
- better ZIP drive handling
- handle usb devices with multiple interfaces (#21487, #22223, #22843)
- removed 'Looking for braille...' line
- fixed multi-CDROM bug (#24280)
- save/restore feature flags (#23364)
- keep feature flags for ide-scsi handled drives (#23550)
* Tue Feb 25 2003 snwint@suse.de
- fixed 64 bit int -> pointer gcc warnings
- fixed minor database lookup bug
- database parser logs to logfile, not stderr
- support serial mice with really strange vendor ids (#24137)
* Mon Feb 24 2003 snwint@suse.de
- add fibre channel adapters to storage controller list (#23686)
* Mon Feb 24 2003 snwint@suse.de
- fixed gcc warnings
- updated module info
- increased major version
* Tue Feb 18 2003 snwint@suse.de
- added pppoe detection
- updated X11 data
* Tue Feb 18 2003 snwint@suse.de
- removed experimental code causing segfault on compaq machines
* Mon Feb 10 2003 snwint@suse.de
- fixed pci base addresses on 64bit archs (#21075)
- remove mouse probing from hwbootscan, it sometimes
  hangs and takes too long.
- add --fast to --cdrom probe, so the cdrom is not opened.
- updated X11 data
* Tue Jan 21 2003 snwint@suse.de
- detection of more Microcom modems
- updated the pcmcia controllers fallback list
- added a minimal man page
- add AVM Fritz!Card DSL USB
- updated X11 data
* Tue Jan 14 2003 snwint@suse.de
- added Myrinet support (#21130)
- make it compile on !(x86_64 & ia64) again
* Thu Jan  9 2003 snwint@suse.de
- fixed some network card names (#22795)
- added wheel mouse data (#22797)
- make it compile on x86_64 & ia64 again
* Fri Dec 13 2002 snwint@suse.de
- fixed qla* module info (#21567)
- use eepro100 instead of e100 on ia64 (#21055)
- rewrote assignment of BIOS driver numbers
- slight cleanup of int10 code
- changed tg3/bcm* on ia64 (#21984)
- one ncr53c8xx vs. sym53c8xx issue (#21984)
- cleanup ISDN ids, remove unsupported protocols (#22179)
- cdrom feature list (dvd, cdr, etc)
* Wed Nov  6 2002 snwint@suse.de
- joined with 8.1 branch:
- ia64: switch back to reading ACPI tables for SMP detection.
- 'hwscan --pci' should add prom id (#19648)
- fixed floppy detection (#20269)
- x11 data update (#20182)
- added IBM ServeRAID ids (#20268)
- add "Virtual" to veth description string (#20319)
- added aacraid driver info (#20592)
- don't run yast if no keyboard is attached (#19768)
- updated tg3/bcm5700 driver info (#19913)
- updated megaraid info (#21043)
- do some consistency checks on legacy data from BIOS area (#21462)
- check for REDIRECT in hwscan init script (in case it gets called
  from the commandline). #17773
* Wed Sep 18 2002 snwint@suse.de
- fixed chksum call causing hwinfo to hang in some cases on ia64
- don't overwrite vga modelist
* Wed Sep 11 2002 snwint@suse.de
- avoid alignment problems on ia64
- fixed usb-cdrom probing (#19407)
- removed '--fast' for disk probing; instead, fixed i2o & cciss (#19440)
* Tue Sep 10 2002 snwint@suse.de
- probe also USB isdn controllers (#18830)
- added '--help' option to check_hd & convert_hd
- converted pci info to utf8
- probe for cdrom & disk at boot (#19297)
- '--fast' option has effect on disk probing (no i2o & cciss)
- dmfe instead of tulip (#19271)
- convert_hd now understands XML properly
- removed outdated docs
* Mon Sep  9 2002 kkeil@suse.de
- probe ISDN USB too (#18830)
* Sat Sep  7 2002 snwint@suse.de
- make sure usb floppies are reported as such (#12262)
* Fri Sep  6 2002 olh@suse.de
- do not package uClibc files on ppc
* Fri Sep  6 2002 snwint@suse.de
- new x11 data
- report s390x arch properly
* Fri Sep  6 2002 snwint@suse.de
- build uClibc version, not dietlibc (uClibc works with linuxrc)
* Fri Sep  6 2002 snwint@suse.de
- added amd-8111 info
- fixed dpt info (#18914)
- always smp on s390* (#18990)
- changed pcnet32 description (#18892)
* Wed Sep  4 2002 snwint@suse.de
- show boot catalog address in cd info
* Wed Sep  4 2002 snwint@suse.de
- fixed ata raid code
- new usb mouse (#18296)
- switched escon adapter from 0x70 to 0x8
- corrected number for CTC, IUCV, HSI and QETH
- fix usb isdn adapter detection (#18829)
- updated pci & usb data
* Mon Sep  2 2002 snwint@suse.de
- updated x11 data
* Mon Sep  2 2002 snwint@suse.de
- got rid of gcc warning
- braille detection on sparc
- fixed script that reads CDB data
- log error messages from vm86 code
- better chipcard reader support
- use _exit instead of exit on some more places.
- prepared for uclibc
- save & restore resource data
- code for detekting configured CTC, IUCV, HSI and QETH
  adapters on s390/s390x
- fixed iSeries network id
* Wed Aug 28 2002 snwint@suse.de
- changed dasd.c to accept old and new format of /proc/dasd/devices
- better serial mouse detection (#18384)
- added x86_64 x11 data
* Mon Aug 26 2002 msvec@suse.cz
- added some microcom modems detection (#15359)
* Mon Aug 26 2002 snwint@suse.de
- use "reprobe" as yast2 argument, not (.reprobe)
- added some new hardware types
- fixed usb & ieee1394 controller detection
* Fri Aug 23 2002 snwint@suse.de
- check cpuid for hyperthreading (#13532)
- add new bus id 'Virtual IO' for DASD (#18202)
- use grub on x86_64
- fixed s390 cpu detection
* Tue Aug 20 2002 snwint@suse.de
- mls: x86 emu for BIOS calls on ia64
* Mon Aug 19 2002 snwint@suse.de
- mls: x86 emu for BIOS calls on x86_64
- updated x11 data
* Fri Aug 16 2002 snwint@suse.de
- segfault in hwinfo, part 2
- fixed symbios module entry
- changes in libhd interface
* Wed Aug 14 2002 snwint@suse.de
- fixed Requires & PreReq
* Tue Aug 13 2002 snwint@suse.de
- get isdn model name from isdn database
- updated megaraid info
- 'make install' creates /etc/init.d
- uses BuildRoot
* Tue Aug 13 2002 snwint@suse.de
- added info for firewire module
- fixed convert_hd to work with perl 5.8
* Tue Aug 13 2002 snwint@suse.de
- rearranged build order, so dietlibc doesn't break the build process
* Mon Aug 12 2002 snwint@suse.de
- fixed evil segfault in hwinfo
- updated docs
* Fri Aug  9 2002 snwint@suse.de
- moved unique key file to var/lib/hardware/unique-keys
- moved things from var/lib/libhd to var/lib/hardware
- added HD_VERSION #define to hd.h
* Thu Aug  8 2002 snwint@suse.de
- minor libhd interface changes
- extended isdn package info
- detect dvb cards
- fixed reading driver info
- updated driver info
- changed tv card detection code
- hwinfo-internal no longer needed
* Wed Aug  7 2002 snwint@suse.de
- fixed segfault while probing for video
* Mon Aug  5 2002 snwint@suse.de
- gmac -> sungem
- don't source rc.config
- report cardbus cards
- _exit instead of exit to avoid calling QT destructors in Yast2
- activated new database code
* Mon Aug  5 2002 kukuk@suse.de
- hwbootscan.rc: move "kbd" and "hotplug" to "Should-Start"
  section, they don't exist always.
* Sat Jul 27 2002 adrian@suse.de
- add %%run_ldconfig
* Mon Jul 22 2002 snwint@suse.de
- updated x11 data
* Mon Jul 22 2002 snwint@suse.de
- run hwbootscan rc script after "kbd" script
- don't _change_ config status in hwbootscan
- save %%gs register around vm86() syscall (%%gs may be used in glibc)
- isdn changes
- better handling of dasd devs
- grub instead of lilo on ix86
* Thu Jul 11 2002 snwint@suse.de
- don't source rc.config
- run hwbootscan rc script after "kbd" script
- don't _change_ config status in hwbootscan
- save %%gs register around vm86() syscall (%%gs may be used in glibc)
* Fri Jul  5 2002 kukuk@suse.de
- Use %%ix86 macro
* Thu Jun 13 2002 snwint@suse.de
- made ia64 cpu model entry more useful
- get bios led status
* Wed Jun  5 2002 snwint@suse.de
- assign hardware added via 'hwprobe' a proper inital status
- added alsa driver info
- dropped old pnpdump() code
* Thu Apr 25 2002 arvin@suse.de
- use %%{_libdir} for libraries
- disable (temporarily?) use of dietlibc on x86-64
* Wed Apr 24 2002 kkaempf@suse.de
- add x86-64 support.
* Wed Mar 27 2002 snwint@suse.de
- prevent doubled cdrom hardware items
* Wed Mar 27 2002 snwint@suse.de
- fixed cdrom device detection (#15553)
- don't assign lp8 to nonexistent usb printers
* Mon Mar 25 2002 snwint@suse.de
- updated help texts
* Mon Mar 25 2002 snwint@suse.de
- recognize fibre channel controllers as storage controllers
* Sun Mar 24 2002 snwint@suse.de
- read bios data in libhd_tiny (to allow vaio handling in linuxrc, #12075)
- read /etc/module.pcimap, too (it's there during installation)
- new x11 data
- de4x5.o vs. tulip.o issue (#15303)
- added Netgear WLAN-Card data (#14848)
* Thu Mar 21 2002 snwint@suse.de
- remove /var/lib/hardware/LOCK in hwbootscan (#15217)
- updated X11 data
- prefer tg3 over bcm5700
- fixed broken framebuffer detection: reenabled & fixed pci setup code
* Mon Mar 18 2002 snwint@suse.de
- fixed segfault in ide code
* Sat Mar 16 2002 snwint@suse.de
- fixed bug that caused 'Processor' scsi devices to be treated
  as disks (mentioned in #15007)
* Thu Mar 14 2002 snwint@suse.de
- udated mptbase driver info (#14732)
- better handling of usb-storage devices
- add mouse info we got from smbios
- use info from modules.pcimap
- detect memory size > 4GB (#14287)
* Sat Mar  9 2002 snwint@suse.de
- made hwbootscan an init script again, started after hotplug.
- do not delete the reconfig.needed files, but set configured=no
  and needed=no to avoid problems with unsupported graphic cards.
- added usb ids from usbutils
- fixed network module info (#14529)
- improved smbios parser
- updated x11 driver info
- isdn: fix wrong names (AVM) and add more USB devices
- disabled pci setup code that caused infinite loops on
  some systems with isa gfxcards
* Mon Mar  4 2002 snwint@suse.de
- new isdn data
- look at /proc/apm, too
- updated network driver info
- detect fujitsu siemens notebook lcd
- updated x11 driver info
- updated pci device list
- check for isapnp devs in boot.hwscan, too
* Fri Mar  1 2002 snwint@suse.de
- detect USB scanner by just looking if the module is usbscanner
- new scanner ids
- camera subclass ids were 1 off from enumeration
- added some new hardware classes: bios, bridge, hub, usb_ctrl
- added '--pci' and '--isapnp' options to hwscan
- fixed evil segfault caused by reading some hardware configs
- added '--fast' option to hwscan: don't check for tricky hardware
  as serial mice or parport zips unless they had been found
  previously
- boot.hwscan: probe for mice & pci hardware only (to be faster)
- don't try to access 'not available' devices
* Fri Mar  1 2002 ro@suse.de
- force activation of boot.hwscan using "Y"
* Mon Feb 25 2002 snwint@suse.de
- meissner: boot.hwscan:
  probe for storage, network, tv, sound handware
- updated x11 data
- handle usb ehci controller
- added basic smbios parser
* Thu Feb 21 2002 snwint@suse.de
- meissner: boot.hwscan: fixed confused curses output
- new isdn database
- update 'not available' state
- changed unique_id algorithm for usb devices
* Tue Feb 19 2002 kukuk@suse.de
- Fix insserv call
* Mon Feb 18 2002 kkeil@suse.de
- for better YaST dialogs here is a driver name field now in
  ISDN database
* Mon Feb 18 2002 snwint@suse.de
- meissner: hwbootscan init script was changed to boot.hwscan
  bootscript, (#13318); $?=0 replaced by rc_reset as suggested
- added new scanner
- updated x11 data
- experimental support for hpt3* ideraid
* Thu Feb 14 2002 snwint@suse.de
- link against dietlibc only on i386 & ppc; it doesn't really work
  on other archs
* Tue Feb 12 2002 snwint@suse.de
- meissner: mouse probing is in choose_mouse
- meissner: added arguments for light probing '(.reprobe)' as suggested by tom
* Mon Feb 11 2002 snwint@suse.de
- integrated isdn database
* Fri Feb  8 2002 kkeil@suse.de
- isdn database now in libhd, support for multiple isdn driver
* Thu Feb  7 2002 snwint@suse.de
- renamed a function to avoid conflicts with linuxrc
* Thu Feb  7 2002 snwint@suse.de
- fixed dac960 detection: we used to return just the 1st disk
* Thu Feb  7 2002 snwint@suse.de
- make hd_list() work properly if LIBHD_TINY is defined
- added new braille display
- hwinfo accepts '--netcard' as alias to '--network_ctrl'
- first attempt to handle ide raid controller
- use /proc/partitions to find disks, too
* Mon Feb  4 2002 snwint@suse.de
- store a config string along with the config status
* Mon Feb  4 2002 snwint@suse.de
- added post* scripts to start hwbootscan
* Mon Feb  4 2002 snwint@suse.de
- fixed bug that prevented hwprobe env var to work in some cases
- changed hd_change_status() prototype
* Mon Jan 28 2002 snwint@suse.de
- hwscan: touch /var/lib/hardware/.update if things have changed
- meissner: added boot scripts
* Mon Jan 21 2002 snwint@suse.de
- increased major version number, as we're incompatible to v3 meanwhile
- added function to set hardware config status data directly
* Sun Jan 20 2002 snwint@suse.de
- updated hwscan so it does something useful
- updated x11 data
* Mon Jan 14 2002 snwint@suse.de
- don't build tinydiet on sparc
* Mon Jan 14 2002 snwint@suse.de
- next try with dietlibc on sparc
* Mon Jan 14 2002 snwint@suse.de
- olh: assume veth always present
- make it work with dietlibc on sparc
- new class: hw_usb_ctrl
* Fri Jan  4 2002 snwint@suse.de
- reimplemented iSeries veth device detection (#12680)
- don't build tinydiet on axp & s390
* Thu Jan  3 2002 schwab@suse.de
- Don't build tinydiet on ia64.
* Fri Dec 14 2001 snwint@suse.de
- create version for linking against dietlibc
- mls: continue even if some vbe calls fail
* Wed Dec  5 2001 snwint@suse.de
- moved database location
* Mon Nov 26 2001 snwint@suse.de
- prepare for arm
* Thu Nov 22 2001 snwint@suse.de
- ppc: detect swim3 floppy (#11643)
- ppc: pr_prom needs pr_pci in some cases
- add monitor entry based on fbdev data, if we have
  nothing better (#11344)
- work around incorrect iMac monitor data
- more apple monitor fixes
- don't load parport modules on pmac (#11743)
- provide monitor sync data if they are missing
- gmac controllers are powered off when unconfigured, so
  we have to provide the class id ourself (#11733)
- handle iSeries network and storage devices
  return ppc64 when uname -m returns it
- read country code from usb devices
- call cpu probe for keyboard query
- reduced libhd_tiny size
* Wed Oct  3 2001 olh@suse.de
- fix the check for active framebuffer
  the current one is a hack and doesnt work in all cases
* Thu Sep 27 2001 olh@suse.de
- use pc104 instead of powerpcps2
* Mon Sep 24 2001 snwint@suse.de
- updated X11 data
- no longer default to XF3 for installation on ppc (#11260)
* Mon Sep 24 2001 snwint@suse.de
- added LSIFC9xx/LSI409xx Fibre Channel (#11251)
* Mon Sep 24 2001 snwint@suse.de
- use aic7xxx_old one some controllers (#11202)
- use de4x5 instead of tulip for one card (#11093)
- updated X11 data
* Thu Sep 20 2001 snwint@suse.de
- make AIPTEK tablet a mouse again
- added old_unique_id field
* Wed Sep 12 2001 snwint@suse.de
- rewrote floppy detection to make it work on non-i386 archs
* Tue Sep 11 2001 snwint@suse.de
- get current video mode
* Mon Sep 10 2001 snwint@suse.de
- updated X11 data
- make it work with diet-libc
- should correctly report vmware cards now
* Tue Sep  4 2001 snwint@suse.de
- changed unique_id calculation (#10139)
- introduced arch_ppc64, CHRP64 -> CHRP
* Mon Sep  3 2001 snwint@suse.de
- usb printer device names have changed
- new x11 data
- fixed segfault bug in ide-scsi handling
* Wed Aug 29 2001 snwint@suse.de
- new x11 data
- ignore obviously broken ddc info
* Mon Aug 27 2001 snwint@suse.de
- new qlogic driver info (#9868)
- completely new x11 data
* Thu Aug 23 2001 snwint@suse.de
- fixed to work with the new cpqarray driver
- fixed evil database bug (#9798)
* Mon Aug 20 2001 snwint@suse.de
- removed usb network module info
- added iSeries disks
* Fri Aug 17 2001 snwint@suse.de
- fixed some drivers.audio entries
- install in $DESTDIR
- handle ide-scsi drives
- fix segfault bug in apm detection
- added usb network data
* Mon Aug  6 2001 snwint@suse.de
- fixed tv card detection
* Tue Jul 31 2001 snwint@suse.de
- make now builds shared version per default
* Tue Jul 31 2001 snwint@suse.de
- integrated hwscan
* Fri Jul 27 2001 snwint@suse.de
- added chipcard reader support
- added camera (webcam) support
- added framebuffer support (currently: VESA)
* Thu Jul 26 2001 snwint@suse.de
- report smp capability only if >1 processors are active
- added access functions for /var/lib/hardware/ to libhd
- hwinfo: no progress info if output is redirected
- hwinfo: multiple arguments allowed
- assign a hw_class
* Mon Jul 23 2001 snwint@suse.de
- SMP code can now handle empty MP tables
- support module lists in driver info
- new 'manual' flag indicating hardware that was not
  detected but entered manually
- report usb capability only if the controller has an irq assigned
* Fri Jul 13 2001 kukuk@suse.de
- SUNs fiberchannel controller could also be in the unspecified
  section
* Thu Jul 12 2001 kukuk@suse.de
- Add support for sunqfe Card
* Wed Jun 27 2001 snwint@suse.de
- added usb scanner detection
- set gpm protocol to imps2 for wheel mice
- bios based monitor detection enabled per default
- made usb module loading default
* Tue Jun 19 2001 snwint@suse.de
- fixed for s390x
* Wed Jun 13 2001 snwint@suse.de
- fixed framebuffer mode detection bug (#8620)
- prefer e100.o over eepro100.o (#8797)
* Thu May 31 2001 schwab@suse.de
- Don't dereference free'd pointer.
* Mon May 14 2001 snwint@suse.de
- use isapnp_reset=0 for loading isa-pnp.o (#8075)
* Fri May 11 2001 snwint@suse.de
- have i2o cards listed as storage controllers (#6335)
* Thu May 10 2001 snwint@suse.de
- increase /dev/psaux timeout
- adapted missing keyboard detection for kernel 2.4
* Thu May 10 2001 snwint@suse.de
- less things in libhd_tiny.a
- read block 0 from disks _before_ going to look for the boot device
- vmware detection clobbers %%ebx; fixed
- completely new monitor data base (#7536)
* Mon May  7 2001 snwint@suse.de
- preserve %%ebx in i10_v86.c::vm86_rep
* Mon May  7 2001 snwint@suse.de
- rewrote isapnp detection for 2.4 kernel
- updated driver info data
- added "Baum" braille display detection
* Thu May  3 2001 snwint@suse.de
- added vmware check
- don't do scsi write cache detection in vmware
- added ia64 smp detection
- ia64 x11 data added
- use tulip instead of de4x5 (#7317)
* Mon Apr 30 2001 snwint@suse.de
- updated x11 data
- fixed multi-head display handling
- adapted compaq smart array detection for kernel 2.4
* Wed Apr 25 2001 snwint@suse.de
- parport detection updated for kernel 2.4
- add scsi hostadapter info to debug output
- usb-storage again
- boot_ia64 -> boot_elilo
* Fri Apr 20 2001 snwint@suse.de
- better usb-storage support
* Thu Apr 19 2001 snwint@suse.de
- reworked floppy detection
- identify devices with removable media
- zip drives are always reported as floppies
* Wed Apr 18 2001 snwint@suse.de
- reworked ps/2 mouse code
- provide number of buttons/wheels for mice
- fixed specfile
* Tue Apr 17 2001 kkaempf@suse.de
- fix filelist in specfile
  call ldconfig at end of "make install"
* Sat Apr  7 2001 snwint@suse.de
- new output format for support tool
- more options for hwinfo
- include pcmcia/cardbus cards in device lists
* Thu Apr  5 2001 snwint@suse.de
- new major version due to incompatible interface changes
- integrated experimental changes (split was after v1.90)
* Tue Apr  3 2001 snwint@suse.de
- fixed segfault bug in alpha smp code
* Mon Mar 26 2001 snwint@suse.de
- unique id format changed
* Wed Feb 28 2001 snwint@suse.de
- stepan: removed ISDN on alpha
- avoid trigraphs while generating the data base
* Thu Feb 22 2001 snwint@suse.de
- fixed hd_copy() segfault bug (ppc)
* Wed Feb 21 2001 snwint@suse.de
- implemented SMP detection on ppc
* Tue Feb 20 2001 snwint@suse.de
- backport of new SMP detection code (ia32)
- get console speed from kernel command line (ppc)
* Thu Feb 15 2001 snwint@suse.de
- fixed evil scsi device detection bug
  (missing scsi devices under some strange circumstances)
- don't probe physical scsi geometry
* Mon Feb 12 2001 snwint@suse.de
- changed display adapter detection code to prefer sbus cards
* Fri Feb  9 2001 snwint@suse.de
- kkaempf: "ld -shared" is forbidden, changed to "gcc"
* Wed Jan 31 2001 snwint@suse.de
- mls: new oem stuff
* Mon Jan 29 2001 snwint@suse.de
- kukuk: sparc keyboard patches
* Thu Jan 18 2001 snwint@suse.de
- fixed ISAPnP device name handling
* Wed Jan 17 2001 snwint@suse.de
- updated dac960 driver info
* Wed Jan 17 2001 snwint@suse.de
- added '--help' option to hwinfo
- implemented a basic getopt-style hwinfo interface
- activate pr_bios if pr_misc is set
* Tue Jan 16 2001 snwint@suse.de
- back to old version scheme to avoid update problems
* Mon Jan 15 2001 snwint@suse.de
- updated scsi driver info
* Mon Jan 15 2001 snwint@suse.de
- make XF 4 default if no X11 info is found (ia32 only)
- fixed serial line detection bug
* Fri Jan 12 2001 snwint@suse.de
- fix minor bug in printer detection
- fix bios disk number detection
- sym*.o instead of ncr*.o for 53C875
- quick fix for Wacom tablets
* Thu Jan 11 2001 snwint@suse.de
- arvin: made res_pppd_option work
- arvin: fixed detection of terminal adapters
- sped up new modem stuff if no modem is connected
* Wed Jan 10 2001 snwint@suse.de
- introduced res_pppd_option
* Tue Jan  9 2001 snwint@suse.de
- smid@suse.cz: improved modem init string code
* Mon Jan  8 2001 snwint@suse.de
- fixed color depth handling
- fixed multi-soundcard bug
* Sun Jan  7 2001 snwint@suse.de
- kendy@suse.cz: use BIOS port info for parport
- 8139too instead of rtl8139 whenever possible
* Wed Dec 20 2000 snwint@suse.de
- added modem init string patch from smid@suse.cz
* Tue Dec 19 2000 snwint@suse.de
- added cciss stuff
* Mon Dec 18 2000 snwint@suse.de
- BIOS lba stuff now works
- updated x11 data
* Fri Dec 15 2000 snwint@suse.de
- hwinfo can now update x11 info in install.inf
* Thu Dec 14 2000 schwab@suse.de
- Build pnpdump only on i386 and alpha.
- Make shared library executable.
* Wed Dec 13 2000 snwint@suse.de
- hwinfo can now update braille info in install.inf
- activate alva braille detection
* Tue Dec 12 2000 snwint@suse.de
- added symlink
* Tue Dec 12 2000 snwint@suse.de
- new version number scheme (due to shared lib)
- create shared libhd
- report BIOS lba extension support
- rearranged building libhd_tiny a bit
* Tue Dec 12 2000 snwint@suse.de
- fixed isapnp segfault bug
* Fri Dec  8 2000 snwint@suse.de
- new alva detection code
- added cd-r/dvd detection
- read "el torito" boot info
* Thu Dec  7 2000 snwint@suse.de
- fixed evil hddb bug
- added 3d script field
* Fri Dec  1 2000 snwint@suse.de
- changed to new package name
* Thu Nov  9 2000 snwint@suse.de
- started work on hddb fix
- renamed timeout -> hd_timeout
- remove memory leaks, part 2 (ppc)
- add CD-RW detection (and DVD)
- remove memory leaks, part 1
* Tue Oct 10 2000 snwint@suse.de
- distinguish between chrp & chrp64
- provide a unique key for every hardware item
* Tue Oct 10 2000 snwint@suse.de
- cpu/smp detection code improved
* Thu Sep 28 2000 snwint@suse.de
- sparc: added x11 info
* Fri Sep 22 2000 snwint@suse.de
- ppc: fixed serial line & modem detection
* Thu Sep 21 2000 snwint@suse.de
- provide CHPID on s390
* Wed Sep 20 2000 snwint@suse.de
- added missing closedir()
* Mon Sep 18 2000 snwint@suse.de
- improved /proc/interrupt parsing
- ppc: always return a ps/2 mouse for PreP & CHRP
- skip serial device detection for console & yast2ser /proc/cmdline
  entries
- ids updated
* Fri Sep 15 2000 snwint@suse.de
- ppc: changed some ids
* Wed Sep 13 2000 snwint@suse.de
- serial console on ppc
* Wed Sep 13 2000 snwint@suse.de
- ppc x11 driver info
- ppc serial console
- braille only on ia32
- fixed scsi segfault bug
* Mon Sep 11 2000 snwint@suse.de
- updated device ids
- added basic i2o support
- disabled isapnp on ppc
* Thu Sep  7 2000 snwint@suse.de
- fixed modem segfault bug
- fixed Zip device detection
* Wed Sep  6 2000 snwint@suse.de
- s390: network devices
* Tue Sep  5 2000 snwint@suse.de
- s390: finds disks
- ppc: better sound detection
* Fri Aug 25 2000 snwint@suse.de
- new platform cpu entry on alpha
* Wed Aug 23 2000 snwint@suse.de
- made libhd at least to compile on s390
- slightly changed memory detection
- ADB mice: /dev/input/mice
- added monitor detection on ppc
- fixed iso9660 info reading
* Mon Aug 14 2000 snwint@suse.de
- added PROM parser for ppc; currently handles
  SCSI, network, sound & floppy devices
* Wed Aug  9 2000 snwint@suse.de
- added pr_misc to hw_isdn
- fixed memory size detection
- added 'generation' to system entry (for ppc)
- new scsi detection code
- kukuk: PS/2 keyboard detection on UltraSPARC
* Tue Aug  1 2000 kukuk@suse.de
- Add PS/2 keyboard detection on UltraSPARC
* Fri Jul 28 2000 snwint@suse.de
- fixed 'x11' parameter parsing
* Thu Jul 27 2000 snwint@suse.de
- added '--special' option to hwinfo (needed for live CD)
* Mon Jul 24 2000 snwint@suse.de
- SMP detection: look for 'apic' flag
- updated x11 data
* Thu Jul 20 2000 snwint@suse.de
- updated x11 data
* Thu Jul 20 2000 snwint@suse.de
- fixed Vaio detection
- updated special ide chipset list
- more functions in LIBHD_TINY
- updated x11 data
* Wed Jul 19 2000 snwint@suse.de
- updated x11 data
* Tue Jul 18 2000 snwint@suse.de
- dropped alva probing
- updated x11 data
* Mon Jul 17 2000 snwint@suse.de
- updated x11 data
* Sat Jul 15 2000 snwint@suse.de
- fixed isapnp isdn probing bug
- updated x11 data
* Thu Jul 13 2000 snwint@suse.de
- fixed bootdevice detection bug
- detect PowerBooks
* Wed Jul 12 2000 snwint@suse.de
- updated alsa driver info
- updated minicdb id data
- fixed missing isapnp sound cards bug
- added Sony Vaio detection
- changed lance driver entry
- fixed isdn/network card bug
* Tue Jul 11 2000 snwint@suse.de
- pnpdump: start port scanning at port 0x20b, not 0x203
  (skips potential game port)
- get ids directly from minicdb
* Fri Jul  7 2000 snwint@suse.de
- fixed hw_sys/hw_tv probing bug
* Thu Jul  6 2000 snwint@suse.de
- new 'system' hw entry
- sparc smp detection: active -> probed
* Wed Jul  5 2000 snwint@suse.de
- added parallel Zip drive detection
* Mon Jul  3 2000 snwint@suse.de
- don't list cardbus/pcmcia devs in hd_list()
- add multimedia/video boards to display adapters
* Tue Jun 27 2000 snwint@suse.de
- fixed bug in braille detection
* Tue Jun 27 2000 snwint@suse.de
- fixed braille display probing
* Mon Jun 26 2000 snwint@suse.de
- updated README
- fixed bug in 'hwprobe' handling
* Mon Jun 26 2000 snwint@suse.de
- new usb mouse devices
* Thu Jun 22 2000 snwint@suse.de
- activated serial line scanning in linuxrc
- extendend 'hwprobe=' features
* Wed Jun 21 2000 snwint@suse.de
- changed (driver_info_x11_t).x11.raw to str_list_t
- fhp_old braille detection implemented
- alva & ht braille stuff added
* Wed Jun 21 2000 snwint@suse.de
- added 'x11' kernel cmdline param
* Tue Jun 20 2000 snwint@suse.de
- fixed mk_ids (used to drop all non-x11 ids)
- improved 'hwprobe=' functionality
- fhp braille detection implemented
* Tue Jun 20 2000 snwint@suse.de
- updated pciutils & sax/sax2 data
- added fire gl1
- added 'hwprobe' env resp. kernel cmdline param
* Mon Jun 19 2000 ro@suse.de
- up to 1.01
* Fri Jun  9 2000 snwint@suse.de
- improved ddc parsing (new syslinux!)
* Fri Jun  9 2000 snwint@suse.de
- added hw_monitor, hw_printer, hw_tv, hw_scanner
* Thu Jun  8 2000 snwint@suse.de
- added hd_list() function
* Tue Jun  6 2000 snwint@suse.de
- new SaX[2] data
- changed mk_ids to provide 3d *and* non-3d x11 entries
* Mon Jun  5 2000 snwint@suse.de
- new *display_list function
* Wed May 31 2000 snwint@suse.de
- provides info about bios disk ids
* Tue May 30 2000 snwint@suse.de
- extended X11 driver info (for XF86 4.0)
- added Thorsten's small SPARC patch
- extended serial line info
- note: v0.95 was a ppc quick-hack only version needed for 6.4;
  it will not be integrated into the main tree
* Fri May 26 2000 kukuk@suse.de
- Add device name for serial console
* Wed May 24 2000 snwint@suse.de
- fixed tmp file security hole
- added hd_{mouse/keyboard/floppy}_list() functions
* Mon May 15 2000 kukuk@suse.de
- Add missing break.
* Mon May 15 2000 snwint@suse.de
- integrated Thorsten Kukuk's patches (mostly SPARC stuff)
* Thu May 11 2000 kukuk@suse.de
- Don't open /dev/ttyS? on SPARC
* Wed May  3 2000 kukuk@suse.de
- linuxrc should probe for mouse on SPARC
* Fri Apr 28 2000 kukuk@suse.de
- Probe for Sun Mouse only if we have a Sun Keyboard
* Fri Apr 28 2000 kukuk@suse.de
- Implement SBUS Probing for SPARC
* Wed Apr 26 2000 kukuk@suse.de
- Probe for Sun Mouse and SPARC CPU
- Fix compiling with new kernel headers
* Mon Apr 17 2000 snwint@suse.de
- ADB mouse driver info extended
- color code stuff updated
* Tue Apr 11 2000 snwint@suse.de
- fixed XkbModel typo on intel/axp
- ia64 patches from Andreas
- new Mac color code
* Mon Apr  3 2000 snwint@suse.de
- fixed XkbModel typo on intel/axp
* Fri Mar 31 2000 snwint@suse.de
- changed XkbModel to "powerpcps2" on chrp machines
- more iMac colors
* Fri Mar 24 2000 snwint@suse.de
- read color code on macs
* Tue Mar 21 2000 snwint@suse.de
- a lot of ppc & sparc improvements
* Tue Mar 14 2000 snwint@suse.de
- see ChangeLog
* Wed Mar  8 2000 snwint@suse.de
- adapted for release
* Wed Mar  8 2000 snwint@suse.de
- see ChangeLog
* Wed Mar  8 2000 snwint@suse.de
- see ChangeLog
* Wed Mar  8 2000 snwint@suse.de
- see ChangeLog
* Mon Mar  6 2000 snwint@suse.de
- see ChangeLog
* Sun Mar  5 2000 snwint@suse.de
- some monitor data
* Sat Mar  4 2000 snwint@suse.de
- see ChangeLog
* Fri Mar  3 2000 snwint@suse.de
- small fixes
* Wed Mar  1 2000 ro@suse.de
- fixed filelist
* Wed Mar  1 2000 snwint@suse.de
- see ChangeLog
* Mon Feb 28 2000 snwint@suse.de
- see ChangeLog
* Sat Feb 26 2000 snwint@suse.de
- see ChangeLog
* Fri Feb 25 2000 snwint@suse.de
- see ChangeLog
* Thu Feb 24 2000 snwint@suse.de
- see ChangeLog
* Wed Feb 23 2000 snwint@suse.de
- see ChangeLog
* Tue Feb 22 2000 snwint@suse.de
- changed x11/3d driver info
* Thu Feb 17 2000 snwint@suse.de
- see ChangeLog
* Wed Feb 16 2000 snwint@suse.de
- see ChangeLog
* Thu Feb 10 2000 snwint@suse.de
- see ChangeLog
* Sat Feb  5 2000 snwint@suse.de
- see ChangeLog
* Tue Feb  1 2000 snwint@suse.de
- see ChangeLog
* Fri Jan 28 2000 snwint@suse.de
- new interface functions
* Wed Jan 26 2000 snwint@suse.de
- see ChangeLog file
* Mon Jan 17 2000 snwint@suse.de
- new database format
- various other stuff
* Mon Jan 10 2000 snwint@suse.de
- new version, with basic ppc & sparc support
* Wed Dec 15 1999 snwint@suse.de
- first version
