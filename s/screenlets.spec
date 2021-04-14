Name:           screenlets
Version:        0.1.2
Release:        1
License:        GPL
URL:            http://www.screenlets.org/index.php/Home
Summary:        OsX Like Dashboard
Group:          System/X11/Utilities
Source:         screenlets_0.1.2.tar.gz
BuildRequires:  python2-devel
BuildArch:	noarch
Obsoletes:      universal-applets
Requires:       gnome-python2
Requires:       gnome-python2-gconf
Requires:       gnome-python2-canvas
Requires:       gnome-python2-gnomevfs
Requires:       gnome-python2-bonobo
Requires:       gnome-python2-extras
Requires:       gnome-python2-libegg
Requires:       gnome-python2-gtkhtml2
Requires:       gnome-python2-desktop
Requires:       gnome-python2-applet
Requires:       gnome-python2-gnomekeyring
Requires:       gnome-python2-libwnck
Requires:       gnome-python2-rsvg
Requires:       pygtk2
Requires:       pyxdg
Requires:       dbus-python2
Requires:       python2-imaging
Requires:       python2-dateutil

%description
Screenlets are small owner-drawn applications (written in Python)
that can be described as 'the virtual representation of things 
lying/standing around on your desk'. Sticknotes, clocks, rulers, ...
the possibilities are endless.
You do NOT need Compiz or Beryl to use screenlets

%prep
%setup -q -n screenlets

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --skip-build --root $RPM_BUILD_ROOT --prefix /usr
sed -i 's,GenericName.*,GenericName[en_US]=Screenlets,' $RPM_BUILD_ROOT/usr/share/applications/screenlets-manager.desktop
sed -i 's,Categories.*,Categories=Utility;Desktop;,' $RPM_BUILD_ROOT/usr/share/applications/screenlets-manager.desktop
bash -c "echo X-SuSE-translate=false >> $RPM_BUILD_ROOT/usr/share/applications/screenlets-manager.desktop"
##rm -f $RPM_BUILD_ROOT/usr/share/applications/*

sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*/*.py %{buildroot}%{_datadir}/%{name}-manager/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGELOG README TODO
%{_bindir}/*
%dir %{_datadir}/screenlets/
%dir %{_datadir}/screenlets-manager/
%dir /usr/lib*/python*/site-packages/%{name}/
%{_datadir}/screenlets/*
%{_datadir}/screenlets-manager/*
%{_datadir}/applications/*
%{_datadir}/icons/screenlets.svg
%{_datadir}/locale/*/LC_MESSAGES/screenlets-manager.mo
%{_datadir}/locale/*/LC_MESSAGES/screenlets.mo
/usr/lib*/python*/site-packages/%{name}/*
/usr/lib*/python*/site-packages/%{name}-*-py*.egg-info

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2
- Rebuilt for Fedora
* Mon Nov 10 2008 - some-guy <muhammedu@gmail.com>
- Work with older distros
* Sat Nov 08 2008 - some-guy <muhammedu@gmail.com>
- Clean up
- Works better with OBS
* Mon Sep 29 2008 - some-guy <muhammedu@gmail.com>
- Fix for factory
* Sat Jul 19 2008 - Aleksandar Kanchev <aleksandar.kanchev@gmail.com>
- add support for Fedora 9
* Mon Jun 30 2008 - some-guy <muhammedu@gmail.com>
- fix for 11 and factory
* Sun Jun 01 2008 - some-guy <muhammedu@gmail.com>
- upgraded to 0.1.2
* Sun May 18 2008 - Andrea Florio <andrea@links2linux.de>
- apgraded to svn 20080518 revison 338
* Thu Apr 30 2008 - Andrea Florio <andrea@links2linux.de>
- apgraded to svn 20080430 revison 308
* Wed Apr 09 2008 - Andrea Florio <andrea@links2linux.de>
- apgraded to svn 20080408 revison 260
* Tue Apr 01 2008 Andrea Florio - <andrea@linsk2linux.de>
- Update to snv 20080401 revision 233
* Sun Mar 23 2008 Andrea Florio - <andrea@linsk2linux.de>
- Update to snv 20080323 revision 214
* Tue Mar 18 2008 Andrea Florio - <andrea@linsk2linux.de>
- Update to snv 20080318 revision 206
* Sun Mar 16 2008 Andrea Florio - <andrea@links2linux.de>
- Update to snv 20080316 revision 199
* Sat Mar 15 2008 Andrea Florio - <andrea@links2linux.de>
- Update to snv 15032008 revision 198
* Thu Feb 29 2008 Andrea Florio - <andrea@links2linux.de>
- Update to snv 29022008 revision 191
* Sat Feb 16 2008 Andrea Florio <andrea@links2linux.de>
- Update to snv 16022008 revision 182
* Mon Feb 09 2008 Andrea Florio <andrea@links2linux.de>
- Update to snv 09022008 revision 174
* Tue Jan 29 2008 Andrea Florio <andrea@links2linux.de>
- Update to snv 29012008 (more stable than previous one)
* Mon Jan 28 2008 Andrea Florio <andrea@links2linux.de>
- Update to snv 28012008
* Mon Nov 19 2007 Andrea Florio <andrea@links2linux.de>
- Initial revision
