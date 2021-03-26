%global commit_date 20111218
%global commit fb940ec
%global provider linuxmint
%global alt_name MGSE
%global tarball %{provider}-%{alt_name}-%{commit}

Name:           gnome-shell-extensions-mgse
Version:        %{commit_date}
Release:        2.1
Summary:        Linux Mint GNOME Shell Extensions
License:        GPLv3
URL:            https://github.com/%{provider}/%{alt_name}/
Source0:        https://github.com/%{provider}/%{alt_name}/tarball/master/%{tarball}.tar.gz
BuildArch:      noarch

%description
GNOME Shell Extensions from Linux Mint distribution:
  * alttab
  * bottompanel
  * mediaplayer
  * menu
  * noa11y
  * notifications
  * shutdownmenu
  * smartoverview
  * trash
  * userthemes
  * windowlist
  * xrandr

%package -n gnome-shell-extension-mgse-alttab
Summary:        GNOME Shell extension Alt Tab
Group:          User Interface/Desktops
Requires:       gnome-shell

%description -n gnome-shell-extension-mgse-alttab
Traditional Alt Tab.

%package -n gnome-shell-extension-mgse-bottompanel
Summary:        GNOME Shell extension Bottom Panel
Group:          User Interface/Desktops
Requires:       gnome-shell

%description -n gnome-shell-extension-mgse-bottompanel
Add a panel to the bottom of the screen.

%package -n gnome-shell-extension-mgse-mediaplayer
Summary:        GNOME Shell extension Media Player
Group:          User Interface/Desktops
Requires:       gnome-shell

%description -n gnome-shell-extension-mgse-mediaplayer
Media Player Control in GNOME 3.

%package -n gnome-shell-extension-mgse-menu
Summary:        GNOME Shell extension Menu
Group:          User Interface/Desktops
Requires:       gnome-shell

%description -n gnome-shell-extension-mgse-menu
An advanced GNOME Shell Menu.

%package -n gnome-shell-extension-mgse-noa11y
Summary:        GNOME Shell extension No A11Y
Group:          User Interface/Desktops

%description -n gnome-shell-extension-mgse-noa11y
Hides the accessibility button.

%package -n gnome-shell-extension-mgse-notifications
Summary:        GNOME Shell extension Notifications
Group:          User Interface/Desktops
Requires:       gnome-shell

%description -n gnome-shell-extension-mgse-notifications
Places important notifications in the top panel.

%package -n gnome-shell-extension-mgse-shutdownmenu
Summary:        GNOME Shell extension Shutdown Menu
Group:          User Interface/Desktops
Requires:       gnome-shell

%description -n gnome-shell-extension-mgse-shutdownmenu
Replace Suspend menu with Shutdown and add Suspend/Hibernate to Power Off
dialog.

%package -n gnome-shell-extension-mgse-smartoverview
Summary:        GNOME Shell extension Smart Overview
Group:          User Interface/Desktops
Requires:       gnome-shell

%description -n gnome-shell-extension-mgse-smartoverview
Arrange windows in overview in a smart way.

%package -n gnome-shell-extension-mgse-trash
Summary:        GNOME Shell extension Trash Can
Group:          User Interface/Desktops
Requires:       gnome-shell

%description -n gnome-shell-extension-mgse-trash
Adds a trash can to the panel.

%package -n gnome-shell-extension-mgse-userthemes
Summary:        GNOME Shell extension User Themes
Group:          User Interface/Desktops
Requires:       gnome-shell

%description -n gnome-shell-extension-mgse-userthemes
Load shell themes from user directory.

%package -n gnome-shell-extension-mgse-windowlist
Summary:        GNOME Shell extension Window List
Group:          User Interface/Desktops
Requires:       gnome-shell

%description -n gnome-shell-extension-mgse-windowlist
Adds a window list to the panel.

%package -n gnome-shell-extension-mgse-xrandr
Summary:        GNOME Shell extension Monitor Status
Group:          User Interface/Desktops
Requires:       gnome-shell

%description -n gnome-shell-extension-mgse-xrandr
Add a systems status menu for rotating monitors (overrides what is currently
provided by gnome-settings-daemon).

