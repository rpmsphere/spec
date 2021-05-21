%define gettext_package gnome-panel-2.0

%define gtk2_version 2.7.1
%define libglade2_version 2.5.0
%define libgnomeui_version 2.5.4
%define gnome_desktop_version 2.9.91
%define libwnck_version 2.9.92
%define libbonobo_version 2.3.0
%define libbonoboui_version 2.3.0
%define gnome_vfs2_version 2.9.1
%define gnome_menus_version 2.11.1
%define evolution_data_server_version 1.1.4
%define orbit_version 2.4.0
%define gtk2_version 2.7.1
%define dbus_version 0.60
%define gnome_doc_utils_version 0.3.2
%define gconf_version 2.14

%define use_evolution_data_server 1

Summary: GNOME panel
Name: gnome-panel
Version: 2.16.1
Release: 7 
URL: http://www.gnome.org
Source0: ftp://ftp.gnome.org/pub/GNOME/pre-gnome2/sources/gnome-panel/%{name}-%{version}.tar.bz2
Source1: ossii-panel-default-setup.entries
Source2: gnome-compiler-flags.m4
Source3: redhat-panel-backwards-compat-config.schemas
Source4: add-translations.sh
License: GPL 
Group: User Interface/Desktops

Requires: gnome-desktop >= %{gnome_desktop_version}
Requires: libwnck >= %{libwnck_version}
Requires: gnome-menus >= %{gnome_menus_version}
%if %{use_evolution_data_server}
Requires: evolution-data-server >= %{evolution_data_server_version}
%endif

Prereq: /bin/awk, /bin/cat, /bin/ln, /bin/rm
Prereq: GConf2 >= 2.6.0-2
Prereq: scrollkeeper
Prereq: gtk2 >= %{gtk2_version}
Requires(post): GConf2 >= %{gconf_version}
Requires(post): scrollkeeper
Requires(post): hicolor-icon-theme
Requires(pre): GConf2 >= %{gconf_version}
Requires(preun): GConf2 >= %{gconf_version}
Requires(postun): scrollkeeper

BuildRequires: which
BuildRequires: libxml2-python
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: scrollkeeper
BuildRequires: libxslt
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: libglade2-devel >= %{libglade2_version}
BuildRequires: libgnomeui-devel >= %{libgnomeui_version}
BuildRequires: gnome-desktop-devel >= %{gnome_desktop_version}
BuildRequires: libwnck-devel >= %{libwnck_version}
BuildRequires: libbonobo-devel >= %{libbonobo_version}
BuildRequires: libbonoboui-devel >= %{libbonoboui_version}
BuildRequires: gnome-vfs2-devel >= %{gnome_vfs2_version}
BuildRequires: gnome-menus-devel >= %{gnome_menus_version}
BuildRequires: gnome-doc-utils >= %{gnome_doc_utils_version}
BuildRequires: gtk-doc
%if %{use_evolution_data_server}
BuildRequires: evolution-data-server-devel >= %{evolution_data_server_version}
BuildRequires: ORBit2-devel >= %{orbit_version}
BuildRequires: dbus-devel >= %{dbus_version}
%endif

Patch0: gnome-panel-2.12.1-vendor.patch
Patch2: gnome-panel-2.10.1-speak-to-us-ye-old-wise-fish.patch
Patch6: gnome-panel-2.13.5-switch-user.patch
Patch8: gnome-panel-2.15.91-use-beagle.patch
Patch9: gnome-panel-2.13.91-ignore-unknown-options.patch
Patch12: gnome-panel-2.14.2-xio-error.patch
Patch13: gnome-panel-2.15.90-move-suspend-to-menu.patch
Patch14: gnome-panel-2.15.92-no-seconds.patch
Patch15: gnome-panel-2.16.0-compiz-support.patch
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=198134
Patch16: gnome-panel-2.16.0-fix-chinese.patch
Patch17: gnome-panel-2.16.1-launcher-copy.patch
Patch18: gnome-panel-2.16.0-respect-session-properties.patch
Patch19: gnome-panel-2.16.1-hide-lock-screen-if-root.patch

Conflicts: gnome-power-manager < 2.15.3

%description
The GNOME panel provides the window list, workspace switcher, menus, and other 
features for the GNOME desktop.

%package devel
Summary: Headers and libraries for Panel Applet development
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: gtk2-devel >= %{gtk2_version}
Requires: libbonoboui-devel >= %{libbonoboui_version}
Requires: libgnomeui-devel >= %{libgnomeui_version}
Requires: pkgconfig

%description devel
Panel Applet development package. Contains files needed for developing
Panel Applets using the libpanel-applet library.

%prep
%setup -q

%patch0 -p1 -b .vendor
%patch2 -p1 -b .speak-to-us-ye-old-wise-fish
%patch6 -p1 -b .switch-user
%patch8 -p1 -b .use-beagle
%patch9 -p1 -b .ignore-unknown-options
%patch12 -p1 -b .xio-error
%patch13 -p1 -b .move-suspend-to-menu
%patch14 -p1 -b .no-seconds
%patch15 -p0 -b .compiz-support
%patch16 -p1 -b .fix-chinese
%patch17 -p1 -b .launcher-copy
%patch18 -p1 -b .respect-session-properties
%patch19 -p1 -b .hide-lock-screen-if-root

