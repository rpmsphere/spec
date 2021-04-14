%define modname pyamg

Name:           python-%{modname}
Version:        4.0.0
Release:        1
Summary:        A python module and library of AMG solvers
URL:            http://code.google.com/p/pyamg/
License:        See LICENSE.txt
Group:          Development/Libraries/Python
Source:         http://pyamg.googlecode.com/files/%{modname}-%{version}.tar.gz
Requires:       python3-scipy numpy
BuildRequires:  python3-devel
BuildRequires:	gcc-c++ numpy python3-scipy atlas-devel suitesparse-devel
BuildRequires:  python-sphinx environment-modules
BuildRequires:  python-pygments python3-setuptools

%description
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a convenient
Python interface.

%prep
%setup -q -n %{modname}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS -fpermissive -Wno-format-security"
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc INSTALL.txt LICENSE.txt
%{python3_sitearch}/%{modname}*

%changelog
* Wed Jul 31 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.0
- Rebuilt for Fedora
* Sun Oct 10 2011 scorot@gtt.fr - 2.0.0
- fix python-Sphinx requirement
* Fri Mar 18 2011 scorot@gtt.fr - 2.0.0
- version 2.0.0
- build documentation
* Fri Jan 21 2011 scorot@gtt.fr - 1.0.0
- Initial release
