%undefine _debugsource_packages
Name:           vala-panel
Version:        0.3.75
#Version:        0.4.91
Release:        1
Summary:        A Gtk3 desktop panel based on Vala
License:        GPL-3.0+
Group:          System/GUI/Other
URL:            https://github.com/rilian-la-te/vala-panel
Source:         https://github.com/rilian-la-te/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8
BuildRequires:  gettext
BuildRequires:  vala >= 0.24
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.2.0
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.4.0
Recommends:     %{name}-lang = %{version}
Recommends:     %{name}-plugins-base = %{version}
Recommends:     %{name}-sntray = %{version}
Suggests:       %{name}-appmenu = %{version}
Suggests:       %{name}-plugins-wnck = %{version}

%description
Vala Panel is a desktop panel written in Vala and Gtk3.
Initially it was a fork of LXPanel but 0.2.0 is completely
rewritten in Vala. It offers same functionality as LXPanel but:
 * It has a slightly bigger memory usage.
 * X11 dependency is stripped from panel core (but it is not tested
   on another display servers, such as Wayland and Mir, right now).
 * Some of former LXPanel plugins are separate binaries now
   and live in another packages (volume applet for example).

%package devel
Summary:        Development files for vala-panel
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       pkgconfig(gtk+-3.0) >= 3.12.0
Requires:       pkgconfig(libpeas-1.0) >= 1.2.0
Requires:       pkgconfig(libwnck-3.0) >= 3.4.0

%description devel
Vala Panel is a desktop panel written in Vala and Gtk3.

This is a development package for vala-panel.

%package plugins-base
Summary:        Plugins for vala-panel -- non-X11 plugins
Group:          System/GUI/Other

%description plugins-base
This package contains main plugins for vala-panel: clock,
launchbar, applications menu and so on.

%package plugins-wnck
Summary:        Plugins for vala-panel -- X11 plugins
Group:          System/GUI/Other

%description plugins-wnck
This package contains X11 plugins for vala-panel: tasklist,
system tray, and others.

%prep
%setup -q
#rm vapi/glib-2.0.vapi
sed -i '35,36d' vapi/gio-addons-2.0.vapi
#sed -i '35,36d' lib/dbusmenu/gio-addons-2.0.vapi
sed -i 's|monitor_unref|monitor_free|' applets/drawing/monitors/monitors.vala

%build
%cmake -DCMAKE_C_FLAGS="-fPIC -I/usr/include/harfbuzz" \
  -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
  -DGSETTINGS_COMPILE=OFF
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

%post
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas

%postun
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas

%post plugins-base
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas

%postun plugins-base
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas

%post plugins-wnck
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas

%postun plugins-wnck
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas

%files -f %{name}.lang
%doc LICENSE README.md
%config %{_sysconfdir}/xdg/vala-panel/
%{_mandir}/man?/vala-panel.?.*
%{_mandir}/man?/vala-panel-runner.?.*
%{_bindir}/vala-panel
%{_bindir}/vala-panel-runner
%{_datadir}/glib-2.0/schemas/org.valapanel.gschema.xml
%{_libdir}/libvalapanel.so.*
%{_datadir}/vala/
%{_datadir}/vala-panel/
%{_datadir}/glib-2.0/schemas/org.valapanel.toplevel.gschema.xml
%{_datadir}/icons/hicolor/*/apps/vala-panel.*
%{_datadir}/applications/org.valapanel.application.desktop
%{_datadir}/metainfo/org.valapanel.application.appdata.xml

%files devel
%{_libdir}/libvalapanel.so
%{_includedir}/vala-panel/
%{_libdir}/pkgconfig/vala-panel.pc

%files plugins-base
%{_datadir}/glib-2.0/schemas/org.valapanel.builtin.gschema.xml
%{_datadir}/glib-2.0/schemas/org.valapanel.plugins.gschema.xml
%dir %{_libdir}/vala-panel/
%dir %{_libdir}/vala-panel/applets/
%{_libdir}/vala-panel/applets/libclock.so
%{_libdir}/vala-panel/applets/libcpu.so
%{_libdir}/vala-panel/applets/libdirmenu.so
%{_libdir}/vala-panel/applets/libkbled.so
%{_libdir}/vala-panel/applets/liblaunchbar.so
%{_libdir}/vala-panel/applets/libmenumodel.so
%{_libdir}/vala-panel/applets/libseparator.so
%{_libdir}/vala-panel/applets/libmonitors.so
%{_libdir}/vala-panel/applets/libicontasks.so
%{_libdir}/vala-panel/applets/icontasks.plugin
%{_libdir}/vala-panel/applets/clock.plugin
%{_libdir}/vala-panel/applets/cpu.plugin
%{_libdir}/vala-panel/applets/dirmenu.plugin
%{_libdir}/vala-panel/applets/kbled.plugin
%{_libdir}/vala-panel/applets/launchbar.plugin
%{_libdir}/vala-panel/applets/menumodel.plugin
%{_libdir}/vala-panel/applets/separator.plugin
%{_libdir}/vala-panel/applets/monitors.plugin

%files plugins-wnck
%{_datadir}/glib-2.0/schemas/org.valapanel.X.gschema.xml
%{_libdir}/vala-panel/applets/libxembed.so
%{_libdir}/vala-panel/applets/libdeskno.so
%{_libdir}/vala-panel/applets/libtasklist.so
%{_libdir}/vala-panel/applets/libwincmd.so
%{_libdir}/vala-panel/applets/libpager.so
%{_libdir}/vala-panel/applets/libbuttons.so
%{_libdir}/vala-panel/applets/libtasklist-xfce.so
%{_libdir}/vala-panel/applets/tasklist-xfce.plugin
%{_libdir}/vala-panel/applets/xembed.plugin
%{_libdir}/vala-panel/applets/deskno.plugin
%{_libdir}/vala-panel/applets/tasklist.plugin
%{_libdir}/vala-panel/applets/wincmd.plugin
%{_libdir}/vala-panel/applets/pager.plugin
%{_libdir}/vala-panel/applets/buttons.plugin

%changelog
* Fri Jan 17 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.75
- Rebuilt for Fedora
* Sat May  7 2016 sor.alexei@meowr.ru
- Fix build by using upstream glib-2.0.vapi.
* Wed Jun 24 2015 cdenicolo@suse.com
- correct license is GPL-3.0+, see LICENSE-file
* Fri Jun 19 2015 sor.alexei@meowr.ru
- Initial package
