Summary:	Filesystem benchmark tool
Name:		iozone3
Version:	420
Release:	4.1
License:	Public Domain
Group:		Monitoring
URL:		http://www.iozone.org/
Source0:	http://www.iozone.org/src/current/%{name}_%{version}.tar

%description
This program allows one to characterize the filesystem performance
of vendors platform. It supports single stream, throughput,
pthreads, async I/O and much more.

%prep
%setup -n %{name}_%{version}

%build
make -C src/current linux CFLAGS="%{optflags}" LDFLAGS="%{optflags} -Wl,--allow-multiple-definition"

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 src/current/iozone %{buildroot}%{_bindir}
install -m 755 src/current/gnu3d.dem %{buildroot}%{_bindir}
install -m 755 src/current/gengnuplot.sh %{buildroot}%{_bindir}
install -m 755 src/current/fileop %{buildroot}%{_bindir}
install -m 755 src/current/Generate_Graphs %{buildroot}%{_bindir}
install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 docs/iozone.1 %{buildroot}%{_mandir}/man1

%files
%doc docs/*.gz src/current/Gnuplot.txt docs/*.pdf docs/*.doc
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 420
- Rebuild for Fedora
* Sat Oct 19 2013 umeabot <umeabot> 420-2.mga4
+ Revision: 530327
- Mageia 4 Mass Rebuild
* Mon Jul 22 2013 dams <dams> 420-1.mga4
+ Revision: 457233
- new version 420
* Sat Jan 12 2013 umeabot <umeabot> 414-2.mga3
+ Revision: 354443
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Nov 06 2012 dams <dams> 414-1.mga3
+ Revision: 314582
- new version 414
- clean specfile
* Tue Jul 12 2011 dams <dams> 397-1.mga2
+ Revision: 123075
- Update to 397
* Fri Apr 08 2011 ennael <ennael> 326-2.mga1
+ Revision: 82120
- clean spec file
- imported package iozone3
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 326-2mdv2011.0
+ Revision: 619675
- the mass rebuild of 2010.0 packages
* Mon Sep 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 326-1mdv2010.0
+ Revision: 440691
- update to new version 326
- compile with %%optflags and %%ldflags
- spec file clean
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 287-4mdv2010.0
+ Revision: 429516
- rebuild
* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 287-3mdv2009.0
+ Revision: 247242
- rebuild
* Tue Feb 26 2008 Erwan Velu <erwan@mandriva.org> 287-1mdv2008.1
+ Revision: 175414
- release 287
  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 281-1mdv2008.1
+ Revision: 131599
- kill re-definition of %%buildroot on Pixel's request
* Thu Feb 01 2007 Lenny Cartier <lenny@mandriva.com> 281-1mdv2007.0
+ Revision: 115813
- Import iozone3
