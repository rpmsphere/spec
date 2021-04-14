%undefine _debugsource_packages
Name:		dockbarx
Version:	0.93
Release:	4
Group:		Graphical desktop/GNOME
License:	GPL
Summary:	TaskBar with groupping and group manipulation.
Source:		%{name}-%{version}.tar.gz
URL:		https://launchpad.net/dockbar/dockbarx
Requires:	gnome-python2-gconf
Requires:       python2-pyxdg
Requires:       python2-pillow
Requires:       python2-xlib
Requires:       python2-keybinder
Requires:	dbus-python
Requires:	mate-panel
Requires:	gnome-python2-desktop
Requires:	gnome-python2-libwnck
Requires:	numpy numpy-f2py
#Requires:	deskbar-applet
#Requires:      gnome-python2-applet
BuildRequires: python2
BuildArch:  noarch

%description
GNOME TaskBar with groupping and group manipulation. This is an
Experimental version of GNOME Dockbar.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/avant-window-navigator/applets
cp -r AWN/* $RPM_BUILD_ROOT%{_datadir}/avant-window-navigator/applets

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%{python2_sitelib}/dockbarx
%{python2_sitelib}/*.egg-info
%{_bindir}/*
/usr/lib/bonobo/servers/GNOME_DockBarXApplet.server
%{_datadir}/applications/*.desktop
%{_datadir}/avant-window-navigator/applets/DockBarX.desktop
%{_datadir}/avant-window-navigator/applets/DockBarX/DockBarX.py*
%{_datadir}/dockbarx
%{_datadir}/namebar
%{_datadir}/icons/hicolor/*/apps/dockbarx.png
%{_datadir}/locale/*/LC_MESSAGES/*.mo

%changelog
* Fri Jun 14 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.93
- Rebuilt for Fedora
* Sun Aug 01 2010 Texstar <texstar at gmail.com> 0.39.6-1pclos2010
- create package
