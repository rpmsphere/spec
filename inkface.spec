Name: inkface
Version: 0.2.5
Release: 4.1
Summary: SVG based GUI framework library
Group: Development/Libraries
License: GPL v3
URL: http://code.google.com/p/altcanvas/
Source0: http://altcanvas.googlecode.com/files/%{name}_%{version}_1.tar.gz
Source1: inkface-setup.py
BuildArch: noarch
BuildRequires: python2

%description
Inkface is an SVG based GUI framework with Python bindings.

%prep
%setup -q -n %{name}2
cp -f %{SOURCE1} setup.py
sed -i 's/canvas\.canvas/canvas/' inkface/clutter/__init__.py

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc apps docs tests utils
%{python2_sitelib}/%{name}*

%changelog
* Mon Mar 07 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.5-1
- Rebuild for Fedora
