Summary: 	Themes for the Matchbox Desktop
Name: 		matchbox-themes-extra
Version: 	0.3
Release: 	8.1
URL: 		https://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	https://matchbox-project.org/sources/matchbox-themes-extra/%version/%{name}-%{version}.tar.bz2
BuildArch:	noarch

%description
Extra themes for the Matchbox Desktop.

%prep
%setup -q

%build
%configure
make

%install
%makeinstall

%files
%doc README TODO
%{_datadir}/icons/*
%{_datadir}/themes/*

%changelog
* Fri Feb 20 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_7
- update by mgaimport
* Fri Oct 18 2013 umeabot <umeabot> 0.3-7.mga4
+ Revision: 507725
- Mageia 4 Mass Rebuild
* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_6
- update by mgaimport
* Sat Jan 12 2013 umeabot <umeabot> 0.3-6.mga3
+ Revision: 359431
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_5
- mageia import
* Sun Apr 10 2011 dmorgan <dmorgan> 0.3-5.mga1
+ Revision: 82946
- imported package matchbox-themes-extra
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.3-5mdv2010.0
+ Revision: 429964
- rebuild
* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-4mdv2009.0
+ Revision: 252056
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request
* Tue Nov 06 2007 Funda Wang <fundawang@mandriva.org> 0.3-2mdv2008.1
+ Revision: 106257
- Rebuild
- import matchbox-themes-extra
* Tue Jul 27 2004 Austin Acton <austin@mandrake.org> 0.3-1mdk
- initial package
