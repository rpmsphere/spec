%undefine _debugsource_packages
%define old_name gcom

Summary:        GPRS/EDGE/3G/HSDPA datacard control tool
Name:           comgt
Version:        0.32
Release:        6.1
Source0:        https://www.pharscape.org/3G/%{name}/%{name}.%{version}.tgz
Patch0:         comgt-0.32-string-format.patch
Patch1:         comgt-0.32-fix-man-page-typo.patch
License:        GPLv2+
Group:          Communications/Mobile
URL:            https://pharscape.org/comgt.html
Provides:       %{old_name} = %{version}-%{release}
Obsoletes:      %{old_name} < %{version}-%{release}
Requires:       usb_modeswitch

%description
comgt is a datacard control tool for Option GlobeTrotter
GPRS/EDGE/3G/HSDPA and Vodafone 3G/GPRS.

It is a scripting language interpreter useful for establishing
communications on serial lines and through PCMCIA modems as well as
GPRS and 3G datacards.

comgt has some features that are rarely found in other utilities of the
same type.

%prep
%setup -q -n %{name}.%{version}
%autopatch -p1

%build
make

%install
install -m755 %{name} -D %{buildroot}%{_sbindir}/%{name}
install -m644 %{name}.1 -D %{buildroot}%{_mandir}/man1/%{name}.1
ln -s %{_sbindir}/%{name} %{buildroot}%{_sbindir}/%{old_name}

%files
%doc CHANGELOG gprs.txt TODO umts.txt
%{_mandir}/man1/%{name}.1*
%{_sbindir}/%{name}
%{_sbindir}/%{old_name}

%changelog
* Fri Jul 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.32
- Rebuilt for Fedora
* Fri Feb 05 2016 umeabot <umeabot> 0.32-19.mga6
+ Revision: 937640
- Mageia 6 Mass Rebuild
* Fri Feb 05 2016 umeabot <umeabot> 0.32-18.mga6
+ Revision: 937187
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 0.32-17.mga5
+ Revision: 744127
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.32-16.mga5
+ Revision: 678497
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 0.32-15.mga4
+ Revision: 503453
- Mageia 4 Mass Rebuild
* Fri Jan 11 2013 umeabot <umeabot> 0.32-14.mga3
+ Revision: 348083
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sat Oct 20 2012 malo <malo> 0.32-13.mga3
+ Revision: 308487
- spec clean-up
- update RPM group
* Sun Jan 23 2011 blino <blino> 0.32-12.mga1
+ Revision: 33358
- imported package comgt
* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.32-12mdv2011.0
+ Revision: 603842
- rebuild
* Wed May 19 2010 Olivier Blin <oblin@mandriva.com> 0.32-11mdv2010.1
+ Revision: 545448
- require usb_modeswitch since most modems needs to switched explicitely to 3G mode nowadays (#57544)
* Mon Mar 29 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.32-10mdv2010.1
+ Revision: 528749
- fix permissions of docs
- fix typo in man page (P1)
- update URL
- build with %%optflags & %%ldflags
- fix build with -Werror=format-security (P0)
- be more accurate on GPL versioning for license
- don't define name, version & release on top of spec
- cosmetics
* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.32-9mdv2010.1
+ Revision: 520030
- rebuilt for 2010.1
* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.32-8mdv2010.0
+ Revision: 413258
- rebuild
* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.32-7mdv2009.1
+ Revision: 350729
- rebuild
* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.32-6mdv2009.0
+ Revision: 220507
- rebuild
* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.32-5mdv2008.1
+ Revision: 149125
- rebuild
- kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Tue Jun 26 2007 Adam Williamson <awilliamson@mandriva.org> 0.32-2mdv2008.0
+ Revision: 44575
- restore gcom (needed for drakconnect)
* Wed Jun 20 2007 Adam Williamson <awilliamson@mandriva.org> 0.32-1mdv2008.0
+ Revision: 41675
- new release 0.32; rebuild for 2008
- Import comgt
* Thu Sep  7 2006 Olivier Blin <blino@seggie.mandriva.com> 0.3-2mdv2007.0
- gcom has changed name to comgt
* Thu Apr 20 2006 Olivier Blin <oblin@mandriva.com> 0.3-1mdk
- initial release
