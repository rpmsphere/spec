Name: icewmcc
Version: 2.9
Release: 2.1
Summary: IceWM Control Center
License: GPL
Group: Graphical desktop/Icewm
Source0: icecc-2.9.tar.bz2
URL: https://icecc.sourceforge.net/
Requires: icewm
BuildRequires: qt3-devel

%description
The IceWM Control Center allows you to run a various tool for IceWM's
configuration. It contains: menu/toolbar editor, background switcher,
themes switcher, keys editor, winoptions editor, icons converter and
other usefull tools.

%prep
%setup -q -n icecc-%{version}
sed -i 's|/usr/local|/usr|' icecc.pro
sed -i 's|icecc|icewmcc|' *.h *.cpp *.pro *.xpm
rename icecc icewmcc *

%build
export QTDIR=%{_libdir}/qt-3.3
$QTDIR/bin/qmake
make

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Name=IceWM Control Center
Comment=IceWM Control Center with some tools
Exec=%{name}
Terminal=false
Type=Application
Categories=Application;System;
Icon=/usr/share/icewmcc/help/default/icecc_desk.png
EOF

%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icewmcc

%changelog
* Tue May 10 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.9
- Rebuilt for Fedora
