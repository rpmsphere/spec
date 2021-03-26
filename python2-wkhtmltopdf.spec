%define module wkhtmltopdf

Name:		python2-%{module}
Version:	0.2.1315461079
Release:	19.1
Summary:	Python module for parsing HTML to PDF
Group:		Development/Languages
License:	GPL
URL:		https://github.com/qoda/python-wkhtmltopdf/
Source:		python-%{module}-%{version}.tar.bz2
Patch:		python-wkhtmltopdf.patch
BuildArch:	noarch
BuildRequires:	python2-devel, python2-setuptools

%description
A simple python wrapper for the wkhtmltopdf lib with flash support.

%prep
%setup -q -n python-%{module}-%{version}
%patch -p 0

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
#doc LICENSE
%{python2_sitelib}/*

%changelog
* Sun Jan 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1315461079
- Rebuild for Fedora
* Mon Jan 10 2012 - TI_Eugene <ti.eugene@gmail.com> - 0.2
- Initial RPM release
