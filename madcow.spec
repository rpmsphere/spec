%global debug_package %{nil}
Summary:	Another Python IRC bot
Name:		madcow
Version:	2.2.3
Release:	4.1
Source0:	https://nodeload.github.com/cjones/madcow/madcow-2.2.3.tar.gz
License:	GPL
Group:		Internet
BuildArch:	noarch
BuildRequires:	python2
BuildRequires:	python2-setuptools
URL:		https://github.com/cjones/madcow

%description
Madcow is an extensible python IRC bot with support for SILC and AIM. It is
fully customizable and has a simple API for creating modules that extend its
functionality. Madcow ships with modules that emulate classic Infobot
behavior and many other fun or useful utilities.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc doc/* ChangeLog LICENSE README
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.3
- Rebuild for Fedora
