Summary:      Menu for gnome that brings eye candy the Gnome menu's
Summary(de):  Menu für GNOME, bringt Eye Candy das Gnome-Menüs
Name:         gnomenu
Version:      2.9.1
Release:      10.1
License:      GPLv2
Group:        Graphical desktop/GNOME
Source:       https://launchpad.net/gnomenu/%{name}-%{version}.tar.gz
URL:          https://launchpad.net/gnomenu/
Requires: python2 gnome-python2
#Requires: deskbar-applet
Requires: pygtk2 
Requires: pygtk2-libglade
Requires: python2-pyxdg 
Requires: gnome-python2-desktop
Requires: pycairo
Requires: numpy
#Requires: PyXML
Requires: python2-xlib
Requires: gnome-python2-gconf
Requires:   glibc >= 2.10.1
Requires:   libstdc++ >= 4.4.1
Patch0:         gnomenu-2.9-patch-001
BuildArch: noarch
BuildRequires:  python2

%description
Fully functional menu , supports themes , for a composited or non
composited desktop. It can emulate the look and feel of the most 
beautiful menus of most modern desktops, and it can also use custom
menus, due to its powerful theme XML engine. GnoMenu currently supports
Gnome-Panel, Avant-Window-Navigator, Cairo-Dock and XfApplet.

#german
%description -l de
Voll funktionsfähige Menü unterstützt Themen, für die ein Composite-oder nicht Composite-Desktop. 
Sie können das Aussehen emulieren und die schönsten Menüs der meisten modernen Desktop-PCs erzeugen 
und auch benutzerdefinierte Menüs generieren, aufgrund seiner starken Thema XML-Engine. GnoMenu 
unterstützt derzeit Gnome-Panel, Avant-Window-Navigator, Cairo-Dock und XfApplet.

%prep
%setup -q -n %{name}
%patch 0 -p1

# fix settings
# defaut gnome-search-tool
##      perl -pi -e "s/tracker-search-tool/gnome-search-tool/g" src/lib/gnomenu/backup/Settings_default.xml
##      perl -pi -e "s/tracker-search-tool/gnome-search-tool/g" src/lib/gnomenu/GnoMenu-Settings.py
##      perl -pi -e "s/tracker-search-tool/gnome-search-tool/g" src/lib/gnomenu/Globals.py
# defaut drakconnect
##      perl -pi -e "s/nm-connection-editor/drakconnect/g" src/lib/gnomenu/backup/Settings_default.xml
##      perl -pi -e "s/nm-connection-editor/drakconnect/g" src/lib/gnomenu/GnoMenu-Settings.py
##      perl -pi -e "s/nm-connection-editor/drakconnect/g" src/lib/gnomenu/Globals.py
# defaut synaptic without gksu (Password request with consolekit)
##      perl -pi -e "s/gksu synaptic/synaptic/g" src/lib/gnomenu/backup/Settings_default.xml
##      perl -pi -e "s/gksu synaptic/synaptic/g" src/lib/gnomenu/GnoMenu-Settings.py
##      perl -pi -e "s/gksu synaptic/synaptic/g" src/lib/gnomenu/Globals.py
sed -i '1,2d' src/share/cairo-dock/third-party/GnoMenu/GnoMenu.conf
sed -i 's|python|python2|' Makefile setup.py

%build
make prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
make prefix=%{_prefix} DESTDIR=${RPM_BUILD_ROOT} install

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/avant-window-navigator/applets/GnoMenu/GnoMenu.py %{buildroot}/usr/lib/gnomenu/*.py
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/cairo-dock/plug-ins/Dbus/third-party/GnoMenu/GnoMenu %{buildroot}/usr/lib/gnomenu/*.py %{buildroot}%{_bindir}/*.py

%files
%doc COPYING Changelog README.txt
%{_sysconfdir}/%{name}/prefix
%{_bindir}/GnoMenu.py
/usr/lib/bonobo/servers/GNOME_GnoMenu.server
/usr/lib/%{name}
%{_datadir}/avant-window-navigator
%{_datadir}/cairo-dock
%{_datadir}/%{name}
%{_datadir}/locale

%changelog
* Thu Apr 21 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.9
- Rebuilt for Fedora
* Thu Jul 08 2010 Texstar <texstar at gmail.com> 2.9-2pclos2010
- add obsoletes gnomenu-awn-applet as the previous srpm created
- a separate pacakge 
- convert source file to tar.xz
* Wed Jul 07 2010 maik3531 <maik3531 at yahoo dot de> 2.9-1pclos2010
- 2.9
* Mon Dec 28 2009 maik3531 <maik3531 at yahoo dot de> 2.2.2-2pclos2010
- add default settings
* Sat Dec 26 2009 slick50 <lxgator@gmail.com> 2.2.2-1pclos2010
- initial pkg
