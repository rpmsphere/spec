Name: bb
Summary: AAlib demo
Version: 1.3.0
Release: 12.4
Source: %{name}-%{version}.tar.bz2 
Patch1: %{name}-1.3.0-timer.patch
Group: Games/Other
URL: https://aa-project.sourceforge.net/aalib/
BuildRequires:  aalib-devel
BuildRequires:  libmikmod-devel
License: GPLv2+

%description
BB is a portable demo based on AAlib.

%prep
%setup -q
%patch 1 -p0 -b .timers

%build
%configure 
make

%install
rm -r $RPM_BUILD_ROOT
%makeinstall 

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

%changelog
* Mon Apr 18 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0
- Rebuilt for Fedora
* Fri Oct 18 2013 umeabot <umeabot> 1.3.0-12.mga4
+ Revision: 503036
- Mageia 4 Mass Rebuild
* Fri Jan 11 2013 umeabot <umeabot> 1.3.0-11.mga3
+ Revision: 346877
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Fri May 06 2011 nanardon <nanardon> 1.3.0-10.mga1
+ Revision: 95628
- imported package bb
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-10mdv2011.0
+ Revision: 616712
- the mass rebuild of 2010.0 packages
* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.3.0-9mdv2010.0
+ Revision: 424020
- rebuild
* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 1.3.0-8mdv2009.0
+ Revision: 271778
- update license
* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.3.0-7mdv2009.0
+ Revision: 243168
- rebuild
* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.3.0-5mdv2008.1
+ Revision: 135828
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Fri Jun 01 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.3.0-5mdv2008.0
+ Revision: 34292
- Rebuild with libslang2.
* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 20:36:53 (52869)
- rebuild
* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 20:33:16 (52868)
Import bb
* Tue Oct 04 2005 Olivier Thauvin <nanardon@mandriva.org> 1.3.0-3mdk
- rebuild
* Sun Jul 25 2004 Marcel Pol <mpol@mandrake.org> 1.3.0-2mdk
- patch1: suse patch for timers.c
- clean in %%install, not in %%prep
- fix buildrequires