. %{SOURCE4}

cp -f %{SOURCE1} gnome-panel/panel-default-setup.entries
cp -f %{SOURCE2} m4
cp -f %{SOURCE3} gnome-panel/panel-compatibility.schemas

%build
# gpm-integration patches Makefile.am and configure.in
automake
autoconf
%configure \
   --disable-gtk-doc \
   --disable-scrollkeeper \
%if %{use_evolution_data_server}
   --enable-eds=yes
%else
   --enable-eds=no
%endif

make

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

#
# Create pager and tasklist schemas for compatibility with older
# configurations which reference the old schema names
#
sed -e 's|/schemas/apps/window_list_applet/prefs/|/schemas/apps/tasklist_applet/prefs/|' $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/window-list.schemas > $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/tasklist.schemas
sed -e 's|/schemas/apps/workspace_switcher_applet/prefs/|/schemas/apps/pager_applet/prefs/|; s|<default>1</default>|<default>2</default>|' $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/workspace-switcher.schemas > $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/pager.schemas

## blow away stuff we don't want
/bin/rm -rf $RPM_BUILD_ROOT/var/scrollkeeper
/bin/rm -f $RPM_BUILD_ROOT%{_libdir}/libpanel-applet-2.*a

# clean up help mess
/bin/mv -f $RPM_BUILD_ROOT/usr/share/omf/gnome-panel/workspace-switcher*.omf \
           $RPM_BUILD_ROOT/usr/share/omf/workspace-switcher
/bin/mv -f $RPM_BUILD_ROOT/usr/share/omf/gnome-panel/window-list*.omf \
           $RPM_BUILD_ROOT/usr/share/omf/window-list
/bin/mv -f $RPM_BUILD_ROOT/usr/share/omf/gnome-panel/fish*.omf \
           $RPM_BUILD_ROOT/usr/share/omf/fish
/bin/rmdir $RPM_BUILD_ROOT/usr/share/omf/gnome-panel

