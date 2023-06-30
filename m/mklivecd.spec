Summary:	Builds a LiveCD from an existing installation
Name:		mklivecd
Version:	0.7.2
Release:	6.1
License:	GPL
Group:		System/Configuration/Boot and Init
URL:		https://livecd.berlios.de/
Source0:	%{name}-%{version}.tar.bz2
Requires:	busybox >= 1.7.0
Requires:	mediacheck, genisoimage, squashfs-tools >= 3.3-3
#Requires:	lzma-kmod, squashfs-lzma-kmod
Requires:	syslinux >= 3.82
Requires:	cpio >= 2.9-2
Requires:	zlib >= 1.2.3-4
Requires:	libmodprobe >= 3.3-pre11.4
Requires:	module-init-tools >= 3.3-pre11.4
BuildArch:  noarch

%description
The mklivecd tools are dedicated to providing you with the capability to
create your own LiveCD or LiveDVD from a currently installed PCLOS distribution.
It can be used to create your own travelling PCLinuxOS-based LiveCD, specialised
LiveCD featuring custom-developed applications or to put together a demo disk
to show off the power of our favourite OS. The possibilities are endless!

Created CD's feature automatic hardware detection and setup. In addition, it
utilises compression technology allowing you to build a LiveCD from a partition
much larger than will typically fit on a CD or DVD.(Up to 2GB for a normal 650MB CD
or around 10GB for a normal 4GB DVD) When booting from this LiveCD, the data is
transparently decompressed as needed with almost no performance impact.

%prep
%setup -q

%build
%__make

%install
rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mkremaster-kde.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Make LiveCD
Comment=Remaster while running from livecd/harddrive
Exec=kdesu /usr/sbin/mkremaster
Icon=/usr/share/icons/cd_burning_section.png
Terminal=false
Type=Application
StartupNotify=false
Categories=X-MandrivaLinux-System;
OnlyShowIn=KDE
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mkremaster.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Make LiveCD
Comment=Remaster while running from livecd/harddrive
Exec=gksu -l /usr/sbin/mkremaster
Icon=/usr/share/icons/cd_burning_section.png
Terminal=false
Type=Application
StartupNotify=false
Categories=X-MandrivaLinux-System;
NotShowIn=KDE
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mkremaster-tinyme.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Make LiveCD
Comment=Remaster while running from livecd/harddrive
Exec=gksu -l /usr/sbin/mkremaster
Icon=/usr/share/icons/cd_burning_section.png
Terminal=false
Type=Application
StartupNotify=false
Categories=System;Utility;Core;GTK;
NotShowIn=KDE
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat > $RPM_BUILD_ROOT%{_datadir}/applications/liveusb-kde.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Make LiveUSB
Comment=Create PCLinuxOS on a Flash Drive
Exec=kdesu /usr/sbin/liveusb
Icon=usbpendrive_unmount.png
Terminal=false
Type=Application
StartupNotify=false
Categories=X-MandrivaLinux-System;
OnlyShowIn=KDE
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING CHANGELOG FAQ README README.BOOTCODES README.USB TODO
%{_sbindir}/mklivecd
%{_sbindir}/hwdetect
%{_sbindir}/liveusb
%{_sbindir}/mkchgsloop
%{_sbindir}/mkremaster
%dir %{_datadir}/mklivecd
%{_datadir}/mklivecd/linuxrc
%{_datadir}/mklivecd/halt.local
%{_datadir}/mklivecd/rc.sysinit
%{_datadir}/applications/mkremaster-kde.desktop
%{_datadir}/applications/mkremaster.desktop
%{_datadir}/applications/mkremaster-tinyme.desktop
%{_datadir}/applications/liveusb-kde.desktop

%changelog
* Mon Jul 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.2
- Rebuilt for Fedora

* Mon Jun 29 2009 Texstar <texstar@gmail.com> 7.2-3pclos2009
- fix some verbage
- cherry pick some changes from unity

* Mon Jun 29 2009 Texstar <texstar@gmail.com> 7.2-2pclos2009
- small mklivecd updates

* Sat Jun 27 2009 Texstar <texstar@gmail.com> 7.2-1pclos2009
- revert to original mkremaster
- add language support
- fix hwdetection with nonetwork
- mklivecd updates

* Thu Jun 25 2009 Texstar <texstar@gmail.com> 7.1-30pclos2009
- try to fix hwdetect no options

* Wed Jun 24 2009 Texstar <texstar@gmail.com> 7.1-29pclos2009
- remove noapic and nolapic as default 

* Mon Jun 22 2009 Texstar <texstar@gmail.com> 7.1-28pclos2009
- update mkremaster zentiy script from travis

