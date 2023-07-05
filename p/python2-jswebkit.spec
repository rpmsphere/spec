Name: python2-jswebkit
Summary: WebKit/JavaScriptCore Python bindings
Version: 0.0.3
Release: 8.1
Group: python
URL: https://code.google.com/p/gwrite/
Source0: https://gwrite.googlecode.com/files/python-jswebkit-%{version}.tar.gz
License: LGPL
BuildRequires: python2-devel, Cython
BuildRequires: webkitgtk4-devel

%description
python2-jswebkit is an cython wrapper for JSContextRef in pywebkitgtk,
which makes it able to call JavaScript functions with WebKit/JavaScriptCore.

%prep
%setup -q -n python-jswebkit-%{version}
sed -i 's|webkit-1.0|webkit2gtk-4.0|' setup.py

%build
python2 setup.py build

%install
python2 setup.py install -O1  --prefix /usr --skip-build --root $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog License*
%{python2_sitearch}/*

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.3
- Rebuilt for Fedora
