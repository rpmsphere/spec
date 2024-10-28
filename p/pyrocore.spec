%undefine _debugsource_packages
Summary: Python Torrent Tools
Name: pyrocore
Version: 0.4.2
Release: 7.1
Source0: https://pypi.python.org/packages/source/p/pyrocore/%{name}-%{version}.zip
License: GNU GPL v2
Group: Internet
URL: https://code.google.com/p/pyroscope/
BuildArch: noarch
BuildRequires:  python2
BuildRequires: python2-setuptools
Requires: rtorrent

%description
PyroScope is a collection of tools for the BitTorrent protocol and especially
the rTorrent client. It offers the following components:
* CommandLineTools for automation of common tasks, like metafile creation,
  and filtering and mass-changing your loaded torrents
* Patches to improve your rTorrent experience, like new commands and canvas coloring
* rTorrent extensions like a QueueManager and statistics (work in progress)
* A modern and versatile rTorrent web interface (currently on hold)

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install -O1 --root=$RPM_BUILD_ROOT
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc
mv $RPM_BUILD_ROOT/usr/EGG-INFO $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%{_bindir}/*
%{python2_sitelib}/*
%{_datadir}/doc/%{name}-%{version}

%changelog
* Sat Jan 26 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuilt for Fedora
