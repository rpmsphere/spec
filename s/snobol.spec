%global debug_package %nil

Name: snobol
Version: 4.1.5
Release: 1
Summary: The SNOBOL programming language
Group: Development/Other
License: BSD
URL: http://www.snobol4.org
Source0: ftp://ftp.ultimate.com/%name/%{name}4-1.5.tar.gz
Patch1: snobol-4.1.4.1-makefile.patch
Patch2: snobol-4.1.4.1-doc.patch
BuildRequires: gcc-c++
BuildRequires: tcl-devel
BuildRequires: tk-devel
BuildRequires: gdbm-devel
BuildRequires: m4
Provides: snobol-devel = %version-%release
Source44: import.info

%description
SNOBOL4, while known primarily as a string language excels at any task
involving symbolic manipulations.  It provides run time typing,
garbage collection, user data types, on the fly compilation.  It's
primary weakness is it's simple syntax, and lack of "structured
programming" and "object oriented" constructs.

%prep
%setup -qn %{name}4-1.5
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -Wl,--allow-multiple-definition"
./configure  --prefix=/usr --mandir=%_mandir \
             --snolibdir=%_datadir/snobol4 \
              --with-tcl=%_libdir/tclConfig.sh
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYRIGHT README CHANGES doc/load.txt
%_bindir/snobol*
%_bindir/sdb*
%_datadir/snobol4/
%_mandir/man*/*

%changelog
* Sat Apr 3 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.5
- Rebuild for Fedora
* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.1.5-alt2.qa1
- NMU: rebuild against Tcl/Tk 8.6
* Tue Apr 17 2014 Ilya Mashkin <oddity@altlinux.ru> 4.1.5-alt2
- Build for Sisyphus
* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.5-alt1_4
- update to new release by fcimport
* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.4.1-alt1_4
- update to new release by fcimport
* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.4.1-alt1_3
- initial fc import