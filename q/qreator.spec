Name: qreator
Summary: Create your own QR codes
Version: 16.06.2
Release: 1
Group: Applications/Multimedia
License: GPLv3
URL: http://davidplanella.org/project-showcase/qreator/
Source0: https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python2-devel, intltool
Requires: python2-qrencode

%description
Qreator is an Ubuntu app to easily create your own QR codes.
Encode different types of information in an efficient, compact and cool way.

%prep
%setup -q

%build
python2 setup.py build

%install
install -Dm644 build/share/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

%files
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{python2_sitelib}/*
%{_datadir}/glib-2.0/schemas/net.launchpad.%{name}.gschema.xml

%changelog
* Thu Sep 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 16.06.2
- Rebuilt for Fedora
