Name:           python3-simplesettings
Version:        0.5
Release:        2.1
Summary:        Simple settings initialization for Python libraries
Group:          Development/Languages
License:        ASL 2.0
URL:            https://code.google.com/p/simplesettings/
Source0:        https://pypi.python.org/packages/source/s/simplesettings/simplesettings-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Simple settings initialization for third party apps and libraries
in Python.

%prep
%setup -q -n simplesettings-%{version}

%build
python3 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python3 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name ._* -exec rm -f {} \;

%files
%doc LICENSE
%{python3_sitelib}/simplesettings/
%{python3_sitelib}/simplesettings*.egg-info

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Mon Jul 13 2009 Fabian Affolter <fabian@bernewireless.net> - 0.5-1
- Initial spec for Fedora
