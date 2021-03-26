Name: moblin-clutter-home
License: GPL
Group: User Interface/Desktops
Summary: A clutter based desktop launcher
Version: 0.2
Release: 2
#Source: http://moblin.org/build-results/projects/moblin-clutter-home/lpia/%{name}_%{version}.tar.gz
Source0: %{name}.tar.gz
Source1: moblin-clutter-home-desktop.png
URL: http://www.clutter-project.org
BuildRequires: libtool, GConf2-devel, gtk2-devel, clutter-devel, gnome-menus-devel
Requires: GConf2, gtk2, clutter, gnome-menus

%description
This a Clutter based desktop launcher which provides a way
to view and launch applications from a the home screen of UMPC.

%prep
%setup -q -n moblin-clutter-home

%build
./autogen.sh
%configure
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}%{_libdir}

%__mkdir -p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/clutter-home-switch <<EOF
#!/bin/sh
if ps -C %{name} ; then
  killall -u `whoami` %{name}
else
  %{name}
fi
EOF

#icon
%__mkdir -p %{buildroot}%{_datadir}/pixmaps
%__cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%__mkdir -p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/clutter-home-switch.desktop <<EOF
[Desktop Entry]
Name=Desktop Launcher Switching
Name[zh_TW]=桌面介面切換
Comment=Switching clutter desktop applications launcher
Comment[zh_TW]=切換桌面軟體啟動程式
Exec=clutter-home-switch
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;System;Utility;
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog COPYING
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/clutter-home-switch
%{_sysconfdir}/gconf/schemas/desktop-launcher.schemas
%{_datadir}/%{name}/*.svg
%{_datadir}/applications/clutter-home-switch.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Tue Mar 24 2009 Feather Mountain <john@ossii.com.tw> 0.2-2.ossii
- Add config settings.
- Fix fullscreen in lxde failure.

* Thu Mar 19 2009 Feather Mountain <john@ossii.com.tw> 0.2-1.ossii
- Update to 0.2-1
- Modify by clutter 0.8
- Set comment to center.
- Support PNG icon RGB format by cogl.
- Set minimap-comment to center. And support UTF8.

* Wed Jun 18 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.1-2.ossii
- Add clutter-home-switch

* Wed Jun 4 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.1-1.ossii
- Initial package
