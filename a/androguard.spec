%global debug_package %{nil}
Summary: Reverse engineering, Malware and goodware analysis of Android applications
Name: androguard
Version: 1.9
Release: 4.1
Source0: https://androguard.googlecode.com/files/%{name}-%{version}.tar.gz
License: LGPL
Group: System/Tools
BuildArch: noarch
URL: https://code.google.com/p/androguard/
BuildRequires: python2-devel
BuildRequires: python2-setuptools

%description
Androguard is mainly a tool written in python to play with :
* Dex/Odex (Dalvik virtual machine) (.dex) (disassemble, decompilation),
* APK (Android application) (.apk),
* Android's binary xml (.xml),
* Android Resources (.arsc).

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install -O1 --root=$RPM_BUILD_ROOT
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*.py

sed -i 's|/usr/bin/env python|/usr/bin/python2|' $RPM_BUILD_ROOT%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Sun Jan 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9
- Rebuilt for Fedora
