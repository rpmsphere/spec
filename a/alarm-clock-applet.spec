Name:           alarm-clock-applet
Version:        0.3.4
Release:        6.1
Summary:        An alarm-clock for use with the GNOME panel
License:        GPL-2.0
Group:          Productivity/Office/Other
URL:            https://launchpad.net/alarm-clock/
Source:         https://launchpad.net/alarm-clock/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-icon-theme)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(unique-1.0)
Requires:       gnome-icon-theme

%description
Alarm Clock is a fully-featured alarm clock for your GNOME panel.
It's easy to use yet powerful with support for multiple repeatable
alarms, as well as snoozing and a flexible notification system.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%__make %{?_smp_mflags} CFLAGS+="-Wno-format-y2k -Wno-format-nonliteral -Wl,--allow-multiple-definition"

%install
%makeinstall

%files
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/alarm-clock-applet
%{_datadir}/alarm-clock-applet
%{_datadir}/applications/alarm-clock-applet.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_sysconfdir}/gconf/schemas/alarm-clock.schemas
%exclude %{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/locale/*/LC_MESSAGES/alarm-clock-applet.mo

%changelog
* Wed Jan 17 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.4
- Rebuilt for Fedora
* Mon Mar 11 2013 dimstar@opensuse.org
- Fix alarm-clock-applet-gstreamer1.patch: gconfaudiosink and
  gconfvideosink also no longer exist in GStreamer 1.0. Replace
  them accordingly with autoaudiosink and autovideosink.
* Fri Mar  1 2013 dimstar@opensuse.org
- Port to GStreamer 1.0:
  + Add alarm-clock-applet-gstreamer1.patch: do the port
  + Add gnome-common BuildRequires and call to autogen.sh, as above
    patch touches the build system.
  + Replace pkgconfig(gstreamer-0.10) BuildRerquires with
    pkgconfig(gstreamer-1.0)
- Add pkgconfig(libxml-2.0) BuildRequires: configure verifies for
  its presence, but due to the switch to GStreamer 1.0 it is no
  longer pulled in.
* Wed Jun  6 2012 badshah400@gmail.com
- Update to version 0.3.3:
  + Bugs fixed:
  - lp#290733: Automatically detect daylight savings time
  - lp#800635: Let the WM decide the initial position of the
    list window
  - lp#823585: Check that media player was created successfully
  - lp#908636: Don't show notifications when alarms are
    stopped/snoozed
  - lp#885059: Update timestamp when type is changed for active
    alarms
  - lp#977110: Use segment seeks to prevent playback delays when
    looping
  - lp#824337: Enable alarm when closing the Edit alarm dialog
- Use upstream tarball (.tar.gz) as source.
* Sat Sep 17 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
* Mon May 16 2011 dimstar@opensuse.org
- Replace -devel BuildRequires with pkgconfig() ones:
  + Old: gconf2-devel, glib2-devel, gnome-icon-theme,
    gstreamer-0_10-devel, gtk2-devel, libnotify-devel,
    libunique-devel.
  + New: gconf-2.0, glib-2.0, gnome-icon-theme, gstreamer-0.10,
    gtk+-2.0, libnotify, unique-1.0.
- Remove explicit pkg-config BuildRequires: we know it will be
  brought in with pkgconfig(glib-2.0), for instance.
* Mon Mar 21 2011 dimstar@opensuse.org
- Update to version 0.3.2:
  + Add support for application indicators
  + Countdown label for application indicator
  + New status icon indicating triggered alarms
  + Bugs fixed:
  - lp#565302: Add countdown label (for application indicator)
  - lp#610632: Create ~/.config/autostart if it doesn't exist
  - lp#671962: Add support for libnotify 0.7
  - lp#682999: Properly stop triggered alarms that are not
    playing sound
  - lp#704956: Add support for application indicators
  - lp#706832: Clicking on status icon should bring up list
    instead of snoozing.
* Sat Feb 12 2011 vuntz@opensuse.org
- Add missing relevant macros in %%post/%%postun:
  + %%desktop_database_post/postun because the package ships at
    least one desktop file.
- Pass %%{?no_lang_C} to %%find_lang so that english documentation
  can be packaged with the program, and not in the lang subpackage.
- Change Requires of lang subpackage to Recommends.
* Sun Sep  5 2010 dimstar@opensuse.org
- Use icon cache macros on openSUSE 11.4+.
* Wed Aug 25 2010 vuntz@opensuse.org
- Split a lang subpackage.
- Do not reinstall .desktop file, nor replace categories (just
  append TimeUtility).
- Remove the gtk-update-icon-cache call in %%post for now: it will
  be fixed another way.
* Mon Aug 23 2010 badshah400@gmail.com
- Remove unnecessary Requires: from spec file
* Fri Aug 20 2010 badshah400@gmail.com
- spec file cleanup
* Thu Aug 19 2010 badshah400@gmail.com
- Intital package (upstream version 0.3.1)
