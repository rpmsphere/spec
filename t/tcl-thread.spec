Name: tcl-thread
Version: 2.6.5
Release: 5.1
Summary: A tcl extension implementing memory channels
License: BSD
Group: Development/Tcl
URL: http://tcl.sourceforge.net/
Source: %name-%version.tar.gz
Requires: tcl
BuildRequires: tcl-devel

%description
This is a tcl extension, which creates threads that contain Tcl 
interpreters, and it lets you send scripts to those threads for
evaluation.
Additionaly, it provides script-level access to basic thread 
synchronization primitives, like mutexes and condition variables.

%prep
%setup -q
sed -i 's/@lib@/%_lib/' pkgIndex.tcl.in
sed -i 's|interp->errorLine|Tcl_GetErrorLine(interp)|' generic/threadSvCmd.c generic/threadSpCmd.c

%build
%configure
make

%install
%make_install

%files
%doc ChangeLog license.terms README
%_libdir/tcl/libthread%version.so
%_datadir/tcl/*
%_mandir/mann/*

%changelog
* Thu Feb 26 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.5
- Rebuild for Fedora
* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.6.5-alt1.qa1
- NMU: rebuilt for debuginfo.
* Fri Jun 13 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.5-alt1
- 2.6.5 released
* Wed Nov 21 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.5-alt0.1
- first build for alt linux
