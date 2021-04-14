%define pyname pymodelfit

Name:           python2-%{pyname}
Version:        0.2.dev35
Release:        10.1
Summary:        Framework and GUI tool for fitting data
License:        Apache v2.0
URL:            http://code.google.com/p/pymc/downloads/list
Group:          Development/Libraries/Python
Source0:        %{pyname}-35.tar.bz2
BuildArch:      noarch
BuildRequires:  python2-setuptools
BuildRequires:  numpy, atlas-devel, suitesparse-devel
Requires:       numpy

%description
A pythonic, object-oriented framework and GUI tool for fitting data to models.

%prep
%setup -q -n %{pyname}
sed -i '/use_setuptools/d' setup.py

%build
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%files
%doc README LICENSE
%{python2_sitelib}/*

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Sat Apr  2 2011 ocefpaf@yahoo.com.br
- updated to release 35
* Sat Mar 19 2011 ocefpaf@yahoo.com.br
- updated to release 33
* Sun Feb 27 2011 ocefpaf@yahoo.com.br
- first OpenSuse release
