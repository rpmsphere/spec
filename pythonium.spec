Name: pythonium
Summary: Python 3 to Javascript translator
Version: 0.6.2
Release: 7.1
Group: Development/Tools
License: LGPL
URL: https://pypi.python.org/pypi/pythonium
Source0: https://pypi.python.org/packages/source/p/pythonium/%{name}-%{version}.tar.gz
BuildRequires: python3-devel python3-setuptools
BuildArch: noarch

%description
pythonium is written in Python that produce fast portable javascript code.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

%files
%doc README.rst
%{_bindir}/*
%{python3_sitelib}/*

%changelog
* Wed Dec 11 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.2
- Rebuild for Fedora
