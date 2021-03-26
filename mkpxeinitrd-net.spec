%define BUSYBOX_VERSION 1.11.2
Summary: PXE Network-booting initrd builder
Name: mkpxeinitrd-net
Version: 1.2
%define release_number 34
Release: 35
Source0: %{name}-%{version}-%{release_number}.tar.bz2
Source1: http://www.busybox.net/downloads/busybox-%{BUSYBOX_VERSION}.tar.bz2
Source2: ftp://ftp.kernel.org/pub/software/utils/pciutils/pciutils-2.1.11.tar.gz

License: GPL
Group: System/Kernel and hardware
URL: http://www.fensystems.co.uk/SRPMS.fensys
BuildRequires: glibc-static
# comment this, let drblsrv to install them, since in RH, it's tftp-server, but
# in SuSE, it's tftp.
Requires: tftp-server binutils
Obsoletes: mknbi, mkinitrd-net
Provides: mknbi

%description
mkpxeinitrd-net is a derived program from mkinitrd-net.
mkpxeinitrd-net allows you to build initial ramdisk images (initrds) suitable for use with PXE and Etherboot (Using PXE compatable mode) network-booting software.  This package contains one main utility: mkpxeinitrd-net (to build an initrd containing a specified set of network-card modules).

mkpxeinitrd-net uses code from busybox and pciutils projects.

%prep
%setup -q -n initrd -a1 -a2

%build
# Ugly jobs. Should use patch file for these. This is for gcc (GCC) 3.2.2 20030222.
# From Busybox 1.10.1, the compiling switch for static linking with gcc will be automatically set by scripts/trylink from busybox. Therefore comment these 3:
#perl -pi -e "s/-Wl,--gc-sections//g" busybox-%{BUSYBOX_VERSION}/scripts/trylink
#perl -pi -e "s/-Wl,--sort-section -Wl,alignment//g" busybox-%{BUSYBOX_VERSION}/scripts/trylink
#perl -pi -e "s/^#error Aborting compilation.*//g" busybox-%{BUSYBOX_VERSION}/applets/applets.c
make LIBDIR=%{_libdir}/mknbi

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall tftpbootdir=$RPM_BUILD_ROOT%{_localstatedir}/tftpboot initrdskeldir=$RPM_BUILD_ROOT%{_libdir}/mkpxeinitrd-net/initrd-skel
ln -s %{_localstatedir}/tftpboot $RPM_BUILD_ROOT/tftpboot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/update-pciids.sh
%{_bindir}/mkpxeinitrd-net
%{_bindir}/parse-net-mod
%{_bindir}/parse-nfs-mod
/tftpboot
#
%{_libdir}/mkpxeinitrd-net
%doc README
%doc AUTHORS.busybox LICENSE.busybox COPYING CHANGES

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Oct 14 2008 Wind <yc.yan@ossii.com.tw> 1.2-35.ossii
- Add %makeinstall parameter: initrdskeldir.

* Tue Sep 30 2008 Wei-Lun Chao <bluebat@member.fsf.org> 1.2-34.ossii
- Rebuild for M6(CentOS5)

* Mon Sep 22 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-34
- Bug fixed: if no files in /lib/modules/$KVER/extra, skip copying files.

* Thu Sep 04 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-33
- Bug fixed: suppress the unalias ls message in get-nic-devs.

* Thu Sep 04 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-32
- Put the linked NICs in the higher priority to request IP address.

* Tue Sep 02 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-31
- mkpxeinitrd-net was updated since Lenny puts extra modules in /lib/modules/kernel/$KER_VER/extra/ 
- New upstream busybox 1.11.2.

* Fri Aug 15 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-30
- busybox-1.11.1.config was updated with some minor features added.
- head is linked for busybox.

* Wed Aug 06 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-29
- New upstream busybox 1.11.1.

* Mon Jun 16 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-28
- New upstream busybox 1.10.3.

* Sun Apr 27 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-27
- More prompt was added in linuxrc-or-init.

