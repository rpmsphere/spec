%undefine _debugsource_packages
Name: python-pymcu
Summary: Python Micro Controller Wrapper
Version: 1.0.12
Release: 4.1
Group: Development/Libraries
License: freeware
URL: http://www.pymcu.com/moduleOverview.html
Source0: https://pypi.python.org/packages/source/p/pymcu/pymcu-1.0.12.zip
BuildRequires: python
BuildArch: noarch

%description
The pyMCU python module is the interface wrapper between the computer and
the microcontroller.

%prep
%setup -q -n pymcu-1.0.12

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%{python2_sitelib}/*

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.12
- Rebuilt for Fedora
