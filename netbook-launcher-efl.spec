Name: netbook-launcher-efl
Version: 0.3.3
Release: 2
Summary: A lite version of netbook launcher written in EFL
License: GPLv3
Group: Graphical desktop/GNOME
URL: https://launchpad.net/launch-lite-proj
BuildRequires: edje-devel embryo-devel libXau-devel libcanberra-devel libelementary-devel libgnomeui-devel liblauncher-devel libnotify-devel ecore-devel evas-devel eet-devel libeina-devel unique-devel
BuildRequires: intltool >= 0.34
##BuildRequires: liblauncher
Source0: http://launchpad.net/launch-lite-proj/0.3/0.3.3/+download/%{name}-%{version}.tar.bz2

### change default theme to alternative
Patch0: netbook-launcher-efl-0.2.6-theme.patch

%description
This is a version of netbook-launcher using the Enlightenment Foundation Libraries (EFL)
to run fast on systems with reduced hardware functionality. It provides a modern application
launcher especially suited to small screens.

%prep
%setup -q
%patch0 -p1

###adaptive to current EFL
sed -i 's/eina-0/eina/' configure*
sed -i '/color3/d' data/themes/default/default.edc data/themes/alternative/alternative.edc

### use Droid Sans font in default theme
sed -i 's/font=Sans/font=DroidSans/' data/themes/default/default.edc

### remove storage category
sed -i '/_sidebar_append_item_places(ctxt);/d' src/launcher/sidebar.c

### split preference category
##sed -i '/PREFS_COLLAPSE/d' src/launcher/netbook-launcher.h

### downgrade libnotify for OX2
sed -i 's/NOTIFY_VER=0\.7/NOTIFY_VER=0.4.5/' configure*
sed -i '/notify_notification_new/s/, icon/, icon, NULL/' src/launcher/app_item.c

### modify for notification.h in F15
##sed -i '/notify_notification_new/s/, NULL//' src/launcher/app_item.c

### modify for DSO in F15
sed -i 's/gtk+-2\.0/gtk+-2.0 x11 ecore-input/' configure*
##sed -i 's/\$(LIBS)/$(LIBS) -lX11/' src/launcher/Makefile*

%build
%configure
make %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

%__mkdir -p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/nblauncherefl-switch <<EOF
#!/bin/sh
if ps -C netbook-launche ; then
  pkill -9 netbook-launche
else
  netbook-launcher-efl
fi
EOF
   
%__mkdir -p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/nblauncherefl-switch.desktop <<EOF
[Desktop Entry]
Name=Launcher EFL Switching
Name[zh_TW]=啟動介面 EFL 切換
Comment=Switching desktop applications launcher
Comment[zh_TW]=切換桌面軟體啟動程式
Exec=nblauncherefl-switch
Terminal=false
Type=Application
Icon=gnome-fs-desktop
Encoding=UTF-8
Categories=Application;System;Utility;
EOF

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
%{_sysconfdir}/gconf/schemas/netbook-launcher-efl.schemas > /dev/null || :

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/netbook-launcher-efl.schemas > /dev/null || :
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/applications/nblauncherefl-switch.desktop
%_sysconfdir/gconf/schemas/*
%exclude %_sysconfdir/xdg/autostart/*
%_datadir/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Oct 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> 0.3.3-2.ossii
- Rebuild for OSSII

* Sun Feb 28 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Thu Feb 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Thu Feb 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.2-alt1
- initial