* Sun Apr 27 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-26
- An option for udhcpc port was listed in linuxrc.conf.
- linuxrc-or-init honors udhdpc_port in linuxrc.conf.

* Sun Apr 27 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-25
- Static linking option can be automatically detected in busybox 1.10.1 or later. so comment those manual modification in rpm spec file.

* Sat Apr 26 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-24
- Turn on CONFIG_FEATURE_UDHCP_PORT in Busybox.

* Sat Apr 26 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-23
- New upstream busybox 1.10.1.
- Add entry /bin/bash when failing to mount root dir so that it's easier to debug.

* Fri Mar 28 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-22
- New upstream busybox 1.9.2.

* Mon Feb 18 2008 Steven Shiau <steven _at_ nchc org tw> 1.2-21
- New upstream busybox 1.9.1.

* Wed Dec 12 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-20
- Updated for Ubuntu 7.10, since extra network drivers are located in dir like: /lib/modules/2.6.22-14-generic/ubuntu/net.

* Thu Nov 22 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-19
- Bug fixed: Ugly patches in spec should be done in busybox-%{BUSYBOX_VERSION}/scripts/trylink instead of busybox-%{BUSYBOX_VERSION}/Makefile.

* Thu Nov 22 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-18
- New upstream busybox 1.8.1.

* Sun Oct 27 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-17
- new upstream busybox 1.7.2.

* Fri Sep 21 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-16
- new upstream busybox 1.7.1.

* Sun Sep 16 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-15
- use --clientid-none --vendorclass="$vendor_class_id" with udhcpc. This parameters can let DHCP server know the request is from DRBL client.

* Sun Sep 16 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-14
- use drbl.sourceforge.net instead of drbl.nchc.org.tw in the prompt.

* Wed Aug 29 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-13
- turn on mountpoint from busybox.

* Tue Aug 21 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-12
- bug fixed for mkpxeinitrd-net.

* Tue Aug 21 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-11
- new upstream busybox 1.6.1

* Sun Jun 17 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-10
- show more messages when sleeping after NIC is up.

* Sun Jun 17 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-9
- use dhcp_server_name in udhcpc-post.

* Sun Jun 17 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-8
- update prompt.

* Sun Jun 17 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-7
- add prompt about dhcp server name.

* Sun Jun 17 2007 Steven Shiau <steven _at_ nchc org tw> 1.2-6
- add an variable dhcp_server_name in linuxrc.conf, so that it's easier to use another existing dhcp server. Ref: http://sourceforge.net/forum/forum.php?thread_id=1753834&forum_id=394008

* Tue Dec 19 2006 Steven Shiau <steven _at_ nchc org tw> 1.2-5
- Remounting dev at correct place in linuxrc-or-init both for initramfs and initrd, Uuse "mount --move -n /dev/ /sysroot/dev" instead of "mount -t tmpfs -n -o bind /dev/ /sysroot/dev"
- add nr_inodes=24576 (mount -t tmpfs -n -o nr_inodes=24576,mode=0755 none /dev).

* Fri Dec 16 2006 Steven Shiau <steven _at_ nchc org tw> 1.2-4
- remove unnecessary pause in linuxrc-or-init.

* Thu Dec 14 2006 Steven Shiau <steven _at_ nchc org tw> 1.2-3
- change linuxrc to linuxrc or init in echos.

* Mon Dec 11 2006 Steven Shiau <steven _at_ nchc org tw> 1.2-2
- add comments in linuxrc-or-init.
- add CHANGES

* Mon Dec 11 2006 Steven Shiau <steven _at_ nchc org tw> 1.2-1
- delete the extra line for %.tar.gz ([ -f $*.t*gz ] && ( gunzip $*.t*gz ; bzip2 -9 $*.tar ) || true) in Makefile.
- /bin/switch_root is linked.
- mkpxeinitrd-net supports initramfs now.
- rename linuxrc as linuxrc-or-init, we will use mkpxeinitrd-net to rename it as linuxrc for initrd or init for initramfs.

