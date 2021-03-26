%global debug_package %{nil}

Summary:   An intuitive TUI interface for console applications
Name:      rhtvision
Version:   2.2.1
Release:   11.1
License:   GPL
URL:       http://tvision.sf.net/
Group:     System Environment/Libraries
Source:    https://jaist.dl.sourceforge.net/project/tvision/UNIX/2.2.1%20CVS20161117/rhtvision_2.2.1-4.tar.gz
Patch:     tvision.patch
BuildRequires: gcc-c++

%description 
This is the shared library for programs using the RHTVision library.

The RHTVision library gives an intuitive and user friendly TUI (Textual User
Interface) for programs using this library and running in a console.

This library is based on the Turbo Vision library made by Borland Corporation.
That library was released by Borland under a Public Domain license. RHTVision
is Borland's Turbo Vision library but with enhancements, some changes and a
GPL license.

%package devel
Summary:   RHTVision library development.
Group:     Development/Libraries
Requires:  %{name} = %{version}

%description devel
Libraries and include files you can use for developing applications using
the RHTVision library.

The RHTVision library gives an intuitive and user friendly TUI (Textual User
Interface) for programs using this library and running in a console.

This library is based on the Turbo Vision library made by Borland Corporation.
That library was released by Borland under a Public Domain license. RHTVision
is Borland's Turbo Vision library but with enhancements, some changes and a
GPL license.

%prep
%setup -q -n tvision
%patch -p1
sed -i '1i #include <cstdio>' classes/ipstream.cc include/tv/textdev.h
sed -i '1i #include <cstdlib>' classes/tdesktop.cc
sed -i '1i #include <cmath>' classes/tdesktop.cc classes/tdisplay.cc
sed -i '149s|abs|fabs|' classes/tdesktop.cc
for i in 385 388 400 404 ; do
sed -i "${i}s|abs|fabs|g" classes/tdisplay.cc
done
sed -i 's|require "|require "./|' config.pl
sed -i '2540,2541s|target|(int)target|' classes/x11/x11src.cc

%build
export CXXFLAGS="-O2 -pipe -Wno-narrowing"
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr libdir=$RPM_BUILD_ROOT%{_libdir} install
cd $RPM_BUILD_ROOT%{_libdir}
chmod 755 *
ln -s librhtv.so.%{version} librhtv.so.2

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/lib*.so.*
%{_datadir}/locale/*/LC_MESSAGES/*.mo

%files devel
%{_includedir}/%{name}
%{_libdir}/*.a
%{_libdir}/lib*.so
%{_bindir}/*-config

%changelog
* Fri Jan 20 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.1
- Rebuild for Fedora
* Wed Nov 24 2004 - Michel Catudal mcatudal@comcast.net
- Update to last CVS, added support for debug
* Sun Nov 14 2004 - Michel Catudal mcatudal@comcast.net
- Update to latest CVS code, use same directory name as CVS
  added revision number to match the revision stated
  in the change.log file
* Tue Feb 18 2003 - Michel Catudal bbcat@netonecom.net
- Add documentation
* Sun Jan 5 2003 - Michel Catudal bbcat@netonecom.net
- Released 2.0.1 version
* Sun Oct 6 2002 - Michel Catudal bbcat@netonecom.net
- Version 2 from CVS
* Mon Nov 5 2001 - Michel Catudal bbcat@netonecom.net
- Added copying of include files on include/cl which were missing
* Sun Nov 4 2001 - "Ernas M. Jamil" <ernasm@samba.co.id>
- Added copying of include files which were not done due
  to changes that I was not aware of in the include files.
  The same install script worked before.
  Thanks to Ernas M. Jamil for pointing it out.
