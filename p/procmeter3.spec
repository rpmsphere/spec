Name:           procmeter3
Version:        3.6
Release:        11.1
Summary:        Display actual system parameters
License:        GPL-2.0+
Group:          System/Monitoring
URL:            https://www.gedanken.org.uk/software/procmeter3/
Source:         https://www.gedanken.org.uk/software/procmeter3/download/%{name}-%{version}.tgz
Source1:        procmeter3.desktop
Source2:        procmeter3.png
BuildRequires:  gtk2-devel
#BuildRequires:  gtk3-devel
BuildRequires:  libXt-devel
BuildRequires:  libXaw-devel

%description
With procmeter one can display various system parameters as e.g.
processor load, network load, etc.

%package devel
Summary:        Display actual system parameters -- Development Files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
With procmeter one can display various system parameters as e.g.
processor load, network load, etc.

This package provides files needed to build modules for procmeter.

%prep
%setup -q
%ifarch x86_64 aarch64
sed -i 's|/lib/|/lib64/|' Makefile
%endif
sed -i 's|loff_t|off_t|' modules/longrun.c

%build
make INSTDIR=%{_prefix} CFLAGS="%{optflags}"

%install
%make_install INSTDIR=%{_prefix}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc ChangeLog COPYING NEWS README
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_bindir}/*
%{_libdir}/ProcMeter3
%{_mandir}/man?/*

%files devel
%{_includedir}/ProcMeter3

%changelog
* Mon Mar 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 3.6
- Rebuilt for Fedora
* Tue Feb 21 2012 dimstar@opensuse.org
- Add libX11-devel, libXaw-devel and libXt-devel BuildRequires on
  openSUSE > 12.1 to cater for the reorganization of xorg-x11
  packages.
* Mon Jan 23 2012 vuntz@opensuse.org
- Update to version 3.6:
  + New features
  - Added GTK3 version.
  - Draw line in foreground colour between outputs in
    procmeter3-gtk2.
  + New modules
  - Battery - new /sys/class/power_supply/ battery information.
  + Bug Fixes
  - Don't package up unused LSM and ANNOUNCE files.
  - Add "-lX11" to LDFLAGS (deb#556073).
  - Move installed modules into /usr/lib/ProcMeter3 (deb#651145).
  - Don't always install the procmeterrc.install file
    (deb#651149).
  - Install procmeter.h to /usr/include/ProcMeter3 (deb#651150).
  - Fix Makefiles to stop linking executables each time make is
    run.
  - Don't crash procmeter3-xaw if specified font doesn't exist.
  + Module bug fixes
  - Changed wireless module to remove kernel 2.4.x code.
  - Fixed stat-intr module to not use data from freed memory.
- Changes from version 3.5d:
  + New features
  - Added an option to limit the number of interrupts listed.
  - Allow installation of stripped executables.
  + Bug Fixes
  - Remove gcc-4.4 compilation warnings.
  - Make error messages consistent.
  - Fix several errors in manual pages.
  - Don't crash if /proc/interrupts has very long lines.
- Drop procmeter-as-needed.patch: fixed upstream.
- Drop procmeter3-3.4a.patch: part of the fixes are upstream, and
  the remaining things are fixed by setting the INSTDIR and CFLAGS
  environment variables when calling make.
- Use favor_gtk2 to switch between gtk2 and gtk3 builds:
  + Use gtk3-devel BuildRequires instead of gtk2-devel for gtk3
    builds.
- Create a devel subpackage for development files.
* Mon Sep  5 2011 vuntz@opensuse.org
- Update to version 3.5c:
  + New features:
  - Sort the module menu into alphabetical order.
  + New modules:
  - FanSpeed, Temperature & Voltage: Improved hardware sensors.
  + Bug Fixes:
  - Remove 64-bit compilation warnings and fix variable type
    mismatch.
  - Fixed df module to handle disks bigger than 2TB.
  - Fixed sensors module to handle new directory format.
  - Pass top-level Makefile variables down to sub directories.
- Add procmeter-as-needed.patch: fix build with -Wl,--as-needed.
  Taken from Debian.
- Add libsensors4-devel BuildRequires to build the new sensors.
* Sat Feb 12 2011 vuntz@opensuse.org
- Call relevant macros in %%post/%%postun:
  + %%desktop_database_post/postun because the package ships at
    least one desktop file.
* Tue Dec 29 2009 vuntz@opensuse.org
- Update to version 3.5b:
  + New Features
  - Extended Window Manager Hints can be specified with a -w
    option.
  - Increase the number of interrupts possible in stat-intr.
  + Bug Fixes
  - Be more careful looking for modules (check '.' and '..').
  - Set the locale to "C" to avoid problems parsing numbers.
  - Ensure that graph-min and graph-max options are used
    properly.
  - Extended the line buffer size for parsing /proc/interrupts.
  - Remove fixed size line buffers in modules (realloc more space
    as needed).
  - Allow LCD version to specify priority as a string or numeric
    value.
- Changes from version 3.5a:
  + Bug Fixes
  - Stop the GTK2 version crashing when displayed items are
    removed.
  - Make sure that the right mouse button menu works with no
    outputs displayed.
  - Make the GTK1 and GTK2 version windows resize themselves like
    Xaw version.
  - Updates to manual pages to reflect new executable names.
  - Bug fixes for ACPI module.
- Changes from version 3.5:
  + New features
  - Added a gtk2 version of ProcMeter3.
  - Renamed the executables but added backwards compatibility
    links.
  - Added DESTDIR option to Makefiles.
- Changes from version 3.4g:
  + Bug fixes:
  - Quicker default update of the date displays (useful after
    suspending).
  - Uptime now accurately shows system running time even after
    suspend.
  - Fix ACPI battery discharge rates.
  - Fix for crashes with stat-cpu outputs on multi-CPU machines.
  - Change to use longer integer values for netdev outputs.
  - Search other places for hardware sensors information.
- Changes from version 3.4f:
  + Bug fixes:
  - The biff module re-reads the inbox if the size or timestamp
    change.
  - The df module uses longer strings for reading from
    /proc/mounts.
- Changes from version 3.4e:
  + New or changed modules:
  - Add in the new CPU statistics (iowait, irq, softirq and
    steal).
  - Add in a display of the CPU clock speed.
  + Bug fixes:
  - Fix some spelling mistakes in the manual pages.
  - Change the default scaling for the DiskUsage outputs to 5
    grid lines of 20%%.
  - Fix some gcc-4.x compilation warnings.
  - Fix some ACPI module bugs.
- Changes from version 3.4d:
  + Bug fixes:
  - Updated ACPI support to handle kernel version 2.6.
  - Added support for /dev/mapper in disk statistics.
  - Change to using 64-bit variables from /proc/stat.
- Changes from version 3.4c:
  + Bug fixes:
  - Make grid-max option work for GTK version.
  - Handle kernel 2.6.x better for hardware sensors.
- Changes from version 3.4b:
  + New or changed modules:
  - Handle different header line for hostap wireless driver.
  + Bug fixes:
  - Modules that didn't work with kernel 2.6.x now do.
  - Improved some module initialisation functions.
- Replace gtk-devel BuildRequires with gtk2-devel.
- Update procmeter3-3.4a.patch: some parts were upstreamed.
- Drop procmeter3-3.4a-array.patch: fixed upstream.
- Drop procmeter3-3.4a-ia64.patch: not needed anymore.
- Remove AutoReqProv: it's default now.
- Use makeinstall macro.
* Thu Aug 17 2006 ro@suse.de
- move from /usr/X11R6 to /usr
* Thu Feb 23 2006 pnemec@suse.cz
- fixed ArrayOutOfBound  #152045
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Fri Aug 15 2003 adrian@suse.de
- add desktop file
* Wed Jul  9 2003 ltinkl@suse.cz
- updated sources to version 3.4a
* Mon Feb 17 2003 vbobek@suse.cz
-updated to version 3.4
  * new output format
  * added manpage for modules
  * bug fixes
* Thu Oct 10 2002 prehak@suse.cz
- updated to version 3.3b
* Mon Jan 21 2002 cihlar@suse.cz
- use %%{_lib}
* Thu Jul 26 2001 cihlar@suse.cz
- update to version 3.3a
* Mon May 21 2001 cihlar@suse.cz
- fixed cast warnings on ia64
- fixed includes
* Wed Mar  7 2001 cihlar@suse.cz
- updated to version 3.3
* Tue Nov 14 2000 cihlar@suse.cz
- renamed procmtr -> procmeter
- update to version 3.2a
- bzipped sources
- fixed copyright tag
* Wed May 17 2000 cihlar@suse.cz
- Group sorted
* Fri Apr  7 2000 cihlar@suse.cz
- added BuildRoot
- upgrade to version 3.2
* Tue Jan 25 2000 ro@suse.de
- update to 2.4, cleanup spec
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Jan 16 1997 maddin@suse.de
- first S.u.S.E. version 2.2
- changed paths
- copied documentation to /usr/doc/packages/procmtr
