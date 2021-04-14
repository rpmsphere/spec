Name:          universal-applets
Version:       0.1.2bzr624
Release:       1
License:       GPL
URL:           http://www.screenlets.org/index.php/Home
Summary:       OsX Like Dashboard
Group:         System/X11/Utilities
Source:        universal-applets_0.1.2bzr624-1.tar.gz
BuildRequires: python2-devel
BuildArch:     noarch
Requires:      pyxdg
Requires:      python2-imaging
Requires:      python2-dateutil
Obsoletes:     screenlets
Requires:      gnome-python2
Requires:      gnome-python2-gconf
Requires:      gnome-python2-canvas
Requires:      gnome-python2-gnomevfs
Requires:      gnome-python2-bonobo
Requires:      gnome-python2-extras
Requires:      gnome-python2-libegg
Requires:      gnome-python2-gtkhtml2
Requires:      gnome-python2-desktop
Requires:      gnome-python2-applet
Requires:      gnome-python2-gnomekeyring
Requires:      gnome-python2-libwnck
Requires:      gnome-python2-rsvg
Requires:      pygtk2
Requires:      dbus-python

%description
Screenlets are small owner-drawn applications (written in Python)
that can be described as 'the virtual representation of things
lying/standing around on your desk'. Sticknotes, clocks, rulers, ...
the possibilities are endless.
You do NOT need Compiz or Beryl to use screenlets
 
%prep
%setup -q -n ua-bzr
 
%build
sed 's:PREFIX:/usr:' < src/share/melange/org.UniversalApplets.Melange.service.in > src/share/melange/org.UniversalApplets.Melange.service
sed 's:PREFIX:/usr:' < src/share/screenlets-daemon/org.UniversalApplets.Daemon.service.in > src/share/screenlets-daemon/org.UniversalApplets.Daemon.service
sed 's:PREFIX:/usr:' < src/share/universal-applets-manager/org.UniversalApplets.UniversalAppletsManager.service.in > src/share/universal-applets-manager/org.UniversalApplets.UniversalAppletsManager.service
 
%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root $RPM_BUILD_ROOT --prefix /usr
mkdir -p $RPM_BUILD_ROOT/etc/universal-applets
bash -c "echo /usr > $RPM_BUILD_ROOT/etc/universal-applets/prefix"

##rm -f $RPM_BUILD_ROOT/usr/share/applications/universal-applets-manager.desktop 
convert desktop-menu/screenlets.svg desktop-menu/screenlets.png
install -Dm644 desktop-menu/screenlets.png %{buildroot}%{_datadir}/pixmaps/screenlets.png
rm -f %{buildroot}%{_datadir}/icons/screenlets.svg
sed -i 's|/usr/share/icons/screenlets.svg|screenlets|' %{buildroot}%{_datadir}/applications/universal-applets-manager.desktop

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/universal-applets-manager/*.py
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
bash -c "(kill `ps ax | grep screenlets-daemon | sed 's,.*grep.*,,' | cut -d" " -f2` && kill `ps ax | grep melange | sed 's,.*grep.*,,' | cut -d" " -f2`) &>/dev/null || true"

%files
%doc CHANGELOG README TODO
%dir /etc/universal-applets
%dir %{_datadir}/universal-applets-manager/
%dir %{_datadir}/melange/
%dir %{_datadir}/ua-sidebar/
%dir %{_datadir}/ua-sidebar/themes/
%dir %{_datadir}/ua-sidebar/themes/default/
%{_bindir}/*
/etc/universal-applets/prefix
%{_datadir}/dbus*/services/org.UniversalApplets*
%{_datadir}/universal-applets-manager/*
%{_datadir}/melange/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/screenlets.png
%{_datadir}/locale/*/LC_MESSAGES/screenlets*.mo
%{_datadir}/locale/*/LC_MESSAGES/universal*.mo
%{_datadir}/ua-sidebar/themes/default/*
/usr/lib*/python*/site-packages/screenlets*
/usr/lib*/python*/site-packages/universal_applets-*-py*.egg-info

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2bzr624
- Rebuilt for Fedora
* Mon Mar 02 2009 - some-guy <muhammedu@gmail.com>
- upgraded to bzr
* Mon Mar 02 2009 - some-guy <muhammedu@gmail.com>
- upgraded to bzr
* Mon Mar 02 2009 - some-guy <muhammedu@gmail.com>
- upgraded to bzr
* Mon Mar 02 2009 - some-guy <muhammedu@gmail.com>
- upgraded to bzr
* Wed Feb 11 2009 - Ketil Wendelbo Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
* Sat Dec 20 2008 - Ketil Wendelbo Aanensen <ketil.w.aanensen@gmail.com>
- upgraded to bzr
