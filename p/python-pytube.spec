%undefine _debugsource_packages
Name:       python-pytube
Version:    0.2.0
Release:    6.1
Summary:    A simple, yet versatile Python package for downloading YouTube videos
Group:      Development/Languages/Python
License:    BSD
URL:        https://github.com/NFicano/pytube
Source:     pytube-%{version}.tar.gz
BuildRequires: python2-devel
BuildArch:      noarch

%description
Downloading videos from YouTube shouldn't require some bloatware application,
it's usually a niche condition you want to do so in the first place.
So I Prsent to you, PyTube!

%prep
%setup -q -n pytube-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT --prefix=/usr
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc README.rst LICENSE.txt CHANGES.rst
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Wed May 06 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
