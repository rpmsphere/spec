Name: cardapio
Summary: An alternative Gnome menu, launcher, and much more!
Version: 0.9.202
Release: 1
Group: gnome
License: Free Software
URL: https://launchpad.net/cardapio
Source0: %{name}-bzr886.tgz
BuildArch: noarch
BuildRequires: desktop-file-utils
#Requires: python-gtk2
#Requires: python-tk,
#Requires: python-glade2,
#Requires: python-gmenu,
#Requires: python-keybinder,
#Requires: xdg-user-dirs,
#Requires: xdg-user-dirs-gtk

%description
Cardapio is a launcher that can work in two modes: as a panel applet
(in which case it is an alternative to Gnome's application menu
applet) or as a launcher (in which case it is a lightweight
alternative to Gnome Do). Either way, it features a beautiful,
well-thought-out interface, supports tracker searching, and much more.
Give it a try today!

%prep
%setup -q -n %{name}

%build
#make %{?_smp_mflags}
python2 -m compileall src/

%install
sed -i 's|python |python2 |' Makefile
make install DESTDIR=%{buildroot}
sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}/usr/lib/%{name}/%{name}* %{buildroot}%{_datadir}/dockmanager/scripts/*.py

%files
%{_bindir}/%{name}*
/usr/lib/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/%{name}.pot
%{_datadir}/pixmaps/%{name}-*.png
/usr/lib/bonobo/servers/cardapio.server
/usr/lib/gnome-applets/cardapio-gnome-panel
/usr/lib/matecomponent/servers/cardapio.server
%{_datadir}/avant-window-navigator/applets/cardapio.desktop
%{_datadir}/cinnamon/applets/cardapio@varal.org/applet.js
%{_datadir}/cinnamon/applets/cardapio@varal.org/metadata.json
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dockmanager/metadata/cardapio_helper.py.info
%{_datadir}/dockmanager/scripts/cardapio_helper.py
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.CardapioGnomeApplet.panel-applet
%{_datadir}/gnome-shell/extensions/cardapio@varal.org
%{_datadir}/pixmaps/cardapio-*.svg

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.202
- Rebuilt for Fedora
