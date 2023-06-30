Summary:	An image loading and rendering library for X11R6
Name:		imlib
Epoch:		1
Version:	1.9.15
Release:	39
License:	LGPLv2+
Source0:	https://ftp.gnome.org/pub/GNOME/sources/imlib/1.9/imlib-%{version}.tar.bz2
Source2:	local-hack-gmodule.tar.gz
Patch0:		imlib-1.9.15-autotools-rebase.patch.bz2
Patch1:		imlib-1.9.13-sec2.patch
Patch2:		imlib-1.9.15-bpp16-CVE-2007-3568.patch
Patch3:		imlib-1.9.10-cppflags.patch
Patch4:		imlib-1.9.15-gmodulehack.patch
Patch6:		imlib-1.9.13-underquoted.patch
Patch8:		imlib-1.9.15-lib-bloat.patch
Patch9:		imlib-1.9.15-multilib-config.patch
Patch10:	imlib-1.9.15-check-for-shm-pixmaps.patch
Patch11:	imlib-1.9.15-libpng15.patch
Patch12:	imlib-1.9.15-aarch64.patch
Patch13:	imlib-1.9.15-giflib5.patch
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	giflib-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	libpng-devel >= 1.2.2
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libX11-devel
BuildRequires:	libXt-devel
BuildRequires:	make
BuildRequires:	sed
BuildRequires:	tar
BuildRequires:	zlib-devel
Obsoletes:	imlib-cfgeditor < %{version}-%{release}, Imlib < %{version}-%{release}
Provides:	imlib-cfgeditor = %{version}-%{release}, Imlib = %{version}-%{release}

%description
Imlib is a display depth independent image loading and rendering library.
Imlib is designed to simplify and speed up the process of loading images and
obtaining X Window System drawables. Imlib provides many simple manipulation
routines which can be used for common operations.

The imlib package also contains the imlib_config program, which you can use to
configure the Imlib image loading and rendering library. Imlib_config can be
used to control how Imlib uses color and handles gamma corrections, etc.

%package devel
Summary:	Development tools for Imlib applications
Requires:	imlib%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	giflib-devel%{?_isa}
Requires:	glib-devel%{?_isa}
Requires:	gtk+-devel%{?_isa}
Requires:	libjpeg-devel%{?_isa}
Requires:	libtiff-devel%{?_isa}
Requires:	libX11-devel%{?_isa}
Requires:	libXt-devel%{?_isa}
Requires:	zlib-devel%{?_isa}
# From Fedora 14, %%{_datadir}/aclocal is included in the filesystem package
%if (0%{?rhel} && 0%{?rhel} <= 6) || (0%{?fedora} && 0%{?fedora} <= 13)
Requires:	%{_datadir}/aclocal
%endif

%description devel
The header files, static libraries and documentation needed for
developing Imlib applications. Imlib is an image loading and
rendering library for X11R6.

%prep
%setup -q

## Rebase autotools to EL-5 versions
%patch0 -p1

## CVE-2004-1025, CVE-2004-1026 (integer/buffer overflows) (#235416)
%patch1 -p1 -b .sec2

## CVE-2007-3568 (DoS via a BMP image with a Bits Per Page of 0) (#426091)
%patch2 -p0 -b .bpp16

## -I/usr/include is never necessary
%patch3 -p1 -b .cppflags

## Hook our gmodule hack for libpng into the build
%patch4 -p1 -b .gmodulehack

## Fix underquoted m4 definitions
%patch6 -p1 -b .underquoted

## Don't link against libraries unless we use their symbols
%patch8 -p1 -b .lib-bloat

## Make imlib-config multilib-compatible
%patch9 -p1 -b .multilib

## Check whether the MIT SHM extension supports shared pixmaps
## before trying to use them (#357241)
%patch10 -p1 -b .shmpixmaps

## Patch from gentoo for building against libpng 1.5
%patch11 -b .libpng15

## Add aarch64 support (#925585)
%patch12 -b .aarch64

## Fix build with giflib version 5
%patch13 -b .giflib5

## Local gmodule hack to support building with libpng rather than libpng10
(cd gdk_imlib && tar zxf %{SOURCE2})
sed -i -e	's/gmodule.h/gmodule-local.h/g;
		 s/g_module/local_hack_g_module/g;
		 s/GModule/LocalHackGModule/g;
		 s/G_MODULE/LOCAL_HACK_G_MODULE/g' \
	gdk_imlib/modules.c
sed -i -e 's/-static//g' \
	gdk_imlib/local-hack-gmodule/Makefile

