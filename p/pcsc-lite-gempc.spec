%define _name ifd-gempc

Name:           pcsc-lite-gempc
BuildRequires:  libusb-devel
BuildRequires:  pcsc-lite-devel
Version:        1.0.8
Release:        1
URL:            https://ludovic.rousseau.free.fr/softwares/ifd-GemPC/
Summary:        PCSC driver for the Gemplus GemPC 410/430 smartcard readers
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Productivity/Security
Source0:        https://ludovic.rousseau.free.fr/softwares/ifd-GemPC/%{_name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE pcsc-gempc-1.0.0-devname.diff okir@suse.de -- Use standard device nodes.
Patch:          %{_name}-1.0.0-devname.diff
# PATCH-FIX-OPENSUSE pcsc-gempc-makefile.diff mjancar@suse.cz -- Fix build environment.
Patch1:         %{_name}-1.0.0-makefile.diff
Requires:       pcsc-lite
%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
This package contains a driver for the GemPC 410 and GemPC 430 smart
card readers produced by Gemplus.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup -q -n %{_name}-%{version}
%patch
%patch1
mv README.410 README_410
mv README.430 README_430
for DIR in GemPC410 GemPC430 ; do
    for FILE in $DIR/COPYING* $DIR/TODO* ; do
	SUFFIX=.${FILE##*.}
	if test "$SUFFIX" = ".$FILE" ; then
	    SUFFIX=
	fi
	mv $FILE ${FILE%.*}${DIR#GemPC}$SUFFIX
    done
done
sed -i 's|PCSCLITE_MAX_READERS_CONTEXTS|16|' common/gempc_ifdhandler.h

%build
make %{?jobs:-j%jobs} CFLAGS="$RPM_OPT_FLAGS"

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Changelog README* Gem*/COPYING* Gem*/TODO*
%{ifddir}/ifd*
%{ifddir}/serial/*

%changelog
* Sun May 2 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.8
- Rebuilt for Fedora
* Tue Jan 29 2019 sbrabec@suse.com
- Updated to version 1.0.8:
  * Fix typo in log message.
- Add GPG verification files.
* Wed Mar  6 2013 coolo@suse.com
- update license to new format
* Thu Jul 12 2012 sbrabec@suse.cz
- Updated to version 1.0.7:
  * Fixed immediate binding failure.
  * Further code cleanup and warning fixes.
  * Minor fixes.
* Tue Mar 22 2011 coolo@novell.com
- licenses package is about to die
* Tue Nov  3 2009 coolo@novell.com
- updated patches to apply with fuzz=0
* Wed Aug  5 2009 sbrabec@suse.cz
- Updated to version 1.0.5:
  * Code cleanup and warning fixes.
* Fri Jun 19 2009 coolo@novell.com
- disable as-needed for this package as it fails to build with it
* Wed Apr  8 2009 sbrabec@suse.cz
- Updated to version 1.0.4:
  * Fix powerup sequence when switching to EMV->ISO mode.
  * Allow the header to be read in several calls.
  * gci410emv connected thru an usb adapter now it works fine.
- Added USB modalias supplements.
- Require pcsc-lite.
* Fri Apr  4 2008 sbrabec@suse.cz
- Updated to version 1.0.3:
  * correct a big bug unnoticed for many years and declared on
    PowerPC with gcc 4.x
  * do not strip the library so we have debug symbols if needed,
    strip should be called by the package build process
* Thu Jul 26 2007 sbrabec@suse.cz
- Updated to version 1.0.2:
  * correctly handle empty response from the reader
  * minor fixes
* Fri Jun  1 2007 sbrabec@suse.cz
- Updated to version 1.0.1:
  * Minor fixes.
  * Define interface, bulk_in and bulk_out fields and store the
    device values.
- Build with libusb-devel.
* Fri May 26 2006 schwab@suse.de
- Don't strip binaries.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Jan  3 2006 mjancar@suse.cz
- move to separate source package
* Mon Jan  2 2006 stark@suse.de
- removed obsolete hotplug stuff for cyberjack
- Updated pcsc-lite to version 1.2.9-beta9
- Updated CCID driver to 0.9.4
- Updated GemPC driver to 1.0.0
- package pkgconfig files to be able to build drivers outside
  the package
* Tue Dec 20 2005 ro@suse.de
- removed unpackaged man-page symlinks
* Tue Nov 29 2005 ro@suse.de
- remove keeper from nfb (unused)
* Mon Oct 10 2005 stark@suse.de
- Updated towitoko driver to 2.0.7 and install USB bundle
* Wed Sep 21 2005 stark@suse.de
- Repackaged CCID as bundle for USB usage (#116497)
* Tue Sep 20 2005 stark@suse.de
- handle old reader.conf in upgrade case
- compile with -fno-strict-aliasing
- fixed missing return in ctapi-cyberjack
* Sat Sep 17 2005 stark@suse.de
- Updated pcsc-lite to version 1.2.9beta8 (#116497)
  * use /etc/reader.conf.d/
  * adapted init script to create /etc/reader.conf
- Updated cyberjack driver to version 2.0.9
  * use rpath for cyberjack tools
- Updated ccid driver to version 0.9.3 (#116497)
- Use RPM_OPT_FLAGS everywhere
- Fixed serious compiler warnings
* Mon Sep  5 2005 skh@suse.de
- fix off-by-one error in hotplug_libusb.c [#112964]
* Mon Aug 29 2005 skh@suse.de
- Remove unnecessary files from pcsc-acr38 again [#112927]
* Mon Aug 29 2005 skh@suse.de
- package ACR38 driver in correct bundle format [#112927]
- remove orphaned /var/run/pcscd.pub when necessary [#112928]
- update ACR38u driver to version 100705 to fix crash when reader
  is plugged in [#112964]
* Tue Aug 16 2005 skh@suse.de
- Updated ACR38u driver to version 100703
* Tue Jul 26 2005 okir@suse.de
- Added ACR38u driver
* Tue Jul 26 2005 okir@suse.de
- Updated description in init script (#79287)
* Thu Jun 16 2005 meissner@suse.de
- use RPM_OPT_FLAGS in 1 more driver
- added includes to avoid implict declaration of memcpy and similar.
* Mon Apr 18 2005 ro@suse.de
- make it build with gcc-4
* Thu Mar 17 2005 okir@suse.de
- Disable support for extended-apdus, it eats 32MB of memory (#73629)
* Thu Mar 10 2005 okir@suse.de
- Fix default search location for USB bundles
* Fri Jan 21 2005 okir@suse.de
- Updated to latest upstream version
- Updated several drivers
- Added CCID driver
- Provide a more informative readers.conf file (#42620)
* Thu Jan 20 2005 ro@suse.de
- drop subpackage gpr400
* Wed Apr 28 2004 ro@suse.de
- compile formaticc with no-strict-aliasing
- fix unused return type in musclecard.c
* Wed Mar 31 2004 okir@suse.de
- Properly install testpcsc, formaticc (#37625)
- Build towitoko driver with --enable-win32-com
* Thu Mar 18 2004 okir@suse.de
- cyberjack apps installed in /bin should be executable (#36409)
* Sat Jan 10 2004 adrian@suse.de
- add %%run_ldconfig
* Tue Aug  5 2003 mge@suse.de
- merge ctapi-cyberjack into pcsc-lite: two additional
  packages are created: ctapi-cyberjack and pcsc-cyberjack
* Thu Jun 26 2003 ro@suse.de
- remove unpackaged files from buildroot
- added directories to filelist
* Fri Nov 29 2002 okir@suse.de
- added -fPIC when building eToken driver
* Fri Nov 29 2002 okir@suse.de
- Updated to latest upstream version
- Included driver for Aladdin eToken PRO
- More GNU auto#*@! headaches
- Various minor fixes
* Wed Aug 28 2002 okir@suse.de
- Moved shared objects to /usr/lib64 on ppc64/s390x (#18421)
* Mon Aug  5 2002 olh@suse.de
- fix initscript, Should-start: setserial hotplug
* Fri Aug  2 2002 okir@suse.de
- added PreReq for insserv_and_fillup
* Wed Jul 31 2002 okir@suse.de
- fixed build problem on s390x (force aclocal.m4 regen)
* Wed Jun 26 2002 ro@suse.de
- use -fPIC when building a shared lib
* Wed Jun 12 2002 okir@suse.de
- fix for bug #15051 (hey, it's a palindrome bug:):
  missing %%doc DRIVERS file; misc silly binaries moved
  out of /usr/bin
* Tue Apr 30 2002 okir@suse.de
- Fixed build problem introduced by previous patch
* Tue Apr 30 2002 okir@suse.de
- updated to latest upstream version
- added drivers for these readers: Towitoko, Schlumberger Reflex 6x,
  Gemplus GPR 400, GemPlus GemPC 410/430
* Tue Apr  9 2002 ro@suse.de
- fixed for latest automake/autoconf
* Wed Feb 13 2002 stark@suse.de
- spec-file cleanup
- LSB compliant init-script
* Mon Jan 14 2002 ro@suse.de
- removed START_PCSCD
* Wed Nov 14 2001 ro@suse.de
- call aclocal
* Sun Aug 26 2001 mge@suse.de
- updated to 1.0.0Beta
- fixed /etc/init.d/pcscd status-handling (bug #9069)
* Thu Jun  7 2001 ro@suse.de
- fix broken Makefile.am
* Sun Apr 22 2001 mge@suse.de
- update to 0.9.1
* Wed Apr 18 2001 mge@suse.de
- created package
