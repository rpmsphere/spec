Name: oo2c
Summary: Optimizing Oberon-2 Compiler
Version: 2.1.11
Release: 13.1
Group: Development/Languages
License: GPLv2, LGPLv2
URL: https://sourceforge.net/projects/ooc/
Source0: https://sourceforge.net/projects/ooc/files/ooc2/%{version}/%{name}_64-%{version}.tar.bz2

%description
OOC is an Oberon-2 development platform implemented by a german university at
Kaiserslautern. It consists of an optimizing compiler, a number of related tools,
a set of standard library modules, and a reference manual.

%prep
%setup -q -n %{name}_64-%{version}

%build
%configure
%make_build

%install
#make_install
install -d %{buildroot}%{_mandir}/man1
for i in oo2c oob ooef oowhereis; do
  install -m644 man/$i.1 %{buildroot}%{_mandir}/man1/$i.1
done
install -d %{buildroot}%{_libdir}/oo2c/pkginfo
stage0/oo2c --config oo2crc-install.xml -v --bindir %{buildroot}%{_bindir} --libdir %{buildroot}%{_libdir} --oocdir %{buildroot}%{_libdir}/oo2c -r lib -r . --install-program "/usr/bin/install -c"  --install-package liboo2c
stage0/oo2c --config oo2crc-install.xml -v --bindir %{buildroot}%{_bindir} --libdir %{buildroot}%{_libdir} --oocdir %{buildroot}%{_libdir}/oo2c -r lib -r . --install-program "/usr/bin/install -c"  --install-package oo2c
/usr/bin/install -c rsrc/OOC/oobacktrace %{buildroot}%{_bindir}/oobacktrace
chmod a+x %{buildroot}%{_libdir}/oo2c/install-sh

%files
%doc COPYING PROBLEMS README
%{_bindir}/*
%{_libdir}/lib%{name}.*
%{_libdir}/%{name}
%{_mandir}/man1/*

%changelog
* Thu Oct 11 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.11
- Rebuild for Fedora
