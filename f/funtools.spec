%define __spec_install_post %{nil}
%undefine _debugsource_packages
%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name: funtools
Version: 1.4.6
Release: 20.1
Summary: FITS library and utilities
Group: Applications/Engineering
License: LGPLv2+
#URL: http://hea-www.harvard.edu/RD/funtools/
URL: https://github.com/ericmandel/funtools
#Source0: http://hea-www.harvard.edu/saord/download/funtools/%{name}-%{version}.tar.gz
Source0: %{name}-master.zip
BuildRequires: wcstools-devel tcl-devel zlib-devel
BuildRequires: pkgconfig
Requires: gnuplot
Requires: %{name}-libs = %{version}-%{release}
Requires: tcl(abi)

%description
Funtools, is a "minimal buy-in" FITS library and utility package from
the SAO/HEAD R&D group. The Funtools library provides simplified access to
FITS images and binary tables, as well as to raw array and binary event lists.
The Funtools utilities provide high-level support for processing
astronomical data.
This package contains command-line utilities for managing FITS files.

%package devel
Summary: Headers for developing programs that will use %{name}
Group: Development/Libraries
Requires: %{name}-libs = %{version}-%{release} wcstools-devel tcl-devel

%description devel
These are the header files and libraries needed to develop a %{name} 
application.

%package libs
Summary: A general purpose FITS library
Group: System Environment/Libraries
Obsoletes: funtools < 1.4.0-2
%description libs
This package contains the %{name} run-time library

%package tcl
Summary: Funtools TCL interface
Group: System Environment/Libraries
Requires: %{name}-libs = %{version}-%{release}
Provides: tcl-funtools = %{version}-%{release}
%description tcl
This package contains the %{name} TCL interface

%prep
%setup -q -n %{name}-master

%build
./mkconfigure
%configure --enable-shared=yes --with-wcslib=%{_libdir}/libwcstools.so \
        --with-zlib=%{_libdir}/libz.so --with-tcl=%{_libdir} --enable-dl=yes
make
# Parallel build does not work currently
#make EXTRA_LIBS="-lwcs -lz -ldl -fPIC"
#make shtclfun EXTRA_LIBS="-ltcl -lwcs -lz -ldl -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir} $RPM_BUILD_ROOT%{_datadir}/%{name} $RPM_BUILD_ROOT%{_includedir}/%{name}/fitsy
make INSTALL_ROOT=$RPM_BUILD_ROOT INSTALL="%{__install} -p" install
mv $RPM_BUILD_ROOT/%{_bindir}/funtools.ds9 $RPM_BUILD_ROOT/%{_datadir}/funtools
mv $RPM_BUILD_ROOT/%{_bindir}/funcalc.sed $RPM_BUILD_ROOT/%{_datadir}/funtools
# Bug #329741
install -p -m 644 fitsy/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/fitsy
# Tcl
mkdir -p $RPM_BUILD_ROOT%{tcl_sitearch}/tclfuntools
cp pkgIndex.tcl $RPM_BUILD_ROOT%{tcl_sitearch}/tclfuntools
#mv $RPM_BUILD_ROOT%{_libdir}/libtcl* $RPM_BUILD_ROOT%{tcl_sitearch}/tclfuntools
%ifarch x86_64 aarch64
mv $RPM_BUILD_ROOT/usr/lib/* $RPM_BUILD_ROOT/usr/lib64/
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}

%files libs
%doc COPYING
%{_libdir}/libfuntools*so.*

%files tcl
%{tcl_sitearch}/tclfuntools
#{_mandir}/mann/*

%files devel
%doc doc/*.html
%doc doc/*.pdf
%{_libdir}/*.so
%{_libdir}/pkgconfig/funtools.pc
%exclude %{_libdir}/*.a
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man7/*

%changelog
* Tue May 12 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.6
- Rebuilt for Fedora
* Tue Mar 27 2012 Tom Trebisky<tom@mmto.org> - 1.4.4-5
- funtools was orphaned as of Fedora 16
- I picked up the fedora 1.4.4-4 source rpm and am building from there.
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Fri Jul 09 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 1.4.4-3
- License in subpackages
* Wed Dec 23 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 1.4.4-2
- EVR bump
* Wed Dec 23 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 1.4.4-1
- New upstream source
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Tue Feb 19 2009 Sergio Pascual  <sergiopr at fedoraproject.org> - 1.4.0-9
- Catching up the soname revertion in wcstools-devel
* Fri Feb 13 2009 Sergio Pascual  <sergiopr at fedoraproject.org> - 1.4.0-8
- Using wcstools-devel instead of libwcs-devel
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.0-7
- Autorebuild for GCC 4.3
* Fri Jan 04 2008 Sergio Pascual <sergiopr at fedoraproject.org> 1.4.0-6
- Tcl files in a separate subpackage
- Following PackagingDrafts/Tcl
* Thu Jan 03 2008 Sergio Pascual <sergiopr at fedoraproject.org> 1.4.0-5
- Rebuilt for tcl 8.5
* Fri Nov 09 2007 Sergio Pascual <sergiopr at fedoraproject dot org> 1.4.0-4
- Adding some packages to devel requires
* Tue Oct 16 2007 Sergio Pascual <sergiopr at fedoraproject dot org> 1.4.0-3
- Fixing wcs headers
* Sat Oct 13 2007 Sergio Pascual <sergiopr at fedoraproject dot org> 1.4.0-2
- Fixing bug #329741
- Splitting libs in funtools-libs
* Mon Aug 20 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 1.4.0-1
- New upstream version, changed license and buildroot lines
* Sun Jul 22 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 1.3.0-0.5.b34
- New upstream version
* Thu May 03 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 1.3.0-0.5.b33
- New upstream version
* Mon Mar 26 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 1.3.0-0.4.b29
- Funtools Approved
- Parallel make does not work
- Problem with undefined non weak symbols in libtclfun fixed
* Fri Mar 23 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 1.3.0-0.3.b29
- Removed _smp_mflags
* Thu Mar 22 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 1.3.0-0.2.b29
- Updated funtools-makefile.patch
- Added EXTRA_LIBS to compilation step
* Tue Mar 20 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 1.3.0-0.1.b29
- Initial spec file
