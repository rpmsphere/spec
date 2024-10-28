Summary:        Utilities for configuring ISA Plug-and-Play (PnP) devices
Name:           isapnptools
Version:        1.27
Release:        6.1
License:        GPLv2+
Group:          System/Kernel and hardware
URL:            https://www.roestock.demon.co.uk/isapnptools/
Source0:        ftp://metalab.unc.edu/pub/Linux/system/hardware/%{name}-%{version}.tgz
Patch1:         %{name}-demo2.patch
Patch2:         isapnptools-1.26-gcc4-fix.patch
Patch3:         isapnptools-1.26-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:  flex

%description
The isapnptools package contains utilities for configuring ISA
Plug-and-Play (PnP) cards which are in compliance with the PnP ISA
Specification Version 1.0a.  ISA PnP cards use registers instead of
jumpers for setting the board address and interrupt assignments.  The
cards also contain descriptions of the resources which need to be
allocated.  The BIOS on your system, or isapnptools, uses a protocol
described in the specification to find all of the PnP boards and
allocate the resources so that none of them conflict.

Note that the BIOS doesn't do a very good job of allocating resources.
So isapnptools is suitable for all systems, whether or not they
include a PnP BIOS. In fact, a PnP BIOS adds some complications.  A
PnP BIOS may already activate some cards so that the drivers can find
them.  Then these tools can unconfigure them or change their settings,
causing all sorts of nasty effects. If you have PnP network cards that
already work, you should read through the documentation files very
carefully before you use isapnptools.

Install isapnptools if you need utilities for configuring ISA PnP
cards.

%package        devel
Summary:        Devel libraries for configuring ISA Plug-and-Play (PnP) devices
Group:          Development/C

%description    devel
The isapnptools package contains utilities for configuring ISA
Plug-and-Play (PnP) cards which are in compliance with the PnP ISA
Specification Version 1.0a.  ISA PnP cards use registers instead of
jumpers for setting the board address and interrupt assignments.  The
cards also contain descriptions of the resources which need to be
allocated.  The BIOS on your system, or isapnptools, uses a protocol
described in the specification to find all of the PnP boards and
allocate the resources so that none of them conflict.

Note that the BIOS doesn't do a very good job of allocating resources.
So isapnptools is suitable for all systems, whether or not they
include a PnP BIOS. In fact, a PnP BIOS adds some complications.  A
PnP BIOS may already activate some cards so that the drivers can find
them.  Then these tools can unconfigure them or change their settings,
causing all sorts of nasty effects. If you have PnP network cards that
already work, you should read through the documentation files very
carefully before you use isapnptools.

Install isapnptools-devel if you need to do development with ISA PnP
cards.

%prep
%setup -q
%patch 1 -p1
%patch 3 -p0 -b .format_not_a_string_literal_and_no_format_arguments
find | xargs chmod u+w

%build
export LDFLAGS=-Wl,--allow-multiple-definition
#ifarch aarch64
#export CC=clang CXX=clang++
#endif
%configure
make
perl -pi -e "s/^\([^#]\)/#\1/" etc/isapnp.gone
%ifarch alpha aarch64
perl -pi -e "s/#IRQ 7/IRQ 7/" etc/isapnp.gone
%endif 

%install
%make_install
install -m644 etc/isapnp.gone -D %{buildroot}%{_sysconfdir}/isapnp.gone

%files
%doc README
%doc config-scripts/YMH0021
%config(missingok,noreplace) %attr(0644,root,root) %{_sysconfdir}/isapnp.gone
%{_sbindir}/*
%{_mandir}/man*/*

%files devel
%doc AUTHORS COPYING NEWS doc
%{_libdir}/*.a
%{_includedir}/isapnp

%changelog
* Sun Mar 26 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.27
- Rebuild to Fedora
* Sun Jun 15 2014 wally <wally> 1.27-4.mga5
+ Revision: 636634
- rebuild for mga5
* Wed Jan 23 2013 fwang <fwang> 1.27-3.mga3
+ Revision: 391275
- update rpm group
* Sat Jan 12 2013 umeabot <umeabot> 1.27-2.mga3
+ Revision: 354508
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Sep 13 2012 fwang <fwang> 1.27-1.mga3
+ Revision: 293647
- new version 1.27
* Sat Feb 18 2012 pterjan <pterjan> 1.26-16.mga2
+ Revision: 210449
- Fix license tag
* Wed Mar 23 2011 ennael <ennael> 1.26-15.mga1
+ Revision: 75829
- clean spec file
- imported package isapnptools
* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.26-15mdv2011.0
+ Revision: 605984
- rebuild
* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.26-14mdv2010.1
+ Revision: 520133
- rebuilt for 2010.1
* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.26-13mdv2010.0
+ Revision: 425388
- rebuild
* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 1.26-12mdv2009.1
+ Revision: 316954
- fix build with -Werror=format-security (P3)
* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.26-11mdv2009.0
+ Revision: 221644
- rebuild
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 1.26-10mdv2008.1
+ Revision: 134100
- rebuild
* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.26-9mdv2008.1
+ Revision: 127177
- kill re-definition of %%buildroot on Pixel's request
* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1.26-9mdv2007.1
+ Revision: 145398
- Import isapnptools
* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1.26-9mdv2007.1
- use the %%mrel macro
- bunzip patches
* Sat Sep 10 2005 Olivier Blin <oblin@mandriva.com> 1.26-8mdk
- fix typo in summary
* Fri Aug 19 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.26-7mdk
- fix build with gcc 4 (P2)
- fix file permissions
- %%mkrel
