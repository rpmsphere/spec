Name:           x11-tools
License:        GPLv2+ ; MIT License (or similar)
Group:          System/X11/Utilities
Provides:       xf86tools 3ddiag
Obsoletes:      xf86tools 3ddiag
Version:        0.1
Release:        192.1
Summary:        Tools for the X Window System
Source2:        xf86debug
Source3:        switch2nv
Source4:        switch2nvidia
Source6:        wmlist
Source8:        kroot
Source31:       xim
Source32:       xim.template
Source33:       none
Source34:       sysconfig.language-%{name}
Source35:       nvidia-pre-install
Source36:       nvidia-post-uninstall
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Some useful tools for the X Window System.



Authors:
--------
    Stefan Dirsch <sndirsch@suse.de>
    Ludwig Nussel <lnussel@suse.de>

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
install -m 755 $RPM_SOURCE_DIR/xf86debug      $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_SOURCE_DIR/wmlist         $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_SOURCE_DIR/kroot          $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/etc/X11/xim.d
install -m 644 $RPM_SOURCE_DIR/xim  $RPM_BUILD_ROOT/etc/X11
install -m 644 $RPM_SOURCE_DIR/none $RPM_BUILD_ROOT/etc/X11/xim.d
mkdir -p $RPM_BUILD_ROOT/etc/skel
install -m 644 $RPM_SOURCE_DIR/xim.template $RPM_BUILD_ROOT/etc/skel/.xim.template
mkdir -p  $RPM_BUILD_ROOT/var/adm/fillup-templates/
install -c -m0644 $RPM_SOURCE_DIR/sysconfig.language-%{name} $RPM_BUILD_ROOT/var/adm/fillup-templates/
install -m 755 $RPM_SOURCE_DIR/switch2nv $RPM_BUILD_ROOT%{_bindir} 
install -m 755 $RPM_SOURCE_DIR/switch2nvidia $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/usr/lib/nvidia
install -m 755 $RPM_SOURCE_DIR/nvidia-pre-install \
  $RPM_BUILD_ROOT/usr/lib/nvidia/pre-install
install -m 755 $RPM_SOURCE_DIR/nvidia-post-uninstall \
  $RPM_BUILD_ROOT/usr/lib/nvidia/post-uninstall

