%global debug_package %{nil}

Name: tut
Group: Development/Languages
Version: 2016.04.01
Release: 1
License: BSD
URL:	http://tut-framework.sourceforge.net/
Summary: Elegant C++ unit test framework
Source: tut-framework-master.zip
BuildRequires: waf
#BuildArch: noarch

%description
TUT is a unit test framework for C++, written in pure C++. It makes use of
C++ templates to reduce the responsibilities of the user and provide an
intuitive and easy-to-use interface. Unlike other test unit frameworks for
C++, TUT doesn't use macros, since their usage conceals actual implementation
and (what's worse) can interfere with client application.

TUT completely fits into a single header file. No library compilation is
required, thus a lot of portability problems are avoided and integration with
client code is very simple.

%package devel
Summary: Elegant C++ unit test framework
Group: Development/Languages

%description devel
TUT is a unit test framework for C++, written in pure C++. It makes use of
C++ templates to reduce the responsibilities of the user and provide an
intuitive and easy-to-use interface. Unlike other test unit frameworks for
C++, TUT doesn't use macros, since their usage conceals actual implementation
and (what's worse) can interfere with client application.

TUT completely fits into a single header file. No library compilation is
required, thus a lot of portability problems are avoided and integration with
client code is very simple.

%prep
%setup -q -n tut-framework-master

%build
waf configure --prefix=/usr
waf build
sed -i 's|2016-04-01|2016.04.01|' build/tut.pc

%install
install -Dm 644 build/tut.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/tut.pc
install -d $RPM_BUILD_ROOT%{_includedir}
install -m 644 include/*.h $RPM_BUILD_ROOT%{_includedir}
install -d $RPM_BUILD_ROOT%{_includedir}/tut
install -m 644 include/tut/* $RPM_BUILD_ROOT%{_includedir}/tut
#waf install

%files devel
%doc README
%{_libdir}/pkgconfig/tut.pc
%{_includedir}/tut
%{_includedir}/*.h

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue May 05 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2016.04.01
- Rebuild for Fedora
* Mon Sep 21 2009 admin@eregion.de
- add patch for libtut to allow snowglobe build
* Wed Jul 01 2009 admin@eregion.de
- converted to a "clean" buildservice spec
* Tue Feb  5 2008 César Gómez Martín <cesar.gomez@gmail.com>
- version 0.0.20070706-1
- New maintainer.
- New upstream release (2007-07-06).
- Removed unzip from Build-Depends and debian/rules
- Standard-Version 3.7.2--> 3.7.3
- Added Homepage field to debian/control
- Patches have been recreated to fit the new upstream version
* Fri Jun  9 2006 martin f. krafft <madduck@debian.org>
- version 0.0.20060329-1
- New upstream release.
* Sat May 14 2005 martin f. krafft <madduck@debian.org>
- version 0.0.20040326-6
- Removed suggestion for libtut-doc, which does not exist.
* Fri May 13 2005 martin f. krafft <madduck@debian.org>
- version 0.0.20040326-5
- Fixed missing homepage link in README.docs.
* Fri May 13 2005 martin f. krafft <madduck@debian.org>
- version 0.0.20040326-4
- Added documentation (from webpage).
* Fri May 13 2005 martin f. krafft <madduck@debian.org>
- version 0.0.20040326-3
- Added README.gcc-3.4 with notes for users of gcc 3.4.
- pkg-config file now goes to /usr/share/pkgconfig, as supported by newer
  pkg-config libraries.
- Added versioned suggestion on pkg-config 0.16.0-1.
* Wed May 11 2005 martin f. krafft <madduck@debian.org>
- version 0.0.20040326-2
- Fixed Makefiles in examples. (thanks to Petri Latvala for "insisting"
  I fix this, and subsequent testing.)
* Wed May 11 2005 martin f. krafft <madduck@debian.org>
- version 0.0.20040326-1
- Initial release.
