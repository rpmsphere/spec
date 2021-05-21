Name:           lxlauncher-gmenu
Version:        0
Release:        0.819
Summary:        Lightweight desktop applications launcher based on libgnome-menu
Group:          Applications/System
License:        GPL
URL:            http://sourceforge.net/projects/lxde/
Source0:        http://downloads.sourceforge.net/lxde/%{name}.tar.gz
Source1:        lxswitch.png
Source2:	lxlauncher-background.png
Source3:	oxstore-launcher.menu
Patch0:		lxlauncher-fixnobackground.patch
BuildRequires:  gettext, gtk2-devel, gnome-menus-devel, startup-notification-devel
Requires:       gtk2, gnome-menus

%description
LXLauncher is an open source clone of Asus launcher for EeePC.
It outperformes the original launcher developed by Xandros.

%prep
%setup -q -n %{name}
%patch0 -p1
sed -i -e 's/#define BUTTON_SIZE	120/#define BUTTON_SIZE	130/' -e 's/#define IMG_SIZE	48/#define IMG_SIZE	96/' src/lxlauncher.c
sed -i -e 's/box, img, FALSE, TRUE/box, img, TRUE, TRUE/' -e 's/box, label, FALSE, TRUE/box, label, TRUE, TRUE/' src/lxlauncher.c
sed -i '/gtk_widget_set_size_request( label, BUTTON_SIZE - 10, -1 );/d' src/lxlauncher.c
cp -f %{SOURCE3} data/launcher.menu

%build
export LIBS=-lX11
sh autogen.sh --prefix=/usr
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}
%find_lang lxlauncher

%__mkdir -p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/lxlauncher-switch <<EOF
#!/bin/sh
if ps -C lxlauncher ; then
  pkill lxlauncher
else
  lxlauncher
fi
EOF

%__mkdir -p %{buildroot}%{_datadir}/applications
%__install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/lxswitch.png
%__cat > %{buildroot}%{_datadir}/applications/lxlauncher-switch.desktop <<EOF
[Desktop Entry]
Name=Launcher Switching
Name[zh_TW]=啟動介面切換
Comment=Switching lightweight desktop applications launcher
Comment[zh_TW]=切換輕量桌面軟體啟動程式
Exec=lxlauncher-switch
Terminal=false
Type=Application
Icon=lxswitch
Encoding=UTF-8
Categories=Application;System;Utility;
EOF
%__install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/lxlauncher/background.png

%clean
%__rm -rf %{buildroot}

%files -f lxlauncher.lang
%defattr(-,root,root,-)
%doc NEWS README AUTHORS ChangeLog COPYING
%{_bindir}/lxlauncher
%attr(0755,root,root) %{_bindir}/lxlauncher-switch
%{_datadir}/lxlauncher
%{_datadir}/pixmaps/lxswitch.png
%{_datadir}/applications/lxlauncher-switch.desktop
%{_datadir}/desktop-directories/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Jan 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0-0.818.ossii
- Fix icon size and text justify
- Add BuildRequires: startup-notification-devel, Source3: oxstore-launcher.menu

* Thu Jan 22 2009 Wind <yc.yan@ossii.com.tw> - 0-0.816.ossii
- Fix the 'Cannot setup background image' problem -- User can put the background image to datadir/lxlauncher/background.png [file]

* Tue Aug 5 2008 Wei-Lun Chao <bluebat@member.fsf.org> - 0-0.814.ossii
- Initial RPM release
