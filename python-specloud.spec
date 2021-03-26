%global debug_package %{nil}
Name:           python-specloud
Version:        0.4.4
Release:        4.1
URL:            http://github.com/hugobr/specloud
Summary:        Install nosetests and Plugins to Ease BDD Unit Specs
License:        MIT
Group:          Development/Languages/Python
Source:         specloud-%{version}.tar.gz
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildArch:      noarch

%description
The command line tool `specloud` colorizes green for tests
with no failures and no errors and red for tests with
failures and/or errors

The project was born as a proof of concept and I named
it firstly `pyunitbdd`. But that's a terrible name. So I
renamed the project to `specloud`.

%prep
%setup -q -n specloud-%{version}

%build
export CFLAGS="%{optflags}"
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.4
- Rebuild for Fedora
* Fri Jul 22 2011 toms@suse.de
- First initial build 0.4.4 (proof of concept)
