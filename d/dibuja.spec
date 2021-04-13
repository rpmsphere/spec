Name: dibuja
Version: 0.21.12
Release: 1
Summary: Gtk based basic paint program
License: GPLv3
Group: Graphics
URL: https://launchpad.net/%name
Source: %url/trunk/%version/+download/%name-%version.tar.gz
BuildRequires: intltool gtk2-devel gegl04-devel exiv2-devel
BuildRequires: atlas

%description
Dibuja is a program for quick small editing and drawing.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libdir/gegl-0.?/*
%_datadir/applications/%name.desktop
%_datadir/%name/
%_defaultdocdir/%name/
%_datadir/pixmaps/dibuja.*

%changelog
* Sun Apr 4 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.21.12
- Rebuild for Fedora
* Sun Apr 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0
* Thu Jun 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt2
- fixed docdir
* Thu Jun 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- first build for Sisyphus
