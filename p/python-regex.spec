Name:           python-regex
Version:        0.1.20130626
Release:        4.1
Summary:        Alternative regex implementation
License:        Python Software Foundation License
URL:            https://code.google.com/p/mrab-regex-hg/
Source0:        https://pypi.python.org/packages/source/r/regex/regex-2013-06-26.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	python-devel

%description
This new regex implementation is intended eventually to replace Python's
current re module implementation.

%prep
%setup -q -n regex-2013-06-26

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%{python_sitearch}/*

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.20130626
- Rebuild for Fedora
* Mon Jun 10 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 0.1.20120613
- Initial package
