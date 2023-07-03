%undefine _debugsource_packages
Name: pynguin
Summary: Python Turtle Graphics Application
Version: 0.16
Release: 3.1
Group: Applications/Education
License: GPLv3
URL: https://code.google.com/p/pynguin/
Source0: https://pynguin.googlecode.com/files/%{name}-%{version}.tgz
BuildRequires: python2-devel
BuildArch: noarch
Requires: PyQt4

%description
Pynguin is a unified editor, interactive console, and graphics display area
written using Python and the PyQt toolkit. Pynguin is meant to be an easy
environment for introducing programming concepts to beginning programmers.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_docdir}/%{name}
%{python2_sitelib}/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Jun 09 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.16
- Rebuilt for Fedora