* Fri Oct 27 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-26
- test before modprobe af_packet, and add more notes about af_packet.
- remove README.DRBL.

* Thu Oct 26 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-25
- if module of NIC is not found, show error message and enter shell to debug (insert-modules)

* Thu Oct 26 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-24
- buggy busybox 1.2.2, diskless client is not able to find the NIC module. Back to use busybox 1.2.1.

* Thu Oct 26 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-23
- new upstream busybox 1.2.2

* Sun Oct 22 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-22
- increase the rsize and wsize to 65536 (was 8192) for NFS client parameters (udhcpc-post).

* Sun Oct 08 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-21
- comment some unnecessary codes in mkpxeinitrd-net.

* Thu Oct 04 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-20
- bug fixed: kernel/net/packet should be copied to initrd for Debian based.

* Thu Oct 04 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-19
- bug fixed: parse-nfs-mod is not installed in rpm/deb.

* Wed Oct 03 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-18
- add parse-nfs-mod.
- update mkpxeinitrd-net to work with newer nfs.ko in 2.6.17-2.6.18 (now it need fscache.ko), add we use parse-nfs-mod to get that.

* Wed Sep 20 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-17
- change #!/bin/sh to #!/bin/bash in mkpxeinitrd-net.

* Fri Sep 15 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-16
- new upstream busybox 1.2.1

* Thu Jul 27 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-15
- sign the rpm with gpg.

* Sat Jul 01 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-14
- new upstream busybox 1.2.0

* Fri May 19 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-13
- new upstream busybox 1.1.3

* Tue Apr 11 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-11
- new upstream busybox 1.1.2

* Fri Apr 7 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-10
- update the prompt when loading modules.

* Fri Apr 7 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-9
- add an option -nu|--no-usb-modules to exclude USB keyboard related modules.

* Tue Mar 28 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-8
- downgrade busybox 1.1.1 to 1.1.0, since failed to mount nfs root.

* Tue Mar 28 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-7
- new upstream busybox 1.1.1

* Mon Mar 27 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-6
- The mode of files in /usr/lib/mkpxeinitrd-net/initrd-skel/etc should be 644.
- Add usbcore.ko in initrd.

* Thu Mar 16 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-5
- add necessary usb modules for usb keyboard to make it work in initrd.

* Mon Mar 13 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-4
- remove some unnecessary lines in initrd/udhcpc-post.

* Sun Mar 12 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-3
- use node_root for sysroot, not $IP now. Therefore we do not have to link /tftpboot/node_root to $IP
- it should be ro, not rw for NFS option.

* Mon Mar 06 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-2
- update notes in udhcpc-post.
- DRBL SSI is ready.

* Thu Mar 02 2006 Steven Shiau <steven _at_ nchc org tw> 1.1-1
- add drbl single system image support. (Not ready yet)

* Sat Feb 18 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-9
- add an option to set the pause time (secs) after network card is up. This is specially for some switch which need extra time to link, check https://sourceforge.net/forum/message.php?msg_id=3583499 for more details.

* Sat Feb 11 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-8
- refine some codes.

* Fri Feb 10 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-7
- do not show error messages when loading modules in linuxrc.

* Fri Feb 10 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-6
- We will try to find the NIC module from (1) the hwdata pcitable and (2) the table from kernel, if both are found with different modules, we will use both.

* Sat Feb 04 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-5
- turn off gettty applet since it's useless.

* Thu Feb 02 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-4
- turn on gettty applet.

* Wed Feb 01 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-3
- turn on more applets for busybox 1.1.0

* Wed Feb 01 2006 Steven Shiau <steven _at_ nchc org tw> 1.0-2
- update with busybox 1.1.0

* Sat Oct 28 2005 Steven Shiau <steven _at_ nchc org tw> 1.0-1
- rename the program as mkpxeinitrd-net, no more mkinitrd-net, to avoid confusion.
