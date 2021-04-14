%define __python /usr/bin/python2
Summary:	Python Module for embedding C/C++
Name:		pyembedc
Version:	0.22
Release:	4.1
Source0:	http://sourceforge.net/projects/pyembedc/files/embedc-%{version}.tar.gz
License:	GPLv2
Group:		Development/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Requires:	python
URL:		http://pyembedc.sourceforge.net/
BuildRequires: python

%description
Python module to embed C/C++ code within Python programs and scripts.
Transparently allow native access to python data from C code and vice versa.
Module provides all the "glue" to dynamically convert data types, arrays
and structures.

%prep
%setup -q -n embedc-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc README.txt
%{python_sitelib}/*

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.22
- Rebuilt for Fedora
