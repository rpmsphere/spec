Name: salutatoi
Summary: An XMPP (Jabber) client
Version: 0.3.0
Release: 12.1
Group: Applications/Internet
License: AGPL
URL: http://sat.goffi.org/
Source0: ftp://ftp.goffi.org/sat/sat-%{version}.tar.bz2
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: pygobject2
BuildRequires: python2-wxpython
BuildArch: noarch

%description
SàT is made on a daemon/frontend architecture.
Its aim is not only to be an instant messagery client: XMPP offer a lot more,
and differents tools will come in the future.

%prep
%setup -q -n sat-%{version}
sed -i '/use_setuptools/d' setup.py

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
rm %{buildroot}%{_bindir}/sat
sed -i 's|%{buildroot}||' %{buildroot}%{python2_sitelib}/sat/sat.sh
ln -s ../..%{python2_sitelib}/sat/sat.sh %{buildroot}%{_bindir}/%{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%{_datadir}/doc/sat
%{_bindir}/*
%{python2_sitelib}/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo

%changelog
* Wed Dec 11 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuilt for Fedora
