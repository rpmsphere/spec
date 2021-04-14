Name:           python-pycukes
Version:        0.2
Release:        3.1
URL:            http://github.com/hugobr/pycukes
Summary:        A Cucumber-like BDD framework built on top of Pyhistorian
License:        MIT License
Group:          Development/Languages/Python
Source:         http://pypi.python.org/packages/source/p/pycukes/pycukes-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python-should_dsl
#BuildRequires:  python-story_parser
#BuildRequires:  python-pyhistorian
Requires:       python-should_dsl
Requires:       python-story_parser
Requires:       python-pyhistorian
BuildArch:      noarch

%description
PyCukes is a Cucumber-like BDD tool built on top of Pyhistorian.
PyCukes was created to fill the gap pyhistorian left, so with it is
possible to talk to your stakeholders first with text files, instead
of simple understendable python files like Pyhistorian.

%prep
%setup -q -n pycukes-%{version}

%build
export CFLAGS="%{optflags}"
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
sed -i 's|/bin/python$|/usr/bin/python3|' %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{python3_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Sat Jul 23 2011 toms@suse.de
- Initial version 0.2
