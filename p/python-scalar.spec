%undefine _debugsource_packages
%define modname scalar

Name:           python-%{modname}
Version:        2.2
Release:        6.1
Summary:        A python module for manipulating scalar with physical units
URL:            https://russp.us/scalar.htm
License:        BSD
Group:          Development/Libraries/Python
Source:         %{modname}-%{version}.tar.gz
BuildRequires:  python-devel
BuildArchitectures: noarch

%description
Scalar is designed to represent physical scalars and to eliminate errors
involving implicit physical units (e.g., confusing angular degrees and
radians). The standard arithmetic operators are overloaded to provide
syntax identical to that for built-in numeric types. The scalar class
does not define any units itself but is part of a package that includes
a complete implementation of the standard metric system of units and many
standard non-metric units. It also allows the user to define a specialized
or reduced set of appropriate physical units for any particular application
or domain. Once an application has been developed and tested, the scalar
class can easily be switched off, if desired, to achieve the execution
efficiency of operations on built-in numeric types, which can be nearly
two orders of magnitude faster. The scalar class can also be used for
discrete units to enforce type checking of integer counts, thereby enhancing
the built-in dynamic type checking of Python.

%prep
%setup -q -n %{modname}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc license
%{python2_sitelib}/*

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuilt for Fedora
* Sat Mar 19 2011 scorot@gtt.fr - 2.2
- Initial release
