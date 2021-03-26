Name:		exfatprogs
Summary:	Utilities for exFAT file system
Epoch:		1
Version:	1.0.4
Release:	1
License:	GPLv2
Group:		File tools
URL:		https://github.com/exfatprogs/exfatprogs
Source0:	https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#rename		exfat-utils

%description
A set of utilities for creating, checking and labeling exFAT file system.

%prep
%setup -q

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%doc COPYING NEWS README.md
%{_sbindir}/*
%{_mandir}/man8/*

%changelog
* Mon Oct 05 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.4
- Rebuild for Fedora
* Thu Apr 23 2020 tmb <tmb> 1:1.0.2-1.mga8
+ Revision: 1571421
- fix build
+ tv <tv>
- obsolete exfat-utils
- 1.0.2
- rename exfat-utils -> exfatprogs
- rename exfat-utils -> exfatprogs
* Thu Apr 09 2020 tmb <tmb> 1:1.0.1-1.mga8
+ Revision: 1565820
- switch to official exfat-utils
* Fri Mar 20 2020 tmb <tmb> 1.3.0-2.mga8
+ Revision: 1558369
- Validate UTF-8 byte sequence
* Fri Feb 21 2020 umeabot <umeabot> 1.3.0-2.mga8.tainted
+ Revision: 1548867
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%configure2_5x
* Sat Dec 29 2018 luigiwalser <luigiwalser> 1.3.0-1.mga7.tainted
+ Revision: 1345903
- 1.3.0
* Thu Sep 20 2018 umeabot <umeabot> 1.2.8-2.mga7.tainted
+ Revision: 1278213
- Mageia 7 Mass Rebuild
* Sun Mar 25 2018 kekepower <kekepower> 1.2.8-1.mga7.tainted
+ Revision: 1212443
- Update to version 1.2.8
* Sat Oct 07 2017 daviddavid <daviddavid> 1.2.7-1.mga7.tainted
+ Revision: 1170006
- new version: 1.2.7
* Wed Mar 22 2017 wally <wally> 1.2.6-1.mga6.tainted
+ Revision: 1094280
- new version 1.2.6
* Wed Jan 13 2016 daviddavid <daviddavid> 1.2.3-1.mga6.tainted
+ Revision: 922444
- new version: 1.2.3
* Sun Oct 25 2015 wally <wally> 1.2.1-1.mga6.tainted
+ Revision: 895344
- new version 1.2.1
  * fixes heap overflow (CVE-2015-8026) and endless loop in exfatfsck (mga#17013)
- fix URL
* Tue Aug 25 2015 wally <wally> 1.1.1-2.mga6.tainted
+ Revision: 869333
- submit pkg to tainted (mga#16034)
* Sun Aug 23 2015 ycantin <ycantin> 1.1.1-1.mga6
+ Revision: 868417
- new version 1.1.1
* Wed Oct 15 2014 umeabot <umeabot> 1.1.0-3.mga5
+ Revision: 746283
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 1.1.0-2.mga5
+ Revision: 679060
- Mageia 5 Mass Rebuild
* Mon Jul 21 2014 wally <wally> 1.1.0-1.mga5
+ Revision: 655278
- new version 1.1.0
* Sat Oct 19 2013 umeabot <umeabot> 1.0.1-2.mga4
+ Revision: 523743
- Mageia 4 Mass Rebuild
* Fri May 24 2013 wally <wally> 1.0.1-1.mga4
+ Revision: 426804
- new version 1.0.1
- rediff P0
* Fri Jan 11 2013 umeabot <umeabot> 0.9.8-2.mga3
+ Revision: 349856
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Oct 09 2012 wally <wally> 0.9.8-1.mga3
+ Revision: 303948
- import exfat-utils based on .spec from upstream
