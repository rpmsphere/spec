Name:           fsgamer
License:        GPLv3
Group:          Amusements/Games
Version:        0.1.2
Release:        4.1
Summary:	Full-screen Linux gaming, improved
URL:		https://bitbucket.org/michaelb/fsgamer
Source:         https://cdn.bitbucket.org/michaelb/fsgamer/downloads/%{name}_%{version}.tar.gz
Requires:       espeak, openbox
BuildRequires:  intltool, python2-distutils-extra
BuildRequires:  python2-devel
BuildArch:	noarch

%description
FSGamer runs games in their own X server, which can improve the speed,
reduce annoying interruptions, and make switching between fullscreen games
and your desktop easy and reliable.

%prep
%setup -q -n %{name}

%build
python2 setup.py build

%install
python2 setup.py install --prefix=/usr --root=$RPM_BUILD_ROOT
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
sed -i 's|Categories=Game;|Categories=Game;Emulator;|' %{buildroot}%{_datadir}/applications/%{name}.desktop

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.md AUTHORS COPYING
%{_bindir}/%{name}
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%exclude %{_datadir}/doc/fsgamer/README.md
%{_datadir}/glib-2.0/schemas/net.launchpad.fsgamer.gschema.xml
%{_datadir}/help/*/%{name}

%changelog
* Mon Mar 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2
- Rebuilt for Fedora
