%undefine _debugsource_packages
Name:           python-unum
Version:        4.1.1
Release:        7.1
Summary:        Unum allows defining and manipulating true quantities
Group:          Development/Libraries/Python
License:        LGPL
URL:            https://home.scarlet.be/be052320/Unum.html
Source0:        kiv-unum-409befe069ac.zip
BuildArch:      noarch
BuildRequires:  python2-devel unzip python2-setuptools python-nose

%description
Unum stands for 'unit-numbers'. It is a pure Python module that allows defining
and manipulating true quantities, i.e. numbers with units like volts, hours, 
meter-per-second. Consistency between units is checked at each expression
evaluation; unit conversion and unit output formatting are performed automatically
when needed. It is stable, lightweight and easy-to-use.

%prep
%setup -q -n kiv-unum-409befe069ac

%build
python2 setup.py build

%install
python2 setup.py install -O1 --skip-build --prefix=%{_prefix} --root $RPM_BUILD_ROOT
rm -rf %{buildroot}%{python2_sitelib}/tests
# fix wrong end of lines
sed -i 's/\r//' docs/*.*
 
%files
%doc docs/*
%{python2_sitelib}/*

%changelog
* Fri Jan 06 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.1
- Rebuilt for Fedora
* Sat Apr 02 2011 scorot@gtt.fr
- Correct package group
* Fri Apr 01 2011 scorot@gtt.fr
- first package
