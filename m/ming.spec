%define _legacy_common_support 1

Summary:        An SWF output library
Name:           ming
Version:        0.4.9
Release:        0.git20181112.7
License:        LGPLv2
Group:          System/Libraries
URL:            https://www.libming.org/
#Source0:       https://prdownloads.sourceforge.net/ming/%%{name}-%%{version}.tar.bz2
Source0:        https://github.com/libming/libming/archive/master.zip
# make ming-config multilib-compatible
Patch0:         ming-multilib.patch
# install perl modules to vendorarch dir and link dynamically with libming.so
Patch1:         ming-perl.patch
# fix parallel make calls to bison causing generated code corruption
# https://github.com/libming/libming/issues/49
Patch2:         ming-parallel-make.patch
# drop -dev from version, perl doesn't like it
Patch4:         ming-version.patch
# https://github.com/libming/libming/pull/145
Patch100:       ming-pr145.patch
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
#BuildRequires: multiarch-utils >= 1.0.3
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  giflib-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xcb)

# gotta conflict here, otherwise stuff will be linked against installed libs...
BuildConflicts: ming-devel

%description
Ming is a c library for generating SWF ("Flash") format movies. This
package only contains the basic c-based library.

%package        devel
Summary:        Ming development files
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}

%description devel
The %{name}-devel package contains the header files
and static libraries necessary for developing programs using the
%{name}-devel library (C and C++).

%package -n     perl-SWF
Summary:        Ming perl module
Group:          Development/Perl
Provides:       perl-ming
Obsoletes:      perl-ming
Requires:       %{name} = %{version}-%{release}

%description -n perl-SWF
Ming perl module - perl wrapper for the Ming library.

%package        utils
Summary:        Ming utilities
Group:          File tools
Requires:       %{name} = %{version}-%{release}

%description utils
This package contains various ming utilities.

%prep
%setup -qn libming-master
%autopatch -p1

%build
./autogen.sh
autoreconf -fi
%configure --disable-static \
           --disable-python
%make_build

pushd perl_ext
    perl Makefile.PL LIBS="-L%{_libdir} -ljpeg -lpng -lz -lm -lgif" INSTALLDIRS=vendor </dev/null
    make
#    make test
popd

#check
#make_build check

%install
%make_install

# install the perl extension
%make_install -C perl_ext

# fix docs
cp perl_ext/README perl_ext.README
cp util/README util.README
chmod 644 NEWS HISTORY INSTALL *README* TODO

# cleanup
rm -rf %{buildroot}%{perl_vendorlib}/*/auto/SWF/include

# nuke rpath
find %{buildroot}%{perl_vendorarch} -name "*.so" | xargs chmod 0755
find %{buildroot}%{perl_vendorarch} -name "*.so" | xargs chrpath -d

find %{buildroot} -name '*.la' -delete

#multiarch_binaries %{buildroot}%{_bindir}/ming-config

%files
%doc NEWS HISTORY README TODO
%{_libdir}/libming.so.*

%files devel
#{multiarch_bindir}/ming-config
%{_bindir}/ming-config
%{_libdir}/libming.so
%{_libdir}/pkgconfig/libming.pc
%{_includedir}/*
#%%{_mandir}/man3/Ming_*
#%%{_mandir}/man3/destroySWFMovie.3*
#%%{_mandir}/man3/newSWF*

%files -n perl-SWF
%doc perl_ext.README perl_ext/examples
%{perl_vendorarch}/SWF
%{perl_vendorarch}/SWF.pm
%{perl_vendorarch}/auto/SWF
%{_mandir}/man3*/SWF*
%exclude %{_libdir}/perl5/perllocal.pod

%files utils
%doc util.README
%{_bindir}/dbl2png
%{_bindir}/gif2dbl
%{_bindir}/gif2mask
%{_bindir}/listaction
%{_bindir}/listaction_d
%{_bindir}/listfdb
%{_bindir}/listjpeg
%{_bindir}/listmp3
%{_bindir}/listswf
%{_bindir}/listswf_d
%{_bindir}/makefdb
%{_bindir}/makeswf
%{_bindir}/png2dbl
%{_bindir}/raw2adpcm
%{_bindir}/swftocxx
%{_bindir}/swftoperl
%{_bindir}/swftophp
%{_bindir}/swftopython
%{_bindir}/swftotcl

