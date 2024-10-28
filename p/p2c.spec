Summary:        A Pascal to C translator
Name:           p2c
Version:        1.22
Release:        26.1
License:        GPL
Group:          Development/Other
Source0:        ftp://csvax.cs.caltech.edu/pub/p2c-1.22.tar.bz2
URL:            https://www.ccrnp.ncifcrf.gov/~toms/p2c/
Patch2:         p2c-newpatch.patch
# Fixes conflicting types for 'my_memcpy' build error: thanks Anssi
Patch3:         p2c-1.22-memcpy.patch
Patch4:         p2c-1.22-getline.patch

%description
P2c is a system for translating Pascal programs into the C language.
P2c accepts input source files in certain Pascal dialects:  HP
Pascal, Turbo/UCSD Pascal, DEC VAX Pascal, Oregon Software Pascal/2,
Macintosh Programmer's Workshop Pascal and Sun/Berkeley Pascal.  P2c
outputs a set of .c and .h files which make up a C program equivalent
to the original Pascal program.  The C program can then be compiled
using a standard C compiler, such as gcc.

Install the p2c package if you need a program for translating Pascal
code into C code.

%package        devel
Summary:        Files for p2c Pascal to C translator development
Group:          Development/Other

%description    devel
The p2c-devel package contains the files necessary for development
of the p2c Pascal to C translation system.

Install the p2c-devel package if you want to do p2c development.

%prep
%setup -q
%patch 2 -p1 -b .new
%patch 3 -p1 -b .memcpy
%patch 4 -p0 -b .getline
mkdir src/shlib
mkdir include
ln -s ../src include/p2c

%build
cp src/sys.p2crc src/p2crc
make RPM_OPTS="$RPM_OPT_FLAGS -fPIC"
make RPM_OPTS="$RPM_OPT_FLAGS -fPIC" shlib -C src

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}{%{_mandir}/man1,%{_prefix}/lib,%{_libdir},%{_includedir}}
make install RPM_INSTALL=%{buildroot} LIBDIR=$RPM_BUILD_ROOT%{_libdir} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/p2c*
%{_libdir}/libp2c.so*
%{_prefix}/lib/p2c
%{_mandir}/man1/p2c.1*

%files devel
%{_libdir}/libp2c.a
%{_includedir}/p2c

%changelog
* Sun Nov 18 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.22
- Rebuilt for Fedora
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.22-19mdv2011.0
+ Revision: 666972
- mass rebuild
* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.22-18mdv2011.0
+ Revision: 607048
- rebuild
* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.22-17mdv2010.1
+ Revision: 523544
- rebuilt for 2010.1
* Sun Oct 04 2009 Funda Wang <fwang@mandriva.org> 1.22-16mdv2010.0
+ Revision: 453307
- fix getline conflicts
* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1.22-15mdv2009.1
+ Revision: 365982
- rediff memcpy patch
* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.22-15mdv2009.0
+ Revision: 223406
- rebuild
  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.22-14mdv2008.1
+ Revision: 179115
- rebuild
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Fri Jun 08 2007 Adam Williamson <awilliamson@mandriva.org> 1.22-13mdv2008.0
+ Revision: 37052
- bunzip2 patch; fix build (patch3); rebuild for new era
- Import p2c
* Tue May 03 2005 PerØyvind Karlsen <pkarlsen@mandriva.com> 1.22-12mdk
- compile with -fPIC (fixes build on x86_64)
- fix lib64 path
- let rpm take care of stripping binaries and bzip2'ing man pages
- fix summary-ended-with-dot
- cosmetics
* Wed Jul 23 2003 PerØyvind Karlsen <peroyvind@sintrax.net> 1.22-11mdk
- rebuild
- macroize
- fix install
* Thu Jan 16 2003 Daouda LO <daouda@mandrakesoft.com> 1.22-10mdk
- rebuild (glibc and/or unpackaged files)
- new URL
- GPL license
* Sun Feb  3 2002 Daouda LO <daouda@mandrakesoft.com> 1.22-9mdk
- rebuild ( cleanup - URL tag ... )
* Tue Mar 6 2001 Daouda Lo <daouda@mandrakesoft.com> 1.22-8mdk
- spec clean up
- rebuild -> add p2cc
- replace buildroot dir
* Tue Aug 29 2000 Etienne Faure <etienne@mandrakesoft.com> 1.22-7mdk
- use _mandir macro
* Mon Apr  3 2000 Adam Lebsack <adam@mandrakesoft.com> 1.22-6mdk
- Release build.
* Mon Nov 29 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- move defattr to before doc
* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
* Mon Apr 12 1999 Preston Brown <pbrown@redhat.com>
- fixed group.
* Sun Mar 21 1999 Michael Maher <mike@redhat.com>
- Merged patched tar ball on gribble with original 
  installation.  Was missing important parts of 
  make files.  
- Fixed many errors in Makefiles. 
- moved 'basic' stuff into doc
* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1
- buildroot
- binary files and man page should really be in the main package, 
  not -devel
* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
