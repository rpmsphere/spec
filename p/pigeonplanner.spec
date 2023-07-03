%undefine _debugsource_packages
Name: pigeonplanner
Summary: A simple to use pigeon database
Version: 2.2.2
Release: 4.1
Group: Applications/Databases
URL: https://www.pigeonplanner.com/
Source0: https://sourceforge.net/projects/pigeonplanner/files/pigeonplanner/Pigeon%20Planner%20%{version}/%{name}-%{version}.tar.gz
License: GPLv3
BuildArch: noarch
BuildRequires:  python2
BuildRequires: python2-setuptools

%description
Pigeon Planner is free and open-source racing pigeon software. The goal is to
be a simple, yet powerful pigeon organizer. Enter your pigeons with all of
their details in the user friendly interface and let the program calculate
the pedigree and relatives. Results can be given for each pigeon and then be
compared between all races and pigeons.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install -O1 --prefix /usr --skip-build --root $RPM_BUILD_ROOT
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc AUTHORS CHANGES COPYING README
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{python2_sitelib}/*

%changelog
* Tue Feb 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.2
- Rebuilt for Fedora
