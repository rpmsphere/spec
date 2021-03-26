%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary: Constructionist learning platform
Name:    sugar
Version: 0.98.8
Release: 3%{?dist}
URL:     http://sugarlabs.org/
License: GPLv2+
Group:   User Interface/Desktops
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.bz2
Patch0:  sugar-gnomekeyring.patch
Patch1:  sugar-background.patch

BuildRequires: gettext
BuildRequires: GConf2-devel
BuildRequires: gobject-introspection
BuildRequires: gtk3-devel
BuildRequires: gtksourceview3-devel
BuildRequires: intltool
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig
BuildRequires: python

Requires: dbus-x11
Requires: ethtool
Requires: gnome-keyring-pam
Requires: gstreamer-plugins-espeak
Requires: gstreamer-python
Requires: metacity
Requires: NetworkManager
Requires: openssh
Requires: gtksourceview3
Requires: python-telepathy
Requires: python-xklavier
Requires: sugar-artwork
Requires: sugar-toolkit
Requires: sugar-toolkit-gtk3
Requires: telepathy-mission-control
Requires: upower
Requires: xdg-user-dirs
Requires: gvfs
Requires: libwnck3

BuildArch: noarch

%description
Sugar provides simple yet powerful means of engaging young children in the 
world of learning that is opened up by computers and the Internet. With Sugar,
even the youngest learner will quickly become proficient in using the 
computer as a tool to engage in authentic problem-solving.  Sugar promotes 
sharing, collaborative learning, and reflection, developing skills that help 
them in all aspects of life. 

Sugar is also the learning environment for the One Laptop Per Child project. 
See http://www.laptop.org for more information on this project.

%package emulator
Summary: The emulator for the Sugar Learning Platform
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: xorg-x11-server-Xephyr
# for xdpyinfo
Requires: xorg-x11-utils

%description emulator
The emulator let's you test and debug sugar. For example it allows you to run 
multiple instances of sugar. 

%package cp-all
Summary: All control panel modules 
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Requires: %{name}-cp-datetime %{name}-cp-frame %{name}-cp-language %{name}-cp-background
Requires: %{name}-cp-modemconfiguration %{name}-cp-network %{name}-cp-power %{name}-cp-keyboard
# Currently broken
# Requires: %{name}-cp-updater

%description cp-all
This is a meta package to install all Sugar Control Panel modules

%package cp-datetime
Summary: Sugar Date and Time control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-datetime
This is the Sugar Date and Time settings control panel

%package cp-frame
Summary: Sugar Frame control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-frame
This is the Sugar Frame settings control panel

%package cp-keyboard
Summary: Sugar Keyboard control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-keyboard
This is the Sugar Keyboard settings control panel

%package cp-language
Summary: Sugar Language control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-language
This is the Sugar Language settings control panel

%package cp-modemconfiguration
Summary: Sugar Modem configuration control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-modemconfiguration
This is the Sugar Modem configuration control panel

%package cp-network
Summary: Sugar Network control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-network
This is the Sugar Network settings control panel

%package cp-power
Summary: Sugar Power control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-power
This is the Sugar Power settings control panel

%package cp-updater
Summary: Sugar Activity Update control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-updater
This is the Sugar Activity Updates control panel

%package cp-background
Summary: Sugar Background control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-background
This is the Sugar Background control panel


%prep
%setup -q
%patch0 -p1 -b .keyring
%patch1 -p1
sed -i '/exit 3/d' bin/sugar*

%build
autoreconf
%configure
make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=%{buildroot}
mkdir %{buildroot}/%{_datadir}/sugar/activities
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%find_lang %{name}

%post
if (update-mime-database -v &> /dev/null); then
  update-mime-database "%{_datadir}/mime" > /dev/null
fi

