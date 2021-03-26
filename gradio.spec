Name:           gradio
Version:        7.2
Release:        2.1
Summary:        GTK3 app for finding and listening to internet radio stations
License:        GPL-3.0+
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/haecker-felix/gradio
Source:         https://github.com/haecker-felix/gradio/archive/v%{version}.tar.gz#/Gradio-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vapigen) >= 0.16

%description
Gradio is a native GTK application. It lets you browse, search and find radio
stations, as well as listen to them, without needing to use a browser or enter
an internet radio stream URL. The application uses the Community Radio Browser
website for its database backend.

%prep
%setup -q -n Gradio-%{version}

%build
%{meson}
%{meson_build}

%install
%{meson_install}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/gradio
%{_datadir}/appdata/de.haeckerfelix.gradio.appdata.xml
%{_datadir}/applications/de.haeckerfelix.gradio.desktop
%{_datadir}/icons/hicolor/*/apps/de.haeckerfelix.gradio.png
%{_datadir}/icons/hicolor/scalable/apps/de.haeckerfelix.gradio.svg
%{_datadir}/icons/hicolor/symbolic/apps/de.haeckerfelix.gradio-symbolic.svg
%{_datadir}/glib-2.0/schemas/de.haeckerfelix.gradio.gschema.xml
%{_datadir}/dbus-1/services/de.haeckerfelix.gradio.service
%{_datadir}/gnome-shell/search-providers/*
%{_datadir}/locale/*/LC_MESSAGES/gradio.mo

%changelog
* Mon Nov 05 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 7.2
- Rebuild for Fedora
* Mon Jan 22 2018 mvetter@suse.com
- Update to version 7.1:
  * Simplified filter options
  * Optionally display technical information
  * Filter by tags
  * Tags can be edited
  * Updated translations
  * Some design tweaks
  * Show detailed export status (m3u)
  * Access to radio-browser.info database
* Sat Dec 16 2017 mvetter@suse.com
- Update to version 7.0:
  * The "Discover" section is back
  * Merged "Add" and "Search" page
  * New unified library view
  * Library can now be exported as M3U playlist
  * New first launch experience
  * Connection to the database is now encrypted
  * Collections can now be renamed
  * Stations can now be removed from collections
  * Redesigned selection toolbar
  * Redesigned application menu
  * Redesigned collections popover
  * Some performance and memory usage improvements
* Tue Sep 26 2017 mvetter@suse.com
- Update to version 6.0.2:
  * Add GNOME Shell search provider
  * Bugfix #213[2] cannot play m3u8 stations
  * Bugfix #214[3] application is not translated
* Mon Sep 18 2017 mvetter@suse.com
- Update to versoin 6.0.1:
  * New keyboard shortcuts
  * New translations
  * bugfix #208[1] Duplicated appmenu on non GNOME desktops
  * bugfix #209[2] No title is displayed if it contains an & sign
- Remove gradio-add-missed-translation.patch
* Sun Sep 10 2017 zaitor@opensuse.org
- Update to version 6.0
- Switch to meson build system following upstream port.
- Add gradio-add-missed-translation.patch: Add translation already
  in place in tarball, but missing in LINGUAS file.
* Sun Feb  5 2017 mailaender@opensuse.org
- update to version 5.0
* Sat Jul 30 2016 mailaender@opensuse.org
- initial packaging of version 4.0.1
