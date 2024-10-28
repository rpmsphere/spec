%undefine _debugsource_packages
Name:           python-pyhistorian
Version:        0.6.8
Release:        2.1
URL:            https://github.com/hugobr/pyhistorian
Summary:        BDD Tool for Writing Specifications Using Given-When-Then Templates
License:        MIT License
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/p/pyhistorian/pyhistorian-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-should_dsl
BuildRequires:  python-termcolor
Requires:       python-should_dsl
Requires:       python-termcolor
BuildArch:      noarch

%description
The goal of *pyhistorian* is to write an internal Given-When-Then
template using Python. The ideas came from JBehave, RBehave,
Cucumber and others.

It's possible to write your stories in English and Portuguese,
choose your preferred.

%prep
%setup -q -n pyhistorian-%{version}

%build
export CFLAGS="%{optflags}"
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%{python2_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.8
- Rebuilt for Fedora
* Sat Jul 23 2011 toms@suse.de
- Initial version 0.6.8
