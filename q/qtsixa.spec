%undefine _debugsource_packages

Name: qtsixa
Summary: Sixaxis Joystick Manager
License: GPLv2
Group: Hardware/Joystick
URL: http://qtsixa.sourceforge.net/
Version: 1.5.1
Source: QtSixA-%{version}-src.tar.gz
Release: 18.4
BuildRequires: libpng-devel, python3-PyQt4-devel, jack-audio-connection-kit-devel
BuildRequires: dbus-devel, qt4-devel, glib2-devel, bluez-libs-devel, libusb-devel
Requires: sixad

%description
This package provides a useful GUI to control the sixad modules.
QtSixA is written in PyQt.

%package -n sixad
Summary: SixA Daemon
Group: Hardware/Joystick
Requires: python-qt4

%description -n sixad
This package provides background daemon for connecting PS3 hardware
(Sixaxis/DualShock3 and Keypads) to a Linux-compatible machine.

%prep
%setup -q -n QtSixA-%{version}
sed -i '1i #include <unistd.h>' sixad/shared.h

%build
export QTDIR=%{_libdir}/qt4
make

%install
%make_install
chmod +x %{buildroot}%{_bindir}/*

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/* %{buildroot}%{_sbindir}/*

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc README COPYING TODO
%{_bindir}/*
%{_datadir}/qtsixa/*
%{_datadir}/applications/qtsixa.desktop
%{_datadir}/pixmaps/qtsixa.xpm

%files -n sixad
%{_bindir}/sixad
%{_sbindir}/*
%config /etc/default/sixad
/etc/init.d/sixad
/etc/logrotate.d/sixad

%changelog
* Fri Jan 03 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.1
- Rebuilt for Fedora
