Name: vpython-wx
Summary: Experimental version of VPython based on wxPython
Version: 6.11
Release: 7.1
Group: Development/Libraries
License: GPC
URL: http://sourceforge.net/projects/vpythonwx/
Source0: http://sourceforge.net/projects/vpythonwx/files/%{version}-release/%{name}-src.%{version}.tgz
BuildRequires: numpy
BuildRequires: python2-wxpython
BuildRequires: gtkglextmm-devel
BuildRequires: boost-devel
BuildRequires: python2-devel
BuildRequires: boost-python2-devel
BuildRequires: atlas
Provides: python-visual, vpython
Obsoletes: python-visual
Requires: numpy
Requires: python2-wxpython
Requires: python-Polygon
Requires: python-ttfquery

%description
It differs from the older VPython (5.74 and before) by eliminating nearly
all platform-dependent code and by eliminating the threading associated
with rendering. The new version makes one essential change to the syntax of
VPython programs. Now, an animation loop MUST contain a rate statement,
which limits the number of loop iterations per second as before but also
when appropriate (about 30 times per second) updates the 3D scene and handles
mouse and keyboard events. Without a rate statement, the scene will not be
updated until and unless the loop is completed.

%prep
%setup -q -c
#sed -i -e '2,9d' -e "s|'boost_python-mt-py' + versionString|'boost_python'|" setup.py
sed -i "s|'boost_python-py' + versionString|'boost_python'|" setup.py
sed -i 's|boost/python/numeric.hpp|boost/python/numpy.hpp|' include/util/vector.hpp
sed -i -e 's|boost/signals.hpp|boost/signals2.hpp|' -e 's|boost::signal|boost::signals2::signal|' include/util/gl_free.hpp
sed -i -e 's|boost::python::numeric|boost::python::numpy|' -e 's|array |ndarray |' include/label.hpp src/core/label.cpp

%build
#python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --prefix=%{_prefix}

%files
%doc README.md *.txt
%{python_sitearch}/*

%changelog
* Thu Dec 31 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 6.11
- Rebuild for Fedora
