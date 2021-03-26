%global debug_package %{nil}
Name:       python-yapps
Version:    2.1.1
Release:    9.1
Summary:    Yet Another Python Parser System
Group:      Development/Languages/Python
License:    Public Domain
URL:        http://theory.stanford.edu/~amitp/yapps/
Source:     http://theory.stanford.edu/~amitp/yapps/yapps%{version}.tar.gz
BuildRequires: python2-devel
BuildArch:      noarch

%description
Yapps (Yet Another Python Parser System) is an easy to use parser generator
that is written in Python and generates Python code. Although there are several
parser generators already available for Python, I had different goals,
including learning about recursive descent parsers. Yapps is simple, is easy to
use, and produces human-readable parsers. It is not fast, powerful, or
particularly flexible. Yapps is designed to be used when regular expressions
are not enough and other parser systems are too much: situations where you may
write your own recursive descent parser.

%prep
%setup -q -n Yapps-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT --prefix=/usr
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
mv $RPM_BUILD_ROOT%{_bindir}/yapps2 $RPM_BUILD_ROOT%{_bindir}/yapps

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc NOTES PKG-INFO README ChangeLog examples
%{_bindir}/yapps
%{python2_sitelib}/*

%changelog
* Sun Nov 04 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.1
- Rebuild for Fedora
* Mon Mar 29 2010 puzel@novell.com
- use proper RPM group
- build as noarch for opensuse >= 11.2
