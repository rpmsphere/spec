%global debug_package %{nil}
Summary: A complete proxy class for controlling amaroK from Python
Name: python-amarok
Version: 0.1.1
Release: 8.1
Source0: %{name}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildArch: noarch
Vendor: Manuel Amador (Rudd-O) <dragonfear@gmail.com>
Requires: python-commandsplus python-Observable
URL: http://www.usm.edu.ec/~amadorm/software/
BuildRequires: python-devel

%description
This module contains a nearly feature-complete class that can be used
to control amaroK from amaroK scripts.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT --prefix=/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING ChangeLog TODO
%{python2_sitelib}/*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuild for Fedora
