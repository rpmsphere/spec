%undefine _debugsource_packages
Name: pyds9
Summary: A Python Connection to DS9 via XPA
Version: 1.7
Release: 3.1
Group: Development/Languages/Python
License: GPL
URL: https://hea-www.harvard.edu/saord/ds9/pyds9/
Source0: https://hea-www.harvard.edu/saord/download/ds9/python/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python-devel
Requires: ds9, xpa

%description
The XPA messaging system provides seamless communication between many kinds
of Unix programs, including Tcl/Tk programs such as ds9. The pyds9 module
uses a Python interface to XPA to communicate with ds9. It supports
communication with all of ds9’s XPA access points.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{python2_sitelib}
install -m644 ds9.py xpa.py $RPM_BUILD_ROOT%{python2_sitelib}

%files
%doc COPYING PKG-INFO README changelog
%{python2_sitelib}/*

%changelog
* Wed Jun 04 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
