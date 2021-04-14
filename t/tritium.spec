Name: tritium
Summary: A tabbed/tiling window manager
Version: 0.3.5
Release: 8.1
Group: User Interface/X
License: GPLv2
URL: http://sourceforge.net/projects/tritium/
Source0: http://sourceforge.net/projects/tritium/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Requires: python2-xlib, python-plwm
BuildRequires: python2-devel, python2-xlib, python-plwm
BuildArch: noarch

%description
Tritium is a tiling/tabbed window manager for the X Window System
inspired by the ion3 window manager.  It was written completely from
scratch in Python and shares no actual code with ion3.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
rm %{buildroot}%{_datadir}/applications/%{name}.desktop

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING README TODO
%{_sysconfdir}/X11/%{name}
%{_bindir}/%{name}
%{python2_sitelib}/*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.5
- Rebuilt for Fedora
