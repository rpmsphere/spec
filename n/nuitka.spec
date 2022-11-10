%undefine _debugsource_packages

Name: nuitka
Version: 1.1.6
Release: 1
Summary: Python compiler with full language support and CPython compatibility
License: ASLv2.0
Group: Development/Python
URL: https://pypi.python.org/pypi/Nuitka/
Source: http://nuitka.net/releases/Nuitka-%version.tar.gz
BuildArch: noarch
BuildRequires: python3-devel python3-setuptools

%description
Nuitka is **the** Python compiler. It is a seamless replacement or
extension to the Python interpreter and compiles **every** construct
that CPython 2.6, 2.7, 3.2, 3.3, and 3.4 have. It then executed
uncompiled code, and compiled code together in an extremely compatible
manner.

You can use all Python library modules or and all extension modules
freely. It translates the Python into a C level program that then uses
"libpython" to execute in the same way as CPython does. All optimization
is aimed at avoiding overhead, where it's unnecessary. None is aimed at
removing compatibility, although there is an "improved" mode, where not
every bug of standard Python is emulated, e.g. more complete error
messages are given.

%prep
%setup -q -n Nuitka-%version

%build
%py3_build

%install
%py3_install

%files
%doc *.rst
%{_bindir}/*
%{python3_sitelib}/*

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.6
- Rebuilt for Fedora
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.11-alt1.git20150318.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.11-alt1.git20150318.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)
* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.11-alt1.git20150318
- Initial build for Sisyphus
