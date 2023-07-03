Name:		svgalib
Version:	1.9.25
Release:	29
Summary:	Low-level fullscreen SVGA graphics library
License:	Public Domain
URL:		https://www.svgalib.org/
Source0:	https://www.arava.co.il/matan/svgalib/svgalib-%{version}.tar.gz
Source1:	svgalib-todo
Patch0:		svgalib-1.9.21-makefiles.patch
Patch1:		svgalib-1.4.3-fhs.patch
Patch2:		svgalib-1.9.21-demos.patch
Patch3:		svgalib-1.9.21-cfg.patch
Patch4:		svgalib-1.9.25-kernel-2.6.26.patch
Patch5:		svgalib-1.9.25-round_gtf_gtfcalc_c.patch
Patch6:		svgalib-1.9.25-vga_getmodenumber.patch
Patch7:		svgalib-1.9.25-quickmath-h-redefinitions.patch
#Exclusivearch:	%{ix86} x86_64
BuildRequires:  make
BuildRequires:  gcc

%description
The svgalib package provides the SVGAlib low-level graphics library
for Linux.  SVGAlib is a library which allows applications to use full
screen graphics on a variety of hardware platforms. Some games and
utilities use SVGAlib for their graphics. For details on
supported chipsets, see man 7 svgalib (when svgalib is installed).

%package devel
Summary:	Development tools for the SVGAlib graphics library
Requires:	%{name} = %{version}-%{release}
Provides:	libvga-devel = %{version}-%{release}

%description devel
The svgalib-devel package contains the libraries and header files
needed to build programs which will use the SVGAlib low-level graphics
library.

%prep
%setup -q
%patch0 -p1 -b .makefiles
%patch1 -p1 -b .fhs
%patch2 -p1
%patch3 -p1 -b .defaultcfg
%patch4 -p1
%patch5 -p1 -b .round_gtf_gtfcalc_c
%patch6 -p1
%patch7 -p1

#the testlinear demo needs svgalib's internal libvga header, so copy it to the
#demo dir
cp src/libvga.h demos

%build
#%{?_smp_mflags} doesn't work on x86_64 chances are it will fail on
#some i386 machines too.
make OPTIMIZE="$RPM_OPT_FLAGS -Wno-pointer-sign" LDFLAGS= \
  prefix=%{_prefix} \
  NO_HELPER=y \
  INCLUDE_ET4000_DRIVER=y \
  INCLUDE_OAK_DRIVER=y \
  INCLUDE_MACH32_DRIVER=y \
  INCLUDE_ET3000_DRIVER=y \
  INCLUDE_GVGA6400_DRIVER=y \
  INCLUDE_ATI_DRIVER=y \
  INCLUDE_G450C2_DRIVER=y \
  INCLUDE_ET4000_DRIVER_TEST=y \
  INCLUDE_FBDEV_DRIVER_TEST=y \
  INCLUDE_VESA_DRIVER_TEST=y \
  shared
cd utils
make OPTIMIZE="$RPM_OPT_FLAGS -Wno-pointer-sign" LDFLAGS= \
  prefix=%{_prefix}
cd ..
cd threeDKit
make OPTIMIZE="$RPM_OPT_FLAGS -Wno-pointer-sign -I../gl" LDFLAGS= \
  prefix=%{_prefix} lib3dkit.so.%{version}
cd ..

%install
mkdir -p $RPM_BUILD_ROOT/etc/vga
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
make \
  TOPDIR=$RPM_BUILD_ROOT \
  prefix=$RPM_BUILD_ROOT/%{_prefix} \
  mandir=$RPM_BUILD_ROOT/%{_mandir} \
  sharedlibdir=$RPM_BUILD_ROOT/%{_libdir} \
  NO_HELPER=y \
  MANFORMAT=compressed \
  "INSTALL_PROGRAM=install -p -m 755" \
  "INSTALL_SCRIPT=install -p -m 755" \
  "INSTALL_SHLIB=install -p -m 755" \
  "INSTALL_DATA=install -p -m 644" \
  install