export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
	%{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :
fi

%postun
if (update-mime-database -v &> /dev/null); then
  update-mime-database "%{_datadir}/mime" > /dev/null
fi

%post emulator
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%preun emulator
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files -f %{name}.lang
%doc COPYING README

%config %{_sysconfdir}/dbus-1/system.d/nm-user-settings.conf
%config %{_sysconfdir}/gconf/schemas/sugar.schemas

%dir %{_datadir}/sugar
%dir %{_datadir}/sugar/activities
%{_datadir}/sugar/*

%{python_sitelib}/*

%{_datadir}/xsessions/sugar.desktop

%{_bindir}/*
%exclude %{_bindir}/sugar-emulator
%dir %{_datadir}/sugar/extensions/cpsection/
%exclude %{_datadir}/sugar/extensions/cpsection/[b-z]*
%{_datadir}/sugar/extensions/cpsection/about*

%{_datadir}/mime/packages/sugar.xml

%files emulator
%{_bindir}/sugar-emulator
%{_datadir}/applications/sugar-emulator.desktop
%{_datadir}/icons/hicolor/scalable/apps/sugar-xo.svg

%files cp-all

%files cp-datetime
%{_datadir}/sugar/extensions/cpsection/datetime

%files cp-frame
%{_datadir}/sugar/extensions/cpsection/frame

%files cp-keyboard
%{_datadir}/sugar/extensions/cpsection/keyboard

%files cp-language
%{_datadir}/sugar/extensions/cpsection/language

%files cp-modemconfiguration
%{_datadir}/sugar/extensions/cpsection/modemconfiguration

%files cp-network
%{_datadir}/sugar/extensions/cpsection/network

%files cp-power
%{_datadir}/sugar/extensions/cpsection/power

%files cp-updater
%{_datadir}/sugar/extensions/cpsection/updater

%files cp-background
%{_datadir}/sugar/extensions/cpsection/background

%changelog
* Fri Jun 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> 0.98.8-3
- Add background patch

* Sun May 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.8-2
- Update default control panels

* Fri May 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.8-1
- Sugar 0.98.8 stable release

* Fri Apr 12 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.7-1
- Sugar 0.98.7 stable release

* Fri Mar 22 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.6-1
- Sugar 0.98.6 stable release

* Fri Mar  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.5-1
- Sugar 0.98.5 stable release

* Sat Feb 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.4-1
- Sugar 0.98.4 stable release

* Fri Dec 21 2012 Simon Schampijer <simon@laptop.org> - 0.98.3-1
- Sugar 0.98.3 stable release

* Tue Dec 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.2-1
- Sugar 0.98.2 stable release

* Mon Dec 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-1
- Sugar 0.98.1 stable release

* Thu Nov 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.0-1
- Sugar 0.98.0 stable release

* Tue Nov 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.13-1
- 0.97.13 devel release

* Sat Nov 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.12-1
- 0.97.12 devel release 

* Sat Nov 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.11-1
- 0.97.11 devel release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.10-1
- 0.97.10 devel release

* Thu Oct 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.9-1
- 0.97.9 devel release

* Tue Oct 16 2012 Daniel Drake <dsd@laptop.org> 0.97.8-1
- 0.97.8 devel release

* Thu Oct 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.7-1
- 0.97.7 devel release

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.6-1
- 0.97.6 devel release

* Thu Oct  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.5-2
- Split out Control Panels to sub packages
- Update gnome-keyring patch. RHBZ 862581
- Add patch to update build dependencies

* Thu Sep 27 2012 Daniel Drake <dsd@laptop.org> - 0.97.5-1
- New development release

* Thu Sep 20 2012 Daniel Drake <dsd@laptop.org> - 0.97.4-1
- New development release

* Thu Sep 13 2012 Daniel Drake <dsd@laptop.org> - 0.97.3-1
- New development release

* Tue Aug 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.2-1
- 0.97.2 devel release

* Tue Aug 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.1-1
- 0.97.1 devel release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.3-1
- 0.96.3 stable release

* Tue Jun  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.2-1
- 0.96.2 stable release

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-2
- Add patch to create gnome keyring if it doesn't exist

* Mon Apr 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-1
- 0.96.1 stable release

* Tue Apr 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.0-1
- 0.96.0 stable release

* Thu Apr 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.7-1
- devel release 0.95.7

* Mon Mar 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.6-1
- devel release 0.95.6

* Wed Mar 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.5-1
- devel release 0.95.5

* Tue Mar  6 2012 Daniel Drake <dsd@laptop.org> - 0.95.4-2
- Add dependency on sugar-toolkit-gtk3 (needed to launch activities)

* Thu Feb  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.4-1
- devel release 0.95.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-3
- Drop premature sugar-base obsoletion

* Thu Dec 22 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-2
- Obsolete sugar-base

* Wed Dec 21 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-1
- devel release 0.95.3

* Wed Nov 16 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-1
- devel release 0.95.2

* Tue Oct 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.1-1
- devel release 0.95.1

* Wed Oct 19 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.94.1-1
- 0.94.1 stable release

* Thu Sep 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.94.0-1
- 0.94.0 stable release

* Tue Sep 20 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.93.5-1
- 0.93.5 dev release

* Wed Sep  7 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.93.4-1
- 0.93.4 dev release

* Tue Sep  6 2011 Daniel Drake <dsd@laptop.org> - 0.93.3-2
- Updated NetworkManager-0.9 support patch

* Fri Aug 26 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.93.3-1 
- 0.93.3 dev release

* Fri Aug 19 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.93.2-2
- Add xdg-user-dirs dep

* Fri Aug 19 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.93.2-1 
- 0.93.2 dev release

* Mon Jul 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.4-1
- 0.92.4

* Fri Jul  8 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.3-1
- 0.92.3

* Thu Jun  9 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.2-1
- 0.92.2

* Wed Jun  8 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.1-6
- Add an extra NM patch

* Tue May 24 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.1-5
- Add patch for NM-0.9 (thanks to John Dulaney for his assistance)

* Tue May 17 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.1-4
- Drop previous patch, in wider testing it breaks more than it fixes

* Mon Apr 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.1-3
- Add patch to fix jabber online status b.sl.o #2483

* Mon Apr 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.1-2
- Fix the sugar desktop icon in emulator

* Thu Apr 14 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.1-1
- 0.92.1 release

* Tue Mar 01 2011 Simon Schampijer <simon@laptop.org> - 0.92.0-2
- added upower (battery status indicator) and ConsoleKit
  (logged users information) as runtime dependencies

* Mon Feb 28 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.0-1
- 0.92.0 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.3-4
- Drop patch to enable sugar-settings-manager

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.3-3
- bump build

* Mon Nov  1 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.3-2
- add gnome-keyring-pam as dep to fix prompt

* Fri Oct 15 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.3-1
- 0.90.3 release

* Tue Oct  5 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.2-1
- 0.90.2 release

* Fri Oct  1 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.1-1
- 0.90.1 stable release

* Wed Sep 29 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.0-1
- 0.90.0 stable release

* Tue Sep 21 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.10-1
- New upstream devel 0.89.10 release

* Sat Sep 18 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.9-1
- New upstream devel 0.89.9 release

* Fri Sep  3 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.8-1
- New upstream devel 0.89.8 release

* Tue Aug 31 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.7-1
- New upstream devel 0.89.7 release

* Mon Aug 30 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.6-1
- New upstream devel 0.89.6 release

* Fri Aug 27 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.5-1
- New upstream devel 0.89.5 release

* Tue Aug 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.4-1
- New upstream devel 0.89.4 release

* Wed Aug 17 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.3-1
- New upstream devel 0.89.3 release

* Wed Aug  4 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.2-1
- New upstream devel 0.89.2 release

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.89.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 14 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.1-1
- New upstream devel 0.89.1 release

* Thu Jun  3 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.88.1-1
- New upstream stable 0.88.1 release

* Sat May 30 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.88.0-3
- Bump build

* Sat May 30 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.88.0-2
- Clean up some descriptions 

* Tue Mar 20 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.88.0-1
- New upstream stable 0.88.0 release

* Wed Mar 10 2010 Sebastian Dziallas <sebastian@when.com> - 0.87.8-1
- New upstream release

* Tue Mar 02 2010 Sebastian Dziallas <sebastian@when.com> - 0.87.6-1
- New upstream release

* Wed Feb 17 2010 Sebastian Dziallas <sebastian@when.com> - 0.87.5-1
- New upstream release

* Tue Feb 16 2010 Sebastian Dziallas <sebastian@when.com> - 0.87.4-2
- Enable sugar-settings-manager support

* Thu Feb 11 2010 Sebastian Dziallas <sebastian@when.com> - 0.87.4-1
- New upstream release

* Tue Jan 12 2010 Sebastian Dziallas <sebastian@when.com> - 0.87.3-1
- New upstream release

* Sat Jan  9 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.87.2-2
- Updated to the new python sysarch spec file reqs

* Wed Dec 23 2009 Sebastian Dziallas <sebastian@when.com> - 0.87.2-1
- New upstream release

* Tue Dec 01 2009 Sebastian Dziallas <sebastian@when.com> - 0.87.1-1
- New upstream release
- Make this noarch again

* Fri Nov 20 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.86.3-5
- One more try

* Fri Nov 20 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.86.3-4
- Create %{_datadir}/sugar/activities

* Fri Nov 20 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.86.3-3
- Own %{_datadir}/sugar/activities. Fixes #532796

* Wed Oct 21 2009 Sebastian Dziallas <sebastian@when.com> - 0.86.3-2
- add missing file to appropriate section

* Wed Oct 21 2009 Sebastian Dziallas <sebastian@when.com> - 0.86.3-1
- Sporadic freezes while scrolling journal #1506
- Suppress race condition with Journal appearing on sugar startup #1373
- Alt+Space not working to show/hide the tray #1476

* Sun Sep 27 2009 Sebastian Dziallas <sebastian@when.com> - 0.86.0-1
- New upstream release

* Fri Sep 18 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.8-2
- Package /usr/share/applications/sugar-emulator.desktop

* Fri Sep 18 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.8-1
- New upstream release

* Fri Sep 11 2009 Simon Schampijer <simon@schampijer.de> - 0.85.7-2
- add python-xklavier dependency

* Fri Sep 11 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.7-1
- New upstream release

* Wed Sep 02 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.5-1
- New upstream release

* Wed Aug 26 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.4-1
- New upstream release

* Sun Aug 02 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.3-1
- New upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.85.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.2-1
- New upstream release

* Thu Apr 16 2009 Simon Schampijer <simon@schampijer.de> - 0.84.6-1
- Only update the connections file when the AP changes state #756
- Initialize the ResultSet after the widget changes size #733

* Wed Apr 08 2009 Simon Schampijer <simon@schampijer.de> - 0.84.5-1
- Remove fixed width from speaker palette #719
- Correctly close the input stream in file transfers #682

* Mon Apr 06 2009 Simon Schampijer <simon@schampijer.de> - 0.84.4-1
- new german and spanish translations

* Mon Apr 06 2009 Simon Schampijer <simon@schampijer.de> - 0.84.3-1
- If user updates an activity installed in /usr/share/activities, both versions remain installed #707
- Sometimes an activity will not start #461
- Grey out the erase option if an activity bundle cannot be erased #620
- AP: Do not write timestamp when not managed to connect #623
- Correct date in 'About my Computer' CP section #639
- Make Jukebox the default activity for ogg-vorbis #423
- Find an available icon for displaying the removable device #627
- CP: Disallow the user from selecting any fallbacks if English (USA) is 
selected (#slo:561)
- Call *mount_finish when the callback is called #326
- Add full licence to data dir #357
- The logout option is available by default
- Resume from home is duplicating activity instances again #600

* Wed Apr 01 2009 Simon Schampijer <simon@schampijer.de> - 0.84.1-4.20090401git4232758da5
- git snapshot

* Tue Mar 24 2009 Simon Schampijer <simon@schampijer.de> - 0.84.1-3.20090324gite16cf854aa
- rebuild without the logout patch

* Tue Mar 24 2009 Simon Schampijer <simon@schampijer.de> - 0.84.1-2.20090324gite16cf854aa
- git snapshot

* Sun Mar 22 2009 Simon Schampijer <simon@schampijer.de> - 0.84.1-1
- Update to latest NM-User config file (same as nm-applet)
- Fix nondeterministic denials for no-interface messages #575
  (Thanks to Dan Williams and Colin Walters for their assistance
  in spotting this. upstream bug fdo #18961)
- Draw the rounding box inside the icon bounds (benzea) #567
- Add Dismiss option to the palette of finished transfers #484
- Resume-by-default uses open with, not just open #547
- Set Pippy as the default for opening python files #287
- Remove duplicates from the activities submenu #497
- Remove transfer icon from frame when the local user cancels it #483
- Restore the icon size after a layout change #157
- enable logout option

* Wed Mar 18 2009 Simon Schampijer <simon@schampijer.de> - 0.84.0-2.20090318gitd3a0839735
- git snapshot

* Tue Mar 03 2009 Simon Schampijer <simon@schampijer.de> - 0.84.0-1
- Focus rectangle corners should be rounded #406
- Restore minimal .xol support #459
- Check the activity version and replace an older version upon download #464
- Friendstray: icon reacting to right click #441
- Network device icons don't react on right click #463
- Don't open a launcher window when that activity is already running #426
- Fall back to application-octet-stream for unknown types #458
- Show a generic icon for clippings, if available #454
- Don't add_bundle on activity dir change when installed already #442
- Make mute sound code togglable
- Keyhandler: Map XF86Search to the journal search
- Keyhandler: Catch all exceptions (thanks to Sascha Silbe)
- Give time for exit to execute when closing the emulator #435
- Dont hardcode the maximum amount of entries to cache in the journal #72
- Add standard Print shortcut to take a screenshot
-  Use keyboard specific keys to set the volume #430
- Update to new DBus policy #307
- Fix palette appearance on right-click #403
- Switch to existing instance of an activity if it's already running #410

* Fri Feb 27 2009 Simon Schampijer <simon@schampijer.de> - 0.83.8-3.20090227gitae381ce5b6
- git snapshot
- Don't add_bundle on activity dir change when installed already #442
- Make mute sound code togglable
- Keyhandler: Map XF86Search to the journal search
- Keyhandler: Catch all exceptions (thanks to silbe)
- Give time for atexit to execute when closing the emulator #435
- Dont hardcode the maximum amount of entries to cache in the journal #72
- Add standard 'Print' shortcut to take a screenshot
- Use keyboard specific keys to set the volume #430
- Update to new DBus policy #307
- Fix palette appearance on right-click #403
- Switch to existing instance of an activity if it's already running #410

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Simon Schampijer <simon@schampijer.de> - 0.83.8-1
- Revert "Add a favorites mode setting for deciding if the favorites view resumes by default or not"
- Listen for changes in the Activities dir and install/uninstall activities accordingly #235
- Fix sorting of favorite icons by installation_time #387
- View Source: Option and accelerator in activity frame palette
- View Source: Use activity icon outline for Bundle Source, part of #360
- View Source: Hide Python Bytecode files #361
- Use the file transfer icons
- Many new translations! 

* Thu Feb 19 2009 Simon Schampijer <simon@schampijer.de> - 0.83.7-3
- actually adding pygtksourceview2 as a dependency

* Thu Feb 19 2009 Simon Schampijer <simon@schampijer.de> - 0.83.7-2
- adding gtksourceview2 as a dependency

* Mon Feb 16 2009 Simon Schampijer <simon@schampijer.de> - 0.83.7-1
- Resume Activity list is not updated directly #322
- Fix network panel on XO (Sascha Silbe) #290
- Only show cp power section on xo #320
- Add logout option to the buddy menu (Sayamindu) #207
- Launch activity also when clicking on the palette icon #335
- Use the activity icon for the 'Start new' palette item #314
- Close the object chooser when the activity is closed #329
- Dates in journal are not translated #55
- Don't mute when right-clicking the speaker icon #278
- Correctly cache the connection to the OHM service #249
- Show launcher screen immediately after the user clicks to start an activity #243
- Use documend-send icon (Gary C Martin) #227
- Try harder to get an icon for a clipping
- Hide the journal activity in the home view #87
- Correctly initialize the TrayIcon
- Add 'View Details' option to object palette in journal
- Translation updates
- Hide OLPC-specific fields on non-xo machines #133
- Add a 'Clear search' button to 'No matching entries' message #266
- Correctly detect when a query in the journal is empty #255
- Avoid launching two instances of the same activity instance #238
- Add start-with option to objectpalette in the journal
- Fix dnd of icons in the favorite view #213
- Right click on AP should reveal palette not connect to AP #10
- Display space used and left in the volume palette in the journal #33
- Don't update the zoom level when a dialog window pops up
- Fix filtering the objectchooser with data types #219 

* Fri Feb 06 2009 Simon Schampijer <simon@schampijer.de> - 0.83.6-2.20090206git7115089fb0
- Fix italian translation
- Set the locale path for sugar-toolkit #55
- Don't mute when right-clicking the speaker icon #278
- Correctly cache the connection to the OHM service #249
- Show launcher screen as soon as possible #243
- Use documend-send icon (Gary C Martin) #227

* Wed Feb 04 2009 Simon Schampijer <simon@schampijer.de> - 0.83.6-1
- Try harder to get an icon for a clipping
- Hide the journal activity in the home view #87
- Correctly initialize the TrayIcon
- Add 'View Details' option to object palette in journal
- Translation updates
- Hide OLPC-specific fields on non-xo machines #133
- Add a 'Clear search' button to 'No matching entries' message #266
- Correctly detect when a query in the journal is empty #255
- Avoid launching two instances of the same activity instance #238
- Add start-with option to objectpalette in the journal
- Fix dnd of icons in the favorite view #213
- Right click on AP should reveal palette not connect to AP #10
- Display space used and left in the volume palette in the journal #33
- Don't update the zoom level when a dialog window pops up
- Fix filtering the objectchooser with data types #219

* Fri Jan 30 2009 Simon Schampijer <simon@schampijer.de> - 0.83.5-3.20090130gitf7807dddc0
- Add 'View Details' option to object palette in journal
- Translation updates
- Hide OLPC-specific fields on non-xo machines #133
- Add a 'Clear search' button to 'No matching entries' message #266
- Correctly detect when a query in the journal is empty #255
- Avoid launching two instances of the same activity instance #238
- Add start-with option to objectpalette in the journal
- Fix dnd of icons in the favorite view #213
- Right click on AP should reveal palette not connect to AP #10
- Display space used and left in the volume palette in the journal #33
- Don't update the zoom level when a dialog window pops up
- Fix filtering the objectchooser with data types #219

* Tue Jan 27 2009 Bernie Innocenti <bernie@codewiz.org> - 0.83.5-2
- Obsolete sugar-journal

* Tue Jan 20 2009 Marco Pesenti Gritti <mpg@redhat.com> - 0.83.5-1
- make the journal entries in the favorites palette resumable
- simplify the constants used to identify favorite layouts
- separate debug settings from xsession #163
- add logout option #207 to xomenu (sayamindu, icon by eben)
- change jabber server without sugar restart #142
- About my XO -> About my Computer
- #196 Fix setting the timezone in debian
- autoconnect to AP that we connected to last #8
- add a favorites mode setting for deciding if the favorites view resumes by default or not
- resume by default the last activity from the favorites view
- implement filtering by file type for removable devices
- #132 Filter by timestamp, not by mtime
- add support for text queries on removable devices
- dont abort if we cannot read a file from a removable device
- add a favorite filter to the journal toolbar
- sanitize the file name when we copy to removable devices
- #36 Refresh the detailed view when the entry changes
- #38 Refresh full metadata when editing so we dont lose properties
- Focus Search is not exposed via dbus anymore #89
- #131 'open with' does not work for clipboard item
- #165 Install bundles when they get into the journal
- add Resume item to the file transfer palette
- #126 Fix erase button in the journal
- following eben's spec for the device positions 

* Sun Jan 04 2009 Simon Schampijer <simon@laptop.org> - 0.83.4-2
- add intltool build require

* Sun Jan 04 2009 Simon Schampijer <simon@laptop.org> - 0.83.4-1
- New download url
- Fix language parsing on Gentoo and ALTLinux #81 (alsroot)
- Change the FRAME_POSITION_RELATIVE to follow eben's spec
- exec sugar-session
- Add wired device icon for the frame
- Only show wireless device in the frame when connecting/connected
- Use jabber.sugarlabs.org by default
- Only create a keydialog for the activating connection
- CanvasPulsingIcon: Don't begin pulse loop on resume if not pulsing
- Use g_timeout_add_seconds() for power efficiency
- Add the journal button to the volumes toolbar in the journal
- Remove jarabe/model/volume.py and use gio instead
- First try at restoring removable devices support in the journal
- make the image viewer activity the default one for iamges

* Wed Dec 21 2008 Bernie Innocenti <bernie@codewiz.org> - 0.83.3-6
- Add missing dependencies on xorg-x11-utils, dbus-x11 and openssh

* Wed Dec 10 2008 Bernie Innocenti <bernie@codewiz.org> - 0.83.3-5
- Spec file cleanup and updates

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.83.3-4
- Rebuild for Python 2.6

* Fri Nov 28 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.83.3-3
- Really add the patch

* Fri Nov 28 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.83.3-2
- Fix the desktop file executable

* Fri Nov 28 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.83.3-1
- Update to 0.83.3

* Thu Nov  6 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.83.2-4
- Fix translations

* Thu Nov  6 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.83.2-2
- Fix gconf schemas installation

* Tue Nov  4 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.83.2-1
- Update to 0.83.2

* Thu Sep 25 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.82.9-1
- #7969 Accidental searches lead to a "blank" Home screen
- #8662 xo man jumps around while zooming
- #8642 Bug in WPA key dialog prevents certain passwords from being accepted
- #8657 Help activity doesn't show up on a clean install.
- #8234 Software update (in Control Panel) crashes X-server.

* Sat Sep 20 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.82.8-1
- #8554 Indicate connected AP in Neighborhood view.
- #7987 Home view XO icon palette for Control Panel has wrong icon
- #7685 Alternate home layouts; fixed ring scaling; better modularization of layouts
- #8148 control panel does have layout problems with languages like mongolian
- #8485 Switching between zoom levels seem to leak

* Tue Sep 16 2008 Simon Schampijer <simon@laptop.org> - 0.82.7-1
- remove numpy finally

* Sat Sep 13 2008 Simon Schampijer <simon@laptop.org> - 0.82.6-1
- #8438 control panel fails when run with python -OO                                                                         
- #8470 SpreadLayout leaks self._collisions                                                                               
- #8375 gst usage in the shell wastes 2.6mb                                                                                        
- #8372 Remove numpy usage from the shell

* Thu Sep 12 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.82.5-1
- #8427 Sugar does not send SetActive(True)
- #8409 Sugar does not save network's BSSIDs in networks.cfg

* Thu Sep 11 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.82.4-1
- #7480 Need to 'reset' the network configurations - short term fix
- #8368 Disable the server plugin if no server was specified

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.82.3-2
- fix license tag

* Sat Sep  6 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.82.3-1
- #8300 Shell _launchers are leaked
- #7856 notify::active behaviour change
- #8250 Invalid POT for "Copyright and License" of control panel

* Wed Sep  3 2008 Jeremy Katz <katzj@redhat.com> - 0.82.2-2
- Require gstreamer-python and telepathy-python (rhbz#447589)

* Fri Aug 29 2008 Simon Schampijer <simon@laptop.org> - 0.82.2-1
- 6929 Control panel: include copyright/licensing info in about dialogue 
- Fix some launcher issues

* Thu Aug 28 2008 Tomeu Vizoso <tomeu@tomeuvizoso.net> - 0.82.1-1
- #2866 Network Manager GUI doesn't report success or failure
- #3993 The color of network icon in Home view becomes white after restarting Sugar.
- #2866 Network Manager GUI doesn't report success or failure
- #7988 Sugar control panel doesn't have a language entry for kreyol
- #7823 Non-modal alerts in CP remain when they shouldn't
- #7733 Cannot install Wikipedia-10.xo
- #7356 regression in activity view performance.
- #7660 XO Neighborhood icon drawing & erase glitches
- #6605 Screen rotates clockwise, while rotation button shows counter clockwise arrows
- #7877 Control Panel / Data & Time: Selecting timezone by typing locks up UI
- #7965 Mirror activities list in RTL locales
- #7220 Mark newly downloaded activities as favorites by default
- #7874 Search entry in Home focuses list view when cleared
- #7971 CP fails to validate all settings correctly
- #7970 Some CP modules set needs_restart to False when they shouldn't
- #7764 Reset Registration with school servers - short term solution
- #7823 Non-modal alerts in CP remain when they shouldn't
- #7874 Search entry in Home focuses list view when cleared
- #7730 Clicking on Speaker icon should Mute/Unmute Sound
- #4656 Non-olpc buddies not shown in the meshview (using salut)
- #7873 Search entry in Home should be focused implicitly

* Fri Aug 22 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.82.0-2.20080822git454def195d
- Fix #6605 #7877 #7965 #7220 #7874 #7971 #7970 #7764 #7823 #7841

* Thu Aug 07 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.82.0-1
- Mirror the intro screen in rtl. Patch by Khaled Kosny Fix #3108
- #7740 react gracefully to dbus services being restarted
- Fix case when already registered 7836
- Redirect keyboard brightness and DCON freeze requests to OHM #7357
- open cp software-updater on first boot after an update 7495
- Activate threads support 7486
- added languages Norwegian and Slovenian
- translation updates

* Fri Aug 01 2008 Simon Schampijer <simon@laptop.org> - 0.81.8-1
- 7248 Speaker device has inconsistent behavior
- 7625 alt+tab switching is slow because activities are notified unneccessary
- 7560 cp: Inconsistent behavior after changing the xo color
- 7641 Control panel sugar theme infelicities.
- 6136 No feedback from 'register' request. 

* Wed Jul 23 2008 Simon Schampijer <simon@laptop.org> - 0.81.7-1
- 7546 Activity launcher fails to show when launching from the journal
- 5664 Copying formatted text out of Browse breaks Journal/clipboard interaction
- 7385 Change the accelerator for switching between views in the home level
- 7249 Device ordering in Frame is not fixed
- 7510 Control Panel 'About Me' incorrectly keeps a name edit when you choose to Cancel out
- 7071 Activities cannot be deleted via GUI
- 4208 Battery indicator's icon fullness inconsistent with indicator %.
- 7430 Favorites view is not preserved
- 7434 Control panel UI for power management.

* Thu Jul 17 2008 Simon Schampijer <simon@laptop.org> - 0.81.6-4.20080715git8137d5c37f
- split the sugar-emulator in it's own package to get rid of the 
  xephyr dependency

* Tue Jul 15 2008 Tomeu Vizoso <tomeu@tomeuvizoso.net> - 0.81.6-3.20080715git8137d5c37f
- 7071 Add an option for uninstalling activities from the home view
- 7476 Order control panel modules logically
- 4208 battery icon consistency fix
- 7354 Maintain correct zoom level after activity launch

* Wed Jul 09 2008 Simon Schampijer <simon@laptop.org> - 0.81.6-2.20080709git8f4819a62e
- git snapshot
- 7430 Preserve the favorites layout across reboots
- 7434 Add power section to the control panel

* Wed Jul 09 2008 Simon Schampijer <simon@laptop.org> - 0.81.6-1
- 7438 sugar shuts down when you click Restart
- 7365 Invites not working
- 7248 Speaker device has inconsistent behavior
- 7339 CPU Spins after starting an activity
- 7015 Add proper alignment support to the tray control
- 5613 Cannot set non-ASCII nick name
- 7046 Deleting activity bundle with journal leaves it showing in Home list view until reboot
- 7391 Make the search field in Home reveal the list view
- 7248 Speaker device has inconsistent behavior
- 7272 Notifications are redundant with new launching feedback
- 7273 Activity icons remain colored after launch 

* Sat Jun 21 2008 Tomeu Vizoso <tomeu@tomeuvizoso.net> - 0.81.5-1
- Fix a bug with activity switching (benzea)
- UI improvements to the control panel frame section (erikos)
- First go at session management implementation (marco)
- New activity launching feedback (eben and marco)
- Speaker device implementation cleanups (mtd)
- Support for 1-1 chat with other xmpp clients (morgs and cassidy)
- Shortcuts improvements for emulation (mtd)
- Additional free form layout for the home view and allow to reorder icons (tomeu)
- Improve layout logic for the icons in the mesh view (tomeu)
- Support for switching activities using alt+tab (benzea)

* Mon Jun 09 2008 Simon Schampijer <simon@schampijer.de> - 0.81.3-1
- Search in the activity list (Tomeu)
- Add installation date in the activity list (Tomeu)
- Improve performance of the activity list (Tomeu)
- Sort activities in the list and ring by installation date (Tomeu)
- Speaker device (Martin Dengler)
- Graphical frontend for the control panel (Simon)
- Rotate the dpad keys when the screen rotate button is pressed (Erik Garrison) 

* Thu May 22 2008 Simon Schampijer <simon@schampijer.de> - 0.81.1-2
- Removed patch to fix activity location

* Thu May 22 2008 Simon Schampijer <simon@schampijer.de> - 0.81.1-1
- Make arrows scroll up and down in scroll views
- Merge activities.default into favorites

* Tue Apr 28 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.79.4-1
- Pylint cleanup.
- Misc graphical fixes.

* Mon Apr 28 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.79.3-2
- Patch to fix system activities location 

* Wed Apr 09 2008 Tomeu Vizoso <tomeu@tomeuvizoso.net> - 0.79.3-1
- Misc graphical fixes.

* Wed Apr  2 2008 Simon Schampijer <simon@laptop.org> - 0.79.2-1
- Frame/Home redesign - Put corner stone

* Fri Mar 28 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.79.1-1
- Update to 0.79.1

* Mon Feb 11 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.79.0-2
- Require sugar-artwork

* Fri Feb  8 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.79.0-1
- Update to 0.79.0, rework dependencies because of the toolkit split

* Sat Feb  2 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.11-2
- Rebuild

* Tue Jan 29 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.11-1
- Fix #5904

* Fri Jan 18 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.10-1
- Fix #1406 #5944 #6051

* Wed Jan 16 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.8-2
- Update the mime db. Fix #5815

* Fri Jan 11 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.8-1
- Fix #5489 #4562 #5765 #5559 #5493 #5573 #5648

* Thu Jan 10 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.7-1
- Fix #4145 #5538 #5760 #5532 #5884

* Sat Dec 22 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.6-1
- Fix #5489

* Wed Dec 19 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.5-1
- Fix #5526 #5512 #4909

* Wed Dec 19 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.4-1
- Fix #4906 #5382 #5364

* Wed Dec 12 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.3-1
- Fix #4965

* Tue Dec 11 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.1-1
- Fix #5154 #5221 #5080

* Wed Dec  5 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.75.0-1
- Update to 0.75.0

* Fri Nov 30 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.70.3-1
- Update to 0.70.3

* Thu Nov 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.70.2-2
- Change the jabber server

* Tue Nov 20 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.70.2-1
- Update to 0.70.2

* Mon Nov 19 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.70.1-1
- Update to 0.70.1

* Wed Nov 14 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.89.20071114git411879e9de
- #4768 Fix memory leak when switching between activities. (marco)

* Tue Nov 13 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.88.20071113git9d28557bbd
- Fix randr. (marco)
- Do not fail if there is not an activity service. (marco)
- Alert when an activity cannot be saved. (rwh)

* Tue Nov 13 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.87.20071113git47e231311b
- Get rid of sound competely to be sure we don't block the device. (marco)

* Tue Nov 13 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.86.20071112git1bf6cdaa81
- #4728, #4764: Set the correct colors for filtered out mesh view icons. (tomeu)

* Fri Nov 09 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.85.20071109gitd6bac927e1
- #4667 Do not display XO outside the mesh view. (marco)
- #4687 Use the right free function, fix a crash. (sjoerd)
- #4724 Display meshbox invite palette menu with colored
  activity icon (erikos)
- Always checkin to the DS from a new file. (tomeu)

* Fri Nov 09 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.84.20071109git55864fa3f6
- Support for the espeak service. (codyl)
- Fix typo in activity launching code. (marco)

* Thu Nov 08 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.83.20071108gite23f012e08
- Launch a few activities outside rainbow containers. (marco)

* Thu Nov 08 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.82.20071108git3e491c2dc7
- #4715: Filter new items that appear in the mesh view. (tomeu)
- #4716: Filter correctly activity icons in the mesh view. (tomeu)
- Use HOME/.i18n in control panel and reset jabber_registered to False (erikos)

* Wed Nov 07 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.81.20071107gitdae3ebe8d1
Snapshot 306d32832f

* Tue Nov  6 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.80.20071106git306d32832f
- Add missing dependency to sugar-base

* Tue Nov 06 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.79.20071106git306d32832f
- Associate ctrl+s to keep. (rwh)

* Tue Nov 06 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.78.20071105git73cae198f5
- Remove the startup sound for now, to not break audio
  for all the activities. (marco)

* Mon Nov 05 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.77.20071105git0a9676171d
- #4650: Failure to write journal files. (marco)

* Mon Nov 05 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.76.20071105gitee8712d1c4
- #3119: Implement some basic search capabilities in the mesh view. (tomeu)

* Sun Nov 04 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.75.20071104gitd456f6c633
- New experimental screenshot code. (marco)

* Sat Nov 03 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.74.20071103gite748f756c0
- #4618: Make the shell service more resilient to failure. (tomeu)

* Fri Nov 02 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.73.20071102git39aca0154d
- Get bundle installation to work again. (marco)

* Fri Nov 02 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.72.20071102gitb6422678e6
- #1941 Call FocusSearch method for popping up the journal. (rwh)

* Fri Oct 19 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.71.20071019gitefd0bbd326
- New snapshot

* Thu Oct 18 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.70.20071018git78f51a1b56
- New snapshot

* Thu Oct 11 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.69.20071010git9c5755d85a
- New snapshot

* Tue Oct  9 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.68.20071009git6c7c6a503b
- New snapshot

* Sun Oct  7 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.67.20071007git143f9ac9c6
- New snapshot

* Sun Oct  7 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.66.20071007git143f9ac9c6
- New snapshot

* Sat Oct  6 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.65.20071006gitc74013db1f
- New snapshot

* Sat Oct  6 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.64.20071005git79ba6b91b7
- New snapshot

* Thu Oct  4 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.63.20071004gitacca55e861
- New snapshot

* Mon Oct  1 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.61.20071001gited40d65791
- New snapshot

* Fri Sep 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.60.20070928gitb8ec83c5b8
- New snapshot

* Wed Sep 26 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.59.20070926git5a595ea04e
- New snapshot

* Tue Sep 25 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.58.20070925git5a595ea04e
- New snapshot

* Mon Sep 24 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.57.20070924git5a595ea04e
- New snapshot

* Sat Sep 22 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.56.20070922git5a595ea04e
- New snapshot

* Thu Sep 20 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.55.20070920git5a595ea04e
- New snapshot

* Wed Sep 19 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.54.20070919gitb8ce5083b7
- New snapshot

* Wed Sep 19 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.53.20070919gitb8ce5083b7
- New snapshot

* Tue Sep 18 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.52.20070918gitb8ce5083b7
- New snapshot

* Tue Sep 18 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.51.20070917gitb8ce5083b7
- New snapshot
- Add a patch to set the jabber server to jabber.laptop.org

* Mon Sep 17 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.50.20070917gited22733941
- New snapshot

* Sat Sep 15 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.49.20070915git8ef6c57f8b
- New snapshot

* Fri Sep 14 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.48.20070914git0a666e23cf
- New snapshot

* Wed Sep 12 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.47.20070912git47f473189e
- New snapshot

* Tue Sep 11 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.46.20070911git8b784a6223
- New snapshot

* Mon Sep 10 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.45.20070910git79237f3114
- New snapshot

* Sun Sep  9 2007 Dan Williams <dcbw@redhat.com> - 0.65-0.44.20070909gita1f5cece18
- New snapshot

* Sun Sep  9 2007 Dan Williams <dcbw@redhat.com> - 0.65-0.43.20070909git6b6470ebcb
- New snapshot

* Fri Sep  7 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.42.20070907gitc8700feccf
- New snapshot

* Thu Sep  6 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.41.20070906gitd9a30c23ff
- New snapshot

* Tue Sep  4 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.40.20070904git0ad6398cf1
- New snapshot

* Mon Sep  3 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.39.20070903git0b3f687749
- New snapshot

* Sat Sep  1 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.34.20070901gitfeb462d08d
- New snapshot

* Thu Aug 30 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.33.20070830gite65fef5c79
- New snapshot

* Wed Aug 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.32.20070829git23ad88db0c
- New snapshot

* Tue Aug 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.30.20070827git246ec1e4aa
- New snapshot

* Wed Aug 22 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.29.20070822gitd38cacfe2c
- New snapshot

* Mon Aug 20 2007 John (J5) Palmieri <mpg@redhat.com> - 0.65-0.28.20070820gite83b98a8f6
- New snapshot

* Mon Aug 20 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.28.20070820gitb24a28a77d
- New snapshot

* Tue Aug 14 2007 John (J5) Palmieri <johnp@redhat.com> - 0.65-0.27.20070814gitd93122bf5e
- New snapshot

* Wed Aug  1 2007 Dan Williams <dcbw@redhat.com> - 0.65-0.27.20070801gitd22f00d894
- New snapshot
    * Don't set a presence server by default (except in the emulator) (dcbw)

* Tue Jul 31 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.26.20070731git7ddd46589e
- New snapshot

* Sun Jul 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.25.20070729git285099fe08
- New snapshot

* Fri Jul 27 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.24.20070727git285099fe08
- New snapshot

* Wed Jul 25 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.23.20070725git088c7612e3
- New snapshot

* Tue Jul 24 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.22.20070724git9ac5d38e90
- New snapshot

* Mon Jul 23 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.21.20070723git4a924a8e5d
- New snapshot

* Mon Jul 23 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.20.20070723git943c78ffa7
- New snapshot

* Fri Jul 20 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.19.20070720git8ae99aaa87
- New snapshot

* Thu Jul 19 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.18.20070719gitf6f3f2b520
- New snapshot

* Tue Jul 17 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.16.20070717git5212790236
- New snapshot

* Tue Jul 17 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.15.20070716gitfd7336c2f1
- New snapshot

* Mon Jul 16 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.14.20070715git9f4da4e6d1
- New snapshot

* Fri Jul 13 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.13.20070713git4c352d1f83
- New snapshot

* Wed Jul 11 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.12.20070711gitec7eb2ebbb
- New snapshot

* Tue Jul 10 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.11.20070710gitb83a9ec27d
- New snapshot

* Tue Jul 10 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.4.20070710git42f0bcc48d
- New snapshot

* Tue Jul 10 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.3.20070710git757b2b8ce6
- New snapshot

* Mon Jul  9 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.2.20070709gitaa6a024368
- New snapshot

* Sun Jul  8 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.10.20070708gitf8cf7ff1ce
- New snapshot

* Fri Jul  6 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.9.20070706gitcebf25739b
- #1930: Only take preview before closing. (tomeu)

* Fri Jul  6 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.7.20070706git8af15d4e73
- Nicer tooltips. Improved sizing logic. (marco)
- Do not popdown the frame when palettes are active. (marco)
- Add macedonian translation. (ArangelAngov)
- Add brazilian translation. (DiegoZacarao)
- Some fixes for changing the selected clipboard object. (tomeu)
- Fix palettes around the mesh edges. (edsiper)

* Fri Jul  6 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.6.20070706gitde8b3b4c01
- Use HAL to get battery informations.
- Improvements in the mesh view layout.
- Hide the active palette when another popup.
- Icons in the buddy menu items

* Tue Jul  3 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.4.20070703gitcc2b8884c0
- Use the new palette widget everywhere in the UI
- Do not always show the shutdown palette on startup
- Implement primary and secondary state for palettes
- Fix several frame/zoom level bugs 

* Fri Jun 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.3.20070629git30bee7e43a
- Better palette positioning
- Reject invalid nick names in the intro screen
- Make startup notification work from the journal and clipboard
- Do not create a new object when resuming from the journal

* Thu Jun 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.2.20070628git0d6760b194
- New snapshot

* Thu Jun 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.10.20070628git03ef9c034e
- New snapshot

* Wed Jun 27 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.9.20070627git381df08442
- New snapshot

* Wed Jun 27 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.8.20070627git69ba74ddc2
- New snapshot

* Tue Jun 26 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.7.20070626git4f748dba9b
- New snapshot

* Tue Jun 26 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.4.20070626gitgit84127380dc
- New snapshot

* Thu Jun 21 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.3.20070620git0e4efae7ae
- python-telepathy is the name of the package in Fedora

* Wed Jun 20 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.2.20070620git0e4efae7ae
- Update to 0.65
- Fix versioning scheme

* Tue Jun 19 2007 John (J5) Palmieri <johnp@redhat.com> - 0.64-7.git3b1ee5a0bc.1
- add a %%doc line with COPYING COPYING.LIB and README
- fix up BR's
- fix buildroot

* Thu Jun 14 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.64-6.git3b1ee5a0bc.1
- Remove gst-plugins build dep

* Thu Jun 14 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.64-5.gita1e3dbaf9e.1
- New snapshot

* Mon Jun  4 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.64-3.gitb2980d7bd6.1
- New snapshot

* Wed May 30 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.git9ea6b18027.1
- Updated snapshot

* Thu May 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-1.gitb1ed24498c.1
- Journal API fixes

* Thu May 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-1.git0c77275ba7.2
- New snapshot

* Thu May 17 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.87.20070517git
- Presence service fixes

* Thu May 17 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.86.20070517git
- Ps and browser fixes

* Wed May 16 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.85.20070516git
- Journal perf fixes

* Tue May 15 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.84.20070515git
- Some ps fixes

* Tue May 15 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.83.20070515git
- Fix mozilla components initialization

* Tue May 15 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.82.20070515git
- Journal and ps fixes

* Mon May 14 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.81.20070514git
- Improved activity toolbar

* Mon May 14 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.80.20070514git
- Fix sugar browser

* Mon May 14 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.79.20070514git
- Several datastore and presence service fixes

* Fri May 11 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.78.20070511git
- Fix cursors

* Fri May 11 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.77.20070511git
- Various theme fixes and correct dpi

* Thu May 10 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.76.20070510git
- New snapshot

* Mon May  7 2007 Dan Williams <dcbw@redhat.com> - 0.63-2.75.20070406git
- Fix nickname encoding and length issues

* Fri Apr  6 2007 Dan Williams <dcbw@redhat.com> - 0.63-2.74.20070406git
- Network manager UI fixes (don't show adhoc APs)
- Fix the 'execute' command so the camera button works
- Blacklist failed buddy service resolutions in the PS

* Thu Apr  5 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.73.20070405git
- Network manager UI fixes

* Tue Apr  3 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.72.20070403git
- Do not abort on X errors

* Tue Apr  3 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.71.20070403git
- Do not kill the process for X errors in mozilla

* Fri Mar 30 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.70.20070331git
- Fix for back/forward on frames

* Fri Mar 30 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.69.20070330git
- Fix pdf downloading on broken servers

* Fri Mar 30 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.68.20070330git
- Some fixes for the new ap status feedback

* Thu Mar 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.67.20070329git
- Fixes for the mesh device UI

* Thu Mar 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.66.20070329git
- Better feedback for the ap states on the mesh view.

* Thu Mar 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.65.20070329git 
- Fix pdf mime type. Mesh network support.

* Wed Mar 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.64.20070328git
- Improve rollovers behavior. Disable the presence service.

* Mon Mar 26 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.62.20070326git
- Misc bugfixes

* Fri Mar 23 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.61.20070323git
- Support for translations. Bugfixes.

* Thu Mar 22 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.60.20070322git
- Fix gtkrc path

* Thu Mar 22 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.59.20070322git
- Add a gtkrc. Some fixes.

* Wed Mar 21 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.58.20070321git
- Don't hardcode font for arabic. Entry style fixes.

* Tue Mar 20 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.57.20070320git
- Some style fixes

* Mon Mar 19 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.56.20070319git
- File chooser size fixes

* Sun Mar 18 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.55.20070318git
- More frame and saving fixes

* Sat Mar 17 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.54.20070317git
- Suggest name on save. Frame fixes.

* Fri Mar 16 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.53.20070316git
- Several bug fixes

* Fri Mar 16 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.52.20070316git
- FIx file picker buttons

* Thu Mar 15 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.51.20070315git
- Fix donut and devices sizing

* Thu Mar 15 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.50.20070315git
- Several bugfixes

* Thu Mar 15 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.49.20070315git
- Downloads fixes and improvements

* Wed Mar 14 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.48.20070314git
- Improve the frame behavior and animation
- Add API to save image and web pages

* Sun Mar 11 2007 Dan Williams <dcbw@redhat.com> - 0.63-2.47.20070308git.1
- Better frame animation

* Thu Mar  8 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.47.20070308git
- Add a default picture

* Wed Mar  7 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.46.20070307git
- More nm fixes. Fix keyboard grabbing.

* Wed Mar  7 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.45.20070307git
- Some nmclient signals cleanups

* Wed Mar  7 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.44.20070307git
- Fix the doubling access points bug. Fix some access point state bugs.

* Wed Mar  7 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.43.20070307git
- Simple but efficient implementation of spreadbox

* Mon Mar  5 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.42.20070306git
- Update snapshot

* Mon Mar  5 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.41.20070305git
- Update snapshot

* Mon Mar  5 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.40.20070305git
- Update snapshot

* Sat Mar  3 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.39.20070305git
- Update snapshot

* Sat Mar  3 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.38.20070304git
- Update snapshot

* Sat Mar  3 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.37.20070304git
- Update snapshot

* Fri Mar  2 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.36.20070302git
- Update snapshot

* Thu Mar  2 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.34.20070302git
- Update snapshot

* Thu Mar  2 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.33.20070302git
- Update snapshot

* Thu Feb 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.32.20070302git
- Update snapshot

* Thu Feb 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.31.20070301git
- Update snapshot

* Wed Feb 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.30.20070228git
- Update snapshot

* Wed Feb 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.28.20070228git
- Update snapshot

* Wed Feb 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.27.20070228git
- Update snapshot

* Wed Feb 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.26.20070228git
- Update snapshot

* Wed Feb 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.25.20070228git
- Update snapshot

* Wed Feb 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.24.20070228git
- Update snapshot 

* Tue Feb 27 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.23.20070227git
- Update snapshot

* Sat Feb 24 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.22.20070224git
- Update to 0.63-2.22.20070224git

* Thu Feb 15 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.21.20070215git
- Update to 0.63-2.21.20070215git

* Thu Feb  8 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.20.20070208git
- Update to 0.63-2.20.20070208git

* Tue Feb  5 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.20.20070203git.1
- Remove dep on pygtkmozembed

* Sun Feb  3 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.20.20070203git
- Update to 0.63-2.20.20070203git

* Sun Feb  3 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.19.20070203git
- Update to 0.63-2.19.20070203git

* Wed Jan 31 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.18.20070131git
- Update to 0.63-2.18.20070131git

* Wed Jan 31 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.17.20070131git
- Update to 0.63-2.17.20070131git

* Wed Jan 31 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.16.20070131git
- Update to 0.63-2.16.20070131git

* Wed Jan 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.15.20070129git
- Update to 0.63-2.15.20070129git

* Wed Jan 17 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.14.20070167git
- Update to 0.63-2.14.20070117git

* Tue Jan 16 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.13.20070116git
- Update to 0.63-2.13.20070116git

* Mon Jan 15 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.12.20070115git
- Update to 0.63-2.12.20070115git

* Sat Jan 13 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.11.20070113git
- Update to 0.63-2.11.20070113git

* Fri Jan 12 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.10.20070112git
- Update to 0.63-2.10.20070112git

* Thu Jan 11 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.9.20070111git
- Update to  0.63-2.9.20070111git

* Wed Jan 10 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.8.20070110git
- Update to 0.63-2.8.20070110git

* Wed Jan 10 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.7.20070110git
- Update to 0.63-2.7.20070110git

* Tue Jan  9 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.6.20070109git
- Update to 2.6.20070109git

* Tue Jan  9 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.5.20070109git
- Update to 2.5.20070109git

* Mon Jan  8 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.4.20070108git
- Update to 2.4.20070108git

* Mon Jan  8 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.3.20070108git
- Update to 2.3.20070108git

* Mon Jan  8 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.1.20070108git
- Update to 2.1.20070108git

* Fri Jan  5 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.2.20070105git 
- Update to 0.63-2.2.20070105git

* Fri Jan  5 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-2.1.20070105git 
- Update to 0.63-2.1.20070105git

* Thu Nov 21 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.63-1
- Update to 0.63

* Wed Nov 20 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.62-1
- Update to 0.62

* Mon Nov 18 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.61-1
- Update to 0.61

* Mon Nov 18 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.60-1
- Update 0.60
- Addd the service files 

* Fri Nov 17 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.59.1-1
- Update to 0.59.1

* Mon Nov 14 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.59-1
- Update to 0.59

* Mon Nov 14 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.58-1
- Update to 0.58

* Sun Nov 12 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.57-1
- Update 0.57

* Sun Nov 12 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.56-1
- Update 0.56

* Sun Nov 12 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.54-1
- Updat 0.54

* Fri Nov 10 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.53-1
- Update 0.53

* Fri Nov 10 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.52-1
- Update to 0.52

* Thu Nov  9 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.51-1
- Update to 0.51

* Wed Nov  8 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.50-1
- Update to 0.50

* Sun Nov  5 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.49-1
- Update to 0.49

* Sat Nov  4 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.48-1
- Update to 0.48

* Fri Nov  3 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.47-1
- Update to 0.47

* Mon Oct 30 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.46-1
- Update to 0.46

* Sat Oct 28 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.45-1
- Update to 0.45

* Thu Oct 26 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.44-1
- Update to 0.44

* Thu Oct 26 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.43-1
- Update to 0.43

* Wed Oct 25 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.42-1
- Update to 0.42

* Tue Oct 24 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.41-1
- Update to 0.41

* Fri Oct 20 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.40-1
- Update to 0.40

* Fri Oct 20 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.39-1
- Update to 0.39

* Thu Oct 19 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.38-1
- Update to 0.38

* Wed Oct 18 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.37-1
- Update to 0.37

* Tue Oct 17 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.36-1
- Update to 0.36

* Tue Oct 17 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.35-1
- Update to 0.35

* Fri Oct 13 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-1
- Update to 0.34

* Fri Oct  6 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.33-1
- Update 0.33

* Fri Oct  6 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.32-1
- Update 0.32

* Fri Oct  6 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.31-3
- Add req for vte

* Fri Oct  6 2006 John (J5) Palmieri <johnp@redhat.com> - 0.31-2
- Add req for hippo-canvas-python

* Thu Oct  5 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.31-1
- Update to 0.31

* Wed Oct  4 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.30-1
- Update to 0.30
- Update dependencies

* Mon Sep 11 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.29-1
- Update to 0.29

* Mon Sep 11 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.29-1
- Update to 0.29

* Mon Sep 11 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.28-1
- Update to 0.28

* Mon Sep 11 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.27-1
- Update to 0.27

* Mon Sep 11 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.26-1
- Update to 0.26

* Fri Aug 25 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.25-1
- Update to 0.25

* Fri Aug 25 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.24-1
- Update to 0.24

* Fri Aug 25 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.23-1
- Update to 0.23
- Add build req pygtk2-devel

* Wed Aug 23 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.22-2
- Rebuild

* Wed Aug 23 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.22-1
- Update to 0.22

* Tue Aug 22 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.21-1
- Update to 0.21

* Tue Aug 22 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.20-2
- Requires matchbox-window-manager

* Tue Aug 22 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.20-1
- Update to 0.20
- Fix requires
- Require python-devel
- Require perl-XML-Parser
- Missing make on build
- Require gettext

* Tue Aug 22 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.19-3
- Remove .la

* Tue Aug 22 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.19-2
- Package some missing files

* Tue Aug 22 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.19-1
- Build 0.19

* Sun Jun 30 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.18-1
- Build 0.18

* Sun Jun 30 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.17-1
- Build 0.17

* Sun Jun 29 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.16-1
- Build 0.16

* Sun Jun 24 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.15-1
- Build 0.15

* Sat Jun 23 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.14-1
- Build 0.14

* Fri Jun 22 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.13-1
- Build 0.13

* Fri Jun 22 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.12-4
- Add pkgconfig to build requires

* Fri Jun 22 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.12-3
- Remove build requires

* Fri Jun 22 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.12-2
- Make this noarch

* Fri Jun 22 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.12-1
- Update to release 0.12

* Tue Jun 21 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.11-1
- Update to release 0.11

* Tue Jun 21 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.10-1
- Update to release 0.10

* Tue May 21 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.9-1
- Update to release 0.9

* Tue May 21 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.8-1
- Update to release 0.8

* Tue May 21 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.7-1
- Update to release 0.7

* Tue May 21 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.6-1
- Update to release 0.6

* Tue May 17 2006 Marco Pesenti Gritti <mpg@redhat.com> - 0.4-1
- Update to release 0.4
- No more dbus .services files

* Tue May 16 2006 David Zeuthen <davidz@redhat.com> - 0.3-1
- Update to release 0.3

* Tue May 16 2006 David Zeuthen <davidz@redhat.com> - 0.2-3
- Add Requires: avahi-tools

* Tue May 16 2006 David Zeuthen <davidz@redhat.com> - 0.2-2
- Add Requires: libxml2-python

* Mon May 08 2006 David Zeuthen <davidz@redhat.com> - 0.2-1
- Initial package
