%global debug_package %{nil}
Name:		python-nxt
Version:	2.2.2
Release:	4.1
Summary:	A pure-python driver/interface/wrapper for the Lego Mindstorms NXT robot
Group:		Applications/Engineering
License:	GPLv2+
URL:		http://code.google.com/p/nxt-python/
Source0:	http://nxt-python.googlecode.com/files/nxt-python-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python2-devel
Requires:	pybluez, pyusb, pygtk2
Provides:	nxt_python, nxt-python

%description
nxt-python is a python driver/interface for the Lego Mindstorms NXT robot.
The 1.x releases aim to improve on NXT_Python's interface and should be
compatible with scripts which use it while the 2.x releases improve on the
API in backwards-incompatible ways and will not work with NXT_Python scripts.

%prep
%setup -q -n nxt-python-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%doc LICENSE README 
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Sun Mar 10 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.2
- Rebuild for Fedora
