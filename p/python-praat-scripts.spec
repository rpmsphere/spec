%define __python /usr/bin/python3

Name: python-praat-scripts
Summary: Interface for running Praat scripts through Python
Version: 0.1.14
Release: 4.1
Group: Development/Libraries
License: GPLv3
URL: http://pypi.python.org/pypi/python-praat-scripts/
Source0: https://pypi.python.org/packages/source/p/python-praat-scripts/python-praat-scripts-0.1.14.tar.gz
BuildRequires: python3
BuildArch: noarch

%description
Interface for running Praat scripts through Python.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%doc CHANGES.txt LICENSE.txt README.md
%{python3_sitelib}/*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.14
- Rebuilt for Fedora