%find_lang %{gettext_package}

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`

#
# Clear out the old defaults
#
gconftool-2 --direct --config-source=$GCONF_CONFIG_SOURCE --recursive-unset /apps/panel > /dev/null || :
gconftool-2 --direct --config-source=$GCONF_CONFIG_SOURCE --recursive-unset /schemas/apps/panel > /dev/null || :

#
# Install the schemas
#
gconftool-2 --makefile-install-rule \
	%{_sysconfdir}/gconf/schemas/clock.schemas \
	%{_sysconfdir}/gconf/schemas/fish.schemas \
	%{_sysconfdir}/gconf/schemas/pager.schemas \
	%{_sysconfdir}/gconf/schemas/panel-compatibility.schemas \
	%{_sysconfdir}/gconf/schemas/panel-general.schemas \
	%{_sysconfdir}/gconf/schemas/panel-global.schemas \
	%{_sysconfdir}/gconf/schemas/panel-object.schemas \
	%{_sysconfdir}/gconf/schemas/panel-toplevel.schemas \
	%{_sysconfdir}/gconf/schemas/tasklist.schemas \
	%{_sysconfdir}/gconf/schemas/window-list.schemas \
	%{_sysconfdir}/gconf/schemas/workspace-switcher.schemas \
  > /dev/null || :

#
# Install the default setup into /apps/panel and /apps/panel/default_setup
#
gconftool-2 --direct --config-source=$GCONF_CONFIG_SOURCE --load %{_sysconfdir}/gconf/schemas/panel-default-setup.entries > /dev/null || :
gconftool-2 --direct --config-source=$GCONF_CONFIG_SOURCE --load %{_sysconfdir}/gconf/schemas/panel-default-setup.entries /apps/panel > /dev/null || :

/sbin/ldconfig

%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/gconf/schemas/clock.schemas \
	%{_sysconfdir}/gconf/schemas/fish.schemas \
	%{_sysconfdir}/gconf/schemas/pager.schemas \
	%{_sysconfdir}/gconf/schemas/panel-compatibility.schemas \
	%{_sysconfdir}/gconf/schemas/panel-general.schemas \
	%{_sysconfdir}/gconf/schemas/panel-global.schemas \
	%{_sysconfdir}/gconf/schemas/panel-object.schemas \
	%{_sysconfdir}/gconf/schemas/panel-toplevel.schemas \
	%{_sysconfdir}/gconf/schemas/tasklist.schemas \
	%{_sysconfdir}/gconf/schemas/window-list.schemas \
	%{_sysconfdir}/gconf/schemas/workspace-switcher.schemas \
  > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/gconf/schemas/clock.schemas \
	%{_sysconfdir}/gconf/schemas/fish.schemas \
	%{_sysconfdir}/gconf/schemas/pager.schemas \
	%{_sysconfdir}/gconf/schemas/panel-compatibility.schemas \
	%{_sysconfdir}/gconf/schemas/panel-general.schemas \
	%{_sysconfdir}/gconf/schemas/panel-global.schemas \
	%{_sysconfdir}/gconf/schemas/panel-object.schemas \
	%{_sysconfdir}/gconf/schemas/panel-toplevel.schemas \
	%{_sysconfdir}/gconf/schemas/tasklist.schemas \
	%{_sysconfdir}/gconf/schemas/window-list.schemas \
	%{_sysconfdir}/gconf/schemas/workspace-switcher.schemas \
  > /dev/null || :
fi

%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%files -f %{gettext_package}.lang

%doc AUTHORS COPYING ChangeLog NEWS README

%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/gnome/panel
%{_datadir}/gnome/help/*
%{_datadir}/gnome-panelrc
%{_datadir}/idl/gnome-panel-2.0
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/omf/clock
%{_datadir}/omf/fish
%{_datadir}/omf/window-list
%{_datadir}/omf/workspace-switcher
%{_datadir}/man/man*/*
%{_bindir}/*
%{_libexecdir}/*
%{_libdir}/bonobo/servers/*.server
%{_libdir}/*.so.*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_sysconfdir}/gconf/schemas/*.entries

%files devel
%defattr(-, root, root)
%{_libdir}/pkgconfig/*
%{_includedir}/panel-2.0
%{_libdir}/*.so
%{_datadir}/gtk-doc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed May 14 2008 Wei-Lun Chao <bluebat@member.fsf.org> - 2.16.1-7.ossii
- Use ossii-panel-default-setup.entries as SOURCE1
- Rebuild for M6(CentOS5)

* Thu Nov 30 2006 Ray Strode <rstrode@redhat.com> - 2.16.1-6
Resolves: #216719
- don't show "Lock Screen" menu item if running as root (bug
  216719)

* Wed Nov 29 2006 Ray Strode <rstrode@redhat.com> - 2.16.1-5
Resolves: #212773
- don't ask user if they want to logout if they've set the
  preference not to 

* Thu Nov 16 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-4
- Fix previous patch and also include the fix
  for gnome bug 359707

* Tue Nov 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-3
- Fix copying of launchers by DND, bug 214334

* Wed Nov  8 2006 Ray Strode <rstrode@redhat.com> - 2.16.1-2
- fix chinese translation. Patch from Caius Chance
  <cchance@redhat.com> (bug 198134)

* Mon Nov  6 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1
- Update to 2.16.1 to fix bug 214045 

* Wed Nov  1 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-7
- Drop the Deployment Guide again, since we are adding a 
  Documentation submenu.  

* Tue Oct 31 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-6
- Add the Deployment Guide to the menus (#213191)

* Wed Oct 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-5
- Fix scripts according to packaging guidelines

* Wed Sep 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-4.fc6
- Copy translations for "Suspend" menu item from
  gnome-power-manager

* Tue Sep 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-3.fc6
- Fix some directory ownership issues
- Add a %%preun to uninstall gconf schemas
- Require hicolor-icon-theme (#204237)

* Mon Sep 18 2006 Soren Sandmann <sandmann@redhat.com> - 2.16.0-2.fc6
- Add patch to make the pager preference box deal with viewports when compiz
  is running. (Bug 205905).

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0

* Fri Sep  1 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-3.fc6
- Avoid unneeded wakeups in the clock applet (204862)

* Fri Aug 25 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-2.fc6
- Install omf files in the proper location (#201034)

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-1.fc6
- Update to 2.15.92
- Require pkgconfig in the -devel package
- Drop upstreamed patches
- Drop stale code from .spec

* Fri Aug 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.91-4.fc6
- Make clearing recent files work more than once

* Wed Aug 16 2006 Ray Strode <rstrode@redhat.com> - 2.15.91-3.fc6
- add more complete fix for bug 201439

* Fri Aug 15 2006 Alexander Larsson <alexl@redhat.com> - 2.15.91-2.fc6
- Also use beagle for search actions (#201424)

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.91-1.fc6
- Update to 2.15.91

* Wed Aug  9 2006 Ray Strode <rstrode@redhat.com> - 2.15.90-5
- remove suspend from logout dialog

-* Mon Aug  7 2006 Matthew Barnes <mbarnes@redhat.com> - 2.15.90-4
- Rebuild against evolution-data-server-1.7.91

* Mon Aug  7 2006 Ray Strode <rstrode@redhat.com> - 2.15.90-3
- fix double free in menu editor launcher (bug 201439)

* Fri Aug  4 2006 Ray Strode <rstrode@redhat.com> - 2.15.90-2
- move suspend to menu again
- remove autogenerated panel-typebuiltins.c from move-suspend-to-menu (caolanm)

* Fri Aug  4 2006 Ray Strode <rstrode@redhat.com> - 2.15.90-1
- update to 2.15.90

* Fri Jul 28 2006 Ray Strode <rstrode@redhat.com> - 2.14.2-8
- don't get stuck in infinite recursion loop from previous
  fix.  Patch by Fredric Crozat

* Wed Jul 26 2006 Ray Strode <rstrode@redhat.com> - 2.14.2-7
- don't try to talk to X if the connection is dead (bug 200149)

* Tue Jul 18 2006 Ray Strode <rstrode@redhat.com> - 2.14.2-6
- change "Suspend" to "Hibernate" where appropriate (bug 190791)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.14.2-5.1
- rebuild

* Mon Jun 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-5
- Add a patch to support transparent backgrounds in the
  notification area

* Wed Jun 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-4
- Update to new gnome-power-manager interface
- Conflict with gnome-power-manager < 2.15.3

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-3
- Add missing BuildRequires

* Mon May 29 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-2
- Update to 2.14.2
- Drop upstreamed patches

* Mon May 22 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-4
- Make it build in mock

* Fri May 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-3
- Close the about dialog

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-2
- Update to 2.14.1
- Update patches

* Mon Mar 13 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-1
- update to 2.14.0

* Tue Feb 28 2006 Karsten Hopp <karsten@redhat.de> 2.13.91-5
- Buildrequires: ORBit2-devel, which, libxml2-python, libX11-devel,
  libXt-devel, gnome-doc-utils, dbus-devel

* Mon Feb 27 2006 Ray Strode <rstrode@redhat.com> - 2.13.91-4
- ignore unknown options (bug 182734)

* Sun Feb 19 2006 Ray Strode <rstrode@redhat.com> - 2.13.91-3
- bring back shutdown menu item

* Wed Feb 15 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.91-2
- fix up the gnome-power-manager integration patch

* Mon Feb 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.91-1
- update to 2.13.91

* Mon Feb 13 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-3
- use beagle if available for search tool

* Sun Feb 12 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-2
- add first pass at gnome power manager integration

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13.90-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13.90-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 27 2006 Matthias Clasen <mclasen@redhat.com> 2.13.90-1
- Update to 2.13.90

* Fri Jan 20 2006 Matthias Clasen <mclasen@redhat.com> 2.13.5-2
- Remove "Switch user" button

* Tue Jan 17 2006 Matthias Clasen <mclasen@redhat.com> 2.13.5-1
- Update to 2.13.5

* Thu Jan  5 2006 Matthias Clasen <mclasen@redhat.com> 2.13.4-1
- Update to 2.13.4
- reinstate the desktop-menu-renaming

* Wed Dec 21 2005 Ray Strode <rstrode@redhat.com> 2.13.3-3
- add patch from cvs to fix crasher bug

* Tue Dec 20 2005 Matthias Clasen <mclasen@redhat.com> 2.13.3-2
- Rebuild against new libedataserver

* Thu Dec 15 2005 Matthias Clasen <mclasen@redhat.com> 2.13.3-1
- Update to 2.13.3
- Use sed rather than patch for po files

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Dec  2 2005 Matthias Clasen <mclasen@redhat.com> 2.13.2-1
- Update to 2.13.2

* Sun Nov 13 2005 John (J5) Palmieri <johnp@redhat.com> 2.12.1-7
- Fix patch to refrence about-fedora.desktop and not fedora-about.desktop

* Sun Nov 13 2005 John (J5) Palmieri <johnp@redhat.com> 2.12.1-6
- add about fedora menu item
- readd gnome-main-menu.png as fedora-logo now installs it to
  the Bluecurve theme

* Sat Nov 12 2005 Florian La Roche <laroche@redhat.com>
- remove gnome-main-menu.png as this is part of fedora-logos

* Tue Nov  1 2005 Ray Strode <rstrode@redhat.com> 2.12.1-4
- rename "Desktop" menu to "System" menu (bug 170812)

* Thu Oct 20 2005 Matthias Clasen  <mclasen@redhat.com> 2.12.1-3
- Add trash applet to the default setup

* Mon Oct 17 2005 Matthias Clasen  <mclasen@redhat.com> 2.12.1-2
- Change the "Cancel" button on the "add to" dialog to "Close"
 
* Thu Oct  6 2005 Matthias Clasen  <mclasen@redhat.com> 2.12.1-1
- Update to 2.12.1
- Update patches

* Fri Sep 30 2005 Mark McLoughlin <markmc@redhat.com> 2.12.0-3
- Remove hacks to add battery applet to default panel configuration
  where ACPI/APM is available (#169621) and GIMLET in CJK locales (#169430) 

* Wed Sep 14 2005 Jeremy Katz <katzj@redhat.com> - 2.12.0-2
- we have mozilla (and e-d-s) on ppc64 now

* Tue Sep  6 2005 Mark McLoughlin <markmc@redhat.com> 2.12.0-1
- Update to 2.12.0

* Mon Aug 22 2005 Mark McLoughlin <markmc@redhat.com> 2.11.92-1
- Update to 2.11.92.

* Tue Aug 16 2005 Mark McLoughlin <markmc@redhat.com> 2.11.91-3
- Rebuild for new cairo

* Wed Aug 10 2005 Mark McLoughlin <markmc@redhat.com> 2.11.91-2
- Fix "Adjust Date & Time" (#165586)

* Wed Aug 10 2005 Mark McLoughlin <markmc@redhat.com> 2.11.91-1
- Update to 2.11.91

* Wed Aug 10 2005 Mark McLoughlin <markmc@redhat.com> 2.11.90-2
- Bump gtk2 req to 2.7.1
- Remove bogus/stale reqs: libxslt-devel, startup-notification-devel,
  gnome-keyring, libpng-devel, fontconfig-devel, libtool, automake,
  autoconf ...

* Thu Aug  4 2005 Matthias Clasen <mclasen@redhat.com> 2.11.90-1
- New upstream version

* Tue Jul 26 2005 Mark McLoughlin <markmc@redhat.com> 2.11.4-3
- Rebuild

* Tue Jul 12 2005 Matthias Clasen <mclasen@redhat.com> 2.11.4-2
- Rebuild

* Fri Jul  8 2005 Matthias Clasen <mclasen@redhat.com> 2.11.4-1
- Update to 2.11.4

* Mon Jun 27 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-11
- Fix "panel doesn't notice new screen size" issue (bug #160439)

* Wed May 11 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-10
- Fix "dialogs pop up under panel dialogs" issue (bug #156425)

* Wed May  4 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-9
- Fix crash with "Recent Documents" menu (bug #156633)

* Mon May  2 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-8
- Update to new OpenOffice.org .desktop file locations in
  openoffice.org-1.9.97-3 (bug #156064)

* Wed Apr 27 2005 Mark McLoughlin <markmc@redhat.com> - 2.10.1-7
- Add patch to clamp the size of the icons on the panel at 48x48. Fixes
  "moved the panel to the side, can't move it back" issue (rh #141743)

* Wed Apr 27 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-6
- Reference the OpenOffice.org Impress .desktop file correctly

* Wed Apr 27 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-5
- Update launcher locations for OpenOffice.org icons

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 2.10.1-4
- silence %%post

* Mon Apr 25 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-3
- Add patch to make Wanda not use non-existent fortune
  command (rh #152948)

* Mon Apr 18 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-2
- Add the battery applet to the panel in %post if ACPI is
  available (bug #143828) 

* Mon Apr  4 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-1
- Update to 2.10.1

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 2.10.0-2
- Update the GTK+ theme icon cache on (un)install

* Mon Mar 14 2005 Matthias Clasen <mclasen@redhat.com> 2.10.0-1
- Update to 2.10.0
- Bump BuildRequires for libwnck
- Update patches

* Wed Mar  4 2005 Mark McLoughlin <markmc@redhat.com> 2.9.91-4
- Fix a BuildRequires

* Wed Mar  2 2005 Mark McLoughlin <markmc@redhat.com> 2.9.91-3
- Rebuild with gcc4

* Thu Feb 10 2005 Mark McLoughlin <markmc@redhat.com> - 2.9.91-2
- Require gnome-desktop 2.9.91

* Wed Feb  9 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.91-1
- Update to 2.9.91

* Mon Feb  7 2005 Mark McLoughlin <markmc@redhat.com> - 2.9.90-4
- Don't use --makefile-install-rule to install .entries files (#147112)

* Fri Feb  4 2005 Mark McLoughlin <markmc@redhat.com> - 2.9.90-3
- Update schemas list (#147112)

* Thu Feb  3 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.90-2
- Look for vendor-prefixed .desktop files

* Mon Jan 31 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.90
- Update to 2.9.90

* Fri Jan 28 2005 Florian La Roche <laroche@redhat.com>
- rebuild

* Thu Jan 27 2005 Jeremy Katz <katzj@redhat.com> - 2.8.1-8
- really disable e-d-s support

* Wed Jan 26 2005 David Malcolm <dmalcolm@redhat.com> - 2.8.1-7
- Make the evolution-data-server dependency optional at packaging time.
- Disable it for now to ease transition to Evolution 2.2 (bug #146283)

* Fri Nov 26 2004 Mark McLoughlin <markmc@redhat.com> - 2.8.1-6
- Add patch to fix launcher animation artifact (bug #136938)

* Fri Nov 12 2004 Mark McLoughlin <markmc@redhat.com> - 2.8.1-5
- Use /apps/panel for configuration so that homedir sharing with
  previous versions works reasonably well. This is the location
  upstream is using from GNOME 2.10 onwards.
- Install old pager.schemas and tasklist.schemas so that
  old configurations which reference the old schema names
  continue to work

* Mon Nov  1 2004 Mark McLoughlin <markmc@redhat.com> - 2.8.1-4
- Fix use-correct-applications-uri patch to not crash on
  ia64 - fix from Dave Malcolm (#136908)

* Mon Oct 18 2004  <jrb@redhat.com> - 2.8.1-3
- change redhat-web.desktop and redhat-email.desktop to be in /usr/share instead of using the menu path

* Fri Oct 15 2004 Matthias Clasen <mclasen@redhat.com>
- Make dropping non-ASCII uris work.  (#135874)

* Tue Oct 12 2004 Mark McLoughlin <markmc@redhat.com>
- Update to 2.8.1
- Change the default no. pager rows back to 1
- Add a new tamil translation

* Thu Oct  7 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0.1-3
- Add the Input Method Switcher applet in certain locales (#134659)

* Fri Oct  1 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0.1-2
- New panel layout from Bryan and Seth

* Wed Sep 29 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0.1-1
- Update to 2.8.0.1

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-2
- Remove the print launcher from the default setup - it was removed
  from the desktop-printing package a while ago 

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-1
- Update to 2.8.0

* Tue Aug 31 2004 Mark McLoughlin <markmc@redhat.com> 2.7.92.1-1
- Update to 2.7.92.1

* Mon Aug 30 2004 Mark McLoughlin <markmc@redhat.com> 2.7.92-1
- Update to 2.7.92

* Wed Aug 25 2004 Mark McLoughlin <markmc@redhat.com> 2.7.91.1-2
- Pipe gconftool stdout to /dev/null - fixes bug #130506

* Thu Aug 19 2004 Mark McLoughlin <markmc@redhat.com> 2.7.91.1-1
- Update to 2.7.91.1

* Wed Aug 18 2004 Mark McLoughlin <markmc@redhat.com> 2.7.91-1
- Update to 2.7.91

* Tue Aug 10 2004 Mark McLoughlin <markmc@redhat.com> - 2.7.90-1
- Update to 2.7.90 and remove a bunch of patches

* Mon Aug  2 2004 David Malcolm <dmalcolm@redhat.com> - 2.6.0-11
- added dependency on evolution-data-server and rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr 19 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-9
- Install battstat on the default panel on ppc too

* Mon Apr 19 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-8
- Only put the battstat applet on the default panel on ix86 (i.e. the
  platforms where apmd is built) - bug #121098

* Thu Apr 15 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-7
- Fix typo with laptop battery detection scriptlet - bug #120921

* Thu Apr 15 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-6
- Overwrite panel-compatibility.schemas with
  redhat-panel-backwards-compat-config.schemas and install that so
  it doesn't seem like we've forgotten panel-compatibility.schemas

* Thu Apr  8 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-5
- Fix problem with apm detection in %post on machines whose
  APM bios doesn't have battery lifetime support

* Wed Apr  7 2004 Mark McLoughlin <markmc@redhat.com> - 2.6.0-4
- Add patch to make the applications list in the run dialog work
  correctly with the new vfs menu module. Bug #118305.

* Mon Apr  5 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-3
- Fix "vailed to parse hour_format" warnings on install (bug #119956)

* Fri Apr  5 2004 Mark McLoughlin <markmc@redhat.com> - 2.6.0-2
- Add patches to fixup how we install the default setup
- Require GConf2-2.6.0-2 for gconftool-2 --load fix

* Wed Mar 31 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-1
- Update to 2.6.0

* Wed Mar 10 2004 Mark McLoughlin <markmc@redhat.com>
- Update to 2.5.92

* Wed Mar 03 2004 Mark McLoughlin <markmc@redhat.com> 2.5.91-2
- Use the main menu icon in the menu bar (#100407)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Mark McLoughlin <markmc@redhat.com> 2.5.91-1
- Update to 2.5.91
- Split off a -devel package (#108618)
- Add a scrollkeeper PreReq and scrollkeeper, intltool and
  libpng-devel BuildRequires. (#110928, Maxim Dzumanenko)

* Fri Feb 27 2004 Mark McLoughlin <markmc@redhat.com> 2.5.90-1
- Update to 2.5.90
- Resolve conflicts with the lockf patch and re-work slightly

* Thu Feb 19 2004 Jeremy Katz <katzj@redhat.com> - 2.5.3.1-6
- and again for real this time

* Wed Feb 18 2004 Jeremy Katz <katzj@redhat.com> - 2.5.3.1-5
- rebuild without e-d-s

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 06 2004 Dan Williams <dcbw@redhat.com> 2.5.3.1-3
- Add in file locking retries for egg-recent-model stuff, as with
   gedit.  Makes gnome-panel and other apps like gedit not fight
   for recent files list on NFS home directories

* Tue Jan 27 2004 Alexander Larsson <alexl@redhat.com> 2.5.3.1-2
- Add evolution-data-server dependency and rebuild

* Thu Oct  9 2003 Owen Taylor <otaylor@redhat.com> 2.4.0-2
- Look up the largest size available when picking default images for 
  panel stock icons (#106673)

* Thu Sep  4 2003 Alexander Larsson <alexl@redhat.com> 2.3.90-1
- update to 2.3.90
- Add backwards compat panel config schemas

* Wed Aug 27 2003 Alexander Larsson <alexl@redhat.com> 2.3.7-1
- update to 2.3.7
- patch the right icon for the main menu (#102672)
- PreReq a new gconf (#102530)

* Mon Aug 25 2003 Alexander Larsson <alexl@redhat.com> 2.3.6.2-4
- Don't lock all objects on panel
- use "make DESTDIR=... install" so gconf rules are right

* Mon Aug 18 2003 Alexander Larsson <alexl@redhat.com> 2.3.6.2-3
- Update the default panel setup handling to the new way

* Thu Aug 14 2003 Jonathan Blandford <jrb@redhat.com> 2.3.6.2-1
- remove the right .la files.

* Thu Aug 14 2003 Alexander Larsson <alexl@redhat.com> 2.3.6.2-1
- update for gnome 2.3

* Tue Jul 29 2003 Havoc Pennington <hp@redhat.com> 2.2.2.1-3
- disable gtk doc

* Mon Jul 28 2003 Havoc Pennington <hp@redhat.com> 2.2.2.1-3
- rebuild

* Wed Jul  9 2003 Alexander Larsson <alexl@redhat.com> 2.2.2.1-2
- Fix redhat menu icon

* Mon Jul  7 2003 Havoc Pennington <hp@redhat.com> 2.2.2.1-1
- 2.2.2.1
- remove memleaks patch, now upstream
- remove applet-sm patch now upstream
- remove "null" patch, now upstream
- remove recent-monitor patch now upstream
- remove notification area crash fix, now upstream

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com> 2.2.0.1-8
- Rebuild with an updated libtool to fix #84742

* Thu Feb 20 2003 Havoc Pennington <hp@redhat.com> 2.2.0.1-6
- fix memleaks, #84489 #84467
- use icon theme for button widgets instead of stock ID #82301

* Fri Feb 14 2003 Havoc Pennington <hp@redhat.com> 2.2.0.1-5
- disable session management for all applets

* Tue Feb 11 2003 Havoc Pennington <hp@redhat.com> 2.2.0.1-4
- fix #83683 for real, very embarassing bug in the end

* Tue Feb 11 2003 Havoc Pennington <hp@redhat.com> 2.2.0.1-3
- add assertions to try to narrow down #83683 more

* Tue Feb 11 2003 Tim Waugh <twaugh@redhat.com> 2.2.0.1-2
- Fix notification area crash (bug #83683).

* Wed Feb  5 2003 Havoc Pennington <hp@redhat.com> 2.2.0.1-1
- 2.2.0.1

* Mon Feb  3 2003 Matt Wilson <msw@redhat.com> 2.2.0-2
- added gnome-panel-2.1.90.1-null.patch to avoid segv on 64 bit platforms
  #82978

* Mon Feb  3 2003 Alexander Larsson <alexl@redhat.com> 2.2.0-1
- Update to 2.2.0
- Add patch to disable monitoring in recent-files, since it made you not able to unmount cds.

* Thu Jan 30 2003 Matt Wilson <msw@redhat.com> 2.1.90.1-6
- disable optimizations on x86_64 to work around gcc bug

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan 13 2003 Jonathan Blandford <jrb@redhat.com>
- put the control-center second

* Sat Jan 11 2003 Havoc Pennington <hp@redhat.com>
- fix the extra separator left when we lack screenshot menuitem

* Fri Jan 10 2003 Havoc Pennington <hp@redhat.com>
- fix the clock

* Thu Jan  9 2003 Havoc Pennington <hp@redhat.com>
- remove enhanced-errors patch now upstream
- change how we're doing the laptop-specific config to avoid cut-and-paste
- update clock-addons patch
- remove hardcoded change to default panel icon size, we'll put it in bluecurve
  theme.
- run xscreensaver fortune instead of just "fortune" from the fish
- add printer icon to panel

* Wed Jan  8 2003 Havoc Pennington <hp@redhat.com>
- 2.1.90.1

* Mon Dec 16 2002 Tim Powers <timp@redhat.com> 2.1.4-4
- rebuild

* Mon Dec 16 2002 Havoc Pennington <hp@redhat.com>
- rebuild

* Sat Dec 14 2002 Havoc Pennington <hp@redhat.com>
- require gnome-desktop 2.1.4
- include datadir/fish

* Fri Dec 13 2002 Havoc Pennington <hp@redhat.com>
- 2.1.4

* Mon Dec  2 2002 Havoc Pennington <hp@redhat.com>
- 2.1.3
- build req startup-notification-devel

* Wed Nov 13 2002 Havoc Pennington <hp@redhat.com>
- 2.1.2
- system tray is now in the main gnome-panel package

* Wed Oct 23 2002 Havoc Pennington <hp@redhat.com>
- 2.0.10
- remove memleaks-and-clock-format patch, should be upstream
- remove WIN_POS_MOUSE purge, done upstream

* Mon Oct 14 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix postun script

* Tue Oct  8 2002 Havoc Pennington <hp@redhat.com>
- 2.0.9 with menu edit stuff
- system-tray-applet 0.15 that doesn't crash all the time
- merge/remove patches as appropriate

* Wed Aug 28 2002 Owen Taylor <otaylor@redhat.com>
- Fix problem with "hold down print screen" (71432)

* Tue Aug 27 2002 Jonathan Blandford <jrb@redhat.com>
- panel-properties OnlyShowIn=GNOME;
- somehow the po file got screwed up.  Works now
- update po files

* Sun Aug 25 2002 Havoc Pennington <hp@redhat.com>
- fix from #71762 for clock applet popdown key
- no WIN_POS_MOUSE fixes #72167
- fix for #72540 from George

* Wed Aug 21 2002 Havoc Pennington <hp@redhat.com>
- system tray applet 0.11 with a small memleak fix and a couple translations

* Thu Aug 15 2002 Jonathan Blandford <jrb@redhat.com>
- menu tweaks

* Wed Aug 14 2002 Tim Powers <timp@redhat.com>
- bump release

* Wed Aug 14 2002 Preston Brown <pbrown@redhat.com>
- put battery applet on panel for laptops (#67296)

* Mon Aug 12 2002 Havoc Pennington <hp@redhat.com>
- 2.0.6 final from gnome 2.0.1
- remove gnome-panel-screenshot patch now upstream

* Thu Aug  8 2002 Jonathan Blandford <jrb@redhat.com>
- new system-tray-applet version
- Fix gnome-panel-screenshot

* Tue Aug  6 2002 Havoc Pennington <hp@redhat.com>
- 2.0.4
- replace gnome-logo-icon-transparent.png with redhat-main-menu.png
  for the foot menu

* Fri Aug  2 2002 Havoc Pennington <hp@redhat.com>
- fix desktop (logout/lock) menu item location
  in Alt+F1 and in new menu applets
- remove Screenshot... menu item

* Fri Aug  2 2002 Havoc Pennington <hp@redhat.com>
- move around default applets, remove some of them
- system tray 0.9
- change default menu flags
- blow unpackaged files out of build root

* Wed Jul 31 2002 Havoc Pennington <hp@redhat.com>
- 2.0.3
- own libexecdir stuff

* Thu Jul 25 2002 Havoc Pennington <hp@redhat.com>
- new system tray that's prettier and doesn't clip the icon

* Wed Jul 24 2002 Havoc Pennington <hp@redhat.com>
- system tray 0.7 that doesn't crash on startup
- get Mozilla desktop file right so we get web browser launcher

* Wed Jul 24 2002 Havoc Pennington <hp@redhat.com>
- system tray 0.6 with server file fixed (work dammit)

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- tweak applet positions but I think it's just broken
- system tray 0.5 moved back to libdir not libexecdir

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- remove ltmain.sh hack
- new system-tray-applet that works

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- put office suite stuff on the panel

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- 2.0.2.90 cvs snap

* Wed Jul 10 2002 Havoc Pennington <hp@redhat.com>
- update the clock patch to be a little smarter in a couple ways

* Thu Jun 27 2002 Owen Taylor <otaylor@redhat.com>
- Fix problem where system tray applet was being looked for in /unst
- Fix a crash in the system tray applet

* Wed Jun 26 2002 Owen Taylor <otaylor@redhat.com>
- Fix typo in the pt_BR translation that was causing GConf problems

* Mon Jun 24 2002 Havoc Pennington <hp@redhat.com>
- add the system tray applet
- add system tray applet by default
- add more launcher by default

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Havoc Pennington <hp@redhat.com>
- use correct gettext package name, and add check for missing translations

* Mon Jun 17 2002 Havoc Pennington <hp@redhat.com>
- add the calendar and configuration patch 

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- 2.0.0
- add control center desktop file to file list
- add gnome-panelrc to file list
- try fixing panel size (blind, no text box at home)

* Tue Jun 11 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue Jun 11 2002 Havoc Pennington <hp@redhat.com>
- updates to default configuration

* Tue Jun 11 2002 Havoc Pennington <hp@redhat.com>
- fix schemas installation

* Tue Jun 11 2002 Havoc Pennington <hp@redhat.com>
- unset old panel schemas when installing new ones
- put in a broken panel config to see errors about
- add a patch to give some decent error messages about what's wrong
  with the default panel config

* Sun Jun 09 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Sun Jun  9 2002 Havoc Pennington <hp@redhat.com>
- don't provide/obsolete gnome-core

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed Jun  5 2002 Havoc Pennington <hp@redhat.com>
- 1.5.24
- ldconfig

* Mon Jun 03 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Fri May 31 2002 Havoc Pennington <hp@redhat.com>
- 1.5.23

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- 1.5.22
- provide gnome-core
- add a bunch of extra build requires so build system 
  won't get confused

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 1.5.19

* Fri Apr 19 2002 Havoc Pennington <hp@redhat.com>
- add the keep-libtool-from-relinking hack so 
  we get the gen util applet

* Fri Apr 19 2002 Havoc Pennington <hp@redhat.com>
- obsoletes gnome-core-devel
- include libdir/*.so

* Fri Apr 19 2002 Havoc Pennington <hp@redhat.com>
- get libpanel-applet in the package

* Tue Apr 16 2002 Havoc Pennington <hp@redhat.com>
- Initial build.
