%define __python /usr/bin/python3

Summary:        Python Module for embedding C/C++
Name:           pyembedc
Version:        0.22
Release:        4.1
Source0:        https://sourceforge.net/projects/pyembedc/files/embedc-%{version}.tar.gz
License:        GPLv2
Group:          Development/Libraries
BuildArch:      noarch
Requires:       python
URL:            https://pyembedc.sourceforge.net/
BuildRequires:  python3

%description
Python module to embed C/C++ code within Python programs and scripts.
Transparently allow native access to python data from C code and vice versa.
Module provides all the "glue" to dynamically convert data types, arrays
and structures.

%prep
%setup -q -n embedc-%{version}

%build
python3 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python3 setup.py install --root=$RPM_BUILD_ROOT

%files
%doc README.txt
%{python3_sitelib}/*

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.22
- Rebuilt for Fedora
