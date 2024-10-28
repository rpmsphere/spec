Name:           libtap
Summary:        Write tests that implement the Test Anything Protocol
Version:        1.01
Release:        5.1
URL:            https://jc.ngo.org.uk/trac-bin/trac.cgi/wiki/LibTap
License:        GPL v2 or later
Group:          Development/Libraries
Source0:        tap-%{version}.tar.bz2

%description
The tap library provides functions for writing test scripts that produce
output consistent with the Test Anything Protocol.  A test harness that
parses this protocol can run these tests and produce useful reports indi-
cating their success or failure.

%package devel
Summary:        Development files for tap
Group:          Development/Libraries
Requires:       %name = %version

%description devel
This package contains header files to develop applications using tap.

%prep
%setup -q -n tap-%{version}

%build
%configure --disable-static
make all %{?jobs:-j%jobs}

%install
%makeinstall
rm %buildroot/%_libdir/libtap.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%doc README
%_mandir/man3/tap.3.gz
%_libdir/libtap.so.0
%_libdir/libtap.so.0.0.0

%files devel
%_includedir/tap.h
%_libdir/libtap.so

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.01
- Rebuilt for Fedora
* Mon Sep 15 2008 lrupp@suse.de
- initial version 1.01
