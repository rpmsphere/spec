%global debug_package %{nil}

Name: regina
Version: 3.9.1
Release: 5.1
Group: Development/Languages
Source: http://dl.sourceforge.net/project/regina-rexx/regina-rexx/%{version}/Regina-REXX-%{version}.tar.gz
License: LGPL
URL: http://regina-rexx.sourceforge.net
Summary: Rexx Interpreter binaries, language files and sample programs

%description
Regina is an implementation of a Rexx interpreter, compliant with
the ANSI Standard for Rexx (1996). It is also available on several other
operating systems. For more information on Rexx, visit http://www.rexxla.org

%package devel
Group: Programming
Summary: Regina Rexx development libraries and header file.
Requires: %{name}

%description devel
Regina is an implementation of a Rexx interpreter, compliant with
the ANSI Standard for Rexx (1996).  It is also available on several other
operating systems. For more information on Rexx, visit http://www.rexxla.org

%prep
%setup -q -n Regina-REXX-%{version}

%build
./configure --prefix=/usr --mandir=%{_mandir} --libdir=%{_libdir}
make

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%post
ldconfig

%postun
ldconfig

%files
%{_mandir}/man1/*.1.*
/usr/etc/rxstack
%{_datadir}/Regina-REXX
%{_bindir}/rexx
%{_bindir}/regina
%{_bindir}/rxqueue
%{_bindir}/rxstack
%{_libdir}/libregina.so.*

%files devel
%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_includedir}/rexxsaa.h
%{_datadir}/man/man1/regina-config.1.*
%{_bindir}/regina-config

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Nov 13 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 3.9.1
- Rebuild for Fedora
* Mon Jan 02 2012 Mark Hessling
- Vendor package
