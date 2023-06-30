%undefine _debugsource_packages
Name: gosiege
Summary: Go Siege
Version: 0.3
Release: 11.1
Group: Amusements/Games
License: GPLv2
URL: https://sourceforge.net/projects/gosiege/
Source0: https://sourceforge.net/projects/gosiege/files/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires: python2-devel
BuildArch: noarch

%description
Go Siege is a transformation of the ancient Chinese game of Go into a massively
multiplayer online game in which hundreds of players can compete simultaneously.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}
cp README CREDITS COPYING Changelog %{buildroot}%{_datadir}/doc/%{name}-%{version}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
sed -i 's|twisted.python.components|zope.interface|' %{buildroot}%{python2_sitelib}/%{name}/interfaces.py

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}*

%files
%{_datadir}/doc/%{name}-%{version}
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_mandir}/man6/%{name}.6.*
%{python2_sitelib}/%{name}*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
