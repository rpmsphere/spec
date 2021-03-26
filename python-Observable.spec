Summary: A reusable implementation of the Observer/Observable pattern in Python
Name: python-Observable
Version: 0.1.0
Release: 9.1
Source0: %{name}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildArch: noarch
Vendor: Manuel Amador (Rudd-O) <dragonfear@gmail.com>
URL: http://www.usm.edu.ec/~amadorm/software/
BuildRequires: python-devel

%description
This module has a complete Observer/Observable implementation for Python.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --prefix=/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING ChangeLog TODO
%{python_sitelib}/*

%changelog
* Sun Sep 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Rebuild for Fedora
