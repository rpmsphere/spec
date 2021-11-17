%define pyname Mathics

Name:           mathics
Version:        4.0.0
Release:        1
Summary:        A general-purpose computer algebra system
# Mathics itself is licensed as GPL-3.0 but it includes third-party software with MIT, BSD-3-Clause, and Apache-2.0 Licensing; also includes data from wikipedia licensed under CC-BY-SA-3.0 and GFDL-1.3
License:        GPL-3.0 and BSD-3-Clause and MIT and Apache-2.0
Group:          Development/Languages/Python
URL:            https://mathics.github.io/
Source:         https://github.com/mathics/Mathics/archive/v%{version}.tar.gz#/%{pyname}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-colorama
BuildRequires:  python3-devel
BuildRequires:  python3-django
BuildRequires:  python3-mpmath
BuildRequires:  python3-pexpect
BuildRequires:  python3-dateutil
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-sympy
BuildRequires:  python3-Cython

%description
Mathics is a general-purpose computer algebra system (CAS).
It is meant to be a free, lightweight alternative to Mathematica.

%prep
%setup -q -n %{pyname}-%{version}

# FIX SPURIOUS EXEC PERMISSIONS
#find ./mathics/web/media/js -name "*.js" -exec chmod -x '{}' \;
#find ./mathics/web/media/js -name "*.svg" -exec chmod -x '{}' \;
chmod -x ./mathics/data/ExampleData/{numberdata.csv,InventionNo1.xml}

# WRONG END-OF-FILE ENCODING
sed -i "s/\r$//" ./mathics/data/ExampleData/numberdata.csv

# REMOVE SHEBANGS FROM FILES INSTALLED TO NON-EXEC LOCATIONS
pushd mathics
for d in `find ./ -prune -type d`
do
  find ${d} -name "*.py" -exec sed -i "1,4{/\/usr\/bin\/env/d}" '{}' \;
done
popd

%build
%py3_build

%install
%py3_install

%files
%doc *.rst *.txt
%{python3_sitearch}/mathics
%{python3_sitearch}/%{pyname}*
%{_bindir}/*

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.0
- Rebuilt for Fedora
* Tue Dec 19 2017 badshah400@gmail.com
- Correct License: Includes software licensed as BSD-3-Clause,
  MIT, and Apache-2.0, and data licensed under CC-by-SA-3.0 and/or
  GFDL.
- Use python_expand to run fdupes for both python 2 and 3.
* Mon Dec 18 2017 badshah400@gmail.com
- Initial package.
