Summary:	Parity Archive Volume Set
Name:		parchive2
Version:	0.4
Release:	10.1
Group:		Archiving/Backup
License:	GPL
URL:		http://parchive.sourceforge.net/
Source:		http://sourceforge.net/projects/parchive/files/par2cmdline/0.4/par2cmdline-0.4.tar.gz
Patch0:		par2cmdline-gcc4.patch.bz2

%description
The idea behind this project is to provide a tool to apply the data-
recovery capability concepts of RAID-like systems to the posting and
recovery of multi-part archives on Usenet. With a parity archive, this
tool, and all but one part of a multi-part set you can recover the
missing part.

The key to this mission is a clean file format specification which
provides all the necessary capabilities for programs to easily verify
and regenerate single missing parts out of a set of archives.

We might just be able to make binary posting and downloading on Usenet a
little easier. That's a pretty cool goal!

par2 is complete rewrite of parchive with much additional advantages.
Read all about them on this page:
  http://www.pbclements.co.uk/QuickPar/AboutPAR2.htm

Tip of the day: alias par='par2 r *.((p|P)??|par2)'


%prep
%setup -q -n par2cmdline-0.4
%patch0 -p1

%build
%configure
make

%install
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,755)
%doc AUTHORS COPYING README ROADMAP
%{_bindir}/*

%changelog
* Tue Jan 14 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
* Fri Oct 18 2013 umeabot <umeabot> 0.4-10.mga4
+ Revision: 521327
- Mageia 4 Mass Rebuild
* Mon Jan 21 2013 malo <malo> 0.4-9.mga3
+ Revision: 390331
- updated RPM group
* Sun Jan 13 2013 umeabot <umeabot> 0.4-8.mga3
+ Revision: 362401
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Apr 12 2011 ahmad <ahmad> 0.4-7.mga1
+ Revision: 84023
- imported package parchive2
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4-6mdv2010.0
+ Revision: 430238
- rebuild
* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4-5mdv2009.0
+ Revision: 255036
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- kill extra spacing at top of description
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Sun Dec 09 2007 Olivier Thauvin <nanardon@mandriva.org> 0.4-3mdv2008.1
+ Revision: 116614
- rebuild
- import parchive2
* Mon Jan 02 2006 Lenny Cartier <lenny@mandriva.com> 0.4-2mdk
- rebuild with debian patch
* Tue Jun 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.4-1mdk
- 0.4
* Sat Jul 19 2003 Han Boetes <han@linux-mandrake.com> 0.3-1mdk
- bump
* Fri May 30 2003 Han Boetes <han@linux-mandrake.com> 0.2-1mdk
- Initial MDK built
