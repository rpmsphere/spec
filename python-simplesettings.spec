Name:           python-simplesettings
Version:        0.5
Release:        2.1
Summary:        Simple settings initialization for Python libraries

Group:          Development/Languages
License:        ASL 2.0
URL:            http://code.google.com/p/simplesettings/
Source0:        http://pypi.python.org/packages/source/s/simplesettings/simplesettings-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
Simple settings initialization for third party apps and libraries
in Python.

%prep
%setup -q -n simplesettings-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name ._* -exec rm -f {} \;

%check
%{__python} setup.py test

 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitelib}/simplesettings/
%{python_sitelib}/simplesettings*.egg-info

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuild for Fedora

* Mon Jul 13 2009 Fabian Affolter <fabian@bernewireless.net> - 0.5-1
- Initial spec for Fedora
