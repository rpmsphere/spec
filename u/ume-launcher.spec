Name: ume-launcher
License: GPL
Group: User Interface/Desktops
Summary: A clutter based desktop launcher
Version: 0.3
Release: 6
Source: http://launchpadlibrarian.net/14969174/ume-launcher_0.3ubuntu6.tar.gz
URL: https://launchpad.net/netbook-remix-launcher
BuildRequires: gtk2-devel, GConf2-devel, pango-devel, dbus-glib-devel, clutter-devel
BuildRequires: gnome-desktop-devel, gnome-menus-devel, libwnck-devel, librsvg2-devel, libgnomeui-devel
Requires: gtk2, GConf2, pango, dbus-glib, clutter
Requires: gnome-desktop, gnome-menus, libwnck, librsvg2, libgnomeui

%description
This a the desktop-launcher which takes the place of Nautilus.
Replicates the functionality of Applications/Places/System,
with added support for a user-defined favorites category.

%prep
%setup -q -n ume-launcher-0.3ubuntu6
sed -i 's|clutter-0\.6|clutter-0.8|' configure*
sed -i 's|clutter/cogl|cogl/cogl|' tidy/*.c

%build
%configure
sed -i 's/-lglib-2.0/-lglib-2.0 -lgio-2.0/' src/Makefile
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS TODO COPYING COPYING.tidy
%{_bindir}/ume-launcher
%{_sysconfdir}/xdg/autostart/ume-launcher.desktop
%{_datadir}/desktop-directories/*
%{_datadir}/ume-launcher

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Jul 11 2008 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3-6.ossii
- Update to 0.3-6

* Fri Jun 6 2008 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3-3.ossii
- Initial package