%changelog
* Sun Jul 17 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.9-0.git20181112.7
- Rebuilt for Fedora
* Wed Feb 03 2021 daviddavid <daviddavid> 0.4.9-0.git20181112.7.mga8
+ Revision: 1674603
- disable python2 support
* Thu Jul 23 2020 pterjan <pterjan> 0.4.9-0.git20181112.6.mga8
+ Revision: 1608596
- Add _legacy_common_support
+ umeabot <umeabot>
- Rebuild for perl 5.32
* Tue Feb 18 2020 umeabot <umeabot> 0.4.9-0.git20181112.5.mga8
+ Revision: 1541355
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%configure2_5x
* Thu Dec 26 2019 ns80 <ns80> 0.4.9-0.git20181112.4.mga8
+ Revision: 1470088
- obsolete python-SWF which requires python2
- sync with fedora for CVE-2018-7866, CVE-2018-7873, CVE-2018-7876, CVE-2018-9009, CVE-2018-9132 (mga#25957)
* Tue Aug 27 2019 tmb <tmb> 0.4.9-0.git20181112.3.mga8
+ Revision: 1433903
- rebuild for perl 5.30
* Wed Mar 27 2019 ns80 <ns80> 0.4.9-0.git20181112.2.mga7
+ Revision: 1380596
- update to latest git snapshot for CVE-2018-6358, CVE-2018-786[78], CVE-2018-787[0125], CVE-2018-9165 (mga#24505)
* Sun Sep 23 2018 umeabot <umeabot> 0.4.5-18.mga7
+ Revision: 1299545
- Mageia 7 Mass Rebuild
* Tue Aug 07 2018 guillomovitch <guillomovitch> 0.4.5-17.mga7
+ Revision: 1248765
- rebuild for perl 5.28
* Fri Apr 20 2018 ns80 <ns80> 0.4.5-16.mga7
+ Revision: 1220531
- add patches from fedora for CVE-2017-8782, CVE-2017-998[89], CVE-2017-11704, CVE-2017-1172[89], CVE-2017-1173[0-4], CVE-2017-16883, CVE-2017-16898, CVE-2018-5251, CVE-2018-5294, CVE-2018-6315, CVE-2018-6359 (mga#22815)
* Sat Jul 22 2017 neoclust <neoclust> 0.4.5-15.mga7
+ Revision: 1127216
- Rebuild against new Perl 5.26
* Fri Apr 07 2017 ns80 <ns80> 0.4.5-14.mga6
+ Revision: 1096073
- add a patch for CVE-2017-7578 (incomplete fix for CVE-2016-9831)
* Mon Feb 20 2017 ns80 <ns80> 0.4.5-13.mga6
+ Revision: 1086996
- add patches for CVE-2016-926[4-6], CVE-2016-982[7-9] and CVE-2016-9831 (mga#19751)
* Sat Jun 18 2016 pterjan <pterjan> 0.4.5-12.mga6
+ Revision: 1022161
- Rebuild for perl 5.22.2
* Thu Jan 07 2016 luigiwalser <luigiwalser> 0.4.5-11.mga6
+ Revision: 920403
- rebuild for giflib
- add patch from omdv to fix build with giflib5
* Sat Jun 27 2015 tv <tv> 0.4.5-10.mga6
+ Revision: 846156
- rebuild with soname-ified perl
* Tue Jun 23 2015 sander85 <sander85> 0.4.5-9.mga6
+ Revision: 841637
- Rebuild for perl 5.22
* Wed Oct 15 2014 umeabot <umeabot> 0.4.5-8.mga5
+ Revision: 746898
- Second Mageia 5 Mass Rebuild
* Sat Sep 27 2014 tv <tv> 0.4.5-7.mga5
+ Revision: 727289
- rebuild for missing pythoneggs deps
* Tue Sep 16 2014 umeabot <umeabot> 0.4.5-6.mga5
+ Revision: 682398
- Mageia 5 Mass Rebuild
* Tue Jun 03 2014 pterjan <pterjan> 0.4.5-5.mga5
+ Revision: 630733
- Rebuild for perl 5.20
* Sat May 31 2014 pterjan <pterjan> 0.4.5-4.mga5
+ Revision: 628338
- Rebuild for new Python
* Tue Dec 17 2013 danf <danf> 0.4.5-3.mga4
+ Revision: 558275
- Enabled build-time unit tests
- Added giferrorstring.patch to fix a build issue
+ fwang <fwang>
- fix perm
+ umeabot <umeabot>
- Mageia 4 Mass Rebuild
+ pterjan <pterjan>
- Rebuild to add different pythonegg provides for python 2 and 3
+ blue_prawn <blue_prawn>
- WIP about GifError() function
- updated to last version 0.4.5
* Sun Jun 02 2013 fwang <fwang> 0.4.4-4.mga4
+ Revision: 434932
- rebuild for new libpng
* Wed May 29 2013 fwang <fwang> 0.4.4-3.mga4
+ Revision: 430306
- rebuild for new perl
* Sun Jan 13 2013 luigiwalser <luigiwalser> 0.4.4-2.mga3
+ Revision: 362402
- try to fix giflib API problem
- fix for automake 1.13
+ umeabot <umeabot>
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sat Sep 22 2012 fwang <fwang> 0.4.4-1.mga3
+ Revision: 296572
- clean up spec
- update file list
- drop .a and .la files
- update file list
- new version 0.4.4
* Thu May 31 2012 fwang <fwang> 0.4.3-9.mga3
+ Revision: 251964
- rebuild for new perl
* Sun Sep 11 2011 fwang <fwang> 0.4.3-8.mga2
+ Revision: 142420
- drop unused req
* Sun Sep 11 2011 fwang <fwang> 0.4.3-7.mga2
+ Revision: 142412
- fix build with libpng 1.5
- rebuild for new libpng
* Mon Sep 05 2011 fwang <fwang> 0.4.3-6.mga2
+ Revision: 138596
- rebuild for updated perl build flags
* Mon Jun 13 2011 sander85 <sander85> 0.4.3-5.mga2
+ Revision: 105769
- fix build for perl 5.14
- Rebuild for perl 5.14
* Wed Apr 20 2011 obgr_seneca <obgr_seneca> 0.4.3-4.mga1
+ Revision: 89033
- cleaned up spec file
- imported package ming
* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 0.4.3-4mdv2011.0
+ Revision: 592110
- rebuild for py2.7
* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.4.3-3mdv2011.0
+ Revision: 564308
- rebuild for perl 5.12.1
* Thu Jul 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.4.3-2mdv2011.0
+ Revision: 556780
- perl 5.12 rebuild
* Mon Feb 08 2010 Emmanuel Andry <eandry@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 502214
- fix BR
- New version 0.4.3
- rediff p0
- drop p3 (now useless)
- update files list
* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-7mdv2010.1
+ Revision: 488787
- rebuilt against libjpeg v8
* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-6mdv2010.0
+ Revision: 416661
- rebuilt against libjpeg v7
* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 0.4.2-5mdv2009.1
+ Revision: 319826
- fix str fmt
- rebuild for new python
* Fri Nov 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-3mdv2009.1
+ Revision: 305486
- really make it backportable...
* Fri Nov 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-2mdv2009.1
+ Revision: 305468
- make it backportable
* Thu Sep 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-1mdv2009.0
+ Revision: 288076
- 0.4.2
- rediffed P0
- dropped redundant patches
* Mon Aug 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-0.rc1.1mdv2009.0
+ Revision: 275712
- 0.4.0.rc1
- drop implemented and obsolete patches
- fix linkage (P0)
- rediffed two patches
- drop the perl and python sources, it's bundled now
* Sat Aug 23 2008 Emmanuel Andry <eandry@mandriva.org> 0.3.0-10mdv2009.0
+ Revision: 275267
- apply devel policy
- drop old conditionnal
- check major
* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-9mdv2009.0
+ Revision: 265127
- rebuild early 2009.0 package (before pixel changes)
* Wed Jun 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-8mdv2009.0
+ Revision: 218120
- fix build
  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
* Wed Jan 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-7mdv2008.1
+ Revision: 153649
- added P5 from PLD to make it link against the shared lib
- added some spec file fixes

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
  + Pixel <pixel@mandriva.com>
    - rebuild for perl-5.10.0
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-5mdv2008.0
+ Revision: 89931
- rebuild
* Wed Jan 31 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.0-4mdv2007.0
+ Revision: 115787
- Fix Buildrequires (thanks iurt)
- Rebuild against new python
- Import ming
* Wed Jul 26 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-1mdv2007.0
- 0.3.0
* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.3.0-0.beta2.7mdk
- fix requires
* Sat May 20 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.3.0-0.beta2.6mdk
- fix buildrequires
* Tue Feb 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-0.beta2.5mdk
- rebuild
* Tue Feb 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-0.beta2.4mdk
- fix multiarch compliance
* Tue Feb 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-0.beta2.3mdk
- fix one minor glitch in the spec file
* Tue Feb 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-0.beta2.2mdk
- the code is too borked to be unbundled...
* Wed Nov 02 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-0.beta2.1mdk
- 0.3.0 beta2
- drop upstream patches; P0
- rediffed P2,P3
- fix sane microversion (P4)
- fix deps
- the perl and python sub packages has been broken out
* Wed Nov 02 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-1.20050815.1mdk
- new snap (20050815)
- rediffed P0 (different approach)
- rediffed P1 (gcc4)
- added P2 (DESTDIR)
- added the python sub package, fixes #18919
- added P3 to pass -fPIC to the compiler cflags when building the lib
* Wed Nov 02 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta1.9mdk
- added one gcc4 patch
* Fri Dec 31 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3-0.beta1.8mdk
- revert latest "lib64 fixes"
* Tue Dec 28 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3-0.beta1.7mdk
- lib64 fixes
- nuke rpath
* Fri Dec 10 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3-0.beta1.6mdk
- added an obvious lib64 fix
* Thu Dec 02 2004 Abel Cheung <deaddog@mandrake.org> 0.3-0.beta1.5mdk
- And another...
* Thu Dec 02 2004 Abel Cheung <deaddog@mandrake.org> 0.3-0.beta1.4mdk
- Fix BuildRequires
* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.3-0.beta1.3mdk
- Rebuild for new perl
- Rename the perl module to perl-SWF, more compliant with the naming policy
* Tue May 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.beta1.2mdk
- misc spec file fixes
- drop P2, use spec file hack instead
- fix deps
* Mon May 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.beta1.1mdk
- 0.3beta1
- new url
- misc spec file fixes
