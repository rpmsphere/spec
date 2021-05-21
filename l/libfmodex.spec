%undefine _missing_build_ids_terminate_build
%global debug_package %{nil}

Summary: 	FMOD is a cross platform audio library and toolset
Name: 		libfmodex
Version: 	4.18.09
%define _version2       41809
Release: 	1.bin
License: 	see LICENSE.TXT
Group: 		Development/Libraries/C and C++
%ifnarch x86_64
Source0: 	http://www.fmod.org/index.php/release/version/fmodapi%{_version2}linux.tar.gz
Source1:	http://www.fmod.org/index.php/release/version/fmodapi%{_version2}linux64.tar.gz
%else
Source1: 	http://www.fmod.org/index.php/release/version/fmodapi%{_version2}linux.tar.gz
Source0:	http://www.fmod.org/index.php/release/version/fmodapi%{_version2}linux64.tar.gz
%endif
URL:		http://www.fmod.org/
Obsoletes:	fmod <= 4.06.20
Provides:	fmod = 4.06.20

%description
FMOD is a cross platform audio library and toolset to let you easily
implement the latest audio technologies into your title.

The FMOD Ex sound system is a revolutionary new audio engine for
game developers, multimedia developers, sound designers, musicians
and audio engineers, based on the years of experienced of Firelight
Technologies(tm) previous product FMOD.
It also aims high - to push the boundaries of audio implementation
for games and the like while at the same time using minimal resources
and being scalable. This new engine is written from the ground up
since FMOD 3 was released and involves years of experience and
feedback from FMOD users to create the most feature filled and easy
to use product possible, without the rawbacks of legacy
implementation that FMOD 3 may have suffered from its years of
continuous development.

Copyright (c) Firelight Technologies, Pty, Ltd, 2004-2007

%package designerapi
Summary:	FMODex Designer
Group:		Development/Libraries/C and C++
Requires:	libfmodex = %{version}
Provides:	fmod-designerapi = 4.06.20
Obsoletes:	fmod-designerapi <= 4.06.20

%description designerapi
FMODex Designer.

%package devel
Summary:	Development package for the FMODex library
Group:		Development/Languages/C and C++
Requires:	libfmodex = %{version}

%description devel
Development package for the FMODex library.

%prep
%ifnarch x86_64
%setup -q -n fmodapi%{_version2}linux
%else
%setup -q -n fmodapi%{_version2}linux64
%endif
%__sed -i -e 's|ldconfig|#ldconfig|g' \
	Makefile

%build

%install
%__install -dm 755 %{buildroot}%{_libdir}
%__install -dm 755 %{buildroot}%{_includedir}/fmodex

%makeinstall \
	DESTLIBDIR=%{buildroot}%{_libdir} \
	DESTHDRDIR=%{buildroot}%{_includedir}/fmodex