%files
%defattr(-, root, root)
%dir /etc/X11/xim.d
%dir /usr/lib/nvidia
%{_bindir}/xf86debug
%{_bindir}/wmlist
%{_bindir}/kroot
%{_bindir}/switch2nv
%{_bindir}/switch2nvidia
/usr/lib/nvidia/pre-install
/usr/lib/nvidia/post-uninstall
/etc/X11/xim
/etc/X11/xim.d/*
/etc/skel/.xim.template
/var/adm/fillup-templates/sysconfig.language-%{name}

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora
* Tue May  3 2011 tiwai@suse.de
- Add ibus and scim-bridge to sysconfig/language:$INPUT_METHOD
  list
* Thu Jul 29 2010 sndirsch@suse.de
- moved distribution hooks from post-installl to pre-install since
  driver installation is expected to fail due to nouveau driver
  still active
* Thu Jul 29 2010 sndirsch@suse.de
- added distribution hook scripts for nvidia-installer to disable
  nouveau module and remove it from initrd if required
* Tue Sep  1 2009 sndirsch@suse.de
- xf86debug: also handle SIGUSR2 and SIGPIPE
* Fri Mar 27 2009 werner@suse.de
- Speed up adding user environment for the case of having a bash
  as login shell, requested by Michael Meeks <meeks@suse.de>
* Fri Mar  6 2009 sndirsch@suse.de
- wmlist: icewm --> icewm-session (bnc #473511)
* Tue Feb 24 2009 sndirsch@suse.de
- added switch2nv/switch2nvidia from 3ddiag; provides/obsoletes
  3ddiag
* Fri Nov 14 2008 mfabian@suse.de
- bnc#413879: use GTK_IM_MODULE=cedilla instead of
  GTK_IM_MODULE=xim in the case when no fancy input method is
  started.
- add BuildArch:      noarch
* Mon Nov  3 2008 mfabian@suse.de
- bnc#440371: /etc/X11/xim: if gdm passes the language
  to Xsession as the second argument, we should not override this
  in xim.
* Thu Oct 23 2008 mfabian@suse.de
- bnc#413879: /etc/X11/xim: make sure that GTK_IM_MODULE is always
  set to something, input of German umlauts in acroread doesn’t
  work if GTK_IM_MODULE is unset.
* Fri Dec  7 2007 sndirsch@suse.de
- xf86debug: freetype2-debuginfo and xorg-x11-fontenc-debuginfo
  should also be installed
* Wed Nov 28 2007 sndirsch@suse.de
- xf86debug: added 'cont' before 'quit' for a more graceful
  Xserver termination
* Tue Nov 27 2007 sndirsch@suse.de
- xf86debug: use "bt full" instead of "bt"
* Wed Mar 28 2007 mfabian@suse.de
- fix order of changelog entries.
* Tue Mar 20 2007 mfabian@suse.de
- fix typo (thanks to Arvin Schnell for noticing).
* Thu Mar  1 2007 mfabian@suse.de
- Bugzilla #235044: make sure that environment variables from
  the user environment which might influence the start of an
  input method are read (LANG, LC_CTYPE, LC_ALL, INPUT_METHOD).
  Code to fix this by Werner Fink <werner@suse.de>. Thank you!
* Wed Jan 10 2007 sndirsch@suse.de
- xf86debug:
  * generate core file as well
* Mon Aug 21 2006 sndirsch@suse.de
- moved via profile.d scripts to Mesa
- removed bogus BuildRequires to libX11-devel
- use %%fillup_prereq for PreReq
- moved xf86debug, wmlist, kroot to /usr/bin
- removed obsolete Xwrapper symlink and xf86version script
- fixed Xserver path in xf86debug
- cleanup in specfile
* Tue May 23 2006 sndirsch@suse.de
- numlock now in numlockx package
* Sat May 20 2006 sndirsch@suse.de
- /etc/profile.d/via.{csh,sh}:
  * prevent failure, when /var/log/Xorg.0.log is not readable
* Mon Feb 13 2006 sndirsch@suse.de
- disabled via DRI driver once more (Bug #115911, comment #14)
* Fri Feb 10 2006 sndirsch@suse.de
- enabled via DRI driver again (Bug #115911, comment #12)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Oct 14 2005 sndirsch@suse.de
- removed call-browser/desktop-launch (#67130)
- xwinswitch (#128416)
- moved nvidia-installer sources to new package
  tiny-nvidia-installer
* Thu Oct 13 2005 sndirsch@suse.de
- moved nvidia kernel stuff to new package nvidia-gfx-1_0_7676
* Wed Oct 12 2005 mfabian@suse.de
- rename sysconfig.language-xf86tools to
  sysconfig.language-x11-tools, the "fillup_only -an language"
  macro in the postinstall script didn't work anymore because of
  the rename.
- rename the documentation directory to the current name of the
  package.
* Mon Sep 19 2005 sndirsch@suse.de
- fixed build
* Sun Sep 18 2005 sndirsch@suse.de
- NVIDIA_kernel-1.0-7676-1359015.diff.txt:
  * This patch addresses a kernel interaction problem on
    Linux/x86-64 systems that either don't support the no-execute
    page protection feature or on which this feature has been
    disabled by the SBIOS. (#115782)
* Mon Sep 12 2005 sndirsch@suse.de
- nv-fix-gartaddr-xen-disable_pat.diff:
  * disable pat support on Xen by default and will make the driver
    load fail under Xen unless overriden. (#115800)
* Sat Sep 10 2005 garloff@suse.de
- Fix phys vs gart address confusion that breaks under Xen.
* Fri Sep  9 2005 sndirsch@suse.de
- /etc/profile.d/via.{sh,csh}:
  * disable via DRI driver by default (#115911)
* Mon Sep  5 2005 sndirsch@suse.de
- disabled use of ATI_SHIM; will get replaced by new kernel driver
  update mechanism
* Wed Aug 17 2005 sndirsch@suse.de
- nvidia-installer-proxy.diff:
  * fixes tiny-nvidia-installer when FTP_PROXY is set to ""
    (Bug #104727)
* Wed Aug 10 2005 sndirsch@suse.de
- updated nvidia driver to release 1.0-7676 (IA32 and AMD64)
  * Fixed GeForce 7800 GTX clocking problem that affected 3D
    performance.
* Sun Aug  7 2005 sndirsch@suse.de
- link-fglrx-module:
  * libfglrx_ip.a.GCC3-<version> --> libfglrx_ip.a.GCC4-<version>
* Tue Jul 26 2005 sndirsch@suse.de
- link-fglrx-module:
  * adjusted parsing for version string in fglrx driver to new
    driver version
* Mon Jul  4 2005 sndirsch@suse.de
- use RPM_OPT_FLAGS
* Fri Jun 24 2005 sndirsch@suse.de
- updated nvidia driver to release 1.0-7667 (IA32 and AMD64)
- use Makefile template; no longer required to edit any Makefiles
  when doing a version update of the nvidia driver
* Thu Jun 23 2005 sndirsch@suse.de
- link-fglrx-module: "nVidia" --> "fglrx" (copy/paste error)
* Fri Jun  3 2005 sndirsch@suse.de
- removed mknvidiadevs/makedevices.sh. It's no longer required
  since the nVidia X driver now does mknod(2) itself to create the
  device files when it is going to need them. The OpenGL clients
  then use the device files that were created by X.
* Thu Jun  2 2005 sndirsch@suse.de
- updated nvidia driver to release 1.0-7664 (IA32 and AMD64)
* Thu May 19 2005 sndirsch@suse.de
- added link-fglrx-module; script, which links fglrx kernel
  interface (fglrx-linux.o) and binary-only part (nbfglrx_ip.a.GCC3)
  to a new fglrx kernel module
* Fri May 13 2005 mfabian@suse.de
- Bugzilla #81227: Make disabling all fancy input methods
  with INPUT_METHOD=none in /etc/sysconfig/language work for
  Qt3 and GTK2 as well.
* Fri May 13 2005 sndirsch@suse.de
- use norootforbuild
* Wed May  4 2005 sndirsch@suse.de
- package renaming: xf86tools --> x11-tools
* Mon Apr 25 2005 sndirsch@suse.de
- added mknvidiadevs init script, which makes use of makedevices.sh.
  This is required by a dynamic udev, since nVidia is no longer
  allowed to use the udev interface (Bug #70957). mknvidiadevs
  creates devices, which are required by the nVidia driver.
* Thu Mar 31 2005 sndirsch@suse.de
- updated nvidia driver to release 1.0-7174 (IA32 and AMD64)
  * obsoletes NVIDIA_kernel-1.0-7167-1237815.diff.txt
  * obsoletes NVIDIA_kernel-1.0-7167-1233959.diff.txt
* Mon Mar 21 2005 sndirsch@suse.de
- readded wmlist; still to many references (e.g. startx --> #73836,
  /etc/X11/xdm/sys.xsession)
* Sun Mar 13 2005 sndirsch@suse.de
- NVIDIA_kernel-1.0-7167-1237815.diff.txt:
  This patch fixes a compile time error when building against Linux
  2.6.11-bk3 or later, configured without support for AGPGART (i.e.
  CONFIG_AGP unset).
* Fri Mar 11 2005 sndirsch@suse.de
- NVIDIA_kernel-1.0-7167-1233959.diff.txt:
  This patch fixes 2D/3D performance problems when using the Linux
  AGP driver, AGPGART; the built-in NVIDIA AGP driver, NvAGP, is
  not affected by this problem.
* Wed Mar  2 2005 sndirsch@suse.de
- updated nvidia driver to release 1.0-7167 (IA32 and AMD64)
* Mon Feb 28 2005 sndirsch@suse.de
- removed sux; replaced by a symlink to su in coreutils package
* Wed Feb 23 2005 mfabian@suse.de
- introduce the option "INPUT_METHOD=none" to avoid starting
  an input method.
* Tue Feb 22 2005 mfabian@suse.de
- avoid endless loop when ~/.xim is a symlink to /etc/X11/xim
  (thanks to Takashi Iwai <tiwai@suse.de>).
* Mon Feb 21 2005 mfabian@suse.de
- fix another stupid typo in /etc/X11/xim. Sorry.
* Mon Feb 21 2005 mfabian@suse.de
- fix typo in /etc/X11/xim.
* Mon Feb 21 2005 mfabian@suse.de
- add /var/adm/fillup-templates/sysconfig.language-xf86tools
  introducing the variable INPUT_METHOD to be able to change
  the system wide default input method easily.
* Mon Feb 21 2005 mfabian@suse.de
- add new versions of /etc/X11/xim and /etc/skel/.xim.template
  (has previously been in the xorg-x11 package).
* Mon Feb 14 2005 sndirsch@suse.de
- removed wmlist; obsoleted by the new WM desktop files in
  /usr/share/xsessions/
* Thu Feb 10 2005 sndirsch@suse.de
- updated nvidia driver to release 1.0-7163 (IA32 and AMD64)
  * obsoletes previous 1.0-6629 patches according to nVIDIA
* Tue Jan 25 2005 ro@suse.de
- added NVIDIA_kernel-1.0-6629-1201042.diff
* Sun Jan 16 2005 sndirsch@suse.de
- added latest patches for nvidia kernel module by zander ([X]
  required for kernel 2.6.10):
  * NVIDIA_kernel-1.0-6629-1155389.diff
  * NVIDIA_kernel-1.0-6629-1161283.diff
  * NVIDIA_kernel-1.0-6629-1165235.diff [X]
  * NVIDIA_kernel-1.0-6629-1171869.diff [X]
  * NVIDIA_kernel-1.0-6629-1175225.diff
  * NVIDIA_kernel-1.0-6629-1182399.diff
  * NVIDIA_kernel-1.0-6629-1189413.diff
  (german description on http://www.holarse.de/?news=308)
* Sat Nov 20 2004 sndirsch@suse.de
- NVIDIA_kernel-1.0-6629-1161283.diff.txt (Christian Zander@nVIDIA)
  * fixes a memory allocation issue
* Thu Nov 11 2004 sndirsch@suse.de
- don't use a rpm macro for km_nvidia version any longer
* Thu Nov 11 2004 sndirsch@suse.de
- updated nvidia driver to release 1.0-6629 (IA32 and AMD64)
- cleanup in link-nvidia-module
* Tue Sep 21 2004 werner@suse.de
- Make sux more secure (bugzilla #44605)
  * Use a temporary Xauthority file
  * If the last process of a sux terminates remove the temporary
    Xauthority file.
  * Always remove the temporary Xauthority file after one day.
* Thu Sep 16 2004 sndirsch@suse.de
- link-nvidia-module:
  * need to grep now for "NVIDIA X Driver" instead of
    "NVIDIA XFree86 Driver" before to detect the driver version,
    which is required for relinking the nvidia kernel module;
    credits go to root@suse.de (sent from f251), who send me this
    patch :-)
* Wed Sep  1 2004 sndirsch@suse.de
- fixed PreReq for /lib/modules/scripts/nvidia.sh (Bug #44553)
* Wed Aug 25 2004 sndirsch@suse.de
- removed %%pre; removing symlinks xf86config and xinit no longer
  makes sense; it even is completely wrong (Bug #44230)
* Mon Aug 23 2004 schwab@suse.de
- Fix specfile.
* Thu Aug 12 2004 sndirsch@suse.de
- updated to call-browser of SLES9/NLD; added desktop-launch
  symlink to it
* Thu Aug  5 2004 sndirsch@suse.de
- updated nvidia driver to release 1.0-6111 (IA32 and AMD64)
- updated nvidia installer to release 1.0.7
* Sat Jul 24 2004 sndirsch@suse.de
- removed XFree86-compat-libs.sh; no longer required as the shared
  libs (dga, misc, Xv) are now available again (changed upstream)
* Thu Jul  1 2004 sndirsch@suse.de
- updated nvidia kernel module to release 1.0-6106 (x86 and AMD64)
* Wed Jun  9 2004 sndirsch@suse.de
- call-browser:
  * Mozilla was used as browser even in KDE (Bug #41827)
* Thu May  6 2004 sndirsch@suse.de
- splitted off package fonts-config
* Wed May  5 2004 sndirsch@suse.de
- depmod needs to be called with "-a <kernel-version>"
* Wed May  5 2004 sndirsch@suse.de
- link-nvidia-module:
  * call "depmod -a" after relinking to make sure that nvidia kernel
    module will be known after rebooting the new kernel (Bug #39949)
* Fri Apr 16 2004 sndirsch@suse.de
- Bugzilla #39071: TTCap options were never generated, even when
  the option --ttcap or GENERATE_TTCAP_ENTRIES="yes"  in
  /etc/sysconfig/fonts-config was used.
* Tue Apr 13 2004 sndirsch@suse.de
- new improved 'sux' by Werner (Bug #38037)
* Tue Apr  6 2004 sndirsch@suse.de
- sysconfig.fonts-config
  * added missing Path + Description tags (Bug #38501)
* Mon Apr  5 2004 werner@suse.de
- Use getent within sux to avoid calls of yp tools (bug #38077)
* Wed Mar 31 2004 sndirsch@suse.de
- fonts-config:
  * Bugzilla #37569: "fonts missing?": If mkfontscale and/or
    mkfontdir failed or were not yet installed, remove the
    timestamp file to make sure the script tries again when the
    problem with mkfontscale and/or mkfontdir is fixed.
  * added new option --(no)ttcap, changed option --no-gs-fontmap
    to --(no)gs-fontmap.
  * read default values for these two options from
    /etc/sysconfig/fonts-config
  * don't use $freetype_module_supports_ttcap anymore, use the
    new option --(no)ttcap instead.
  * update man-page.
- SuSEconfig.fonts
  * remove "--no-gs-fontmap" option.
* Fri Mar 26 2004 sndirsch@suse.de
- fonts-config:
  * If mkfontscale and/or mkfontdir don't exist or fail, use only
    the handmade fonts.scale.* files or create empty fonts.scale
    fonts.dir files as a last fallback (Bug #37046).
* Wed Mar 24 2004 sndirsch@suse.de
- added sysconfig variables to configure if TTCap entries in
  fonts.dir and ghostscript fontmaps are generated by fonts-config
* Fri Mar 19 2004 sndirsch@suse.de
- removed .orig files to fix build
* Fri Mar 12 2004 sndirsch@suse.de
- fonts-config: call checkproc with absolute path (Bug #35708)
* Mon Mar  8 2004 sndirsch@suse.de
- udated to nvidia-installer release 1.0.6 (kernel 2.6 support
  out-of-the box)
* Mon Mar  1 2004 sndirsch@suse.de
- XFree86-compat-libs.sh:
  * shared libXxf86vm already provided now by XFree86-libs package
    (Bug #35188)
* Sun Feb 29 2004 agruen@suse.de
- Fix for x86_64.
* Fri Feb 27 2004 sndirsch@suse.de
- km_nvidia: new regparm-fix.diff
  * fixes kernel module build; gcc is more strict now in verifying
    prototype and function declaration
* Wed Feb 25 2004 sndirsch@suse.de
- regparm-fix.diff (Andreas Gruenbacher)
  * function definitions didn't match prototypes
* Tue Feb 17 2004 sndirsch@suse.de
- disabled cc-sanity-check to fix nvidia kernel module build for
  bigsmp kernel
* Mon Feb 16 2004 sndirsch@suse.de
- CheckHardware no longer a subpackage
* Sun Feb  8 2004 sndirsch@suse.de
- install precompiled kernel interface into
  /lib/modules/precompiled/<kernel-version>/nvidia/gfx
- removed Makefile.module files for kernel 2.4
- use original nv-kernel.o (binary-only) for compiling nvidia
  kernel module instead of dummy nv-kernel.o; therefore km_nvidia
  is no longer distributable (changed in PDB)
* Thu Jan 29 2004 sndirsch@suse.de
- (hopefully) fixed build with SMP kernel
* Mon Jan 26 2004 sndirsch@suse.de
- link-nvidia-modules:
  * remove /lib/modules/precompiled/<kernel-version> completely
    when called with option "--preun"
* Mon Jan 26 2004 sndirsch@suse.de
- fixed build with usermode kernel
* Sat Jan 24 2004 sndirsch@suse.de
- (hopefully) finally fixed build with kernel 2.6
* Sat Jan 24 2004 sndirsch@suse.de
- udpated nvidia kernel module sources (IA32) to release 1.0-5336
* Sat Jan 24 2004 sndirsch@suse.de
- (hopefully) fixed build with kernel 2.6
* Fri Jan 23 2004 sndirsch@suse.de
- cleanup for kernel 2.4 build
- improved kernel 2.6 build
* Fri Jan 23 2004 sndirsch@suse.de
- added precompiled kernel interface for nvidia kernel module for
  AMD64
* Thu Jan 22 2004 sndirsch@suse.de
- make use of mktemp in xf86debug script (Bug #34080)
* Wed Jan 14 2004 sndirsch@suse.de
- nvidia-installer-1.0.5-ko.diff:
  * 2.6 kernel modules use .ko extension
- Makefile.module/link-nvidia-module:
  * nvidia.mod.o isn't required for relinking 2.6 kernel module
- removed install-nvidia-driver
* Fri Jan  2 2004 sndirsch@suse.de
- updated kernel-2.6 patches; makes use of precompiled kernel
  interfaces possible
* Sun Dec 14 2003 sndirsch@suse.de
- updated nvidia installer to release 1.0.5
- udpated nvidia kernel module sources to release 1.0-5328
- fixed relinking of 2.6 nvidia kernel module
* Thu Dec  4 2003 sndirsch@suse.de
- GameChecker-031204.tar.bz2:
  * fixed build with new Qt
* Tue Dec  2 2003 sndirsch@suse.de
- new fonts-config:
  * add bw=0.5 option when necessary
  * convert old-style face option of freetype module to TTCap style
    option on recent versions of XFree86.
* Thu Nov 27 2003 sndirsch@suse.de
- new fonts-config:
  * use strict
  * the freetype module now supports TTCap since XFree86 >= 4.3.99,
    make use of this
* Wed Nov 12 2003 sndirsch@suse.de
- link-nvidia-module:
  * adjusted for kernel 2.6; modules now use the .ko extension
* Wed Nov 12 2003 sndirsch@suse.de
- km_nvidia: fixed build for kernel 2.6
* Thu Nov  6 2003 sndirsch@suse.de
- SuSEconfig.fonts:
  * added "/usr/X11R6/bin" to $PATH as "mkfontdir" now is a wrapper
    for "mkfontscale", which is located in "/usr/X11R6/bin"
* Thu Oct 30 2003 sndirsch@suse.de
- fixed build for non-i386 archs
* Thu Oct 30 2003 sndirsch@suse.de
- XFree86-compat-libs.sh:
  * script to replace package XFree86-compat-libs, which will be
    dropped for 9.1/SLES9 and later
* Sat Oct 25 2003 sndirsch@suse.de
- nvidia.sh: only call xsload if it exists (Bug #32480)
* Tue Oct 14 2003 sndirsch@suse.de
- CheckHardware:
  * replaced glXIsDirect call by using GLX API (Bug #31884)
  * removed glXIsDirect script
* Tue Sep 30 2003 sndirsch@suse.de
- CheckHardware:
  * new translation for it
* Mon Sep 29 2003 sndirsch@suse.de
- CheckHardware:
  * Check4SoundLibs/CheckFor3DLibs: fixed usage() output
* Fri Sep 26 2003 sndirsch@suse.de
- GameChecker-030926.tar.bz2:
  * better english texts
  * new translations for cs, es, ja, sk
* Wed Sep 24 2003 sndirsch@suse.de
- km_nvidia package / nvidia script:
  * provide nv-linux.o also in precompiled form, so the new nvidia
  installer (>= 1.0.4), i.e. driver (> 1.0-4496) can make use of it
  (Bug #31686)
* Sat Sep 20 2003 sndirsch@suse.de
- added mkprecompiled to filelist; required for generating
  precompiled nv-linux.o later (Bug #31459)
* Fri Sep 19 2003 sndirsch@suse.de
- install-nvidia-driver:
  * check for configured kernel sources no longer required
  * don't use override mechanism for nvidia module
* Fri Sep 19 2003 agruen@suse.de
- Move /lib/modules/`uname -r`/kernel/drivers/video/ \
  nv-linux.o-1.0-4496 to /lib/modules/scripts/nvidia/`uname -r`/.
  In the previous path, the object file was causing depmod errors.
  (Bug #31337)
* Thu Sep 18 2003 sndirsch@suse.de
- nvidia script:
  * removed depmod call
* Thu Sep 18 2003 sndirsch@suse.de
- nvidia script:
  * adjusted options to new calling conventions of k_* packages
- set km_nvidia version to 1.0.4496
* Wed Sep 17 2003 sndirsch@suse.de
- nvidia script:
  * adjusted options to calling conventions of k_* packages
- removed cylic requires to XFree86
* Tue Sep 16 2003 sndirsch@suse.de
- Makefile.module improved
- /usr/bin/link-nvidia-module --> /lib/modules/scripts/nvidia.sh
- nvidia.sh:
  * /lib/modules/nvidia/nv-kernel.o -->
    /lib/modules/scripts/nvidia/nv-kernel.o
* Mon Sep 15 2003 sndirsch@suse.de
- added km_nvidia package (nvidia kernel interface)
- added link-nvidia-module; script, which links nvidia kernel
  interface (nv-linux.o) and binary-only part (nv-kernel.o) to
  a new nvidia kernel module
* Fri Sep 12 2003 sndirsch@suse.de
- added Xwrapper symlink and xf86version script to work around still
  existing $HOME/.xserverrc files
- renamed nvidia-installer to tiny-nvidia-installer as it conflicts
  with official nvidia-installer
* Thu Sep 11 2003 sndirsch@suse.de
- install-nvidia-driver:
  * wrapper script for 'nvidia-installer' (Bug #30417)
* Thu Sep 11 2003 sndirsch@suse.de
- nvidia-installer-1.0.2.diff:
  * improved error/warning message when using nvidia-installer
    without "--update" or "--help" option (Bug #30417)
* Wed Sep 10 2003 sndirsch@suse.de
- call-browser:
  * fixed script; added MozillaFirebird (Bug #30400)
* Mon Sep  8 2003 sndirsch@suse.de
- GameChecker-030908.tar.bz2 (CheckHardware update):
  * fixed i18n support
  * added hungarian translation
* Fri Sep  5 2003 sndirsch@suse.de
- added requires for XFree86 (needs mkfontscale)
* Thu Sep  4 2003 sndirsch@suse.de
- epiphany replaced galeon
* Sat Aug  9 2003 sndirsch@suse.de
- updated nvidia installer (1.0.1 --> 1.0.2)
* Wed Jun 25 2003 hvogel@suse.de
- added fluxbox to wmlist
* Thu May 29 2003 sndirsch@suse.de
- fonts-config:
  * improve explanation of fc-cache in man-page
* Sun Apr 27 2003 sndirsch@suse.de
- added nvidia installer; useful for uninstalling cleanly nvidia
  driver during an update :-)
* Sun Apr 27 2003 sndirsch@suse.de
- added 'call-browser' tool
* Sun Apr 27 2003 sndirsch@suse.de
- fonts-config:
  * We have funny font names like "!y2kbug.ttf" "It wasn't me.ttf"
    "let'seat.ttf" now in free-ttf-fonts.rpm. Use some quoting to
    make ftdump $font work for such fonts.
* Wed Apr 23 2003 sndirsch@suse.de
- removed fonts.conf (now in new fontconfig package)
* Mon Apr 14 2003 sndirsch@suse.de
- sux:
  * fixed use of line option for head
* Mon Apr  7 2003 schwab@suse.de
- Fix quoting in kroot script.
* Mon Mar 31 2003 sndirsch@suse.de
- fixed PreReq and Requires
* Sun Mar 30 2003 sndirsch@suse.de
- removed XftConfig; no longer required with Xft2/XFree86 4.3.0
- removed fetchnvidiadrv; never useful
- removed fonts.html; no longer up-to-date
- removed xf86config/xf86version/xinit; no longer required as
  XFree86 3.x will be dropped
* Thu Mar 27 2003 sndirsch@suse.de
- added 'sux'; removed from XFree86 package
* Thu Mar 20 2003 sndirsch@suse.de
- fonts-config:
  check for fc-cache in two locations: /usr/bin/fc-cache
  and /usr/X11R6/bin/fc-cache to make the same script work
  on SuSE Linux 8.2 and SLEC.
* Tue Mar 11 2003 sndirsch@suse.de
- fonts-config:
  make it faster by ignoring all files which already have a dot in their
  name before checking with perl-File-MMagic whether it is a PostScript
  font. This is only useful for PostScript fonts which don't yet have a
  .pfa extension and these usually don't have dots anywhere in their
  name. Doing this check for all fonts just slows fonts-config down.
* Mon Mar 10 2003 mfabian@suse.de
- fonts-config:
  fc-cache creates non-empty fonts.cache-1 files for the
  CID-keyed fonts, but the CID-keyed fonts don't (yet?) work with
  Xft2. Force the fonts.cache-1 in the CIDFont directories to
  be empty.
* Mon Mar 10 2003 mfabian@suse.de
- Bug #22846: improve fonts.conf:
  * add <dir>/opt/kde3/share/fonts</dir>
  * prefer "Baekmuk Gulim" before "Baekmuk Dotum"
  * add "Fixed" to list of monospace faces to make "Fixed" fall
    back to some monospaced font as well if no "Fixed" is available
  * move mapping of PostScript families to TrueType "equivalents"
    above the include of ~/.fonts.conf.
  * add comment explaining how hinting can be turned off for
    CJK fonts (don't enable by default, I think CJK fonts look
    better with hinting)
  * add rule to use "Misc Console" (or "Misc Console Wide")
    instead of "console"
  * add rules to prefer bitmap fonts and embedded bitmaps in
    TrueType fonts which are off by default but can easily
    enabled in ~/.fonts.conf
  * add aliases for GB18030 fonts
  * prefer "AR PL SungtiL" and "AR PL Mingti2L Big5" for
    monospace over "AR PL KaitiM GB" and "AR PL KaitiM Big5"
* Mon Mar 10 2003 sndirsch@suse.de
- fonts-config:
  * .bdf fonts currently don't work with Xft2, add
  to @blacklist_globs to remove them from fonts.cache-1 files
* Sun Mar  9 2003 sndirsch@suse.de
- fonts-config:
  * check for existance of fonts.cache-1 befor trying to open it.
* Sat Mar  8 2003 sndirsch@suse.de
- fonts-config:
  * remove entries for files in @blacklist_globs from fonts.cache-1 as
    well because these broken fonts don't work with Xft2 either.
  * add "u003043t.gsf" and "u004006t.gsf" to @blacklist_globs
  * add "/opt/kde3/share/fonts" to directory list
  * check if files returned by glob() really exist.
    (glob ("foo") returns "foo", even if "foo" doesn't match, glob("foo*")
    returns nothing if "foo*" doesn't match).
* Mon Mar  3 2003 sndirsch@suse.de
- moved /etc/fonts/fonts.conf to this package (Bug #22846)
* Wed Feb 26 2003 sndirsch@suse.de
- the Hershey-Fonts from ghostscript-fonts-other.rpm have broken
  outlines and don't work with X11, add them to the blacklist
  (Bug #24272)
- removed fetchmsttfonts; should only be available via YOU
* Sat Feb 15 2003 sndirsch@suse.de
- fonts-config:
  * don't create symlinks .pfa -> .gsf.pfa
* Thu Feb 13 2003 sndirsch@suse.de
- fonts-config:
  * check if $DISPLAY is unset first to avoid "unitialized value in
    pattern match" warning message (thanks Bernhard Kaindl).
* Wed Feb 12 2003 sndirsch@suse.de
- added openbox to wmlist
* Mon Feb 10 2003 sndirsch@suse.de
- fonts-config:
  * Add "/usr/X11R6/lib/X11/fonts/encodings" to the list of font
    directories to precess to ensure that a valid encodings.dir is
    created there as well. luit looks for encodings.dir in that
    directory.
* Fri Feb  7 2003 sndirsch@suse.de
- fonts-config: create symlinks to .pfa only if the original font
  doesn't have the .pfa extension already.
* Mon Feb  3 2003 sndirsch@suse.de
- new fonts-config:
  * remove all entries for file names without extension from
    fonts.scale, files without extension won't work with X11
  * use perl module File::MMagic if availaible to create symlinks
    if PostScript fonts in pfa format without a file name extension
    are found (Foo.pfa -> Foo).
  * use the "fmly", "wght", and "slant" fields from the XLFD to
    generate better aliases for Qt into Fontmap.X11-auto
  * fix some typos in documentation
* Fri Jan 31 2003 sndirsch@suse.de
- new fonts-config:
  * generate an oblique entry if only italic is there and vice
    versa (Bug #23240)
* Wed Jan 29 2003 sndirsch@suse.de
- new fonts-config:
  * add extra alias if style equal 'Roman'
* Tue Jan 28 2003 sndirsch@suse.de
- new fonts-config:
  * generate some aliases in ghostscript fontmap
* Tue Jan 28 2003 sndirsch@suse.de
- added wget and cabextract to 'Requires:'
* Tue Jan 28 2003 sndirsch@suse.de
- Revival of fetchmsttfonts (Bug #23142)
* Mon Jan 27 2003 sndirsch@suse.de
- updated fonts-config/SuSEconfig.fonts scripts
  * don't generate ghostscript fontmap by default
* Mon Jan 27 2003 sndirsch@suse.de
- updated fonts-config script
  * added "--help" and "--version" option
  * creates now also a ghostscript fontmap for X11 fonts
    (/usr/share/ghostscript/*/lib/Fontmap.X11-auto)
  * unzip timestamps if required
