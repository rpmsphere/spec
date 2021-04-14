%undefine _debugsource_packages

Name:		libctb
Version:	0.16
Release:	10.1
Summary:	Runtime I/O Control Library
Group:		Applications/Communications
License:	GPLv2+	
URL:		https://iftools.com/start/index.en.php
Source0:	%{name}-%{version}.tar.gz

%description
Runtime I/O Control Library used by FreeDV. You need this rpm package
to run FreeDV on Linux.

%package devel
Summary:  	Development files for I/O Control Library used by FreeDV
Group: 		Applications/Communications
Requires: 	libctb

%description devel
Development files for the I/O Control Library libctb. You need this 
to compile the FreeDV rpm package under Linux.

%prep
%setup -q

%build
cd build/
make
cd ../

%install
BINDIR=$RPM_BUILD_ROOT%{_bindir}
LIBDIR=$RPM_BUILD_ROOT%{_libdir}
DOCDIR=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}
SHAREDIR=$RPM_BUILD_ROOT%{_datadir}/%{name}
rm -rf $RPM_BUILD_ROOT
install -d -m 0775 $LIBDIR
install -d -m 0775 $BINDIR
install -d -m 0775 $INCLUDEDIR
install -d -m 0775 $SHAREDIR
#install -m 0775 lib/* $LIBDIR
cp --archive lib/* $LIBDIR
install -m 0775 build/release/ctbtest $BINDIR
cp --archive include/* $INCLUDEDIR
cp --archive python/ $SHAREDIR/
cp --archive samples/ $SHAREDIR/

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/libctb/python/samples/*.py

%post
/usr/sbin/ldconfig

%postun  
/usr/sbin/ldconfig

%files 
/usr/bin/*
/usr/lib*/lib*
/usr/lib*/gpib32.lib
/usr/share/%{name}
%exclude /usr/share/libctb/python/*/linux/_wxctb.so

%files devel
/usr/include/*
%doc build/COPYRIGHT build/README manual/refman.pdf

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.16
- Rebuilt for Fedora
* Sat Jan 23 2013 Mike Heitmann <mheitmann@n0so.net> 0.16-fc18-2
- Fixed conflict caused by including /usr/libxx
* Sat Jan 19 2013 Mike Heitmann <mheitmann@n0so.net> 0.16-fc18-1
- Update for Fedora 18
* Sun Dec 30 2012 Mike Heitmann <mheitmann@n0so.net> 0.16-3
- Fixed ldconfig path error
* Sun Dec 30 2012 Mike Heitmann <mheitmann@n0so.net> 0.16-2
- Fixed sym links for .so files
* Sun Dec 23 2012 Mike Heitmann <mheitmann@n0so.net> 0.16-1
- Initial SPEC file - creates:
- libctb (runtime) and 
- libctb-devel (development files required for compiling)
