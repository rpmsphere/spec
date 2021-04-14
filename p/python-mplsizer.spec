%define __python /usr/bin/python2
%undefine _debugsource_packages
Name:           python-mplsizer
Version:        1.0.dev8477
Release:        5.1
Summary:        Engine for matplotlib based on wxPython model
License:        MIT
URL:            http://sourceforge.net/projects/matplotlib
Group:          Development/Libraries/Python
Source0:        mplsizer-8477.tar.bz2
BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools
Requires:       python-setuptools

%description
mplsizer is a layout engine that re-creates the wxPython idioms for
use within matplotlib. For example, you may create an MplBoxSizer and
add MplSizerElements to it, including with optional parameters such as
"expand" and "border".

mplsizer currently requires the use of setuptools for "namespace
package" support.

%prep
%setup -q -n mplsizer

%build
%{__python} setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%files
%doc LICENSE.txt README.rst demo
%{python2_sitelib}/*

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Sat Feb 19 2011 ocefpaf@yahoo.com.br
- specfile cleanup
* Tue Jun 29 2010 Filipe Fernandes <ocefpaf@gmail.com> - 1.0
- svn 8477
* Fri Jun 25 2010 Filipe Fernandes <ocefpaf@gmail.com> - 1.0
- svn 8450
* Tue May 25 2010 Filipe Fernandes <ocefpaf@gmail.com> - 1.0
- svn 8335
* Wed May 19 2010 Filipe Fernandes <ocefpaf@gmail.com> - 1.0
- svn 8323
* Mon Mar 15 2010 Filipe Fernandes <ocefpaf@gmail.com> - 1.0
- added demo dir with examples
* Fri Mar 12 2010 Filipe Fernandes <ocefpaf@gmail.com> - 1.0
- first release
