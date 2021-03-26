Name:           netbook-launcher
Version:        2.1.18
Release:        1
License:        GPLv3
Group:          System/Desktop
Summary:        A clutter-based desktop launcher, typically used on netbooks
URL:            https://launchpad.net/netbook-remix-launcher
Source0:        http://launchpad.net/netbook-remix-launcher/2.0/ubuntu-9.10-ui-freeze/+download/%{name}-%{version}.tar.gz
Source1:	netbook-launcher.png
BuildRequires:  glib2-devel pango-devel librsvg2-devel gtk2-devel GConf2-devel
BuildRequires:  libgnomeui-devel gnome-desktop-devel cairo-devel
BuildRequires:  dbus-devel dbus-glib-devel startup-notification-devel
BuildRequires:  libwnck-devel intltool clutter-devel clutter-gtk010-devel
BuildRequires:  gnome-menus-devel libXres-devel
BuildRequires:  liblauncher
BuildRequires:  clutk
BuildRequires:  liblauncher-devel clutk-devel
BuildRequires:  libnotify-devel
BuildRequires:  libwnck-devel
BuildRequires:  unique-devel
Requires:	%{name}-lib

%description
Netbook Launcher is a desktop launcher that uses the clutter UI library.
It is commonly being used on netbook desktops with a resolution of 1024x600 pixels 
and also supposed to support usage on touchscreens. 
It follows the xdg spec standards from freedesktop.org for the Desktop menu layout.

%package lib
Summary:        Library files for %{name}

%description lib
Library files for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:	%{name}-lib

%description devel
Development files for %{name}.

%prep
%setup -q
sed -i 's/#define QUIT_SIZE 64/#define QUIT_SIZE 0/' src/nl-favorite-view.c
sed -i -e 's/-Werror //' -e 's/clutk-0\.2/clutk-0.3/' configure
sed -i '/notify_notification_new/s/, NULL//' src/nl-favorite-item.c

%build
export CFLAGS=-I/usr/include/dbus-1.0
export LIBS='-ldbus-glib-1 -lX11 -lXau'
%configure
make %{?jobs:-j%jobs}

%install
%makeinstall
%find_lang %{name}

%__mkdir -p %{buildroot}%{_libdir}/%{name}/plugins

%__mkdir -p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/nblauncher-switch <<EOF
#!/bin/sh
if ps -C netbook-launche ; then
  pkill -9 netbook-launche
else
  netbook-launcher
fi
EOF

# icons
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/netbook-launcher.png

%__mkdir -p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/nblauncher-switch.desktop <<EOF
[Desktop Entry]
Name=Launcher Switching
Name[zh_TW]=啟動介面切換
Comment=Switching desktop applications launcher
Comment[zh_TW]=切換桌面軟體啟動程式
Exec=nblauncher-switch
Terminal=false
Type=Application
Icon=netbook-launcher
Encoding=UTF-8
Categories=Application;System;Utility;
EOF

%clean
rm -rf %{buildroot}

%files -f %name.lang
%doc AUTHORS TODO COPYING
%{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/nblauncher-switch
%{_datadir}/applications/nblauncher-switch.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_sysconfdir}/gconf/schemas/netbook-launcher.schemas
%exclude %{_sysconfdir}/xdg/autostart/netbook-launcher.desktop

%files lib
%{_libdir}/lib%{name}.so*
%{_libdir}/%{name} 

%files devel
%doc AUTHORS TODO COPYING
%{_libdir}/lib%{name}.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Feb 16 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Exclude autostart
- Update to 2.1.18

* Fri Dec 19 2008 bluebat@member.fsf.org
- Rebuild for OSSII

* Tue Nov 11 2008 claes.backstrom@fsfe.org
- New upstream release 1.5.1

* Wed Oct 29 2008 claes.backstrom@fsfe.org
- New upstream release 1.5.0

* Wed Oct 15 2008 claes.backstrom@fsfe.org
- Initial Package
