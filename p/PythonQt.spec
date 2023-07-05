%define sover   3
%define mypyver 3
%undefine _debugsource_packages

Name:           PythonQt
Version:        3.2
Release:        3
Summary:        Dynamic Python binding for the Qt framework
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://pythonqt.sourceforge.net
Source0:        https://downloads.sourceforge.net/pythonqt/%{name}%{version}.zip
# PATCH-FIX-OPENSUSE PythonQt-add-install-target.patch
Patch0:         %{name}-add-install-target.patch
# PATCH-FIX-UPSTREAM PythonQt-create-pkg-config.patch
Patch1:         PythonQt-create-pkg-config.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Fix-build-with-python-3.8.patch
BuildRequires:  gcc-c++
BuildRequires:  dos2unix
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(python3)

%description
PythonQt offers embedding of the Python scripting language into a
C++ Qt applications. It makes heavy use of the QMetaObject system and
requires Qt 5.x.
It is focused on embedding, not writing entire applications in Python -
that should use PyQt or PySide instead.

%package        devel
Summary:        Header files and development libraries for the pythonqt package
Group:          Development/Libraries/C and C++
#Requires:       lib%{name}-Qt5-Python%{mypyver}-%{sover} = %{version}
#Requires:       lib%{name}_QtAll-Qt5-Python%{mypyver}-%{sover} = %{version}
Requires:       pkgconfig(Qt5Concurrent)
Requires:       pkgconfig(Qt5Multimedia)
Requires:       pkgconfig(Qt5Svg)
Requires:       pkgconfig(Qt5WebKit)
Requires:       pkgconfig(Qt5WebKitWidgets)
Requires:       pkgconfig(Qt5XmlPatterns)
Requires:       pkgconfig(python3)

%description    devel
Header files and development libraries for the PythonQt package.

PythonQt offers embedding of the Python scripting language into a
C++ Qt applications. It makes heavy use of the QMetaObject system and
requires Qt 5.x.
It is focused on embedding, not writing entire applications in Python -
that should use PyQt or PySide instead.

%prep
%setup -q -n %{name}%{version}
find . -type f -exec dos2unix {} \;
%autopatch -p1
sed -r -i -e "s/(unix:PYTHON_VERSION=).*/\1%{mypyver}/g" build/python.prf
sed -i 's|pydebug.h|cpython/pydebug.h|' src/PythonQt.cpp

%build
qmake-qt5 \
  "LIB_INSTALL=%{buildroot}%{_libdir}" \
  "HEADER_INSTALL=%{buildroot}%{_includedir}/PythonQt"
%make_build

%install
%make_install

%files
%doc README
%license COPYING
%{_libdir}/lib%{name}-Qt5-Python%{mypyver}.so.%{sover}*
%{_libdir}/lib%{name}_QtAll-Qt5-Python%{mypyver}.so.%{sover}*

%files devel
%{_includedir}/PythonQt
%{_libdir}/lib%{name}-Qt5-Python%{mypyver}.so
%{_libdir}/lib%{name}_QtAll-Qt5-Python%{mypyver}.so
%{_libdir}/pkgconfig/%{name}-Qt5-Python%{mypyver}.pc
%{_libdir}/pkgconfig/%{name}_QtAll-Qt5-Python%{mypyver}.pc

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2
- Rebuilt for Fedora
* Thu Apr  9 2020 Christophe Giboudeaux <christophe@krop.fr>
- Spec cleanup. Use dos2unix
- Update patches:
  * PythonQt-add-install-target.patch
  * PythonQt-create-pkg-config.patch
- Add patch to fix build with python 3.8:
  * 0001-Fix-build-with-python-3.8.patch
* Mon Mar 12 2018 jengelh@inai.de
- Trim filler wording of descriptions.
* Fri Mar  2 2018 aloisio@gmx.com
- Initial package (version 3.2)
