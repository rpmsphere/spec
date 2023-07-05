%define __python /usr/bin/python3
%define modname enable

Name:           python-%{modname}
Version:        4.6.1
Release:        5.1
Summary:        Low-level drawing and interaction for Python
Group:          Development/Libraries/Python
# Source code is under BSD but images are under different licenses
# and details are inside image_LICENSE.txt
License:        BSD-3-Clause and EPL-1.0 and GPL-1.0 and LGPL-2.1 and LGPL-3.0 and Public Domain
URL:            https://code.enthought.com/projects/enable
Source:         https://www.enthought.com/repo/ets/%{modname}-%{version}.tar.gz
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  Cython
BuildRequires:  python3-setuptools
BuildRequires:  numpy atlas
BuildRequires:  python3-reportlab
BuildRequires:  swig
BuildRequires:  libX11-devel
Requires:       python3-kiva = %{version}

%description
The Enable package is a multi-platform object drawing library built on top of
Kiva. The core of Enable is a container/component model for drawing and event
notification. The core concepts of Enable are:

- Component
- Container
- Events (mouse, drag, and key events)

Enable provides a high-level interface for creating GUI objects, while
enabling a high level of control over user interaction. Enable is a supporting
technology for the Chaco and BlockCanvas projects.

Part of the Enthought Tool Suite (ETS).

%package -n python-kiva
Summary:        DisplayPDF vector drawing engine for Python
Group:          Development/Libraries/Python
Requires:       Cython
Requires:       python-distribute
Requires:       numpy
Requires:       python-reportlab

%description -n python-kiva
Kiva is a multi-platform DisplayPDF vector drawing engine that supports
multiple output backends, including Windows, GTK, and Macintosh native
windowing systems, a variety of raster image formats, PDF, and Postscript.

DisplayPDF is more of a convention than an actual specification. It is a
path-based drawing API based on a subset of the Adobe PDF specification.
Besides basic vector drawing concepts such as paths, rects, line sytles, and
the graphics state stack, it also supports pattern fills, antialiasing, and
transparency. Perhaps the most popular implementation of DisplayPDF is
Apple's Quartz 2-D graphics API in Mac OS X.

Part of the Enthought Tool Suite (ETS).

%prep
%setup -q -n %{modname}-%{version}

%build
python3 setup.py build

%install
rm kiva/_version.py
python3 setup.py install --skip-build --prefix=%{_prefix} --root=%{buildroot}
chmod +x %{buildroot}%{python3_sitearch}/kiva/setup.py
chmod +x %{buildroot}%{python3_sitearch}/kiva/{agg,quartz}/setup.py
chmod +x %{buildroot}%{python3_sitearch}/%{modname}/savage/compliance/{comparator,xml_view,sike}.py
rm examples/kiva/.gitignore

sed -i 's|/usr/bin/env python$|/usr/bin/python3|' %{buildroot}%{python3_sitearch}/*/*.py %{buildroot}%{python3_sitearch}/*/*/*.py %{buildroot}%{python3_sitearch}/*/*/*/*.py

%files -n python-kiva
%doc LICENSE.txt  README.rst TODO.txt image_LICENSE.txt image_LICENSE_CP.txt image_LICENSE_Eclipse.txt image_LICENSE_Nuvola.txt image_LICENSE_OOo.txt
%doc examples/
%{python3_sitearch}/kiva/

%files
%{python3_sitearch}/%{modname}*

%changelog
* Thu Feb 16 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 4.6.1
- Rebuilt for Fedora
* Sat Apr 20 2013 toddrme2178@gmail.com
- Added a note about being part of the Enthought Tool Suite (ETS).
* Thu Apr 18 2013 toddrme2178@gmail.com
- Update to 4.3.0
  * no changelog
* Sat Dec  1 2012 toddrme2178@gmail.com
- Fix glu requires for recent openSUSE versions
* Tue May 22 2012 toddrme2178@gmail.com
- Initial spec file
