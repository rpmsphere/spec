Name: fbmessenger
Version: 0.2.0
Release: 9.1
Summary: Facebook messenger client
License: BSD
URL: http://github.com/oconnor663/linuxmessenger
Source0: %{name}-master.zip
BuildRequires: python3-devel, python3-setuptools, unzip
Requires: python3, python3-qt4, phonon, python3-sip
BuildArch: noarch

%description
A Linux clone of Facebook Messenger for Windows made with PyQt.

%prep
%setup -n %{name}-master

%build
python3 setup.py build

%install
python3 setup.py install --root="$RPM_BUILD_ROOT"
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

%files
%{_bindir}/%{name}
%{python3_sitelib}/%{name}*
%{_datadir}/applications//%{name}.desktop
%{_datadir}/pixmaps//%{name}.png
%doc README.md LICENSE

%changelog
* Mon Sep 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuild for Fedora
* Thu Sep 05 2013 jacko <oconnor663@gmail.com> - 0.2.0-1
- Directory move and path changes
* Wed Apr 17 2013 shuff <shuff@fb.com> - 0.1.0-1
- RPM spec Creation!
