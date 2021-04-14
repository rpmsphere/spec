%undefine _debugsource_packages
Name: python-orange
Summary: A component-based data mining framework
Version: 2.7.8
Release: 26.1
Group: Development/Libraries
License: GPLv3+
URL: http://orange.biolab.si/
Source0: https://pypi.python.org/packages/source/O/Orange/Orange-%{version}.zip
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: numpy atlas
Provides: liborange.so

%description
Orange is a component-based data mining software. It includes a range of data
visualization, exploration, preprocessing and modeling techniques. It can be
used through a nice and intuitive user interface or, for more advanced users,
as a module for Python programming language.

%prep
%setup -q -n Orange-%{version}
%if %{fedora}>23
sed -i -e '/inline double abs/d' -e '/{ return fabs(x); }/d' source/include/stat.hpp
sed -i '1830s|return false;|return NULL;|' source/orange/measures.cpp
sed -i '11s|return result;|return NULL;|' source/include/c2py.hpp
sed -i '5086s|return false;|return NULL;|' source/orange/lib_kernel.cpp
sed -i '5094s|return false;|return NULL;|' source/orange/lib_kernel.cpp
%endif

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc COPYING LICENSES README.txt
%{_bindir}/orange-canvas
%{python2_sitearch}/*

%changelog
* Mon Feb 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.8
- Rebuilt for Fedora
