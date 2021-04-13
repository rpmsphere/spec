%define _name PyUPC-EAN

Summary: A barcode library/module for python
Name: python-upcean
Version: 2.7.10
Release: 5.1
Source0: %{_name}-%{version}.tar.gz
License: Revised BSD License
Group: Development/Libraries
BuildArch: noarch
URL: https://github.com/GameMaker2k/PyUPC-EAN
BuildRequires: python
BuildRequires: python-setuptools

%description
PyUPC-EAN is a barcode library/module for Python. It supports the barcode
formats upc-e, upc-a, ean-13, ean-8, ean-2, ean-5, itf14, codabar, code11,
code39, code93, and msi.

%prep
%setup -q -n %{_name}-%{version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{python_sitelib}/*

%changelog
* Thu Apr 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.10
- Rebuild for Fedora
* Mon Jan 05 2015 Kazuki Przyborowski <kazuki.przyborowski@gmail.com>
- Initial package