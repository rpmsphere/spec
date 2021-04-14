%define __python /usr/bin/python2
Name: python-bitey
Summary: Bitcode Import Tool
Version: 0.0.20120813
Release: 3.1
Group: Applications/Tools
License: BSD
URL: https://github.com/dabeaz/bitey
Source0: bitey-master.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python
BuildArch: noarch

%description
Bitey allows LLVM bitcode to be directly imported into Python as
an high performance extension module without the need for writing wrappers.

%prep
%setup -q -n bitey-master

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%doc CHANGES LICENSE LIMITATIONS README.rst
%{python_sitelib}/*

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.20120813
- Rebuilt for Fedora