* Mon Jun 22 2009 Texstar <texstar@gmail.com> 7.1-27pclos2009
- exclude ^/root/.synaptic/log/*.log
- exclude ^/var/cache/apt/*.bin
- exclude ^/var/lib/apt/lists/*pkglist.*
- exclude ^/var/lib/apt/lists/*release.*

 * Mon Jun 22 2009 Texstar <texstar@gmail.com> 7.1-26pclos2009
- update for testing
- add noapic nolapic as default boot options
- fix hdwdetect to only detect lan not wireless.

* Sun May 10 2009 etjr 0.7.1-25pclos2009
- fix gfxboot for syslinx-3.75

* Wed Mar 11 2009 etjr 0.7.1-24pclos2007
- mklivecd.in - add ^/etc/udev/rules.d/70-persistent* per Texstar

* Fri Jan 09 2009 Gettinther <gettinther@gmail.com> 0.7.1-23pclos2007
- Provide script to accomodate gzip/lzma compression option

* Wed Sep 10 2008 Gettinther <gettinther@gmail.com> 0.7.1-21pclos2007
- Add lzma compression support, Thank you Nico

* Sat Sep 06 2008 Gettinther <gettinther@gmail.com> 0.7.1-20pclos2007
- Code cleanup

* Thu Sep 04 2008 Gettinther <gettinther@gmail.com> 0.7.1-19pclos2007
- Load sata specific modules to try to bypass usb card readers

* Wed Sep 03 2008 Gettinther <gettinther@gmail.com> 0.7.1-18pclos2007
- Added satacd boot code

* Sun Aug 31 2008 Gettinther <gettinther@gmail.com> 0.7.1-17pclos2007
- reinstated support for usb-cdrom in linuxrc

* Sat Jun 28 2008 etjr
- hwdetect.in - add network config
- linuxrc.in - add dpt_i2o to SCSI_MODULES=

* Sat May 31 2008 etjr
- mklivecd.in - fix initrd2
- mklivecd.in - fix both initrd percent

* Sun May 11 2008 etjr
- rc.sysinit.in - fix typo
- hwdetect.in - remove /proc/bus/usb from fstab

* Sat Apr 26 2008 etjr
- halt.local.in change <STDIN> for eject

* Mon Apr 21 2008 etjr
- change ide-cd to ide-cd_mod in Modules.mk
- remove liveusb from menu

* Mon Apr 14 2008 etjr
- minor spec change

* Sun Apr 13 2008 etjr
- minor spelling fixes to bootcodes README

* Sat Apr 12 2008 ikerekes
- updated bootcodes README with the new bootcodes
- fixed linuxrc parameter parsing with "fromusb" parameter

* Fri Apr 11 2008 etjr
- add modules for ide modules
- add Provides for perl

* Mon Apr 7  2008 ikerekes
- fixed bootfromiso code

* Tue Apr 1  2008 ikerekes
- linuxrc total overhaul of the $CDROM_LIST creation (to eliviate [h,s]d[a-t][0-99] problem)
-         total overhaul of the fromusb code (not using load_usb and load_scsi any more, the probe-modules loads those modules)
-         total overhaul of parameter parsing
-         modified livecd= to specify the the cloop file name (as opposed to hard-coded livecd.sqfs) as per c-chan
-         modified the bootfrom to read as bootfromiso= meaning only the iso name without the device portion
-
- rc.sysinit     eliminated changes= cheatcode, implemented changes_dev and changes_file instead
-                the changes_dev is device independent (takes the LABEL= or UUID= mount code
-                the changes_file (if specified) describes a loop mounted changes file (system)
-                total overhaul of parameter parsing 

* Mon Mar 31 2008 texstar
- remove touch fstab/mtab
- add requires drakx-installer-binaries-probe

* Sun Mar 30 2008 ikerekes
- first trial of including prob-modules

* Fri Mar 29 2008 texstar
- add requires to new module-init and libzlib1

* Fri Jan 18 2008 etjr
- add back BusLogic module
- updated liveusb per Jeremiah

* Tue Jan 15 2008 etjr
- updated liveusb per Ivan

* Sun Jan 13 2008 etjr
- rc.sysinit "changes" patch per Ivan

* Sat Jan 12 2008 etjr
- updated liveusb per Ivan
- added zenity percentage to mkchgsloop

* Wed Jan 07 2008 etjr
- add another alias to config_modprobeconf per Texstar
- add mkchgsloop

* Thu Dec 27 2007 etjr
- add config_modprobeconf per Texstar
- change mkremaster menu entry to Make LiveCD

* Sun Dec 2 2007 ikerekes
- improve sata drive search (extend beyond sd[a-b]
- improve changes=loopfile (don't limit to ext2)

* Fri Nov 30 2007 ikerekes
- change=<dev>/<loopfile> ext2 loopmounted file, can reside on vfat (usb stick) or any linux fs.
- Brian's bootfrom mod in the halt.local

* Wed Oct 24 2007 etjr
- more changes in mkremaster.in

* Mon Oct 22 2007 etjr
- i18n-framework from i18n team at mypclinuxos.com

* Thu Oct 17 2007 etjr
- remove BusLogic from modules.mk for vmware server 1.0.4

* Mon Oct 08 2007 etjr
- mkremaster.in
-   more terminals for mklivecd

* Sun Sep 23 2007 etjr
- updated to work with both pclos and tinyme
- mkremaster.in
-  changes for shutdown in livecd

* Mon Sep 17 2007 etjr
- updated mkremaster.in
- added mkremaster and liveusb menu entry in spec

* Sun Aug 19 2007 etjr
- corrected usb-storage and bootsplash per Ivan

* Fri Aug 17 2007 etjr
- More changes by Ivan

* Tue Aug 14 2007 etjr
- Many changes by Ivan

* Wed Aug 08 2007 etjr
- bootfrom /dev/loop fix per Ivan

* Mon Aug 06 2007 etjr
- updated Modules.mk per Ivan

* Wed Jul 25 2007 etjr
- tweak Makefile and Rules.mk
- added liveusb and mkremaster
- option to create iso's with 2 kernels

* Tue Jul 24 2007 etjr
- change the spec back for make rpm

* Fri Jul 20 2007 ocilent1 <ocilent1 at gmail dot com>
- some further insmod cleanups
- tweak spec file a bit

* Fri Jul 20 2007 etjr
- fix insmod for new modules-init-tools-3

* Tue Jul 10 2007 etjr
- changes to use mdev or udevstart

* Sun Jul 8 2007 etjr
- changes for mdev (busybox mdev) - Thanks Gentoo

* Sat Jun 2 2007 etjr
- hwdetect.in
- changes in nofinishinstall
- removed "&" from config_*()

* Fri May 11 2007 Texstar <texstar@gmail.com> 
- add VideoSafeModeFBDev and VideoSafeModeVesa
- in mklivecd and hwdetect

* Fri May 11 2007 Texstar <texstar@gmail.com> 
- change safe mode to use vesa driver instead of fbdev

* Sun May 6 2007 etjr
- hwdetect.in
-  added "&" to config_*(); to suppress verbose bootup  warnings
-  remove duplicate "my $modules_conf" & "my %cmdline" entries
-  remove "my $cdsymlinks" /etc/udev/scripts/cdsymlinks.sh deprecated?
-  fixed - mkdir_p("$prefix/etc/livecd/hwdetect/");
- mklivecd.in
-  added /media$ to $nodirs
- linuxrc.in
-  added mkdir -p /media

* Sat May 5 2007 etjr
- merge in sata changes in hwdetect per Ivan

* Thu May 3 2007 etjr
- changes for moved modules with kernel 2.6.20
- removed 2.4 kernel modules
- removed more unused code

* Mon Apr 30 2007 Texstar <texstar@gmail.com> 
- merge in changes to hwdetect per Ivan

* Wed Mar 28 2007 etjr
- moved /dev/sd[a-b][0-99] first for usb per Nico
- ramdisk size change from 1/3 to 1/2 per Nico

* Sat Mar 24 2007 etjr
- add changelog to spec file

* Tue Mar 6 2007 etjr
- suppress "bootsplash not found ..." warning
- remove some unused code
- --ufs defaults to aufs

* Sat Feb 3 2007 etjr
- hwdetect.in
- changed back config_network();
- hwdetect-lang.in
- changed back 'network probe'

* Fri Feb 2 2007 etjr
- mklivecd.in
- added more excluded files
- change mkisofs to genisoimage
- change blocksize to 224
- change default bootloader back to iso
- change label Framebuffer to VideoSafeMode in iso and grub
- hwdetect.in
- remove config_network();
- hwdetect-lang.in
- remove 'network probe'
- linuxrc.in
- moved "##Probe the scsi devices." section per Ivan
- Cleaned out some unused lines 

* Tue Dec 12 2006 etjr
- added option --ufs to create livecd with unionfs or aufs
- added rc.sysinit.aufs.in
- rc.sysinit.in - create ifcfg-eth0
- hwdetect.in - Texstar's config_network fix
- mklivecd.in
- exclude files ifcfg-eth0, 61-*config.rules, and modprobe.conf
- gfxboot changes
- default to grub

Jaco Greeff <jaco@puxedo.org> 0.6.0-20070506.1
- version 0.6.0-20070506
- updated description
- added squashfs-tools require
- updated requires to include version numbers where earlier versions won't work

* Wed Dec 03 2003 Peroyvind Karlsen <peroyvind@linux-mandrake.com> 0.5.6-2mdk
- spec fixes
- fix unowned dir

* Mon Oct  6 2003 Jaco Greeff <jaco@linuxminicd.org> 0.5.6-1mdk
- version 0.5.6
- spec fixes by Buchan Milne <bgmilne@cae.co.za>

* Sat Sep 27 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.5.5-2mdk
- rebuild

* Thu Sep 25 2003 Jaco Greeff <jaco@linuxminicd.org> 0.5.5-1mdk
- version 0.5.5

* Wed Sep 24 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.5.4-2mdk
- spec fixes

* Tue Sep 23 2003 Jaco Greeff <jaco@linuxminicd.org> 0.5.4-1mdk
- version 0.5.4
- removed patch0, fixed upstream

* Mon Sep 22 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.5.3-1mdk
- initial import into contrib, based on spec file from Jaco Greeff
- fixed requires (mkisofs)
- temporary locale fix to correct calculate initrd size
- correct mdk group name
- some macroszification
