%global debug_package %{nil}
Name: java2python
Summary: Translate Java source code into Python
Version: 0.5.1git
Release: 6.1
Group: Development/Tools
URL: https://github.com/natural/java2python
Source0: %{name}-master.zip
License: LGPL
BuildArch: noarch
BuildRequires: python2-devel

%description
The java2python package can translate any syntactically valid Java source code
file. The generated Python code is not guaranteed to run, nor is guaranteed to
be syntactically valid Python. However, java2python works well many cases, and
in some of those, it creates perfectly usable and workable Python code.

%prep
%setup -q -n %{name}-master
cp license.txt doc

%build
python2 setup.py build

%install
python2 setup.py install -O1 --prefix /usr --skip-build --root %{buildroot}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
mkdir -p %{buildroot}%{_datadir}/doc
mv %{buildroot}/usr/doc %{buildroot}%{_datadir}/doc/%{name}-%{version}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/j2py

%files
%{_bindir}/j2py
%{python2_sitelib}/*
%{_datadir}/doc/%{name}-%{version}

%changelog
* Sun Mar 10 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.1
- Rebuild for Fedora