%prep
%setup -q -n %{tarball}
find . -name "*.po" -delete

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
for extension in alttab bottompanel mediaplayer menu noa11y notifications shutdownmenu smartoverview trash userthemes windowlist xrandr; do
  cp -a mgse-$extension/usr $RPM_BUILD_ROOT
done

# Remove installed documentation
rm $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/*/credits

# Move locales to /usr/share/locale/
mv $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/*/locale/ $RPM_BUILD_ROOT%{_datadir}/

# Find locales for the mgse-shutdownmenu extension
%find_lang gnome-shell-frippery gnome-shell-extension-mgse-shutdownmenu.lang

%posttrans -n gnome-shell-extension-mgse-alttab
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas || :

%postun -n gnome-shell-extension-mgse-alttab
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%posttrans -n gnome-shell-extension-mgse-smartoverview
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas || :

%postun -n gnome-shell-extension-mgse-smartoverview
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%posttrans -n gnome-shell-extension-mgse-userthemes
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas || :

%postun -n gnome-shell-extension-mgse-userthemes
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -n gnome-shell-extension-mgse-alttab
%doc mgse-alttab/usr/share/gnome-shell/extensions/alttab@linuxmint.com/credits
%{_datadir}/glib-2.0/schemas/linuxmint.mgse.alttab.gschema.xml
%{_datadir}/gnome-shell/extensions/alttab@linuxmint.com/

%files -n gnome-shell-extension-mgse-bottompanel
%{_datadir}/gnome-shell/extensions/bottompanel@linuxmint.com/

%files -n gnome-shell-extension-mgse-mediaplayer
%doc mgse-mediaplayer/usr/share/gnome-shell/extensions/mediaplayer@linuxmint.com/credits
%{_datadir}/gnome-shell/extensions/mediaplayer@linuxmint.com/

%files -n gnome-shell-extension-mgse-menu
%{_datadir}/gnome-shell/extensions/menu@linuxmint.com/

%files -n gnome-shell-extension-mgse-noa11y
%{_datadir}/gnome-shell/extensions/noa11y@linuxmint.com/

%files -n gnome-shell-extension-mgse-notifications
%doc mgse-notifications/usr/share/gnome-shell/extensions/notifications@linuxmint.com/credits
%{_datadir}/gnome-shell/extensions/notifications@linuxmint.com/

%files -n gnome-shell-extension-mgse-shutdownmenu -f gnome-shell-extension-mgse-shutdownmenu.lang
%doc mgse-shutdownmenu/usr/share/gnome-shell/extensions/shutdownmenu@linuxmint.com/credits
%{_datadir}/gnome-shell/extensions/shutdownmenu@linuxmint.com/

%files -n gnome-shell-extension-mgse-smartoverview
%doc mgse-smartoverview/usr/share/gnome-shell/extensions/smartoverview@linuxmint.com/credits
%{_datadir}/glib-2.0/schemas/linuxmint.mgse.smartoverview.gschema.xml
%{_datadir}/gnome-shell/extensions/smartoverview@linuxmint.com/

%files -n gnome-shell-extension-mgse-trash
%{_datadir}/gnome-shell/extensions/trash@linuxmint.com/

%files -n gnome-shell-extension-mgse-userthemes
%doc mgse-userthemes/usr/share/gnome-shell/extensions/userthemes@linuxmint.com/credits
%{_datadir}/glib-2.0/schemas/linuxmint.mgse.userthemes.gschema.xml
%{_datadir}/gnome-shell/extensions/userthemes@linuxmint.com/

%files -n gnome-shell-extension-mgse-windowlist
%{_datadir}/gnome-shell/extensions/windowlist@linuxmint.com/

%files -n gnome-shell-extension-mgse-xrandr
%doc mgse-xrandr/usr/share/gnome-shell/extensions/xrandr@linuxmint.com/credits
%{_datadir}/gnome-shell/extensions/xrandr@linuxmint.com/

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Jan 08 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 20111218
- Rebuild for Fedora

* Thu Nov 24 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0-0.1.20111118git7770cbd
- Initial RPM release
