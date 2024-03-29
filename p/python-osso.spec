Name:           python-osso
Version:        0.4
Release:        1
Summary:        Python bindings for libosso library
Source0:        %{name}_%{version}-0maemo5.tar.gz
License:        Python
Group:          Development/Libraries
URL:            http://maemo.org/packages/view/python-osso/

%description
Python bindings for libosso library.

%prep
%setup -q
sed -i 's|glib/.*\.h|glib.h|' osso/libglib.pxd

%build
%{__python} setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files 
%{python_sitearch}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
