%undefine _debugsource_packages
Summary:	Python API of 3D and animated widgets based on pyclutter
Name:		pyclut
Version:	0.2
Release:	5.1
Source0:	http://pyclutter-widgets.googlecode.com/files/%{name}-%{version}.tar.gz
License:	LGPL
Group:		Development/Python
URL:		http://code.google.com/p/pyclutter-widgets/
BuildArch: noarch
BuildRequires: python

%description 
pyclutter-widgets is a pure python module containing easy to use 3D widgets.
Features:
* basics : various shapes
* menus : carrousel, coverflow, thumbnail menu
* controls : buttons, scrollable area, virtual keyboard, clock
* effects : transitions, animations, reflects

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root=$RPM_BUILD_ROOT

%files
%doc README
%{python2_sitelib}/%{name}*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Apr 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
