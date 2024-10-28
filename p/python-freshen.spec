%undefine _debugsource_packages
Name:           python-freshen
Version:        0.2
Release:        4.1
URL:            https://github.com/rlisagor/freshen
Summary:        Clone of the Cucumber BDD framework for Python
License:        GPL
Group:          Development/Languages/Python
Source:         freshen-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
Requires:       python-nose
Requires:       python-yaml
Requires:       pyparsing
BuildArch:      noarch

%description
Freshen is an acceptance testing framework for Python.
It is built as a plugin for Nose.
It uses the (mostly) same syntax as Cucumber.

%prep
%setup -q -n freshen-%{version}

%build
export CFLAGS="%{optflags}"
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot} --record=INSTALLED_FILES.txt

%files -f INSTALLED_FILES.txt
%{python2_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Tue Jul 26 2011 toms@suse.de
- Added missing dependencies python-yaml and python-pyparsing
* Mon Jul 25 2011 toms@suse.de
- Initial version 0.2
