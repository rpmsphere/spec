Name: python-jswebkit
Summary: WebKit/JavaScriptCore Python bindings
Version: 0.0.3
Release: 8.1
Group: python
URL: http://code.google.com/p/gwrite/
Source0: http://gwrite.googlecode.com/files/%{name}-%{version}.tar.gz
License: LGPL
BuildRequires: python-devel, Cython
%if %{fedora}>26
BuildRequires:  webkitgtk4-devel
%else
BuildRequires:  webkitgtk-devel
%endif

%description
python-jswebkit is an cython wrapper for JSContextRef in pywebkitgtk,
which makes it able to call JavaScript functions with WebKit/JavaScriptCore.

%prep
%setup -q
%if %{fedora}>26
sed -i 's|webkit-1.0|webkit2gtk-4.0|' setup.py
%endif

%build
python setup.py build

%install
python setup.py install -O1  --prefix /usr --skip-build --root $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog License*
%{python_sitearch}/*

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.3
- Rebuild for Fedora
