Name:           python3-aiml
Version:        0.9.3
Release:        4
Summary:        An interpreter package for AIML, the Artificial Intelligence Markup Language
License:        BSD-2-Clause
URL:            https://github.com/paulovn/python-aiml
Source:         https://files.pythonhosted.org/packages/source/p/python-aiml/python-aiml-%{version}.zip
BuildRequires:  python3-setuptools
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch

%description
python3-aiml implements an interpreter for AIML, the Artificial Intelligence
Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E. Foundation.
It can be used to implement a conversational AI program.

This package was forked from PyAIML 0.8.6 which seems to have been abandoned
for a long time.

%prep
%setup -q -n python-aiml-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc CHANGES.txt README.rst
%license COPYING.txt
%{_bindir}/*
%{python3_sitelib}/*

%changelog
* Sun Oct 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.3
- Rebuilt for Fedora
* Tue Jun  1 2021 Matej Cepl <mcepl@suse.com>
- Add missing Provides for obsoleted symbol.
* Tue Jun  1 2021 pgajdos@suse.com
- %%check: use %%pyunittest rpm macro
* Wed May 20 2020 Petr Gajdos <pgajdos@suse.com>
- %%python3_only -> %%python_alternative
* Mon Mar  9 2020 Tomáš Chvátal <tchvatal@suse.com>
- Update to 0.9.3:
  * various python compatiblity fixes
* Tue Dec  4 2018 Matej Cepl <mcepl@suse.com>
- Remove superfluous devel dependency for noarch package
* Sun Mar  4 2018 alarrosa@suse.com
- Initial release of python-python-aiml 0.9.1
