Name:          libcfg+
Version:       0.6.2
Release:       17.1
Summary:       A C library that features multi- command line and configuration file parsing
Group:         System/Libraries
URL:           http://platon.sk/projects/libcfg+
Source:        http://platon.sk/upload/_projects/00003/%{name}-%{version}.tar.gz
License:       GPL
BuildRequires: docbook-utils
BuildRequires: w3m

%description
libcfg+ is a C library that features multi- command line and configuration
file parsing. It is possible to set up various special properties such as
quoting characters, deliminator strings, file comment prefixes, multi-line
postfixes, and more. It supports many data types such as booleans, integers,
decimal numbers, strings with many additional data type flags (such as
multiple values for a single option).

%package devel
Group:         Development/Libraries
Summary:       Static libraries and headers for %{name}
Requires:      %{name} = %{version}
AutoReqProv: off

%description devel
libcfg+ is a C library that features multi- command line and configuration
file parsing. It is possible to set up various special properties such as
quoting characters, deliminator strings, file comment prefixes, multi-line
postfixes, and more. It supports many data types such as booleans, integers,
decimal numbers, strings with many additional data type flags (such as
multiple values for a single option).

This package contains static libraries and header files need for development.

%prep
%setup -q

%build
%configure
make LD=gcc CFLAGS="%{optflags} -fpic -fPIC -shared"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# fixup strange shared library permissions
chmod 755 $RPM_BUILD_ROOT%{_libdir}/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/*.so.*
%doc AUTHORS COPYING ChangeLog README TODO

%files devel
%{_includedir}/*.h
%{_includedir}/platon/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_mandir}/man3/*
%{_datadir}/doc/%{name}-%{version}

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.2
- Rebuild for Fedora
* Sat Jul 26 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 0.6.2-5mamba
- specfile updated
* Wed May 10 2006 Stefano Cotta Ramusino <stefano.cotta@qilinux.it> 0.6.2-4qilnx
- fixed strange shared library permissions
* Wed Feb 15 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.6.2-3qilnx
- build libraries in PIC mode
* Tue Sep 14 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.6.2-2qilnx
- moved libcfg+.so library from devel package to main package
* Mon Sep 13 2004 Silvan Calarco <silvan.calarco@mambasoft.it> 0.6.2-1qilnx
- package created by autospec
