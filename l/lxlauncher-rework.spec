Name:           lxlauncher-rework
Version:        0.1
Release:        1
Summary:        Lightweight desktop applications launcher
Group:          Applications/System
License:        GPL
URL:            https://sourceforge.net/projects/lxde/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  gettext, gtk2-devel >= 2.6, gnome-menus-devel, startup-notification-devel
BuildRequires:  menu-cache-devel
Requires:       gtk2 >= 2.6, gnome-menus

%description
LXLauncher is an open source clone of Asus launcher for EeePC.
It outperformes the original launcher developed by Xandros.

%prep
%setup -q -n %{name}
#sed -i 's/2\.18\.0/2.16.0/' configure configure.in

%build
sh autogen.sh
%configure
sed -i 's|-lmenu-cache|-lmenu-cache -lX11|' src/Makefile
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%__cat > %{buildroot}%{_bindir}/%{name}-switch <<EOF
#!/bin/sh
for_process=lxlauncher
[ "\$for_process" == "" ] || killall -9 -u \$USER "\$for_process" || \$for_process \$* &
EOF

%__mkdir -p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}-switch.desktop <<EOF
[Desktop Entry]
Name=Launcher Switching[rework]
Name[zh_TW]=啟動介面切換[rework]
Comment=Switching lightweight desktop applications launcher
Comment[zh_TW]=切換輕量桌面軟體啟動程式
Exec=%{name}-switch
Terminal=false
Type=Application
Icon=launcher-program
Encoding=UTF-8
Categories=Application;System;Utility;
EOF

%files 
%doc NEWS README AUTHORS ChangeLog COPYING
%{_bindir}/lxlauncher
%attr(0755,root,root) %{_bindir}/%{name}-switch
%{_datadir}/applications/%{name}-switch.desktop
%{_datadir}/desktop-directories/*.directory
%{_datadir}/locale/*
%{_datadir}/lxlauncher/*
/etc/xdg/menus/lxlauncher-applications.menu

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Tue Apr 21 2009 Feather Mountain <john@ossii.com.tw> - 0.1-1.ossii
- Build for M6(OSSII)
