Name:           python-should_dsl
Version:        2.0a4
Release:        2.1
URL:            http://github.com/hugobr/should-dsl
Summary:        Should assertions in Python as clear and readable as possible
License:        MIT License
Group:          Development/Languages/Python
Source:         http://pypi.python.org/packages/source/s/should_dsl/should_dsl-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-setuptools
BuildArch:      noarch

%description
The goal of *Should-DSL* is to write should expectations in Python
as clear and readable as possible, using "almost" natural
language (limited - sometimes - by the Python language constraints).

%prep
%setup -q -n should_dsl-%{version}

%build
export CFLAGS="%{optflags}"
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0a4
- Rebuilt for Fedora
* Sat Jul 23 2011 toms@suse.de
- Initial version 2.0a4
