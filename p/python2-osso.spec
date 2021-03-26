Name:           python2-osso
Version:        0.4
Release:        1
Summary:        Python bindings for libosso library
Source0:        python-osso_%{version}-0maemo5.tar.gz
License:        Python
Group:          Development/Libraries
URL:            http://maemo.org/packages/view/python-osso/

%description
Python2 bindings for libosso library.

%prep
%setup -q -n python-osso-%{version}
sed -i 's|glib/.*\.h|glib.h|' osso/libglib.pxd

%build
export CFLAGS=-Wno-deprecated-declarations
python2 setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
python2 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files 
%{python2_sitearch}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
