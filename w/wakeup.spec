%undefine _debugsource_packages
Name: wakeup
Summary: Fully customizable and extensible talking alarm clock
Version: 1.4
Release: 1
Group: Utilities
License: GPL
URL: https://launchpad.net/wakeup
Source0: https://launchpad.net/wakeup/trunk/%{version}/+download/%{name}_%{version}.tar.gz
BuildRequires: python2-devel
BuildArch: noarch

%description
This package has a complete graphical front end with which a user can set an
alarm to wake the computer - from poweroff if possible - and read a
user-defined text. This text can grab relevant information (date, time,
weather, Evolution schedule and tasks, news from an rss feed, number of new
email messages, etc.) and speak that as well, or play music, all as defined
by the user. More capabilities can be added to the alarm via a complete and
simple plugin system. Supports multiple alarms.

%prep
%setup -q -c

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py %{buildroot}%{_datadir}/%{name}/*/*/*.py
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/plugin_scripts/EvolutionData/read_evolution.py
sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/*
%{_mandir}/man1/*.1.*
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/polkit-1/actions/com.ubuntu.wakeup.policy
%{_datadir}/%{name}

%changelog
* Sun Jul 3 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
