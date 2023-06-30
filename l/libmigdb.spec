Summary:   Library of GDB/MI interface
Name:      libmigdb
Version:   0.8.12
Release:   8.1
License:   GPL
Group:     Development/Libraries
Source:    %{name}-%{version}.tar.bz2
Patch:     %{name}.patch
URL:       https://members.xoom.com/stropea/setedit.html
BuildRequires: gcc-c++

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%description 
This library is an attempt to support the GDB/MI interface. MI stands for
machine interface. In this mode gdb sends responses that are "machine
readable" instead of "human readable".

%prep
%setup -q -n libmigdb
%patch -p1

%build
libtoolize
aclocal
autoconf
automake -a
./configure --libdir=%{_libdir}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/local/include $RPM_BUILD_ROOT%{_includedir}
rmdir $RPM_BUILD_ROOT/usr/local

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/*
%{_libdir}/%{name}.*

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.12
- Rebuilt for Fedora
* Sat Nov 27 2010 - mcatudal@comcast.net
- First Fedora 14 release
* Tue Mar 23 2010 - mcatudal@comcast.net
- Updated to SuSE 11.2
* Sat Feb 20 2010 - mcatudal@comcast.net
- Updated to Mandriva 2010.0
* Sat Feb 20 2010 - mcatudal@comcast.net
- Updated to version 0.8.12
* Sat Feb 13 2010 - mcatudal@comcast.net
- First Fedora 12 release
* Sat Sep 26 2009 - mcatudal@comcast.net
- First Fedora 11 release
* Sat Jul 1 2009 - mcatudal@comcast.net
- First Mandriva 2009.1 release
* Sun Dec 28 2008 - mcatudal@comcast.net
- First Fedora 9 release
* Sat May 3 2008 - mcatudal@comcast.net
- First Mandriva release
* Sat Nov 27 2004 - Michel Catudal mcatudal@comcast.net
- First SuSE 9.1 Release
