%global debug_package %{nil}
%define modname pysundials

Name:           python2-%{modname}
Version:        2.5.0a1
Release:        9.1
Summary:        A python module providing bindings for the SUNDIALS suite of solvers
URL:            http://pysundials.sourceforge.net/
License:        BSD
Group:          Development/Libraries/Python
Source:         %{modname}-2.5.0-a1.tar.gz
#Requires:       python2-scipy
Requires:       numpy
BuildRequires:  python2-devel
BuildRequires:	gcc-gfortran numpy sundials-devel
BuildRequires:	atlas-devel suitesparse-devel

%description
PySUNDIALS is a python package providing python bindings for the SUNDIALS
suite of solvers. While python bindings for SUNDIALS will hopefully be
generally useful in the computational scientific community, they are being
developed with the specific aim of providing a robust underlying numerical
solver capable of implementing models conforming to the Systems Biology
Markup Language specification (version 2), including triggers, events,
and delays.

%prep
%setup -q -n %{modname}-2.5.0-a1
sed -i 's|smalldense\.h|dense.h|' src/realtype.c

%build
export CFLAGS="$RPM_OPT_FLAGS"
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc doc/*
%{python2_sitelib}/*

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.0a1
- Rebuild for Fedora
* Fri Jan 21 2011 scorot@gtt.fr - 1.0.0
- Initial release
