%define svn r81625
%define rel 13
%if 0%{?svn:1}
#define release %%mkrel -c %%svn %%rel
%define release 1.%svn.%rel
%else
%define release %rel
%endif

Summary:        Enlightenment weather/forecasts module
Name:           eweather
Version:        0.2.0
Release:        %release
License:        LGPLv2+
Group:          Graphical desktop/Enlightenment
URL:            https://www.enlightenment.org/
# creating archive is quite simple:
# svn export https://svn.enlightenment.org/svn/e/trunk/%%name %%name
# tar cJf %%name-%%svn.tar.xz %%name
%if 0%{?svn:1}
Source:         %name-%svn.tar.xz
%else
Source:         %name-%version.tar.bz2
%endif
Patch0:         eweather-automake-1.13.patch

BuildRequires:  pkgconfig(efl)
BuildRequires:  efl
BuildRequires:  gettext-devel

%description
Enlightenment weather/forecasts module.

%package devel
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %name = %{version}-%{release}

%description devel
%{name} development headers and libraries

%prep
%if 0%{?svn:1}
%setup -qn %name
%else
%setup -qn %name-version
%endif
%patch 0 -p1 -b .automake113

%build
%if 0%{?svn:1}
LC_ALL=C NOCONFIGURE=1 ./autogen.sh
%endif
%configure --disable-static
%make_build

%install
%make_install

rm -rf %buildroot/%{_datadir}/simple
rm -rf %buildroot/%{_datadir}/default

find %buildroot -name *.la | xargs rm