## Change soname to reflect new libpng
sed -i -e 's/10:15:9/11:0:0/g' Imlib/Makefile*

%build
%configure --disable-static

## Remove -L%%{_libdir} from imlib-config if present;
## it's redundant and breaks multilib compatibility
sed -i -e 's,-L%{_libdir} ,,g' imlib-config

## Kill bogus RPATHs
sed -i 's|^sys_lib_dlsearch_path_spec="/lib /usr/lib|sys_lib_dlsearch_path_spec="/%{_lib} %{_libdir}|' libtool

## Build local gmodule hack
tagname=CC make -C gdk_imlib/local-hack-gmodule LIBTOOL=$(pwd)/libtool
cp gdk_imlib/local-hack-gmodule/gmodule-local.h gdk_imlib/

## Avoid unnecessary library linkage in libgdk_imlib
GX_LIBS=$(gtk-config --libs | sed -e 's/-lgtk //; s/-lgmodule //; s/-lXi //')

## Note: parallel build doesn't work reliably
make GX_LIBS="${GX_LIBS}"

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

## Don't package libtool archives
rm -f %{buildroot}%{_libdir}/*.la

%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} <= 27)
# ldconfig scriptlets replaced by RPM File Triggers from Fedora 28
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%if 0%{?_licensedir:1}
%license COPYING.LIB
%else
%doc COPYING.LIB
%endif
%doc README AUTHORS ChangeLog
%config(noreplace) %{_sysconfdir}/im_palette-small.pal
%config(noreplace) %{_sysconfdir}/im_palette-tiny.pal
%config(noreplace) %{_sysconfdir}/im_palette.pal
%config(noreplace) %{_sysconfdir}/imrc
%{_bindir}/imlib_config
%{_libdir}/libImlib.so.11
%{_libdir}/libImlib.so.11.*
%{_libdir}/libgdk_imlib.so.1
%{_libdir}/libgdk_imlib.so.1.*
%{_libdir}/libimlib-bmp.so
%{_libdir}/libimlib-gif.so
%{_libdir}/libimlib-jpeg.so
%{_libdir}/libimlib-png.so
%{_libdir}/libimlib-ppm.so
%{_libdir}/libimlib-ps.so
%{_libdir}/libimlib-tiff.so
%{_libdir}/libimlib-xpm.so

%files devel
%doc doc/*.gif doc/*.html
%{_bindir}/imlib-config
%{_datadir}/aclocal/imlib.m4
%{_includedir}/*.h
%{_libdir}/libImlib.so
%{_libdir}/libgdk_imlib.so
%{_libdir}/pkgconfig/imlib.pc
%{_libdir}/pkgconfig/imlibgdk.pc
%{_mandir}/man1/imlib_config.1*
%{_mandir}/man1/imlib-config.1*

%changelog
* Tue May 26 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.15
- Rebuilt for Fedora

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.15-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.15-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.15-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Paul Howarth <paul@city-fan.org> - 1:1.9.15-36
- Fix build with giflib version 5, second attempt

* Wed Feb 14 2018 Paul Howarth <paul@city-fan.org> - 1:1.9.15-35
- Fix build with giflib version 5

* Wed Feb 14 2018 Paul Howarth <paul@city-fan.org> - 1:1.9.15-34
- Avoid use of arch-specific build-requires (#1545188)

* Thu Feb  8 2018 Paul Howarth <paul@city-fan.org> - 1:1.9.15-33
- ldconfig scriptlets replaced by RPM File Triggers from Fedora 28
- Specify all explicitly-used build requirements
- Use forward-looking conditionals
- Use %%license where possible
- Drop redundant BuildRoot: and Group: tags
- Drop redundant explicit buildroot cleaning
- Drop %%defattr, redundant since rpm 4.4

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.15-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.15-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.15-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.15-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.15-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.15-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.15-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.15-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.15-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Paul Howarth <paul@city-fan.org> 1:1.9.15-23
- tweak config.guess and config.sub to add aarch64 support (#925585)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1:1.9.15-22
- rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> 1:1.9.15-21
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> 1:1.9.15-20
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1:1.9.15-19
- rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May  7 2012 Paul Howarth <paul@city-fan.org> 1:1.9.15-18
- rebuilt for new libtiff in Rawhide

* Thu Jan  5 2012 Paul Howarth <paul@city-fan.org> 1:1.9.15-17
- rebuilt for gcc 4.7

* Sun Nov  6 2011 Paul Howarth <paul@city-fan.org> 1:1.9.15-16
- add patch from gentoo for building with libpng 1.5.x
- nobody else likes macros for commands

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1:1.9.15-15
- rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 14 2010 Paul Howarth <paul@city-fan.org> 1:1.9.15-14
- EL-6 builds don't need manual pkgconfig dependency
- fix up patches to avoid need for autotools during build
- comment patches

* Thu Mar  4 2010 Paul Howarth <paul@city-fan.org> 1:1.9.15-13
- drop %%{_datadir}/aclocal dependency from devel package from Fedora 14,
  where this directory is part of the filesystem package (#533962)
- drop manual pkgconfig dependency from devel package from Fedora 11, where
  this dependency is auto-detected
- drop some of the %%description text no longer appropriate for this legacy
  package
- don't self-obsolete Imlib and imlib-cfgeditor

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1:1.9.15-12
- rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr  1 2009 Paul Howarth <paul@city-fan.org> 1:1.9.15-11
- add libXt-devel dependency for -devel package (#478357)
- use install -p to maintain timestamps where reasonable
- use an alternative approach to rpath-fixing - hacking the supplied libtool
  rather than trying to use the system one

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1:1.9.15-10
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 23 2008 Paul Howarth <paul@city-fan.org> 1:1.9.15-9
- specify Instruction Set Architecture (%%{?_isa}) in devel package requires
  (where available)

* Fri Aug 29 2008 Paul Howarth <paul@city-fan.org> 1:1.9.15-8
- fix patches to apply without fuzz

* Wed Feb 13 2008 Paul Howarth <paul@city-fan.org> 1:1.9.15-7
- rebuild with gcc 4.3.0 for Fedora 9

* Tue Dec 18 2007 Paul Howarth <paul@city-fan.org> 1:1.9.15-6
- include patch to fix a DoS caused via a BMP image with a Bits Per Page (BPP)
  value of 0 (#426091, CVE-2007-3568); thanks to Peter Volkov at Gentoo for
  the heads-up
- remove URL tag; this legacy package has no active upstream source, and
  documentation for it is gradually disappearing from the Internet

* Wed Nov 28 2007 Adam Jackson <ajax@redhat.com> 1:1.9.15-5
- imlib-1.9.15-check-for-shm-pixmaps.patch: MIT-SHM pixmaps are optional,
  so check that they exist before using them. (#357241)

* Thu Aug  9 2007 Paul Howarth <paul@city-fan.org> 1:1.9.15-4
- re-clarify license as GNU Lesser General Public License v2 or later (LGPLv2+)

* Wed Aug  8 2007 Paul Howarth <paul@city-fan.org> 1:1.9.15-3
- redesign of enlightenment.org website removed imlib page, so URL changed
  to enlightenment.sourceforge.net where the original website lived (#251278)
- clarify license as GNU Lesser General Public License v2 or later (LGPL+)

* Tue Apr 10 2007 Paul Howarth <paul@city-fan.org> 1:1.9.15-2
- add patch for CVE-2004-1025, CVE-2004-1026 (integer/buffer overflows)
  (#235416)

* Thu Mar 29 2007 Paul Howarth <paul@city-fan.org> 1:1.9.15-1
- update to 1.9.15
- update gmodulehack patch
- update URL
- version the obsoletes and provides
- require giflib-devel instead of libungif-devel
- remove redundant gtk+ dependency
- devel package requires %%{_datadir}/aclocal and pkgconfig
- remove patches for fixes done upstream (ac25, waitpid, bounds)
- use sed rather than perl for scripted edits
- macro-ize commands where possible, hardcode paths otherwise
- use make with DESTDIR rather than %%makeinstall
- use more explicit names in the %%files lists
- make imlib-config multilib-compatible
- add buildreq libXt-devel (needed for FC5)

* Fri Jan 12 2007 Paul Howarth <paul@city-fan.org> 1:1.9.13-31
- rebuilt

* Sun Sep 03 2006 Michael J. Knox <michael[AT]knox.net.nz> - 1:1.9.13-30
- Fixed for building in mock/rawhide

* Mon Aug 28 2006 Michael J. Knox <michael[AT]knox.net.nz> - 1:1.9.13-29
- Rebuild for FC6

* Thu Jun 29 2006 Michael J. Knox <michael[AT]knox.net.nz> - 1:1.9.13-28
- spec tidy for FE import

* Mon Jun 12 2006 Matthias Clasen <mclasen@redhat.com> - 1:1.9.13-27
- Package review cleanups

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:1.9.13-26.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:1.9.13-26.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov  7 2005 Matthias Clasen <mclasen@redhat.com> 1:1.9.13-26
- Remove static libs from the -devel package

* Tue Nov  1 2005 Matthias Clasen <mclasen@redhat.com> 1:1.9.13-25
- Switch requires to modular X

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> 1:1.9.13-24
- Replace Copyright: with License:
- rebuild with gcc4

* Thu Sep  9 2004 Matthias Clasen <mclasen@redhat.com>
- security fixes

* Thu Aug 12 2004 Matthias Clasen <mclasen@redhat.com> 1:1.9.13-18
- Kill imlib-cfgeditor subpackage. Move imlib_config 
  into imlib package.  (#127878)

* Fri Aug  6 2004 Tim Waugh <twaugh@redhat.com> 1:1.9.13-17
- Fixed underquoted m4 definitions.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Aug  6 2003 Elliot Lee <sopwith@redhat.com>
- Fix libtool

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com>
- add explicit epoch's where needed.

* Fri Jan 24 2003 Jonathan Blandford <jrb@redhat.com>
- add epoch to requires, #77919
- Fix URI, #71008

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov  5 2002 Jeremy Katz <katzj@redhat.com>
- rebuild to fixup Xlib dir in .pc file

* Tue Aug 13 2002 Havoc Pennington <hp@redhat.com>
- bump soname for new libpng, matches Debian soname
- mop up unpackaged files

* Fri Jul 19 2002 Jakub Jelinek <jakub@redhat.com>
- really remove -static

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 17 2002 Havoc Pennington <hp@redhat.com>
- remove -static that messed up prelinking

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 13 2002 Jeremy Katz <katzj@redhat.com>
- rebuild in new environment

* Wed Apr 10 2002 Owen Taylor <otaylor@redhat.com>
- Backport file descriptor leak and extra waitpid fixes from 1.9.14

* Fri Mar 15 2002 Owen Taylor <otaylor@redhat.com>
- Remove netpbm dependencies

* Thu Mar 14 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.9.13
- Bump version for 6.x/7.x split
- Remove automake-1.4 references

* Thu Feb 28 2002 Havoc Pennington <hp@redhat.com>
- backport to Hampton

* Thu Feb  7 2002 Havoc Pennington <hp@redhat.com>
- remove libpng10, instead load libpng without RTLD_GLOBAL in
  gdk_imlib, and break ABI of plain Imlib

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jan  8 2002 Havoc Pennington <hp@redhat.com>
- get rid of -I/usr/include that was hosing up the png build

* Mon Jan  7 2002 Havoc Pennington <hp@redhat.com>
- try to build against libpng10
- minor spec file cleanup

* Mon Jun 18 2001 Than Ngo <than@redhat.com>
- use %%{_tmppath}
- fix to build against new libtool

* Tue Apr 17 2001 Jonathan Blandford <jrb@redhat.com>
- Updated to new version (1.9.10)

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Up Epoch and release

* Tue Aug 01 2000 Jonathan Blandford <jrb@redhat.com>
- updated to new version.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 29 2000 Dave Mason <dcm@redhat.com>
- updated spec file to new RPM Guidelines

* Sat Jun  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- change dependencies from libgr to netpbm

* Wed May 31 2000 Matt Wilson <msw@redhat.com>
- use makeinstall macro
- 1.9.8

* Fri Feb 25 2000 Elliot Lee <sopwith@redhat.com>
- Patch to use fallback locations for palette files.

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- strip format plugins

* Tue Aug 31 1999 Elliot Lee <sopwith@redhat.com>
- Updates from the RHL 6.0 package.

* Mon Jan 11 1999 Carsten Haitzler <raster@redhat.com>
- up to 1.9.0

* Wed Sep 23 1998 Carsten Haitzler <raster@redhat.com>
- up to 1.8.1

* Tue Sep 22 1998 Cristian Gafton <gafton@redhat.com>
- yet another build for today (%%defattr and %%attr in the files lists)
- devel docs are back on the spec file

* Tue Sep 22 1998 Carsten Haitzler <raster@redhat.com>
- Added minor patch for ps saving code.

* Mon Sep 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to version 1.8

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- take out imlib_config from devel package

* Wed Sep 9 1998 Michael Fulbright <msf@redhat.com>
- upgraded to 1.7
- changed name so it will persist if user later install devel imlib
- added subpackage for imlib_config

* Fri Apr 3 1998 Michael K. Johnson <johnsonm@redhat.com>
- fixed typo

* Fri Mar 13 1998 Marc Ewing <marc@redhat.com>
- Added -k, Obsoletes
- Integrate into CVS source tree
