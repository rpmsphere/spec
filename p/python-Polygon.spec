%undefine _debugsource_packages
Name:           python-Polygon
Version:        2.0.8
Release:        6.1
Summary:        Python package that handles polygonal shapes in 2D
License:        LGPL with exception
Group:          Development/Python
URL:            https://www.j-raedler.de/projects/polygon/
Source0:        https://pypi.python.org/packages/source/P/Polygon2/Polygon2-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python2-setuptools

%description
Polygon is a python package that handles polygonal shapes in 2D. It
contains Python bindings for gpc, the excellent General Polygon Clipping
Library by Alan Murta and some extensions written in C and pure Python.
With Polygon you may handle complex polygonal shapes in Python in a very
intuitive way. Polygons are simple Python objects, clipping operations
are bound to standard operators like +, -, |, & and ^. TriStrips can be
constructed from Polygons with a single statement. Functions to compute
the area, center point, convex hull, point containment and much more are
included. This package was already used to process shapes with more than
one million points!

gpc is included in Polygon and is distributed under other license.
gpc homepage: https://www.cs.man.ac.uk/~toby/alan/software/

GPC is free for non-commercial use only. We invite non-commercial users
to make a voluntary donation towards the upkeep of GPC. If you wish to
use GPC in support of a commercial product, you must obtain an official
GPC Commercial Use Licence from The University of Manchester.

%prep
%setup -q -n Polygon2-%version

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%doc doc/* HISTORY
%dir %python2_sitearch/Polygon 
%python2_sitearch/Polygon
%python2_sitearch/Polygon*.egg-info

%changelog
* Tue Feb 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.8
- Rebuilt for Fedora
* Thu Feb 20 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.6-alt1
- Initial build in Sisyphus
