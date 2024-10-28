Summary:        GTK+ Object Builder
Name:           gob2
Version:        2.0.20
Release:        7
License:        GPLv2+
Group:          Development/GNOME and GTK+
Source0:        https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz
URL:            https://www.jirka.org/gob.html
BuildRequires:  flex
BuildRequires:  glib2-devel

%description
GOB2 is a simple preprocessor for making GTK+ objects.  It makes objects
from a single file which has inline C code so that you don't have to edit
the generated files.  Syntax is somewhat inspired by java and yacc.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc README AUTHORS NEWS TODO ChangeLog
%doc examples
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/aclocal/*

%changelog
* Sun May 8 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.20
- Rebuilt for Fedora
* Thu Mar 17 2022 umeabot <umeabot> 2.0.20-7.mga9
+ Revision: 1797053
- Mageia 9 Mass Rebuild
* Thu Feb 13 2020 umeabot <umeabot> 2.0.20-6.mga8
+ Revision: 1512622
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%configure2_5x
* Sun Sep 23 2018 umeabot <umeabot> 2.0.20-5.mga7
+ Revision: 1298006
- Mageia 7 Mass Rebuild
+ kekepower <kekepower>
- Use new make macros
* Mon Feb 08 2016 umeabot <umeabot> 2.0.20-4.mga6
+ Revision: 948148
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 2.0.20-3.mga5
+ Revision: 749342
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 2.0.20-2.mga5
+ Revision: 679843
- Mageia 5 Mass Rebuild
* Tue Feb 04 2014 ovitters <ovitters> 2.0.20-1.mga5
+ Revision: 582557
- new version 2.0.20
* Fri Oct 18 2013 umeabot <umeabot> 2.0.19-3.mga4
+ Revision: 505140
- Mageia 4 Mass Rebuild
* Sat Jan 12 2013 umeabot <umeabot> 2.0.19-2.mga3
+ Revision: 352397
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
+ tv <tv>
- fix URL
* Wed Dec 19 2012 ovitters <ovitters> 2.0.19-1.mga3
+ Revision: 332808
- new version 2.0.19
- switch to xz tarballs
* Sun Jan 22 2012 kamil <kamil> 2.0.18-2.mga2
+ Revision: 199591
- update SOURCE
- clean .spec
* Sun Jan 23 2011 pterjan <pterjan> 2.0.18-1.mga1
+ Revision: 35499
- imported package gob2
* Thu Jan 06 2011 Götz Waschk <waschk@mandriva.org> 2.0.18-1mdv2011.0
+ Revision: 629183
- update to new version 2.0.18
* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.17-2mdv2011.0
+ Revision: 605490
- rebuild
* Fri Apr 02 2010 Götz Waschk <waschk@mandriva.org> 2.0.17-1mdv2010.1
+ Revision: 530794
- update to new version 2.0.17
* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.16-2mdv2010.1
+ Revision: 522742
- rebuilt for 2010.1
* Tue Jul 21 2009 Götz Waschk <waschk@mandriva.org> 2.0.16-1mdv2010.0
+ Revision: 398434
- new version
- drop patch
* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 2.0.15-2mdv2009.1
+ Revision: 364958
- fix str fmt
* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.0.15-2mdv2009.0
+ Revision: 221096
- rebuild
- kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Wed Nov 21 2007 Götz Waschk <waschk@mandriva.org> 2.0.15-1mdv2008.1
+ Revision: 110868
- new version
* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 2.0.14-3mdv2008.0
+ Revision: 91342
- rebuild for 2008
- don't package COPYING
- new license policy
- minor spec clean
* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.0.14-2mdv2007.0
+ Revision: 108670
- Import gob2
* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.0.14-2mdv2007.1
- Rebuild
* Fri Jan 06 2006 Götz Waschk <waschk@mandriva.org> 2.0.14-1mdk
- New release 2.0.14
* Mon Dec 19 2005 Götz Waschk <waschk@mandriva.org> 2.0.13-1mdk
- New release 2.0.13
- use mkrel
* Tue Jul 26 2005 Götz Waschk <waschk@mandriva.org> 2.0.12-1mdk
- New release 2.0.12
* Thu Oct 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.11-1mdk
- New release 2.0.11
* Wed Jul 21 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.9-1mdk
- fix source URL
- New release 2.0.9
* Thu Jun 24 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.8-1mdk
- New release 2.0.8
* Wed Apr 07 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.7-1mdk
- new version