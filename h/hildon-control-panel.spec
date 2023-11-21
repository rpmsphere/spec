Name: hildon-control-panel
License: GPL
Group: User Interface/Desktops
Summary: Hildon control panel
Version: 1.9.5
Release: 1
Source: https://moblin.org/build-results/projects/hildon-control-panel/lpia/hildon-control-panel_%{version}-2ubuntu1.tar.gz
URL: https://www.moblin.org/projects/projects_ui.php
BuildRequires: gnome-vfs2-devel, libhildon-devel, libosso-devel, libhildonhelp-devel
Requires: gnome-vfs2, libhildon, libosso, libhildonhelp
Requires: pkgconfig, osso-af-settings

%description
Control panel to configure the Hildon Desktop.

%prep
%setup -q -n hildon-control-panel
sed -i 's/1\.7/1.16/' autogen.sh

%build
./autogen.sh
%configure --with-x --disable-maemo-tools
make CFLAGS+=-Wno-error

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install
%__install -D -m0644 controlpanel.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
sed -i 's|copa_ap_cp_name.*|Hildon control panel|' %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf %{buildroot}

%files
%doc MAINTAINERS ChangeLog COPYING
%{_bindir}/controlpanel
%{_sysconfdir}/gconf/schemas/hildon-control-panel.schemas
%{_libdir}/pkgconfig/hildon-control-panel.pc
%{_includedir}/hildon-cp-plugin/hildon-cp-plugin-interface.h
#%dir %{_datadir}/applications/hildon-control-panel
%{_datadir}/applications/hildon-control-panel.desktop
%{_datadir}/dbus-1/services/com.nokia.controlpanel.service
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.5
- Rebuilt for Fedora
