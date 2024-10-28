%undefine _debugsource_packages
Name:           python-avc
Version:        0.11.0
Release:        5.1
Summary:        Application View Controller 
URL:            https://avc.inrim.it/html/
License:        GPL
Group:          Development
Source:         https://avc.inrim.it/dist/avc-%{version}.tar.gz
BuildRequires:  python-devel
BuildArch:      noarch

%description
AVC is a multiplatform, fully automatic, live connection among graphical
interface widgets and application variables for the python language.
AVC supports in a uniform way the most popular widget toolkits: GTK+, Qt3,
Qt4, Tk, wxWidgets. The Swing widget toolkit for the java environment is
also supported via the jython compiler. AVC is a python package that can be
imported by any python or jython application.

The display and the control of some application data through a GUI
(Graphical User Interface) is a central problem in GUI programming,
it absorbs a relevant part of the programming effort. AVC makes this
programming very easy, far more easy than traditional solutions based
on MVC (Model View Controller).

%prep
%setup -q -n avc-%{version}

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%files
%doc PKG-INFO README copyright changes COPYING.* doc examples
%{python2_sitelib}/*

%changelog
* Tue Oct 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.0
- Rebuilt for Fedora
