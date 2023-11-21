%define __python /usr/bin/python3.10

Name:           python-natgrid
Version:        1.0.dev8853
Release:        5.1
Summary:        Python interface to NCAR natgrid library
License:        NCL Source Code License
URL:            https://sourceforge.net/projects/matplotlib
Group:          Development/Libraries/Python
Source0:        natgrid-8853.tar.bz2
BuildRequires:  python3.10-devel

%description
Python interface to NCAR natgrid library
(https://www.ncarg.ucar.edu//ngmath/natgrid/nnhome.html).
When installed, will be used by the matplotlib.mlab griddata function.

%prep
%setup -q -n natgrid

%build
python3.10 setup.py build

%install
python3.10 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%files
%doc Copyright.txt README
%{_libdir}/python3.*/site-packages/*

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Wed Dec 29 2010 ocefpaf@yahoo.com.br
- updated to svn revision 8853
* Wed Oct  6 2010 ocefpaf@yahoo.com.br
- updated to 8731
* Tue Jun 29 2010 Filipe Fernandes <ocefpaf@gmail.com> - 1.0
- svn 8477
* Mon Jun 21 2010 Filipe Fernandes <ocefpaf@gmail.com> - 1.0
- svn 8450
* Tue May 25 2010 Filipe Fernandes <ocefpaf@gmail.com> - 1.0
- svn 8335
* Wed May 19 2010 Filipe Fernandes <ocefpaf@gmail.com> - 1.0
- svn 8323
* Fri Mar 12 2010 Filipe Fernandes <ocefpaf@gmail.com> - 1.0
- first release
