%define module rarfile

Name:           python-%{module}
Version:        2.4
Release:        2.1
Summary:        RAR archive reader for Python
Group:          Development/Languages
License:        ISC
URL:            http://rarfile.berlios.de/
Source0:        http://download.berlios.de/%{module}/%{module}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel
Requires:	unrar

%description
This is Python module for RAR archive reading.
The interface is made as zipfile like as possible.
Licensed under ISC license.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README NEWS LICENSE FAQ
%{python_sitelib}/*

%changelog
* Tue Nov 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4-1
- Rebuild for Fedora
