%define __python /usr/bin/python3

Name: python-pies
Summary: The simplest (and tastiest) way to write one program that runs on both Python 2 and Python 3
Version: 2.6.0
Release: 3.1
Group: Development/Libraries
License: MIT
URL: http://timothycrosley.github.io/pies/
Source0: pies-%{version}.tar.gz
BuildRequires: python3-devel
BuildArch: noarch

%description
Pies is a Python 2 and Python 3 compatibility layer with the philosophy that
all code should be Python 3 code. Starting from this viewpoint means that when
running on Python 3, Pies adds virtually no overhead. Instead of providing
a bunch of custom methods (leading to Python code which looks out of place on
any version), Pies aims to backport as many of the Python 3 API calls, imports,
and objects to Python 2 as possible, relying on special syntax only when
absolutely necessary.

%prep
%setup -q -n pies-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot}

%files
%doc LICENSE README.md
%{python3_sitelib}/*

%changelog
* Mon Feb 10 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.0
- Rebuilt for Fedora
