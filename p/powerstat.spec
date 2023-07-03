%undefine _debugsource_packages

Name:           powerstat
Version:        0.02.15
Release:        2.1
Summary:        Laptop power measuring tool
License:        GPL-2.0
Group:          System/Monitoring
URL:            https://kernel.ubuntu.com/~cking/powerstat/
Source:         https://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.gz

%description
Powerstat measures the power consumption of a mobile PC that has a battery
power source. The output is like vmstat but also shows power consumption
statistics. At the end of a run, powerstat will calculate the average,
standard deviation and min/max of the gathered data. 

%prep
%setup -q

%build
#export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install

%files
%doc COPYING
%{_bindir}/powerstat
%{_mandir}/man8/powerstat.8*

%changelog
* Thu Feb 22 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.02.15
- Rebuilt for Fedora
* Wed Jan 31 2018 mardnh@gmx.de
- update to version 0.02.15
  * Makefile: bump version
  * Fix spelling mistake in comment
  * Update copyright year
  * Add GNU format attribute to log_printf
* Wed Nov  1 2017 mardnh@gmx.de
- update to version 0.02.14
  * Makefile: bump version
  * Add geometic mean to statistics
* Fri Oct 20 2017 mardnh@gmx.de
- update to version 0.02.13
  * Makefile: bump version
  * Increase temp buf from 16 to 32 bytes, cleans up gcc warning
  * Add more scanf sanity checking
  * debian/control: update Standards-version to 4.1.1
  * voidify function returns
  * use sizeof an object rather than the objects type
  * Don't use sentinel for end of signals[], use array size instead
  * include <sys/uio.h> for writev
  * powerstat: break wide macro over 2 lines
* Wed Jun 21 2017 mardnh@gmx.de
- update to version 0.02.12
  * Makefile: bump version
  * Makefile: add snapcraft files to dist rule
  * Fix incorrect GPU stats when sample rate is not 1 second (LP: #1699134)
  * snapcraft: add default type and grade keys
  * snapcraft: Makefile: remove icon hack
  * reduce the scope of the variable 'buf'
  * snapcraft.yaml: remove bogos unnecessary libs
  * Add snapcraft files
  * update copyright year
* Wed May 10 2017 mardnh@gmx.de
- update to version 0.02.11
  * Makefile: bump version
  * Makefile: add mascot to dist rule
  * Remove two blank lines
  * Allow float compares a little slop
  * Makefile: add PEDANTIC flags
  * Add powerstat mascot
* Sat Jul 30 2016 mardnh@gmx.de
- update to version 0.02.10
  * Makefile: bump version
  * debian/control: update Standards-Version to 3.9.8
- update to version 0.02.09
  * Makefile: bump version
  * Do not overflow power domain and thermal zone buffers (LP: #1551297)
  * Tag RAPL stats as valid so stats show up in avg, std.dev. (LP: #1551287)
- update to version 0.02.08
  * Makefile: bump version
  * Move N/A message for GPU power right one char
  * Add some more per function comments
  * constify a few more func args
  * Make all non-main functions static
  * Minor fix up on GPU Watts field
  * Add GPU average stats
  * Clean up column formatting
  * add -g GPU stats
  * Update and correct copyright years
* Thu Feb 18 2016 mardnh@gmx.de
- update to version 0.02.07
  * Makefile: bump version
  * Manual: re-work some parts of the manual
  * Manual: add missong comma in SEE ALSO list
  * Move structure links to head of structures
  * Use a more efficient hashing function
* Wed Nov 11 2015 mardnh@gmx.de
- initial package
