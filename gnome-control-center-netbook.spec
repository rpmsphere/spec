# norootforbuild

Name:       gnome-control-center-netbook
Summary:    Utilities to configure the netbook desktop
Version:    2.29.16
Release:    17.1
Group:      System/Desktop
License:    GPLv2+ and GFDL
URL:        http://www.gnome.org
Source0:    http://download.gnome.org/sources/gnome-control-center/2.29/gnome-control-center-%{version}.tar.bz2
Source1:    gnome-appearance-properties.desktop
Source2:    gnome-network-properties.desktop
Source3:    gnome-settings-mouse.desktop
Source4:    keyboard.desktop
Patch0:     MeeGo-patch-out-help-button-for-network.patch
Patch1:     Update-Po-2010-06-21.patch
Patch2:     display-apply.patch
Patch3:     gnome-control-center-netbook-opensuse-build.patch
Patch4:     gnome-control-center-netbook-panel-ref-count.patch
Patch5:     gnome-control-center-netbook-bnc613500-reparent.patch
Requires:   gnome-settings-daemon
Requires:   gnome-icon-theme
Requires:   gnome-menus
Requires:   usermode
Requires:   gnome-desktop
Requires:   dbus-1-x11
Requires(pre): gconf2
Requires(preun): gconf2
Requires(post): /sbin/ldconfig
Requires(post): gconf2
Requires(post): /bin/touch
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(gnome-desktop-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libgnome-menu)
BuildRequires:  pkgconfig(libgnomeui-2.0)
BuildRequires:  pkgconfig(libpanelapplet-2.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libmutter-private)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libgnomekbd)
BuildRequires:  pkgconfig(evolution-data-server-1.2)
BuildRequires:  pkgconfig(xxf86misc)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-audio-0.10)
BuildRequires:  pkgconfig(unique-1.0)
BuildRequires:  libmx-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gnome-doc-utils
BuildRequires:  intltool
BuildRequires:  gnome-common
Provides:   gnome-control-center


%description
The GNOME control-center provides a number of extension points
for applications. This package contains directories where applications 
can install configuration files that are picked up by the control-center
utilities.



%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The control-center package contains configuration utilities for the 
GNOME desktop.

This package contains libraries and header files needed for integrating
configuration of applications such as window managers with the control-center
utilities.



%prep
%setup -q -n gnome-control-center-%{version}

# MeeGo-patch-out-help-button-for-network.patch
%patch0 -p1
# Update-Po-2010-06-21.patch
%patch1 -p1
# display-apply.patch
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i 's|mx-gtk/|mx/|' capplets/security/cc-security-panel.c

%build
%configure --disable-static \
    --disable-scrollkeeper \
    --disable-update-mimedb \
    --enable-moblin \
    --with-window-manager=mutter \
    --with-userpasswd \
    --enable-security

make %{?jobs:-j%jobs} V=1

%install
%makeinstall
find %{buildroot} -type f -name "*.la" -delete -print

install -m 0644 %{SOURCE1} %{buildroot}/%{_datadir}/applications
install -m 0644 %{SOURCE2} %{buildroot}/%{_datadir}/applications
install -m 0644 %{SOURCE3} %{buildroot}/%{_datadir}/applications
install -m 0644 %{SOURCE4} %{buildroot}/%{_datadir}/applications
%find_lang gnome-control-center-2.0
%find_gconf_schemas
cat %{name}.schemas_list > %{name}.lst
cat gnome-control-center-2.0.lang >> %{name}.lst

%pre -f %{name}.schemas_pre

%preun  -f %{name}.schemas_preun

%post
/sbin/ldconfig
%post -n gnome-control-center-netbook-devel -p /sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :

%postun
/sbin/ldconfig
%postun -n gnome-control-center-netbook-devel -p /sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :

%files -f %{name}.lst
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_datadir}/gnome-control-center/keybindings/*.xml
#%{_datadir}/gnome-control-center/default-apps/*.xml
#%{_datadir}/gnome-control-center/glade
%{_datadir}/gnome-control-center/ui
%{_datadir}/gnome-control-center/pixmaps
%{_datadir}/applications/*.desktop
%{_datadir}/applications/mimeinfo.cache
%{_datadir}/desktop-directories/*
%{_datadir}/mime/packages/gnome-theme-package.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/gnome
%{_datadir}/omf
# list all binaries explicitly, so we notice if one goes missing
#%{_bindir}/gnome-about-me
%{_bindir}/gnome-appearance-properties
#%{_bindir}/gnome-at-mobility
#%{_bindir}/gnome-at-properties
#%{_bindir}/gnome-at-visual
%{_bindir}/gnome-control-center
#%{_bindir}/gnome-default-applications-properties
%{_bindir}/gnome-display-properties
#%{_bindir}/gnome-keybinding-properties
%{_bindir}/gnome-keyboard-properties
%{_bindir}/gnome-mouse-properties
%{_bindir}/gnome-network-properties
%exclude %{_bindir}/gnome-typing-monitor
#%{_bindir}/gnome-window-properties
%{_bindir}/gnome-font-viewer
%{_bindir}/gnome-thumbnail-font
%{_sysconfdir}/xdg/menus/gnomecc.menu
#%exclude %{_sysconfdir}/xdg/autostart/gnome-at-session.desktop
%{_libdir}/window-manager-settings/*.so
%{_libdir}/control-center-1/extensions/*.so
%{_libexecdir}/cc-theme-thumbnailer-helper
%exclude %_libexecdir/debug

%files devel
%defattr(-,root,root,-)
%{_includedir}/gnome-window-settings-2.0
%{_libdir}/libgnome-*.so
%{_libdir}/libgnome-*.so*
%{_datadir}/pkgconfig/gnome-keybindings.pc
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gnome-control-center-1

%clean
rm -rf %{buildroot}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Tue Jul 20 2010 glin@novell.com
- Clean up gconf schemas in spec
- Add gnome-control-center-netbook-opensuse-build.patch to pass
  package building against openSUSE 11.3
- Add gnome-control-center-netbook-panel-ref-count.patch to fix
  appearance panel. bmc#2107
- Add gnome-control-center-netbook-bnc613500-reparent.patch to
  avoid blank window. bnc#613500
* Thu Jul 15 2010 awafaa@opensuse.org
- Update to version 2.29.16
* Tue Jun 15 2010 dimstar@opensuse.org
- Fix Requires({Pre,Post,Postun}) to require /usr/bin/gconftool-2
  instead of GConf2 package name.
- BuildRequire pkgconfig(gnome-doc-utils) >= 0.3.2.
* Tue Jun 15 2010 awafaa@opensuse.org
- Import MeeGo based g-c-c to get mutter-moblin building
