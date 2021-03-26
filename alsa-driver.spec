%define kver %(uname -r)

Summary: The Advanced Linux Sound Architecture (ALSA) base files
Name: alsa-driver
Version: 1.0.24
Release: 1
License: GPL
Group: System Environment/Base
Source0: ftp://ftp.alsa-project.org/pub/driver/%{name}-%{version}.tar.bz2
Patch1: alsa-driver-1.0.14rc3-log2.patch
Patch2: idt-blue-linein.patch
Patch5: strict_strtoul.patch
Patch99: http://www.linuxant.com/alsa-driver/alsa-driver-1.0.19-3.patch
URL: http://www.alsa-project.org/

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system. ALSA has the following
significant features: Efficient support for all types of audio interfaces,
from consumer soundcards to professional multichannel audio interfaces,
fully modularized sound drivers, SMP and thread-safe design, user space
library (alsa-lib) to simplify application programming and provide higher
level functionality as well as support for the older OSS API, providing
binary compatibility for most OSS programs.

This package contains the ALSA /dev entries and basic development files.

%package devel
Summary: Kernel header files from the ALSA driver
Group: System Environment/Base

%description devel
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes header files for developing against the ALSA
driver.

%package kmod
Summary: The Advanced Linux Sound Architecture (ALSA) kernel drivers
Group: System Environment/Kernel
%{?_with_devices:Requires: alsa-devices}
%{!?_with_devices:Obsoletes: alsa-devices}

%description kmod
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

%prep
%setup -q
echo %latest_kernel
echo %kernel_version

%patch1 -p1 -b .log2
##%patch2 -p1 -b .blue
##%patch5 -p1 -b .strict_strtoul
##%patch99 -p1
grep bool\; /lib/modules/%{kver}/build/include/linux/types.h > /dev/null \
  && perl -pi -e's,(typedef _Bool bool;),/* $1 */,' include/adriver.h
perl -pi -e's|KERNEL_VERSION\(2, 6, 19\)|KERNEL_VERSION(2, 6, 9)|' usb/usbcompat.h
perl -pi -e's|KERNEL_VERSION\(2, 6, 21\)|KERNEL_VERSION(2, 6, 9)|' usb/usbcompat.h

grep -rl '#include <linux/config.h>' . | xargs perl -pi -e's,#include <linux/config.h>,#include <linux/autoconf.h>,'

%build
%configure \
	--with-kernel=/lib/modules/%{kver}/build \
	--with-moddir=/lib/modules/%{kver}/updates/sound \
	--with-redhat=yes \
	--with-isapnp=yes \
	--with-sequencer=yes \
	--with-oss=yes \
	--with-cards=all

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}
make install-modules DESTDIR=%{buildroot}


%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
rm -rf %{buildroot}

%files kmod
%defattr(-,root,root,-)
/lib/modules/%{kver}/updates/sound

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Feb 09 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.24-1.ossii
- Rebuild for OSSII

* Fri Feb 13 2009 Paulo Roma <roma@lcg.ufrj.br> - 1.0.19-77
- Patched for having input in the blue jack.

* Wed Jan 21 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.19-75
- Update to 1.0.19.

* Sat Dec 27 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.18a.snap-73
- Update to snapshot version to overcome build prolems with latest kernels.

* Tue Nov 25 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.18a-72
- Update to 1.0.18a.

* Sun Nov  2 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.18-71
- Update to 1.0.18.

* Sun Jul 20 2008 Paulo Roma <roma@lcg.ufrj.br> - 1.0.17-69
- Patched for building on RHEL5 (patches 4 and 5).

* Fri Jul 18 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.17-68
- Update to 1.0.17.

* Tue Jul  1 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.17-67_rc3
- Update to 1.0.17rc3.

* Sat Mar 15 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.17-66_hg20080315
- Update to hg20080315.

* Sat Feb 16 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.16-65
- Update to 1.0.16.
- RHEL5 fix no longer needed.

* Sat Dec 29 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.15-64
- Fix build on latest RHEL5 kernels.

* Fri Nov 30 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.15-63
- Fix build on RHEL3 (Adam Yellen <adam@videofurnace.com>).

* Tue Oct 16 2007 Paulo Roma <roma@lcg.ufrj.br> - 1.0.15-62
- Update to 1.0.15.

* Sat Sep 29 2007 Paulo Roma <roma@lcg.ufrj.br> - 1.0.15-61_rc3
- Update to 1.0.15rc3.

* Thu Sep 13 2007 Paulo Roma <roma@lcg.ufrj.br> - 1.0.15-61_rc2
- Update to 1.0.15rc2.

* Tue Jun  5 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.14-61
- Update to 1.0.14 final.

