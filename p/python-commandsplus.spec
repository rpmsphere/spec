%undefine _debugsource_packages
Summary: A better version of the Python commands module
Name: python-commandsplus
Version: 0.2.3
Release: 9.1
Source0: %{name}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildArch: noarch
Vendor: Manuel Amador (Rudd-O) <dragonfear@gmail.com>
URL: https://www.usm.edu.ec/~amadorm/software/
BuildRequires: python python-devel

%description
A Python module with a function that complements the getstatusoutput function
in the standard commands module.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT --prefix=/usr

%files
%doc README COPYING ChangeLog TODO testsuite
%{python2_sitelib}/*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3
- Rebuilt for Fedora
