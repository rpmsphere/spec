%define pyname pymodelfit

Name:           python-%{pyname}
Version:        0.2.dev35
Release:        10.1
Summary:        Framework and GUI tool for fitting data
License:        Apache v2.0
URL:            http://code.google.com/p/pymc/downloads/list
Group:          Development/Libraries/Python
Source0:        %{pyname}-35.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  numpy, scipy, atlas-devel, suitesparse-devel
Requires:       numpy, scipy

%description
A pythonic, object-oriented framework and GUI tool for fitting data to models.

%prep
%setup -q -n %{pyname}
sed -i '/use_setuptools/d' setup.py

%build
%{__python} setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README LICENSE
%{python_sitelib}/*

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
* Sat Apr  2 2011 ocefpaf@yahoo.com.br
- updated to release 35
* Sat Mar 19 2011 ocefpaf@yahoo.com.br
- updated to release 33
* Sun Feb 27 2011 ocefpaf@yahoo.com.br
- first OpenSuse release
