%undefine _debugsource_packages
Name: pytyle3
Summary: A manual tiling manager
Version: 3.0.0
Release: 3.1
Group: User Interface/X
License: WTFPL
URL: https://github.com/BurntSushi/pytyle3
Source0: %{name}-master.zip
BuildRequires: xpybutil, python2-devel
BuildArch: noarch

%description
An updated (and much faster) version of pytyle that uses xpybutil and is
compatible with Openbox Multihead.

%prep
%setup -q -n %{name}-master
sed -i '8,14d' setup.py

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%{_bindir}/%{name}
%{_sysconfdir}/xdg/%{name}
%{python2_sitelib}/*
%{_datadir}/doc/%{name}

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.0
- Rebuilt for Fedora
