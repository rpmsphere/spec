Name: etmqt
Summary: Manage events and tasks using simple text files
Version: 2.3.27
Release: 3.4
Group: Applications/Productivity
License: GPLv3
URL: http://people.duke.edu/~dgraham/etmqt/
Source0: http://people.duke.edu/~dgraham/etmqt/etm_qt-%{version}.tar.gz
BuildRequires: python2-devel
BuildRequires: python2-setuptools
Requires: python2-qt4
BuildArch: noarch

%description
etm is an acronym for event and task manager. This application provides
a simple, intuitive format for using plain text files to store events, tasks
and other data items. Items can be created, modified and viewed in a variety
of convenient ways using either the command line or a cross-platform, PyQt
based GUI. Repetition is supported in a powerful and flexible manner for tasks
as well as events. Supported alarm types in the GUI include display, sound,
voice (using system text to speech), email, text message and process.

%prep
%setup -q -n etm_qt-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%{_bindir}/etm_qt
%{python2_sitelib}/etmQt
%{python2_sitelib}/etm_qt-%{version}-py2.?.egg-info
%{_datadir}/applications/etm_qt.desktop
%{_datadir}/doc/etm_qt
%{_datadir}/icons/etm_qt
%{_datadir}/pixmaps/etm_qt.xpm
%{_mandir}/man1/etm_qt.1.*

%changelog
* Tue Aug 04 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.27
- Rebuilt for Fedora