%files
%{_bindir}/eweather_test
%{_libdir}/eweather
%{_datadir}/eweather
%{_libdir}/*.so.0
%{_libdir}/*.so.0.*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
* Sun Apr 03 2022 umeabot <umeabot> 0.2.0-1.r81625.13.mga9
+ Revision: 1841911
- Mageia 9 Mass Rebuild
* Fri Aug 28 2020 martinw <martinw> 0.2.0-1.r81625.12.mga8
+ Revision: 1619388
- rebuild for fixed spec file
* Thu Feb 13 2020 umeabot <umeabot> 0.2.0-1.r81625.11.mga8
+ Revision: 1512102
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%configure2_5x
* Sun Sep 23 2018 umeabot <umeabot> 0.2.0-1.r81625.10.mga7
+ Revision: 1297637
- Mageia 7 Mass Rebuild
+ kekepower <kekepower>
- Use new make macros
* Mon Feb 01 2016 umeabot <umeabot> 0.2.0-1.r81625.9.mga6
+ Revision: 930006
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 0.2.0-1.r81625.8.mga5
+ Revision: 748295
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.2.0-1.r81625.7.mga5
+ Revision: 679054
- Mageia 5 Mass Rebuild
* Sun May 04 2014 barjac <barjac> 0.2.0-1.r81625.6.mga5
+ Revision: 620044
- fix BRs with new  efl
* Sat Oct 19 2013 umeabot <umeabot> 0.2.0-1.r81625.5.mga4
+ Revision: 523487
- Mageia 4 Mass Rebuild
* Tue May 07 2013 trem <trem> 0.2.0-1.r81625.4.mga3
+ Revision: 412576
- increase release to rebuild
* Fri Jan 11 2013 umeabot <umeabot> 0.2.0-1.r81625.3.mga3
+ Revision: 349808
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Jan 10 2013 sander85 <sander85> 0.2.0-1.r81625.2.mga3
+ Revision: 344728
- Fix build with automake 1.13
* Sat Dec 22 2012 trem <trem> 0.2.0-1.r81625.1.mga3
+ Revision: 334032
- update to release 81625
* Sat Dec 15 2012 trem <trem> 0.2.0-1.r80969.1.mga3
+ Revision: 331123
- update to release 80969
* Sat Dec 08 2012 trem <trem> 0.2.0-1.r80477.1.mga3
+ Revision: 328264
- update to release 80477
* Sat Nov 24 2012 trem <trem> 0.2.0-1.r79568.1.mga3
+ Revision: 321549
- update to release 79568
* Sat Sep 22 2012 trem <trem> 0.2.0-1.r76819.1.mga3
+ Revision: 296651
- update to release 76819
* Sun Sep 16 2012 trem <trem> 0.2.0-1.r76435.1.mga3
+ Revision: 294450
- update to release 76435
- update to release 75400
* Sun Aug 19 2012 trem <trem> 0.2.0-1.r75426.1.mga3
+ Revision: 282220
- update to r75426
* Sun Mar 11 2012 trem <trem> 0.2.0-1.r69188.1.mga3
+ Revision: 222705
- update to release 69188
* Sat Mar 10 2012 trem <trem> 0.2.0-1.r69165.1.mga2
+ Revision: 222440
- update to release 69165
* Sun Mar 04 2012 trem <trem> 0.2.0-1.r68658.1.mga2
+ Revision: 218016
- update to release 68658
* Sat Mar 03 2012 trem <trem> 0.2.0-1.r68649.1.mga2
+ Revision: 217566
- update to release 68649
* Sun Feb 26 2012 trem <trem> 0.2.0-1.r68450.1.mga2
+ Revision: 215234
- update to release 68450
* Sat Feb 25 2012 trem <trem> 0.2.0-1.r68434.1.mga2
+ Revision: 214445
- update to release 68434
* Fri Feb 24 2012 trem <trem> 0.2.0-1.r68363.1.mga2
+ Revision: 213994
- update to release 68363
* Wed Feb 22 2012 trem <trem> 0.2.0-1.r68228.1.mga2
+ Revision: 212097
- update to release 68228
* Sun Feb 19 2012 trem <trem> 0.2.0-1.r68120.1.mga2
+ Revision: 210813
- update to release 68120
* Sat Feb 18 2012 trem <trem> 0.2.0-1.r68102.1.mga2
+ Revision: 210261
- update to release 68102
* Sat Feb 11 2012 trem <trem> 0.2.0-1.r67851.1.mga2
+ Revision: 207564
- update to release 67851
* Sat Feb 11 2012 trem <trem> 0.2.0-1.r67846.1.mga2
+ Revision: 207277
- update to release 67846
* Fri Feb 10 2012 trem <trem> 0.2.0-1.r67830.1.mga2
+ Revision: 206986
- update to release 67830
* Tue Feb 07 2012 trem <trem> 0.2.0-1.r67715.1.mga2
+ Revision: 206018
- update to release 67715
- update to release 67703
- update to release 67702
- update to release 67698
- update to release 67688
- update to release 67680
* Sun Dec 04 2011 trem <trem> 0.2.0-1.r65867.1.mga2
+ Revision: 176112
- update to release 65867
* Tue Nov 29 2011 trem <trem> 0.2.0-1.r65688.1.mga2
+ Revision: 174258
- update to release 65688
* Sun Nov 27 2011 trem <trem> 0.2.0-1.r65613.1.mga2
+ Revision: 172981
- update to release 65613
* Sun Nov 20 2011 trem <trem> 0.2.0-1.r65428.1.mga2
+ Revision: 169763
- update to release 65428
* Thu Nov 17 2011 trem <trem> 0.2.0-1.r65341.1.mga2
+ Revision: 168467
- update to release 65341
* Wed Nov 16 2011 trem <trem> 0.2.0-1.r65269.1.mga2
+ Revision: 168218
- update to release 65269
* Sun Nov 13 2011 trem <trem> 0.2.0-1.r65129.1.mga2
+ Revision: 167180
- update to release 65129
* Fri Nov 11 2011 trem <trem> 0.2.0-1.r65056.1.mga2
+ Revision: 166608
- update to release 65056
* Sat Nov 05 2011 trem <trem> 0.2.0-1.r64753.1.mga2
+ Revision: 163345
- update to release 64753
* Tue Nov 01 2011 trem <trem> 0.2.0-1.r64603.1.mga2
+ Revision: 160831
- update to release 64603
* Mon Oct 31 2011 trem <trem> 0.2.0-1.r64579.1.mga2
+ Revision: 160620
- update to release 64579
* Sun Oct 30 2011 trem <trem> 0.2.0-1.r64519.1.mga2
+ Revision: 160070
- update to release 64519
* Sat Oct 29 2011 trem <trem> 0.2.0-1.r64511.1.mga2
+ Revision: 159833
- update to r64511
* Fri Oct 28 2011 trem <trem> 0.2.0-1.r64501.1.mga2
+ Revision: 159305
- update to r64501
* Wed Oct 26 2011 trem <trem> 0.2.0-1.r64414.1.mga2
+ Revision: 158404
- update to r64414
- use release-version on e17 br package (instead of just version)
* Mon Oct 24 2011 trem <trem> 0.2.0-1.r64328.1.mga2
+ Revision: 157822
- use svn release (instead of stable release)
- spec cleaning
* Mon Sep 26 2011 trem <trem> 0.2.0-0.20100709.4.mga2
+ Revision: 148936
- drop la files
- add two patches to fixes missing library when linking
* Tue Apr 19 2011 ennael <ennael> 0.2.0-0.20100709.3.mga1
+ Revision: 88174
- imported package eweather

* Thu Oct 14 2010 Funda Wang <fwang@mandriva.org> 0.2.0-0.20100709.3mdv2011.0
+ Revision: 585537
- rebuild
- rebuild
- rebuild
* Sat Jul 17 2010 Funda Wang <fwang@mandriva.org> 0.2.0-0.20100709.1mdv2011.0
+ Revision: 554482
- rediff linkage patch
- new snapshot
* Mon Dec 14 2009 Funda Wang <fwang@mandriva.org> 0.2.0-0.20091213.1mdv2010.1
+ Revision: 478423
- add BRs
- fix linkage
- add BR
- import eweather
