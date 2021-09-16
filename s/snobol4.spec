%undefine _debugsource_packages

Name: snobol4
Version: 2.2.1
Release: 1
Summary: The SNOBOL4 programming language
Group: Development/Other
License: BSD
URL: http://www.snobol4.org
Source0: ftp://ftp.ultimate.com/%name/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: tcl-devel
BuildRequires: tk-devel
BuildRequires: gdbm-devel
BuildRequires: m4
Provides: snobol4-devel = %version-%release
Source44: import.info

%description
SNOBOL4, while known primarily as a string language excels at any task
involving symbolic manipulations.  It provides run time typing,
garbage collection, user data types, on the fly compilation.  It's
primary weakness is it's simple syntax, and lack of "structured
programming" and "object oriented" constructs.

%prep
%setup -q
sed -i 's|extern int getopt.*|extern int getopt (int ___argc, char *const *___argv, const char *__shortopts);|' include/lib.h

%build
export CFLAGS="$RPM_OPT_FLAGS -Wl,--allow-multiple-definition"
./configure  --prefix=/usr --mandir=%_mandir \
             --snolibdir=%_libdir/snobol4 \
             --with-tcl=%_libdir/tclConfig.sh
#make %{?_smp_mflags}
make

%install
mkdir -p %{buildroot}%{_mandir}/man{3,7}
make install DESTDIR=$RPM_BUILD_ROOT
mv  %{buildroot}%{_docdir}/%{name}-%{version} %{buildroot}%{_docdir}/%{name}
cp COPYRIGHT README CHANGES doc/load.txt %{buildroot}%{_docdir}/%{name}

%files
%_docdir/%{name}
%_bindir/*
%_libdir/%{name}
%_mandir/man*/*

%changelog
* Sun Sep 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.1
- Rebuilt for Fedora
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
