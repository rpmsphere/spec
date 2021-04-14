%undefine _debugsource_packages
Name: gnomego
Summary: A Go client for the gnome desktop
Version: 0.5.1
Release: 12.1
Group: Amusements/Games
License: GPLv3
URL: http://gnomego.sourceforge.net/
Source0: http://sourceforge.net/projects/gnomego/files/gnomego/GnomeGo%20%{version}/%{name}-%{version}.tar.gz
BuildRequires: python2-devel
BuildRequires: mate-screensaver-devel
BuildRequires: gnugo
BuildRequires: fedora-logos
Requires: gnugo
Requires: gnome-python2-gnome
BuildArch: noarch

%description
GnomeGo is a gnome HIG compatbile frontend for gnugo. It also features
human vs. human play, adds a nautilus sgf file preview and a gnome
screensaver playing bundled professional games.

%prep
%setup -q
sed -i 's|gnome-screensaver|mate-screensaver|' setup.py

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%{_datadir}/doc/%{name}-%{version}
%{_bindir}/*
%{python2_sitelib}/*
%{_libexecdir}/mate-screensaver/sgf-screensaver
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/screensavers/sgf-screensaver.desktop
%{_datadir}/gconf/schemas/sgf-thumbnailer.schemas
%{_datadir}/gnome/help/%{name}/*.xml
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}_64x64.png

%changelog
* Thu Jan 02 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.1
- Rebuilt for Fedora
