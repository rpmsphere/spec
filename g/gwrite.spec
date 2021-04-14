Name: gwrite
Summary: Simple GTK+ HTML5 rich text editor
Version: 0.5.1
Release: 17.1
Group: editors
URL: http://code.google.com/p/gwrite
Source0: http://gwrite.googlecode.com/files/%{name}-%{version}.tar.gz
License: LGPL
BuildArch: noarch
BuildRequires: python2-distutils-extra, intltool, python2-devel
Requires: python2-jswebkit
Requires: pywebkitgtk

%description
gWrite is a simple GTK+ HTML5 WYSIWYG editor, focusing on writing
and simple text formating. It can automatically generate a table of
contents based on the document structure. It aims to be lighter
than OOWrite & OOWeb, and to be as useful as them.

%prep
%setup -q

%build
python2 setup.py build_i18n -m
python2 setup.py build

%install
python2 setup.py install -O1  --prefix /usr --skip-build --root %{buildroot}
install -Dm644 build/mo/fr/LC_MESSAGES/%{name}.mo %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
install -Dm644 build/mo/zh_CN/LC_MESSAGES/%{name}.mo %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/%{name}.mo
install -Dm644 build/share/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc AUTHORS ChangeLog COPYING TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/pixmaps/%{name}.png
%{python2_sitelib}/*

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.1
- Rebuilt for Fedora
