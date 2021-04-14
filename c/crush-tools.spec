Name:         crush-tools
Summary:      Custom Reporting Utilities for Shell
URL:          http://code.google.com/p/crush-tools/
Group:        Text
License:      Apache
Version:      2013.04
Release:      13.1
Source0:      http://crush-tools.googlecode.com/files/crush-tools-2013-04.tar.gz

%description
CRUSH (Custom Reporting Utilities for SHell) is a collection of
tools for processing delimited-text data from the command line or in
shell scripts.

%prep
%setup -q -n crush-tools-2013-04
sed -i 's|use FALLBACK|using FALLBACK|' src/calcfield/calcfield.in

%build
./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir} \
    --build=x86_64 \
    --disable-shared
sed -i 's|-Wall|-Wall -Wno-format-security|' Makefile
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

%files
%{_bindir}/*
%{_includedir}/*
%{_libdir}/lib*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2013.04
- Rebuilt for Fedora
