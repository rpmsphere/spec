%undefine _debugsource_packages
Summary:	A diagramming widget for GTK+ written in Python
Name:		gaphas
Version:	0.4.0
Release:	6.1
License:	LGPL
Group:		Development/Python
Source0:	http://pypi.python.org/packages/source/g/%{name}/%{name}-%{version}.tar.bz2
Source1:         setup.py
URL:		http://gaphor.devjavu.com/projects/gaphor/wiki/Subprojects/Gaphas
BuildRequires:	python-setuptools, python-nose
BuildRequires:	python
BuildArch:	noarch
Requires:   python-decorator 
Requires:	pycairo 
Requires:	pygtk2

%description
Gaphas is a MVC canvas that uses Cairo_ for rendering. One of the nicer things
of this widget is that the user (model) is not bothered with bounding box
calculations: this is all done through Cairo.

%prep
%setup -q
cp %SOURCE1 .

%build
python2 setup.py build
python2 setup.py build_doc

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.txt 
%{python2_sitelib}/gaphas
%{python2_sitelib}/gaphas*egg*

%changelog
* Sun Sep 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
* Mon Jun 01 2009 slick50 <lxgator@gmail.com> 0.4.0-1pclos2009
- initial build
