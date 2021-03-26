Summary:	Tiny C Compiler
Name:		tcc
Version:	0.9.27
Release:	3.1
License:	GPL
Group:		Development/C
URL:		http://bellard.org/tcc/
Source0:	http://download.savannah.nongnu.org/releases/tinycc/%{name}-%{version}.tar.bz2
BuildRequires:	texi2html

%description
C Scripting Everywhere - The Smallest ANSI C compiler.

%prep
%setup -q
sed -i 's|/usr/local|/usr|' configure examples/ex?.c README tcc-doc.html tcc-doc.texi tcc.h

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_docdir}/tcc-doc.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Changelog README TODO *.html examples
%{_bindir}/tcc
%{_libdir}/tcc
%{_libdir}/*.a
%{_includedir}/*.h
%{_mandir}/man1/tcc.1*
%{_datadir}/info/*

%changelog
* Mon May 14 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.27
- Rebuild for Fedora
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.25-2mdv2011.0
+ Revision: 615165
- the mass rebuild of 2010.1 packages
* Tue Dec 01 2009 Thierry Vignaud <tv@mandriva.org> 0.9.25-1mdv2010.1
+ Revision: 472432
- adjust file list for both x86_64 and ia32
- enable build on x86_64 and fix path (patch 3)
- drop patches 1 & 2 (uneeded)
- replace patch 0 by a one-liner perl command
- fix installing
- use %%configure2_5x
- adjust file list
- new release
- new URL
- rebuild
* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.9.23-6mdv2009.0
+ Revision: 242855
- rebuild
- kill re-definition of %%buildroot on Pixel's request
  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Fri Aug 10 2007 Pascal Terjan <pterjan@mandriva.org> 0.9.23-4mdv2008.0
+ Revision: 61306
- Rebuild to sync x86_64
* Mon Feb 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.9.23-3mdv2007.0
+ Revision: 122783
- rebuild in order to get the same extension on x86_64
- Import tcc
* Mon Jun 05 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.23-2mdv2007.0
- fix #22862 (P1)
- added debian patches
* Fri Jun 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.23-1mdv2007.0
- 0.9.23
* Wed May 24 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.9.22-2mdk
- use %%mkrel 2
- rebuild with new toolchain
* Fri May 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.22-1mdk
- 0.9.22
- added P0 by Paul Furber to make is somewhat work under x86_64
* Sat Apr 24 2004 Michael Scherer <misc@mandrake.org> 0.9.20-1mdk
- New release 0.9.20