* Fri Jan 24 2003 sndirsch@suse.de
- improved fonts-config script (also improved manual page)
* Thu Jan 23 2003 sndirsch@suse.de
- added SuSEconfig.fonts/fonts-config scripts
* Tue Jan  7 2003 sndirsch@suse.de
- improved kroot: initial VRoot setting is restored immediately
  after starting the specified root window program
* Fri Nov 22 2002 sndirsch@suse.de
- removed mkfontscale (now in XFree86 package)
* Wed Oct 30 2002 sndirsch@suse.de
- new script 'glXIsDirect' for verifying 3D
- latest CheckHardware sources (GameChecker-021030.tar.bz2)
  * integrated patches (GameChecker.diff, GameChecker2.diff)
  * verify 3D now with new script 'glXIsDirect'
- removed 'fetchnvidiadrv' from filelist
* Thu Oct 24 2002 sndirsch@suse.de
- added fetchnvidiadrv: script for downloading and installing
  nvidia drivers
* Thu Sep 12 2002 sndirsch@suse.de
- fixed dcop path in kroot (Bug #19582)
* Wed Sep 11 2002 sndirsch@suse.de
- new XftConfig:
  * added fallback fonts for cjk (Bug #19424)
* Thu Sep  5 2002 sndirsch@suse.de
- GameChecker2.diff:
  * fixed timing bug between app.exit() and execution of the base
    application (Bug #18935)
* Thu Aug 29 2002 sndirsch@suse.de
- fixed order in wmlist (Bug #18550)
- removed cabextract
* Thu Aug 29 2002 sndirsch@suse.de
- GameChecker.diff:
  * do not run program as child. The missing controlling terminal
    for backgrounded processes will not allow console based
    applications to work (Bug #16562)
* Tue Aug 27 2002 sndirsch@suse.de
- fixed numlock program: KeyRelease event was missing
* Fri Aug 16 2002 sndirsch@suse.de
- adjusted fetchmsttfonts: simply prints a message, that MS
  discontinued the Web fonts program
- removed fetchmsttfonts.sh
- removed w3m 'require'
* Tue Aug  6 2002 sndirsch@suse.de
- updated to GameChecker-020806.tar.bz2:
  * now also allows "--help" as command argument;
    example: CheckHardware /bin/ls --help
* Thu Aug  1 2002 sndirsch@suse.de
- added 'PreReq:'
* Wed Jul 10 2002 sndirsch@suse.de
- added 'gnome2' to wmlist
* Fri Jul  5 2002 sndirsch@suse.de
- added xinit and xf86config scripts; therefore switch2xf86-3x
  resp. switch2xf86-4 of package xf86 are no longer required
* Mon Jun 24 2002 sndirsch@suse.de
- added xwinswitch (xwin.tar.gz) by Ludwig Nussel <lnussel@suse.de>;
  useful for switching to the resolution, which is required by the
  selected application window
* Tue Jun 11 2002 sndirsch@suse.de
- added numlock program to toggle numlock state (on/off) (Bug #7391)
* Sun Jun  9 2002 olh@suse.de
- use suse_update_config, use lib64 on ppc64
* Sun May 19 2002 sndirsch@suse.de
- replaced ttmkfdir with mkfontscale in fetchmsttfonts
* Sat May 18 2002 sndirsch@suse.de
- added mkfontscale; likely will replace ttmkfdir
* Wed May 15 2002 sndirsch@suse.de
- updated to release 020515; integrates the patches:
  * GameChecker-lib64.patch
  * GameChecker-xauth.diff
  * GameChecker.diff
  * GameChecker2.diff
- enabled build of CheckHardware for s390/s390x (again)
- splitted package in xf86tools/CheckHardware
* Tue May  7 2002 meissner@suse.de
- %%_lib fixes
* Sun Mar 31 2002 sndirsch@suse.de
- disabled build of 'CheckHardware' for s390/s390x; S/390 does not
  have any sound or 3D capabilities
* Thu Mar 21 2002 sndirsch@suse.de
- GameChecker-xauth.diff:
  * fixed xauth problem: If CheckHardware create an QApplication object
  this is handled as X11 client if this client replaces itself with
  a new client it may happen that the parent client still exist under
  the same authorization than the parent which is not allowed in terms
  of security. We will exit the application object in front of the execvp
  call and will fork() a new process for the calling application to be
  sure not to run into an access problem.
* Mon Mar 18 2002 sndirsch@suse.de
- GameChecker2.diff
  * fixed return value handling from system() call
  * now also commands without full specified path are allowed for
    generic 'GameWrapper'
  * allow program names with '-' sign in it
  * fixed spacing of button texts
  * adapt gettext keys to currently used en_US translation
  * adapt .po files for all languages according to the new gettext keys
  * fixed segfault while allocating memory for baseName
  * some cleanups
* Sun Mar 17 2002 sndirsch@suse.de
- GameChecker.diff:
  * fixes option parsing of 'CheckHardware'
  * better texts for warnings of 'CheckHardware'
* Sat Mar 16 2002 sndirsch@suse.de
- added Wrapper for starting games (checks for sound and 3D)
* Wed Mar 13 2002 sndirsch@suse.de
- added including of greek XftConfig (located in package xfntgreek)
  to XftConfig
* Thu Feb 28 2002 sndirsch@suse.de
- fixed Bug #14104
  * replaced lynx with w3m
  * added "Requires: w3m"
* Fri Feb 15 2002 sndirsch@suse.de
- removed aliases for "Lucidux Mono/Sans/Serif" (trademark issue)
* Wed Feb 13 2002 sndirsch@suse.de
- give the user a note to exit from less with 'q'
* Thu Feb  7 2002 sndirsch@suse.de
- updated to cabextract 0.5
- adjusted params of cabextract in fetchmsttfonts ("-v" is now "-l")
- use now SuSEconfig in fetchmsttfonts to create fonts.scale/fonts.dir
  files
* Wed Jan 30 2002 sndirsch@suse.de
- added fallbacks if MS fonts are not installed
- added font test webpage
* Sat Jan 26 2002 sndirsch@suse.de
- XftConfig:
  * added fallback to Luxi Sans/Serif/Mono fonts, if MS fonts are
    not available
  * added rules for sub-pixeling hinting and excluded pt range for
    antialiasing (both rules are commented out)
* Wed Jan 23 2002 sndirsch@suse.de
- removed files for latvian support (never really worked); should
  be done via KDE Control center for the future
* Thu Jan 17 2002 sndirsch@suse.de
- added path to ghostscript Type1 fonts (URW)
* Tue Jan  8 2002 sndirsch@suse.de
- added fallback to "Luxi Mono" for monospaced font requests;
  fixes "konsole" AA font problem (made it unusable), if no MS TT
  fonts are installed
* Wed Dec 19 2001 sndirsch@suse.de
- fetchmsttfonts now creates a fonts.scale.msttfonts file only for
  the TTF files, which are fetched; no duplicate entries any more
  in fonts.scale
* Thu Dec 13 2001 sndirsch@suse.de
- better kroot script: vroot will only be false when kdesktop is
  running and when VRoot was not set already. We don't need to do
  anything if either KDesktop isn't running or VRoot was set
  already.
* Wed Dec 12 2001 sndirsch@suse.de
- added wrapper (kroot) for starting X11 programs, which make use
  of root window feature, also with KDE 2
* Tue Nov 20 2001 mfabian@suse.de
- sawmill -> sawfish in wmlist
* Fri Nov 16 2001 sndirsch@suse.de
- added XftConfig; removed from package xf86 to be able to update
  it easier
* Wed Sep  5 2001 sndirsch@suse.de
- removed options "--passive" and "--user-agent" in $WGET_OPTIONS
- lynx is now used for testing of existing EULA instead of wget
  (wget can't fetch EULA any more!)
* Tue Jul 31 2001 sndirsch@suse.de
- replaced 'xfwm' with 'XFce' in 'wmlist' (change request by
  nadvornik@suse.cz)
* Fri Jul 20 2001 sndirsch@suse.de
- moved 'wmlist' script from package susewm to package xf86tools
* Wed Jul 18 2001 cstein@suse.de
- added 'xsplash' to wmlist and changed year in file header to 2001
* Fri Jun 22 2001 sndirsch@suse.de
- better error handling in latvian (un)install scripts
* Tue Jun 19 2001 sndirsch@suse.de
- added fetchmsttfonts.sh for KDE menu
* Mon Jun 18 2001 sndirsch@suse.de
- fetchmsttfonts: print error message if there are problems with
  fetching archives
- added keyboard layout support for latvian:
  * xkb layout files
  * addition to compose table
  * install/uninstall skript for enabling/disabling latvian support
    (patches XF86Config + Compose table)
  * README.SuSE
* Wed May 16 2001 sndirsch@suse.de
- rewritten fetchmsttfonts to use cabextract instead of unzip, so
  that the more recent TT Fonts for Windows 9x/NT/2000 can be used
- added cabextract tool, required for new fetchmsttfonts
* Fri Apr  6 2001 sndirsch@suse.de
- rewritten xf86version ("X -version" is now used to get xf86 version)
* Fri Mar 30 2001 sndirsch@suse.de
- created package
