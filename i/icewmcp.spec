Summary: IceWM Control Panel
Name: icewmcp
Version: 3.2
Release: 1
License: GPL
Group: Graphical desktop/Icewm
URL: http://www.phrozensmoke.com/projects/icewmcp/
Source: IceWMControlPanel-%{version}.tar.bz2
Source1: icewmcp.desktop
Source2: icepref-16.png
Source3: icepref-32.png
Source4: icepref-48.png
Source5: icewmcp-create-links.pl
Requires: icewm python gtk2 pygtk2
Provides: icepref, icepref2
Obsoletes: icepref
BuildArchitectures: noarch

%description
IceWMControlPanel is a configuration utility for IceWM written 
in Python using the Gtk widget set and the PyGTK bindings. 
It currently covers all of the configuration options in the 
controlled by the preferences file for icewm.

%prep
%setup -q -n INSTALL-IceWMCP

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/IceWMCP
mkdir -p %{buildroot}%{_datadir}/applications
cp -a * %{buildroot}%{_datadir}/IceWMCP
mv %{buildroot}%{_datadir}/IceWMCP/locale %{buildroot}%{_datadir}/locale
%{__perl} %{SOURCE5} %{_datadir}/IceWMCP %{buildroot}%{_bindir}
cp %{SOURCE1} %{buildroot}%{_datadir}/applications

#icon
install -D -m644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -D -m644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m644 %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/IceWMCP/*.py
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/IceWMCP/*.py %{buildroot}%{_datadir}/IceWMCP/PyInstallShield
sed -i 's|^python |python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%doc doc/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/IceWMCP
%{_bindir}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2
- Rebuilt for Fedora
* Sun Feb 13 2005 Crispin Boylan <viewtronix@uklinux.net> 3.2-1mdk
- initial cooker package
