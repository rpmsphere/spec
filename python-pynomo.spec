%global debug_package %{nil}
Summary: Nomographs with Python
Name: python-pynomo
Version: 0.2.2
Release: 5.1
Source0: http://sourceforge.net/projects/pynomo/files/pynomo/0.2.2/PyNomo-%{version}.tar.gz
License: GPLv2
Group: Development/Libraries
BuildArch: noarch
URL: http://pynomo.org/
BuildRequires: python

%description
Pynomo is a program to create (pdf) nomographs (nomograms) using Python
interpreter. A nomograph (nomogram) is a graphical solution to an equation.

%prep
%setup -q -n PyNomo-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{python2_sitelib}/*

%changelog
* Sun Jun 30 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuild for Fedora
