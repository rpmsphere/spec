%global debug_package %{nil}
Name: python-pywm
Version: 1.21
Release: 7.1
Summary: Module python for WindowMaker docklets
Summary(ru_RU.UTF-8): Модуль python для написания докапплетов WindowMaker
License: GPL
Group: Development/Python
URL: http://pywmdockapps.sourceforge.net/
Source0: pywmdockapps-%{version}.tar.gz
BuildRequires: libXext-devel libXpm-devel python2-devel
Provides: pywmdockapps

%description
Pywmgeneral is a Python module that will help you develope WindowMaker
dockapps in Python. It is mostly a wrapper around the functions from
the popular wmgeneral.c, but some new functions are added too.

It also contains the Python written module pywmhelpers.py which
contains functions to aid the development of WM dockapps. This module
contains Python functions that wrap up the functions which the
extension module provides. They ease up argument passing and give
nicer return values. Some additional functions, like help for handling
a simple configuration file is also available. This module is better
documented than the pywmgeneral. It is adviced to only use pywmhelpers
and not touch the pywmgeneral module directly at all. For information
about how to use the module, see the documentation in pywmhelpers.py.
It is also possible to import it in the interactive interpreter and
issue 'help(pywmhelpers)'.

%prep
%setup -q -n pywmdockapps-%version

%build
python2 setup.py build

%install
python2 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc README*
%{_bindir}/*
%{python2_sitearch}/*

%changelog
* Tue Aug 21 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.21
- Rebuild for Fedora
* Sat Jan 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus
