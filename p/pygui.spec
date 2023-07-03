%undefine _debugsource_packages
%define module_name PyGUI

Name: pygui
Version: 2.5.3
Release: 4.1
Summary: A project to develop a cross-platform pythonic GUI API
License: GPL
URL: https://www.cosc.canterbury.ac.nz/greg.ewing/python2_gui/
Group: Development/Language
Source0: https://www.cosc.canterbury.ac.nz/greg.ewing/python2_gui/%{module_name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: pygtk2, python-setuptools
BuildRequires: python

%description
The goals of this project are:
*Develop a GUI API that is designed specifically for Python,
 taking advantage of Python's unique language features and
 working smoothly with Python's data types.
*Provide implementations of the API for the three major platforms
 (Unix, Macintosh and Windows) that are small and lightweight,
 interposing as little code as possible between the Python
 application and the platform's underlying GUI facilities, and not
 bloating the Python installations or applications which use them.
*Document the API purely in Python terms, so that the programmer
 does not need to read the documentation for another GUI library,
 in terms of another language, and translate into Python.
*Get the library and its documentation included in the core Python
 distribution, so that truly cross-platform GUI applications may be
 written that will run on any Python installation, anywhere.

%prep
%setup -q -n %{module_name}-%{version}

%build
python2 setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}
python2 setup.py install --root=$RPM_BUILD_ROOT --optimize=2

%files
%doc *.txt Doc Demos Tests
%{python2_sitelib}/GUI
%{python2_sitelib}/PyGUI*

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Fri Mar 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.3
- Rebuilt for Fedora