# install *.hpp (Makefile broken)
%ifarch x86_64
	%__install -dm 755 %{buildroot}%{_includedir}/fmodex
	%__install -m 644 api/inc/*.hpp \
		%{buildroot}%{_includedir}/fmodex
%endif

pushd %{buildroot}%{_libdir}
%ifnarch x86_64
	%__rm -f libfmodex.so
	%__rm -f libfmodexp.so
	ln -s libfmodex.so.%{version}  libfmodex.so
	ln -s libfmodexp.so.%{version} libfmodexp.so
%else
	%__rm -f libfmodex64.so
	%__rm -f libfmodexp64.so
	ln -s libfmodex64.so.%{version}  libfmodex64.so
	ln -s libfmodexp64.so.%{version} libfmodexp64.so
%endif
popd

# plugins
%__install -dm 755 %{buildroot}%{_libdir}/fmod/plugins
%__install -m 644 api/plugins/*.so \
	%{buildroot}%{_libdir}/fmod/plugins

%__install -m 644 fmoddesignerapi/api/lib/*.so \
	%{buildroot}%{_libdir}
%__install -m 644 fmoddesignerapi/api/inc/*.h \
	%{buildroot}%{_includedir}

#%__install -dm 755 %{buildroot}%{_datadir}/%{name}
#%__cp -a examples \
#	%{buildroot}%{_datadir}/%{name}


%clean
[ -d "%{buildroot}" -a "%{buildroot}" != "" ] && %__rm -rf "%{buildroot}"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
# this library has no so-name, to avoid installing the devel-package the *.so
# are packaged in the libfmodex package
%{_libdir}/libfmodex*.so
%{_libdir}/libfmodex*.so.*
%dir %{_libdir}/fmod
%dir %{_libdir}/fmod/plugins
%{_libdir}/fmod/plugins/*.so

%files designerapi
%doc fmoddesignerapi/*.TXT
%doc fmoddesignerapi/examples
%{_libdir}/libfmodevent*
%{_includedir}/fmod_event.h

%files devel
%doc documentation/*
%doc examples
%dir %{_includedir}/fmodex
%{_includedir}/fmodex/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 4.18.09
- Rebuilt for Fedora
* Mon Oct 27 2008 Toni Graffy <toni@links2linux.de> - 4.18.09-0.pm.1
- update to 4.18.09
* Thu Oct 23 2008 Toni Graffy <toni@links2linux.de> - 4.18.08-0.pm.1
- update to 4.18.08
* Thu Oct 16 2008 Toni Graffy <toni@links2linux.de> - 4.18.07-0.pm.1
- update to 4.18.07
* Thu Oct 09 2008 Toni Graffy <toni@links2linux.de> - 4.18.06-0.pm.1
- update to 4.18.06
* Fri Oct 03 2008 Toni Graffy <toni@links2linux.de> - 4.18.05-0.pm.1
- update to 4.18.05
* Mon Sep 22 2008 Toni Graffy <toni@links2linux.de> - 4.18.04-0.pm.1
- update to 4.18.04
* Thu Sep 11 2008 Toni Graffy <toni@links2linux.de> - 4.18.03-0.pm.1
- update to 4.18.03
* Thu Sep 04 2008 Toni Graffy <toni@links2linux.de> - 4.18.02-0.pm.1
- update to 4.18.02
* Sat Aug 30 2008 Toni Graffy <toni@links2linux.de> - 4.18.01-0.pm.1
- update to 4.18.01
* Thu Aug 28 2008 Toni Graffy <toni@links2linux.de> - 4.18.00-0.pm.1
- update to 4.18.00
* Tue Aug 12 2008 Toni Graffy <toni@links2linux.de> - 4.16.10-0.pm.1
- update to 4.16.10
* Wed Aug 06 2008 Toni Graffy <toni@links2linux.de> - 4.16.09-0.pm.1
- update to 4.16.09
* Fri Aug 01 2008 Toni Graffy <toni@links2linux.de> - 4.16.08-0.pm.1
- update to 4.16.08
* Fri Jul 18 2008 Toni Graffy <toni@links2linux.de> - 4.16.06-0.pm.1
- update to 4.16.06
* Fri Jul 11 2008 Toni Graffy <toni@links2linux.de> - 4.16.05-0.pm.1
- update to 4.16.05
* Fri Jul 04 2008 Toni Graffy <toni@links2linux.de> - 4.16.04-0.pm.1
- update to 4.16.04
* Tue Jun 24 2008 Toni Graffy <toni@links2linux.de> - 4.16.03-0.pm.1
- update to 4.16.03
* Fri Jun 20 2008 Toni Graffy <toni@links2linux.de> - 4.16.02-0.pm.1
- update to 4.16.02
* Thu Jun 12 2008 Toni Graffy <toni@links2linux.de> - 4.16.01-0.pm.1
- update to 4.16.01
* Thu Jun 05 2008 Toni Graffy <toni@links2linux.de> - 4.16.00-0.pm.1
- update to 4.16.00
* Fri May 30 2008 Toni Graffy <toni@links2linux.de> - 4.14.07-0.pm.1
- update to 4.14.07
* Sat May 24 2008 Toni Graffy <toni@links2linux.de> - 4.14.06-0.pm.1
- update to 4.14.06
* Sat May 19 2008 Toni Graffy <toni@links2linux.de> - 4.14.05-0.pm.1
- update to 4.14.05
* Sat May 03 2008 Toni Graffy <toni@links2linux.de> - 4.14.04-0.pm.1
- update to 4.14.04
* Fri Apr 25 2008 Toni Graffy <toni@links2linux.de> - 4.14.03-0.pm.1
- update to 4.14.03
* Fri Apr 18 2008 Toni Graffy <toni@links2linux.de> - 4.14.02-0.pm.1
- update to 4.14.02
* Fri Apr 11 2008 Toni Graffy <toni@links2linux.de> - 4.14.01-0.pm.1
- update to 4.14.01
* Fri Apr 04 2008 Toni Graffy <toni@links2linux.de> - 4.14.00-0.pm.1
- update to 4.14.00
* Sat Mar 29 2008 Toni Graffy <toni@links2linux.de> - 4.12.07-0.pm.1
- update to 4.12.07
* Thu Mar 20 2008 Toni Graffy <toni@links2linux.de> - 4.12.06-0.pm.1
- update to 4.12.06
* Fri Mar 14 2008 Toni Graffy <toni@links2linux.de> - 4.12.05-0.pm.1
- update to 4.12.05
* Thu Mar 06 2008 Toni Graffy <toni@links2linux.de> - 4.12.04-0.pm.1
- update to 4.12.04
* Tue Feb 19 2008 Toni Graffy <toni@links2linux.de> - 4.12.03-0.pm.1
- update to 4.12.03
* Fri Feb 15 2008 Toni Graffy <toni@links2linux.de> - 4.12.02-0.pm.1
- update to 4.12.02
* Thu Feb 07 2008 Toni Graffy <toni@links2linux.de> - 4.12.01-0.pm.1
- update to 4.12.01
* Fri Feb 01 2008 Toni Graffy <toni@links2linux.de> - 4.12.00-0.pm.1
- update to 4.12.00
* Fri Jan 25 2008 Toni Graffy <toni@links2linux.de> - 4.10.06-0.pm.1
- update to 4.10.06
* Fri Jan 18 2008 Toni Graffy <toni@links2linux.de> - 4.10.05-0.pm.1
- update to 4.10.05
* Thu Jan 10 2008 Toni Graffy <toni@links2linux.de> - 4.10.04-0.pm.1
- update to 4.10.04
* Thu Dec 20 2007 Toni Graffy <toni@links2linux.de> - 4.10.03-0.pm.1
- update to 4.10.03
* Fri Dec 14 2007 Toni Graffy <toni@links2linux.de> - 4.10.02-0.pm.1
- update to 4.10.02
* Fri Dec 07 2007 Toni Graffy <toni@links2linux.de> - 4.10.01-0.pm.1
- update to 4.10.01
* Thu Dec 06 2007 Toni Graffy <toni@links2linux.de> - 4.10.00-0.pm.1
- update to 4.10.00
* Fri Nov 23 2007 Toni Graffy <toni@links2linux.de> - 4.08.09-0.pm.1
- update to 4.08.09
* Mon Nov 12 2007 Toni Graffy <toni@links2linux.de> - 4.08.08-0.pm.1
- update to 4.08.08
* Tue Nov 06 2007 Toni Graffy <toni@links2linux.de> - 4.08.07-0.pm.2
- added missing hpp-files for 64bit
* Mon Nov 05 2007 Toni Graffy <toni@links2linux.de> - 4.08.07-0.pm.1
- update to 4.08.07
* Thu Oct 18 2007 Toni Graffy <toni@links2linux.de> - 4.08.06-0.pm.1
- update to 4.08.06
* Fri Oct 12 2007 Toni Graffy <toni@links2linux.de> - 4.08.05-0.pm.1
- update to 4.08.05
* Sat Oct 06 2007 Toni Graffy <toni@links2linux.de> - 4.08.04-0.pm.1
- update to 4.08.04
* Fri Sep 28 2007 Toni Graffy <toni@links2linux.de> - 4.08.02-0.pm.1
- update to 4.08.02
* Fri Sep 21 2007 Toni Graffy <toni@links2linux.de> - 4.08.01-0.pm.1
- update to 4.08.01
* Fri Sep 14 2007 Toni Graffy <toni@links2linux.de> - 4.06.27-0.pm.1
- update to 4.06.27
* Sun Sep 02 2007 Toni Graffy <toni@links2linux.de> - 4.06.25-0.pm.3
- rebuild 
* Mon Aug 27 2007 Toni Graffy <toni@links2linux.de> - 4.06.25-0.pm.2
- rebuild to sync repos (pmbs-test)
* Sat Aug 25 2007 Toni Graffy <toni@links2linux.de> - 4.06.25-0.pm.1
- update to 4.06.25
* Fri Aug 03 2007 Toni Graffy <toni@links2linux.de> - 4.06.23-0.pm.1
- update to 4.06.23
* Fri Jun 22 2007 Toni Graffy <toni@links2linux.de> - 4.06.22-0.pm.1
- update to 4.06.22
* Sun Jun 17 2007 Toni Graffy <toni@links2linux.de> - 4.06.21-0.pm.1
- update to 4.06.21
- renamed package to libfmodex4, libfmodex-devel, fmodex-designerapi
- changed package layout according Shared Library Packaging Policy
* Tue Jun 05 2007 Toni Graffy <toni@links2linux.de> - 4.06.20-0.pm.1
- update to 4.06.20
* Sat May 26 2007 Toni Graffy <toni@links2linux.de> - 4.06.19-0.pm.1
- update to 4.06.19
* Fri May 11 2007 Toni Graffy <toni@links2linux.de> - 4.06.18-0.pm.1
- update to 4.06.18
* Fri Apr 27 2007 Toni Graffy <toni@links2linux.de> - 4.06.16-0.pm.1
- update to 4.06.16
- added plugins.so in /usr/lib/fmod/plugins
* Wed Apr 18 2007 Toni Graffy <toni@links2linux.de> - 4.06.15-0.pm.1
- update to 4.06.15
* Tue Apr 10 2007 Toni Graffy <toni@links2linux.de> - 4.06.14-0.pm.1
- update to 4.06.14
* Sun Mar 25 2007 Toni Graffy <toni@links2linux.de> - 4.06.13-0.pm.1
- update to 4.06.13
* Thu Mar 08 2007 Toni Graffy <toni@links2linux.de> - 4.06.12-0.pm.1
- update to 4.06.12
* Sat Feb 24 2007 Toni Graffy <toni@links2linux.de> - 4.06.11-0.pm.1
- initial build 4.06.11
- repacked as tar.bz2
