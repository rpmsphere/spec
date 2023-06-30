Name:           foobnix
Version:        3.1.2git
Release:        1
Summary:        Lightweight and Functional music player for Linux
License:        GPLv3
URL:            https://foobnix.com
Source0:        %{name}-master.zip
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python2-devel
BuildRequires:  gettext
Requires:       dbus-python
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       python-chardet
Requires:       python-gobject
Requires:       python-gobject-base
Requires:       python-mutagen
Requires:       python-simplejson
Requires:       python-six
Requires:       keybinder3
Requires:       webkitgtk3

%description
Supports all popular formats, FLAC, lossless, CUE, and 5000+ radio
stations out of the box. Online music for free. Last.fm and
VKontakte integration and more...
                                                                       
%prep
%autosetup -n %{name}-master

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --root %{buildroot}
%find_lang %{name}

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files -f %{name}.lang
%doc README.md CHANGELOG
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1*
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}-*.egg-info

%changelog
* Fri Nov 29 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1.2git
- Rebuilt for Fedora
* Tue May 31 2016 Maxim Orlov <murmansksity@gmail.com> - 3.1.2-4.20160531git6fed0a2.R
- Update to latest git snapshot
* Mon Apr 25 2016 Maxim Orlov <murmansksity@gmail.com> - 3.1.2-3.20160425git873d7bd.R
- Update to latest git snapshot
- Remove R: pylast
* Thu Dec 31 2015 Maxim Orlov <murmansksity@gmail.com> - 3.1.2-2.20151231gitcdbd6e7.R
- Update to latest git snapshot
* Wed Dec 30 2015 Maxim Orlov <murmansksity@gmail.com> - 3.1.2-1.20151222git5a005ad.R
- Update to latest git snapshot
* Mon Nov 09 2015 Maxim Orlov <murmansksity@gmail.com> - 3.1.01-1.20151104git4585517.R
- Update to latest git snapshot
* Tue Jul 14 2015 Maxim Orlov <murmansksity@gmail.com> - 3.1.00-1
- Update to 3.1.00
* Tue Feb 18 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 2.6.10-1.20140218git236be1f.R
- Update to 2.6.10
* Thu Jan 03 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 2.6.09-1.20121206git35fcb24.R
- Update to 2.6.09
* Thu Dec 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.5.35-1.20120315gitc555fab.R
- Update to the latest git snapshot
* Thu Dec 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.5.32-1.20111222gitdf1d44b.R
- Update to the latest git snapshot
* Wed Nov 02 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.5.25-1.20001102git38b5ed8.R
- Update to the latest git snapshot
- Drop patches
- Update versioning
* Mon Sep 19 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.5.25-1.git49ac470
- Update to the latest git snapshot
* Mon Sep 12 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.23-1.git5295204
- Ver. 2.5.24
* Sun Sep 11 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.23-1.gite391906
- Update to the latest git snapshot
* Sun Aug 14 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.23-1.giteeb56ad
- Update to the latest git snapshot
* Sat Jul 09 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.17-2.git4c93748
- Don't use functions specific to the forked copy of pylast
* Sat Jul 09 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.17-1.git4c93748
- Update to the latest git snapshot
* Wed Jun 29 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.16-1.git31ad572
- Update to the latest git snapshot
* Fri Jun 03 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.15-1.git12b0915
- Update to the latest git tag
* Thu Feb 24 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.5-1
- update to 0.2.5
* Tue Jan 25 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.3-1
- initla build
