Summary:	A full-featured, pure-Python tiling window manager
Name:		qtile
Version:	0.6
Release:	3.1
Source0:	https://github.com/qtile/qtile/archive/%{name}-%{version}.tar.gz
License:	MIT
Group:		User Interface/Desktops
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
BuildRequires:  python-devel
BuildRequires:	python-setuptools
URL:		http://www.qtile.org/

%description
Qtile is simple, small, and extensible. It's easy to write your own layouts,
widgets, and built-in commands.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc *.rst CHANGELOG LICENSE
%{_bindir}/*
%{python_sitelib}/*

%changelog
* Sun Jul 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