* Mon May 14 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.14-60_rc4
- Update to 1.0.14rc4.

* Wed Mar  7 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.14-58_rc3
- Update to 1.0.14rc3.

* Sun Jan 21 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.14-57_rc2
- Update to 1.0.14rc2.

* Mon Oct  2 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.13-55
- Update to 1.0.13.

* Thu Aug 24 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.12-54
- Update to 1.0.12 final.

* Thu Aug 17 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.12-53_rc3
- Update to 1.0.12rc3.

* Tue Aug  8 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.12rc2.

* Sat Jul  1 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.12rc1.

* Tue May  2 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.11 final.

* Tue Apr 11 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.11rc5.

* Tue Apr  4 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.11rc4.

* Fri Nov 18 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.10 final.

* Sun Nov 13 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.10rc3.

* Mon Sep 19 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.9b.

* Tue May 31 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Fix build for 2.4 kernels (alsa bug 0001135).
- Temporarily adjust versioning to Red Hat for 1.0.9.

* Fri May 27 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.9 final.

* Wed May 25 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.9rc4a.

* Fri Jan 14 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.8.

* Tue Nov 16 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.7.

* Mon Aug 16 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.6a.

* Wed Jun  2 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.5a.

* Sat May 29 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.5.

* Sun Apr  4 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.4.

* Tue Mar  9 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.3.

* Tue Jan 27 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.2.

* Wed Jan 21 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Add devices to kmdls (reported by Edward Rudd).

* Fri Jan  9 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.1.

* Wed Dec  3 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.0rc1.

* Wed Nov 26 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to pre3.

* Sat Nov 22 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.0pre2.

* Thu Oct 23 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.9.8.

* Mon Oct 13 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.9.7b.

* Tue Oct  7 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.9.7a.

* Sun Aug  3 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.6.

* Wed Jul  9 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.5.

* Thu Jun 12 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.4.
- Removed workqueue workaround, as it's taken care of by configure.
- Changed $CONSOLE to $ALLWRITE in the makedev script...

* Wed Jun 11 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Provide virtual package for compatibility to freshrpms.net.

* Sun May 25 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.3c.
- Major changes in the makedev.d entry for the new devices.

* Fri May  2 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.3a.

* Thu May  1 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.3.

* Wed Mar 19 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.2.

* Mon Mar 17 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Removed now unneeded vmalloc patch.

* Wed Mar 12 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Introduce %%{error:...} directives.

* Tue Mar 11 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.0rc8d.
- Update to 0.9.1!

* Tue Mar 11 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- New kernel module setup supporting more flavours of kernels.

* Mon Mar 10 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Removed requirements for kernel-source rpm.
- Introduced kmdl_kernelsrcdir variable and command line option.
- Cosmetic changes to descriptions.

* Mon Mar  3 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.0rc8.
- Removed CFLAGS patch, use new MODFLAGS instead.

* Wed Feb 12 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Merge fixes for /sbin/depmod dep and its post/postun scripts.
- Add CFLAGS patch and changes to rebuild for any arch with just the
  right kernel-source installed.
- Minor cleanups inherent to the above.

* Mon Feb  3 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.0rc7.
- Added ability to recompile against non-running kernel.

* Mon Nov 16 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.0rc6.

* Fri Oct 25 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Silent the %%post and %%postun scriplets to avoid unresolved symbol
  warnings during upgrades.

* Wed Oct 23 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.0rc4, then rc5.

* Tue Oct  1 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Removed the dependency about alsa-driver in alsa-kernel to fix apt problems.

* Sun Sep 29 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added -smp to alsa-kernel packages for SMP systems (needs testing).

* Fri Sep 27 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Moved rpmbuild --without options to the description.
- Rebuild for Red Hat Linux 8.0.
- Fixed the /sbin/depmod -a that was run for the wrong sub-package, doh!

* Tue Sep 17 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Fixed yet another (last?) bug on SMP systems.

* Sun Sep  8 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Fixed build on SMP systems, thanks to Chris Ckloiber.

* Thu Aug 29 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Fixed extra files problem with rpm 4.1.
- Added support for disabling isapnp, sequencer and oss.
- Added support to easily modify to build only drivers for specific cards.
- Simplified the device list creation ("alsa" alias in the makedev.d entry).
- Fixed reversed links in the /dev entries.

* Wed Aug 28 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Fix the makedev file that didn't like the CVS tag.
- New sub-package -kernel with only the kernel module (to have multiple
  installations of it easily).
- Fixed kernel arch detection by invoking rpm to query kernel package ;-)

* Tue Aug 27 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Spec file rewrite.
- Added makedev.d stuff to have device files included cleanly.
