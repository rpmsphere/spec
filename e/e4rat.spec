Summary:	Toolset to accelerate the boot process as well as application startups
Name:		e4rat
Version:	0.2.3
Release:	26
License:	GPLv3
Group:		System/Boot and Init
URL:		http://e4rat.sourceforge.net/
Source0:	http://sourceforge.net/projects/e4rat/files/%{name}_%{version}_src.tar.gz
Patch0:		git.diff
Patch1:		e4rat-0.2.2-libdir.patch
Patch2:		e4rat-0.2.3-shared-build.patch
Patch3:		e4rat-0.2.3-gcc7.patch
Patch4:		e4rat-0.2.3-glibc-2.28.patch
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(blkid)
BuildRequires:	audit-libs-devel
#BuildRequires:	auparse-devel
BuildRequires:	libstdc++-devel

%description
e4rat ("Ext4 - Reducing Access Times") is a toolset to accelerate the boot
process as well as application startups. Through physical file realloction
e4rat eliminates both seek times and rotational delays. This leads to a high
disk transfer rate.

Placing files on disk in a sequentially ordered way allows to efficiently
read-ahead files in parallel to the program startup. The combination of
sequentially reading and a high cache hit rate may reduce the boot time by a
factor of three, as the example below shows.

e4rat is based on the online defragmentation ioctl EXT4_IOC_MOVE_EXT from the
Ext4 filesystem, which was introduced in Linux Kernel 2.6.31. Other filesystem
types and/or earlier versions of extended filesystems are not supported.

%prep
%setup -q
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}
mkdir -p %buildroot/var/lib/e4rat

%files
%doc README
%config %{_sysconfdir}/%{name}.conf
%{_sbindir}/%{name}-collect
%{_sbindir}/%{name}-preload
%{_sbindir}/%{name}-realloc
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}-collect.8*
%{_mandir}/man8/%{name}-preload.8*
%{_mandir}/man8/%{name}-realloc.8*
%dir /var/lib/e4rat
%exclude %{_libdir}/lib%{name}-core.so
%{_libdir}/lib%{name}-core.so.*

%changelog
* Wed Feb 12 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3
- Rebuilt for Fedora
* Tue Oct 16 2018 wally <wally> 0.2.3-26.mga7
+ Revision: 1321024
- rebuild for new boost 1.68.0
* Mon Sep 24 2018 umeabot <umeabot> 0.2.3-25.mga7
+ Revision: 1303021
- Mageia 7 Mass Rebuild
* Mon Dec 25 2017 wally <wally> 0.2.3-24.mga7
+ Revision: 1184662
- rebuild for new boost
* Tue Nov 21 2017 tv <tv> 0.2.3-23.mga7
+ Revision: 1178059
- rebuild for boost 1.65
* Fri Sep 29 2017 cjw <cjw> 0.2.3-22.mga7
+ Revision: 1161450
- patch3: fix build with gcc 7
* Sun Feb 14 2016 umeabot <umeabot> 0.2.3-21.mga6
+ Revision: 959976
- Mageia 6 Mass Rebuild
* Sat Dec 26 2015 daviddavid <daviddavid> 0.2.3-20.mga6
+ Revision: 915163
- rebuild for new boost 1.60.0
* Fri Sep 25 2015 tv <tv> 0.2.3-19.mga6
+ Revision: 883530
- rebuild for new boost
* Mon Aug 31 2015 cjw <cjw> 0.2.3-18.mga6
+ Revision: 871562
- rebuild with gcc 5
* Sun Aug 02 2015 daviddavid <daviddavid> 0.2.3-17.mga6
+ Revision: 860512
- rebuild for new boost-1.58.0
* Wed Oct 15 2014 umeabot <umeabot> 0.2.3-16.mga5
+ Revision: 739332
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.2.3-15.mga5
+ Revision: 678905
- Mageia 5 Mass Rebuild
* Fri May 09 2014 tv <tv> 0.2.3-14.mga5
+ Revision: 621576
- patch 0: backport git fixes
- patch 3: drop it (merged in patch 0)
* Sat Feb 08 2014 barjac <barjac> 0.2.3-13.mga5
+ Revision: 586325
- rebuild against boost-1.55
* Sat Oct 19 2013 umeabot <umeabot> 0.2.3-12.mga4
+ Revision: 533209
- Mageia 4 Mass Rebuild
* Mon Aug 26 2013 tv <tv> 0.2.3-11.mga4
+ Revision: 471993
- rebuild with new toolchain
* Tue Jul 09 2013 fwang <fwang> 0.2.3-10.mga4
+ Revision: 451761
- rebuild for new boost
+ malo <malo>
- rebuild for boost 1.53
* Thu Apr 11 2013 ennael <ennael> 0.2.3-8.mga3
+ Revision: 409488
- rebuild for boost 1.53
* Tue Jan 22 2013 tv <tv> 0.2.3-7.mga3
+ Revision: 391052
- adjust group
- fix another mdvism pulling devel packages...
* Fri Jan 18 2013 tv <tv> 0.2.3-6.mga3
+ Revision: 389446
- library does not need main package...
* Thu Jan 17 2013 tv <tv> 0.2.3-5.mga3
+ Revision: 389195
- create /var/lib/e4rat
* Fri Jan 11 2013 umeabot <umeabot> 0.2.3-4.mga3
+ Revision: 349239
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Mon Jan 07 2013 tv <tv> 0.2.3-3.mga3
+ Revision: 341316
- fix bogus libification from mdv...
* Mon Jan 07 2013 tv <tv> 0.2.3-2.mga3
+ Revision: 341315
- do not BR audit (broken by glibc)
- patch 3: fix build
- fix bogus URL
- imported package e4rat
* Mon Jan 07 2013 Thierry Vignaud <tv@mageia.org> 0.2.3-1.mga3
- import from mdv
- clean spec
* Tue May 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.3-1
+ Revision: 797625
- drop patch 0
- Patch1: fix lib dir on install
- Patch2: check for libraries in corrent places, and use dynamic linking
- clean spec file
- add conflicts on preload
- update to new version 0.2.3
* Wed May 11 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.2.1-1
+ Revision: 673556
- Imported to cooker.
  P0: enable dynamic linking.
- Created package structure for e4rat.
