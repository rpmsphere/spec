Name:           python3-vispy
Version:        0.6.1
Release:        1
Summary:        Interactive visualization in Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/vispy/vispy
Source:         https://files.pythonhosted.org/packages/source/v/vispy/vispy-%{version}.tar.gz

%description
Vispy is an interactive 2D/3D data visualization library. It leverages Graphics
Processing Units through the OpenGL library to display large datasets.

%package     -n jupyter-vispy
Summary:        Interactive visualization in the Jupyter notebook
Requires:       jupyter-notebook
Requires:       python3-vispy = %{version}

%description -n jupyter-vispy
Vispy is an interactive 2D/3D data visualization library. It leverages Graphics
Processing Units through the OpenGL library to display large datasets.

This package provides the jupyter notebook extension.

%prep
%setup -q -n vispy-%{version}
sed -i -e '/^#!\//, 1d' vispy/glsl/build-spatial-filters.py vispy/util/transforms.py vispy/visuals/collections/util.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
python3 setup.py build

%install
python3 setup.py install --prefix=/usr --root=%{buildroot}

%files
%doc README.rst
%license LICENSE.txt
%{python3_sitearch}/*

%files -n jupyter-vispy
%license LICENSE.txt
%config /usr/etc/jupyter/nbconfig/notebook.d/vispy.json
%{_datadir}/jupyter/nbextensions/vispy

%changelog
* Mon Oct 21 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuild for Fedora
* Fri Aug  2 2019 Todd R <toddrme2178@gmail.com>
- Update to 0.16.1
  * Fix discrete colormap ordering (#1668)
  * Fix various examples (#1671, #1676)
  * Fix Jupyter extension zoom direction (#1679)
* Tue Jul 23 2019 Todd R <toddrme2178@gmail.com>
- Update to 0.16.0
  * Update PyQt5/PySide2 to use newer GL API
  * Update to PyQt5 as default backend
  * New Cython-based text rendering option
  * New WindbarbVisual
  * Improved JupyterLab/Notebook widget (experimental)
  * Fix various memory leaks
  * Various optimizations and bug fixes
- Add jupyter subpackage
* Wed Apr 17 2019 Todd R <toddrme2178@gmail.com>
- Switch to the qt5 backend.
* Thu Nov  1 2018 Todd R <toddrme2178@gmail.com>
- Update to version 0.15.3
  * Workaround matplotlib 2.2 dropping _cntr private module
  * Try appveyor SSL settings for fixing https download
  * Fix buffer due to unsupported numpy feature
* Sat Mar  3 2018 jengelh@inai.de
- Compact description.
* Thu Jan 18 2018 toddrme2178@gmail.com
- Update to version 0.15.2
  * Fix PyPI packaging to include LICENSE.txt
  * Fix initial axis limits in PlotWidget (#1386)
  * Fix zoom event position in Pyglet backend (#1388)
  * Fix camera importing (#1389, #1172)
  * Refactor `EllipseVisual` and `RectangleVisual` (#1387, #1349)
  * Fix `one_scene_four_cams.py` example (#1391, #1124)
  * Add `two_qt_widgets.py` example (#1392, #1298)
  * Fix order of alignment values for proper processing (#1395, #641)
* Fri Oct 20 2017 toddrme2178@gmail.com
- initial version
