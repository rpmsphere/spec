Name: wcstools
Version: 3.8.7
Release: 14.1
Summary: Software utilities to display and manipulate the WCS of a FITS image
Group: Applications/Engineering
License: GPLv2+
URL: http://tdc-www.harvard.edu/wcstools
Source0: http://tdc-www.harvard.edu/software/wcstools/%{name}-%{version}.tar.gz

%description
Wcstools is a set of software utilities, written in C, which create,
display and manipulate the world coordinate system of a FITS or IRAF
image, using specific keywords in the image header which relate pixel
position within the image to position on the sky.  Auxillary programs
search star catalogs and manipulate images.

%package libs
Summary: Wcstools shared library 
Group: System Environment/Libraries
License: LGPLv2+

%description libs
Shared library necessary to run wcstools and programs based on libwcs.

%package devel
Summary: Libraries, includes, etc. used to develop an application with wcstools
Group: Development/Libraries
License: LGPLv2+
Requires: %{name}-libs = %{version}-%{release}

%description devel
This are the files needed to develop an application using wcstools.

%prep
%setup -q
sed -i 's|LIBWCS = libwcs/libwcs.a|LIBWCS = -L./libwcs -lwcs|' Makefile

%build
%{__make} CFLAGS="%{optflags} -fPIC -Wcomment"
cd libwcs
gcc %{optflags} -fPIC -shared -o libwcs.so.0.0.0 -Wl,-soname,libwc.so.0 *.o -lm
ln -s libwcs.so.0.0.0 libwcs.so.0
ln -s libwcs.so.0.0.0 libwcs.so

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_libdir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_includedir}/wcs
%{__mkdir_p} $RPM_BUILD_ROOT%{_mandir}/man1
%{__install} -p bin/* $RPM_BUILD_ROOT%{_bindir}
%{__cp} -a libwcs/*.so* $RPM_BUILD_ROOT%{_libdir}
%{__install} -p -m 644 libwcs/*.h $RPM_BUILD_ROOT%{_includedir}/wcs
%{__install} -p -m 644 man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
%{__rm} -fr $RPM_BUILD_ROOT

%files
%doc NEWS COPYING Readme Programs
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*

%files libs
%defattr(-,root,root,-)
%doc libwcs/COPYING
%{_libdir}/*.so.*

%files devel
%doc libwcs/COPYING libwcs/NEWS
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/wcs

%changelog
* Sun Oct 28 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.8.7
- Rebuild for Fedora
* Tue Mar 27 2012 Tom Trebisky <tom@mmto.org> - 3.8.4-1
- This package was orphaned by Fedora as of Fedora 16, so
- we are building it locally at the MMT.
- I began with the Fedora 15 source rpm for version 3.8.1
- This included a patch for bug 559863, which as near as I can tell
- has been fixed by the original developers as of version 3.8.4
- I am retaining the fedora shared library patch
- (the funtools package depends on this package,
-  and I think it is beneficial if not essential to have
-  them both using .so format).
- Note that the -soname for this library is libwc, NOT libwcs
-	(don't ask me!!)
- Also note that there is another package "wcslib" or some such
- that also produces a libwcs.so file in conflict with this package.
- The fedora packagers have complained to the package authors, but
- there is no resolution as yet.
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Tue Feb 03 2010 Sergio Pascual <sergiopr at fedoraproject.org> 3.8.1-1
- New upstream source
- Patch to fix bz #559863 from upstream
* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Thu Feb 19 2009 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.0-6
- Reverting soname change
* Sat Feb 14 2009 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.0-5
- Libray and headers renamed as wcstools
* Wed Oct 01 2008 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.0-4
- Fails to build from source bz#465061
* Wed Oct 01 2008 Sergio Pascual <sergiopr at fedoraproject.org> 3.7.0-3
- Fails to build from source bz#465061
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.7.0-2
- Autorebuild for GCC 4.3
* Wed Sep 05 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 3.7.0-1
- New upstream source 3.7.0
* Mon Aug 27 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 3.6.8-2.1
- Rebuild for Fedora 8 to get the build-id
* Tue Mar 20 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.8-2
- Fix for bug #232413
* Mon Mar 19 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.8-1
- New upstream source 3.6.8
- Added pacthes to remove warnings during the compilation
* Mon Feb 26 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.7-1
- New upstream source 3.6.7
* Wed Nov 15 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.6-1
- New upstream source 3.6.6
* Tue Oct 10 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.6-0.1.beta
- New upstream source 3.6.6beta
* Mon Sep 4 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.5-3
- Rebuild.
* Wed Aug 30 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.5-2
- Corrected bug in edhead (patch2) (bug #204642).
* Fri Jun 21 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.5-1
- New upstream source 3.6.5
* Tue Jun 13 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.4-3
- Patched overflows in catutil.c and getdate.c
- Patched incompatible pointer in binread.c
* Mon Jun 12 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.4-2
- Patched edhead.
- libwcs provides libwcs.so.3
- libwcs into System Environment/Libraries group
- Makefile uses ${RPM_OPT_FLAGS} and $(CC)
* Fri Jun 09 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.4-1
- Removed not needed ldconfig in wcstools and libwcs-devel.
* Wed Mar 08 2006 Sergio Pascual <spr@astrax.fis.ucm.es> 3.6.3-1
- Initial RPM file.
