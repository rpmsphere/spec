%undefine _debugsource_packages
Name:           everpad
Version:        2.5.6
Release:        6.1
Summary:        Evernote client for linux desktop
License:        custom
URL:            https://launchpad.net/~nvbn-rm/+archive/everpad-usc
Source0:        https://launchpad.net/~nvbn-rm/+archive/ppa/+files/%{name}_%{version}.orig.tar.xz
Requires: python-pyside
Requires: python-magic
Requires: python-oauth2
Requires: python-sqlalchemy
Requires: python-BeautifulSoup
Requires: qtwebkit
Requires: python-html2text
Requires: shiboken
Requires: dbus-python
Requires: python-keyring
Requires: python-httplib2
Requires: python-regex
BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
BuildArch: noarch

%description
Evernote client well integrated with linux desktop.

%prep
%setup -q -n everpad

%install
python2 setup.py install --root=%{buildroot}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
%find_lang %{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files -f %{name}.lang
%{_bindir}/%{name}*
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/*%{name}*.service
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/*/%{name}*.png
%{_datadir}/kde4
%{_datadir}/pixmaps/%{name}*png
%{_datadir}/unity/lenses/%{name}/%{name}.lens

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.6
- Rebuilt for Fedora
* Mon Jun 10 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 2.5.6-1
- Initial package
