%global _name Nanoshot

Name: nanoshot
Summary: Tool for taking screenshots
Version: 0.2.15
Release: 10.1
Group: Converted/graphics
License: GPLv2
URL: http://nanoshot.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python-pycurl
BuildRequires: gnome-python2-libwnck
BuildRequires: python-pillow
BuildRequires: xdg-utils
BuildRequires: pygobject2
BuildRequires: pygtk2
BuildRequires: dbus-python
BuildRequires: python2

%description
An easy and convenient way to take screenshot. Priority principles:
lightness and comfort. Nanoshot can take screenshots of screen area,
selected windows, web pages and videos.

%prep
%setup -q

%build
./configure --prefix=/usr

%install
sed -i '47,50d' install
./install --root %{buildroot}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}/usr/lib/Nanoshot/*.py %{buildroot}%{_bindir}/*

%files
%doc COPYING README
%{_bindir}/%{_name}
/usr/lib/%{_name}
%{_datadir}/%{_name}
%{_datadir}/icons/hicolor/22x22/status/nanoshot-status-icon.svg
%exclude %{_datadir}/icons/*/status/22/nanoshot-status-icon.svg
%{_datadir}/locale/*/LC_MESSAGES/%{_name}.mo
%{_mandir}/man1/%{_name}.1.*

%changelog
* Mon Dec 05 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.15
- Rebuild for Fedora
