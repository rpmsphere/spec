%global debug_package %{nil}
%define _name PyLogo

Summary: Logo interpreter in Python
Name: pylogo
Version: 0.4
Release: 7.1
Source0: %{_name}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildArch: noarch
URL: http://pylogo.org
BuildRequires:  python2

%description
An interpreter for the Logo educational programming language.
This version of Logo is a faithful representation of the language,
written in a way that makes it compatible with Python code.
Primitives are written in Python, and Python can call Logo code
similar to how it calls Python code.

%prep
%setup -q -n %{_name}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Sun May 05 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
* Sun Jul 18 2010 Ian Bicking <ianb@colorstudy.com>
- Initial package