ln -s libvga.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/libvga.so.1
ln -s libvgagl.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/libvgagl.so.1
ln -s lib3dkit.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/lib3dkit.so.1
#for %ghost
touch $RPM_BUILD_ROOT/etc/vga/fontdata
touch $RPM_BUILD_ROOT/etc/vga/textregs

%files
%doc doc/CHANGES doc/README.joystick doc/README.keymap lrmi-0.6m/README
%doc doc/README.multi-monitor doc/README.vesa doc/TODO doc/dual-head-howto
%dir %{_sysconfdir}/vga/
%config(noreplace) %{_sysconfdir}/vga/dvorak-us.keymap
%config(noreplace) %{_sysconfdir}/vga/libvga.config
%config(noreplace) %{_sysconfdir}/vga/libvga.et4000
%config(noreplace) %{_sysconfdir}/vga/null.keymap
%ghost %{_sysconfdir}/vga/fontdata
%ghost %{_sysconfdir}/vga/textregs
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man[^3]/*

%files devel
%doc demos doc/DESIGN doc/Driver-programming-HOWTO doc/README.patching
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*

%changelog
* Sun Apr 2 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.25
- Rebuilt for Feodra
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.25-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.25-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.25-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.25-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.25-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.25-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.25-23
- Escape macros in %%changelog
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.25-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.25-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.25-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.25-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Mon Aug 03 2015 Jaromir Capik <jcapik@redhat.com> - 1.9.25-18
- Fixing FTBFS caused by quickmath.h function redefinitions (#1240045)
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.25-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.25-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.25-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Thu Sep 19 2013 Jaromir Capik <jcapik@redhat.com> - 1.9.25-14
- Fixing segmentation faults in vga_getmodenumber (#787147)
- Cleaning the spec
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.25-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.25-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Wed Aug 05 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1.9.25-8
- Fixed FTBFS #511561 with svgalib-1.9.25-round_gtf_gtfcalc_c.patch
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Sat May 31 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9.25-5
- Fix building with 2.6.26 kernel headers
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9.25-4
- Autorebuild for GCC 4.3
* Tue Aug 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9.25-3
- FE6 Rebuild
* Mon Jul 17 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9.25-2
- Don't have a different defaultcfg on i386 vs x86_64, having the same
  defaultcfg makes paralel installs possible, add notes about certain settings
  being only valid on i386 to the defaultcfg and patch the config file parser
  to ignore i386 only configfile settings on non i386.
* Sat Jul 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9.25-1
- New upstream release 1.9.25
- Drop ancient Provides: libvga
* Mon Feb 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9.24-2
- Bump release and rebuild for new gcc4.1 and glibc.
- add %%{?dist} for consistency with my other packages
* Thu Jan  5 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9.24-1
- New upstream version, drop merged patches.
* Tue Aug 16 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9.21-5
- Merge with upstream, drop merged patches, fix dark vga modes on radeon.
* Sun Aug 7 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9.21-4
- Add patch 9 which fixes 320x200x256(mode 5) on atleast radeons and probably
  others too.
* Fri Aug 5 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9.21-3
- Add patch 8 to try to fix compilation on ppc.
- PPC has issues with the use of iopl ioperm inb and outb
  functions, upstream has svgalib working on PPC afaik?
- Disabling PPC builds for now, will look into this together with upstream.
* Wed Aug 3 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9.21-2
- I've been working with upstream to get most patches intergrated, so
  most patches are gone now.
- Reviewed and fixed the entire source tree for 64 bit cleanness.
- While working with upstream I've been busy fixing some bugs and improving
  security in nohelper mode. From now on /dev/mem gets closed immediatly
  after getchipset (vga_init) has been called. Lots of work has been done
  to keep all functionality and api & abi compatibility intact, even
  while /dev/mem is no longer available. This does however mean that
  in nohelper mode runinbackground and emulated paging (ppc or secondary card)
  are only available on 2.6 kernels now.
- Made nohelper mode configurable from the configfile, if the user wants he
  can build the kernel module from the svgalib-srcs and use this with the RPM
  packaged libs, all this has not been released by upstream yet. The merged
  part of all this is in patch 0, patch 4 and 5 contain work which still needs
  to be merged.
- Patch6: set some sane default in the configfile.
- Patch7: remove options not available on non-i386 from the configfile when
  building for non-i386.
* Fri Jul 1 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9.21-1
- Yet another attempt at getting svgalib into Fedora Extras (formerly .us).
- Upstream has reintroduced suid root use in 1.9.20 as an alternative to the
  helper-kernel-module. This allows us to build a sane (kernel module free)
  package of the 1.9 (devel) versions. The 1.4 (stable) versions haven't
  seen an update in ages and don't support most modern cards -> Update to the
  latest upstream devel release 1.9.21 .
- Split the Debian patches in some sane parts, redo against 1.9.21 where
  nescesarry.
- Don't patch Makefile.cfg instead just pass the nescesarry options to make
  in %%build and %%install.
- Reintroduce %%_smp_mflags, this seems to work fine with 1.9.21 .
* Tue Jul 27 2004 Hans de Goede <j.w.r.degoede@hhs.nl>
0:1.4.5-0.fdr.6
- Removed unnescesarry and wrong Requires(%%post,%%postun)
- Fixed ExclusiveArch
- Removed the Packager tag
- Removed %%_smp_mflags, this doesn't work
- Modified patch2 so that only the real manpages and not the
  patch backups get gzipped and installed, renamed patch
  to svgalib-1.4.3-man to reflect this change.
- Removed 0-INSTALL from docs
- Don't use README.* this also puts patch backups in the docs
- Moved README.patches from svgalib to svgalib-devel
- Removed unnescesarry creation of dirs in %%install, the Makefile creates
  most for us.
- Removed %%preun removing /etc/vga/fontdate and /etc/vga/textregs,
  instead made them owned by svgalib using %%ghost
- Made files in /etc/vga %%config(noreplace)
* Fri Jul 16 2004 Hans de Goede <j.w.r.degoede@hhs.nl>
0:1.4.5-0.fdr.5
- new RPM on base of the original RH 6.2 SRPM, all the patches from the
  latest debian pkg, and parts from the first fedora releases by Andreas.
* Tue Sep 02 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:1.4.5-0.fdr.4
- Added severn compile fix provided by Michael Schwendt (#444 #6)
* Sat Aug 30 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:1.4.3-0.fdr.3
- Fixed stuff from #444 #4 :)
* Sun Jul 13 2003 Andreas Bierfert (awjb) <andreas.bierfert[AT]awbsworld.de>
0:1.4.3-0.fdr.2
- Fixed minor rpmlint warnings
* Tue Jul 01 2003 Andreas Bierfert (awjb) <andreas.bierfert[AT]awbsworld.de>
0:1.4.3-0.fdr.1
- Initial RPM release.
* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages
* Tue Jan 18 2000 Bill Nottingham <notting@redhat.com>
- update to 1.4.1 final
* Wed Dec 08 1999 Michael Maher <mike@lastfoot.com>
- built pre release of 1.4.1
* Mon Sep 13 1999 Bill Nottingham <notting@redhat.com>
- strip binaries
* Fri Aug 27 1999 Bill Nottingham <notting@redhat.com>
- update to 1.4.0, sort out patches
* Sun May 16 1999 Jeff Johnson <jbj@redhat.com>
- don't remove old binaries (not from BUILD_ROOT!) during install (#2735).
* Wed Mar 31 1999 Preston Brown <pbrown@redhat.com>
- moved temporary svgalib files to /var/lib/svgalib
* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)
* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- verify dumpreg is not setuid (problem #760)
- specfile fiddles
* Thu Jul 30 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.3.0
- security patch
* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel package moved to Development/Libraries
* Mon Apr 06 1998 Erik Troan <ewt@redhat.com>
- updated to svgalib 1.2.13
- uses a build root
* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- removed Mach64 from configuration, as the driver does not work
* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups
