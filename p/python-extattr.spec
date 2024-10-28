%undefine _debugsource_packages
Summary: An interface to the UNIX getfattr and setfattr commands
Name: python-extattr
Version: 0.1.3
Release: 10.1
Source0: %{name}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildArch: noarch
Vendor: Manuel Amador (Rudd-O) <dragonfear@gmail.com>
Requires: python-commandsplus
URL: https://www.usm.edu.ec/~amadorm/software/
BuildRequires: python python-devel

%description
A Python extension created to manipulate extended attributes in filesystems that support them.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT --prefix=/usr

%files
%doc README COPYING ChangeLog testsuite
%{python2_sitelib}/*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.3
- Rebuilt for Fedora
