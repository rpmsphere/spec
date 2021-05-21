Name:           python3-markups
Version:        0.2.4
Release:        2.1
License:        BSD-3-Clause
Summary:        A wrapper around various text markups
URL:            http://launchpad.net/python-markups
Group:          Development/Languages/Python
Source:         http://pypi.python.org/packages/source/M/Markups/Markups-%{version}.tar.gz
BuildRequires:  python3-devel
BuildArch:      noarch

%description
This module provides a wrapper around the various text markup languages,
such as Markdown and reStructuredText (these two are supported by default).

%prep
%setup -q -n Markups-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc LICENSE README examples
%{python3_sitelib}/*

%changelog
* Fri Jun 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4
- Rebuilt for Fedora
* Wed Feb  6 2013 saschpe@suse.de
- Completely redone spec file
* Sat Feb  2 2013 i@marguerite.su
- initial version 0.2.4
