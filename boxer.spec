%global debug_package %{nil}
Name: boxer
Summary: Box graphical user interface
Version: 0.4.0
Release: 3.1
Group: Development/Tools
License: LGPLv2
URL: http://boxc.sourceforge.net/
Source0: http://sourceforge.net/projects/boxc/files/Boxer%20-%20the%20Box%20GUI/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python2
BuildArch: noarch

%description
A graphical user interface, Boxer, which allows you to edit the Box program
and - at the same time - see the figure, zoom in and out, interact with it,
browse the documentation interactively.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/%{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*


%files
%doc ChangeLog COPYING README
%{_bindir}/%{name}
%{python2_sitelib}/*

%changelog
* Fri Dec 11 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuild for Fedora
