%define _python_dist_allow_version_zero 1
%define __python /usr/bin/python3

Name: python-bitey
Summary: Bitcode Import Tool
Version: 0.20120813
Release: 3.1
Group: Applications/Tools
License: BSD
URL: https://github.com/dabeaz/bitey
Source0: bitey-master.zip
BuildRequires: python3
BuildArch: noarch

%description
Bitey allows LLVM bitcode to be directly imported into Python as
an high performance extension module without the need for writing wrappers.

%prep
%setup -q -n bitey-master

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%doc CHANGES LICENSE LIMITATIONS README.rst
%{python3_sitelib}/*

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20120813
- Rebuilt for Fedora
