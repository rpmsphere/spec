%global debug_package %{nil}

Name:           4th
Version:        3.62.4
Release:        3.1
Summary:        The 4tH Compiler
License:        GPLv3
URL:            http://thebeez.home.xs4all.nl/4tH/
Source0:        http://4th.googlecode.com/files/%{name}-%{version}-unix.tar.gz

%description
4tH is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low overhead.
But in the meanwhile 4tH has acquired a reputation as an educational
tool. Its simplicity makes it perfectly suited to learn Forth, from which
it has been derived.

This package is an attempt to suit both audiences. It contains
instructions how to modify the package in order to fit your own
requirements. 4tH in its current form is a calculator for simple teletype
applications. All its basic building blocks (compiler, interpreter,
decompiler, loader and saver) can be called with a single line of C. No
initialization necessary.

On the other hand there are simple instructions to compile the example
applications, which allows you to compile and run very large 4tH programs
(80386 or better). We also included a host of sample applications, like
an adventure game, a line-editor and a Forth calculator.

%prep
%setup -q -n %{name}-%{version}-unix
sed -i -e 's|/usr/lib|%{_libdir}|' -e 's|usr/local|usr|' sources/Makefile
sed -i -e 's|=/usr|=%{buildroot}/usr|' -e 's|-O3|-O2 -g -fPIC|' sources/Makefile

%build
cd sources
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/doc/4th
cd sources
make install
cp ../COPYING ../README $RPM_BUILD_ROOT%{_datadir}/doc/4th

%files
%{_bindir}/*
%{_libdir}/lib*
%{_datadir}/doc/4th
%{_datadir}/man/man1/4th.1.*

%changelog
* Thu Apr 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.62.4
- Rebuilt for Fedora
