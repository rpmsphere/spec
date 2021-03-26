%define pyname datarray

Name:           python2-%{pyname}
Version:        0.0.7.dev151
Release:        5.1
Summary:        Numpy arrays with named axes
License:        BSD
Group:          Development/Libraries/Python
URL:            http://github.com/fperez/datarray
Source0:        %{pyname}-151.tar.bz2
BuildArch:      noarch
BuildRequires:  python2
Requires:       numpy

%description
Datarray provides a subclass of Numpy ndarrays that support:
- individual dimensions (axes) being labeled with meaningful descriptions
- labeled 'ticks' along each axis
- indexing and slicing by named axis
- indexing on any axis with the tick labels instead of only integers
- reduction operations (like .sum, .mean, etc) support named axis arguments
  instead of only integer indices.

%prep
%setup -q -n %{pyname}

%build
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc datarray/LICENSE README.txt
%{python2_sitelib}/*

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.7
- Rebuild for Fedora
* Wed Jun 15 2011 ocefpaf@yahoo.com.br
- updated to release 151
* Thu Jun  2 2011 ocefpaf@yahoo.com.br
- updated to release 129
* Sat Apr  9 2011 ocefpaf@yahoo.com.br
- updated to release 109
* Sat Mar 19 2011 ocefpaf@yahoo.com.br
- first openSUSE release
