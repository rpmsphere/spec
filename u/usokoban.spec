%undefine _debugsource_packages
Name: usokoban
Version: 0.0.9
Release: 1
Summary: Sokoban clone for GNOME
License: GPL
Group: Amusements/Games
URL: https://sokoban.ws/usokoban/usokoban.php
Source: %{name}-%{version}.tar.gz
BuildRequires: glib2-devel, gtk2-devel

%description
The motive of writing USokoban is to provide a new native version of Sokoban for Linux/GNU.
Main Features:
 *Open external XSB Sokoban levelsets
 *Support level size of upto 60x60
 *Support solutions of unlimited length
 *Fast algorithm for box-pushing
 *Unlimited undos
 *Support change of skins
 *Paste levels or solution from clipboard directly
 *Copy solution to clipboard 

%prep
%setup -q

%build
gcc base.c settings.c sokoban.c sokoban2.c solver.c savitch.c -o usokoban `pkg-config --cflags --libs gtk+-2.0` -lgthread-2.0

%install
rm -rf $RPM_BUILD_ROOT
%__install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp skin*.png stopheart*.txt %{buildroot}%{_datadir}/%{name}
%__install -D -m644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -D -m644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README INSTALL
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.9
- Rebuilt for Fedora
