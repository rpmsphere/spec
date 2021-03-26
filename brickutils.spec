%define _name BrickUtils

Summary: Utility for building models with LEGO(R)
Name: brickutils
Version: 0.1.4.0
Release: 8.1
Source0: http://jaist.dl.sourceforge.net/project/brickutils/brickutils-0.1.4.0/%{_name}-%{version}.tar.gz
License: GNU GPL v3
Group: Amusements
BuildArch: noarch
BuildRequires: python2-devel
Vendor: Mario Pascucci <mpascucci@gmail.com>
URL: http://bricksnspace.wordpress.com/brickutils/

%description
BrickUtils is a simple utility for builders that use CAD for designing models,
such as LEGO(R) Digital Designer or MLCAD. The main problem that BrickUtils
tries to solve is the answer at the question: can I build this model with
bricks I own? So, with BrickUtils you can quickly build your brick catalog and
check if you can build a model, but you can maintain your brick collection,
buy bricks on BrickLink and much more.

%prep
%setup -q -n %{_name}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
echo 'Categories=Game;BlocksGame;' >> %{buildroot}%{_datadir}/applications/%{_name}.desktop

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.4.0
- Rebuild for Fedora
