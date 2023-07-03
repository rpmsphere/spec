%define pyname astropysics

Name:           python2-%{pyname}
Version:        1.0
Release:        8.1
Summary:        A python library for astronomy/astrophysics
License:        Apache v2.0
URL:            https://packages.python.org/Astropysics/
Group:          Development/Libraries/Python
Source0:        Astropysics-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-setuptools

%description
A python library for astronomy/astrophysics calculations and data analysis.
The functionality of Astropysics is currently being incorporated into the Astropy project.

%prep
%setup -q -n Astropysics-%{version}
sed -i '24s|^    ||' astropysics/data/ipy_profile_astpys.py
sed -i '/use_setuptools/d' setup.py

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc licenses/*
%{python2_sitelib}/*
%{_bindir}/*

%changelog
* Mon Oct 15 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Sun May  1 2011 ocefpaf@yahoo.com.br
- updated to release 1039
* Sat Apr 23 2011 ocefpaf@yahoo.com.br
- updated to release 1038
* Thu Apr 21 2011 ocefpaf@yahoo.com.br
- updated to release 1036
* Sat Apr 16 2011 ocefpaf@yahoo.com.br
- updated to release 1032
* Sat Apr  2 2011 ocefpaf@yahoo.com.br
- updated to release 1031
* Sat Mar 19 2011 ocefpaf@yahoo.com.br
- updated to release 1021
* Sat Mar 12 2011 ocefpaf@yahoo.com.br
- updated to release 1012
* Tue Mar  8 2011 ocefpaf@yahoo.com.br
- updated to release 1005
* Sat Feb 26 2011 ocefpaf@yahoo.com.br
- first OpenSsuse release
