Name:           python2-simplesettings
Version:        0.5
Release:        2.1
Summary:        Simple settings initialization for Python libraries
Group:          Development/Languages
License:        ASL 2.0
URL:            http://code.google.com/p/simplesettings/
Source0:        http://pypi.python.org/packages/source/s/simplesettings/simplesettings-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description
Simple settings initialization for third party apps and libraries
in Python.

%prep
%setup -q -n simplesettings-%{version}

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name ._* -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE
%{python2_sitelib}/simplesettings/
%{python2_sitelib}/simplesettings*.egg-info

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Mon Jul 13 2009 Fabian Affolter <fabian@bernewireless.net> - 0.5-1
- Initial spec for Fedora
