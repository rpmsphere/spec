Name: mazen
Version: 1.0.1
Release: 5.1
Summary: Simple Gnome-base maze creator
License: GPLv3
Group: Games/Puzzles
URL: http://mazen.sourceforge.net
Source: %name-%version.tar.gz
BuildRequires: gcc-c++ intltool gtkmm24-devel librsvg2-devel cairomm-devel glibmm24-devel

%description
Can create various types of mazes, and export them in PDF, PNG or SVG formats.

%prep
%setup -q

%build
autoreconf -ifv
%configure
%make_build

%install
%make_install
%__install -Dm644 artwork/mazen.png %buildroot%_datadir/pixmaps/%name.png

# menu
%__mkdir_p %buildroot%_datadir/applications
%__cat << EOF > %buildroot%_datadir/applications/%name.desktop
[Desktop Entry]
Name=Mazen
Comment=Simple Gnome-base maze creator
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF

%files
%_bindir/*
%_datadir/doc/%name
%_datadir/%name
%_datadir/pixmaps/*
%_datadir/applications/*

%changelog
* Fri Dec 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuild for Fedora
* Fri Oct 09 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2
- Fix build with gcc5
* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1-alt1.qa1.1
- Rebuilt for gcc5 C++11 ABI.
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.1-alt1.qa1
- NMU: rebuilt for debuginfo.
* Sat Jan 29 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt1
- initial build for ALT
