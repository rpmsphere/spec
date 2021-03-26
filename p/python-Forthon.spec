%define rname Forthon 

Name:           python-%{rname}
Version:        0.8.35
Release:        1
Summary:        Python interface generator for Fortran based codes
Group:          Development/Languages
License:        BSD
URL:            http://hifweb.lbl.gov/Forthon/
Source0:        http://hifweb.lbl.gov/Forthon/Forthon-%{version}.tar.gz
Patch1:		buildfixes.patch
BuildRequires:  python3-devel
BuildRequires:  environment-modules
BuildArch:      noarch

%description
Forthon generates links between Fortran95 and Python. Python is a high level,
object oriented, interactive and scripting language that allows a flexible
and versatile interface to computational tools. The Forthon package generates
the necessary wrapping code which allows access to the Fortran database and
to the Fortran subroutines and functions. This provides a development package
where the computationally intensive parts of a code can be written in
efficient Fortran, and the high level controlling code can be written in the
much more versatile Python language.

The developer creates an interface file that describes what part of the
fortran is to be accessible from Python. Variables defined in Fortran
modules can be made accessible, including scalars, arrays, and variables of
derived type. A subset of the Fortran subroutines, as specified in the
interface file, can be called from Python, with argument lists including
scalars, arrays, and variables of derived type. Arrays can be statically
dimensioned or dynamically dimensioned, in which case Fortran95 style
pointers are used. Variables of derived type can be pointers, and derived
types can have elements which are themselves derived types or pointers to
derived types. A tool is included which will automatically compile the
user's source code and the generated wrapping code into a Python module.

%prep
%setup -q -n %{rname}-%{version}
%patch1 -p1 -b .buildfixes

%build
. /etc/profile.d/modules.sh
python3 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
. /etc/profile.d/modules.sh
python3 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}%{python3_sitearch}/* %{buildroot}%{python3_sitelib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.txt
%{_bindir}/*
%{python3_sitelib}/*

%changelog
* Tue Sep 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.35
- Rebuild for Fedora
* Mon Feb 03 2014 Josko Plazonic <plazonic@princeton.edu>
- initial build
