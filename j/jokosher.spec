%undefine _debugsource_packages
Summary:                A simple yet powerful multi-track studio
Name:                   jokosher
Version:                0.11.5
Release:                12.1
Group:                  Productivity/Multimedia/Sound/Editors and Convertors
License:                GPL
URL:                    https://www.jokosher.org/
Source0:                https://launchpad.net/jokosher/trunk/0.11.5/+download/jokosher-0.11.5.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:  python2-devel
BuildRequires:  shared-mime-info
Requires:               dbus-python
Requires:               gstreamer-plugins-bad-free
Requires:               gstreamer-plugins-base
Requires:               gstreamer-plugins-good
Requires:               gstreamer-plugins-ugly
Requires:               gstreamer-plugin-gnonlin
Requires:               hicolor-icon-theme
Requires:               pycairo
Requires:               python-alsaaudio
Requires:               gnome-python2
Requires:               python2-gstreamer
Requires:               pygtk2
Requires:               pyxdg
Requires:               python2-setuptools
BuildArch:              noarch

%description
Jokosher is a simple and poweful multi-track studio. Jokosher
provides a complete application for recording, editing, mixing and
exporting audio, and has been specifically designed with usability
in mind. The developers behind Jokosher have re-thought audio
production at every level, and created something devilishly simple
to use.

%package help
Summary:        Jokosher help files
Group:          Documentation/Other
Requires:       %{name} = %{version}
Requires:       yelp

%description help
Jokosher help files in yelp format.

%prep
%setup -q

%build
%__python2 setup.py build

%install
%__python2 setup.py install \
        --skip-build \
        --root=%{buildroot} \
        --prefix=%{_prefix}

#DESTDIR=%{buildroot} mime-info-to-mime
%__rm -rf %{buildroot}%{_datadir}/mime-info

# icon
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 Jokosher/jokosher-logo.png \
        %{buildroot}%{_datadir}/pixmaps/%{name}.png

%__chmod 755 %{buildroot}%{python2_sitelib}/Jokosher/Profiler.py
%__chmod 755 %{buildroot}%{python2_sitelib}/Jokosher/JokosherApp.py

%__rm -r %{buildroot}/usr/share/locale/ace
%__rm -r %{buildroot}/usr/share/locale/en_PH
%__rm -r %{buildroot}/usr/share/locale/kk

%find_lang %{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name} %{buildroot}%{python2_sitelib}/Jokosher/*.py

%post
/usr/bin/update-mime-database /usr/share/mime >/dev/null

%postun
/usr/bin/update-mime-database /usr/share/mime >/dev/null

%files -f %{name}.lang
%exclude %{_datadir}/gnome
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%dir %{python2_sitelib}/Jokosher
%{python2_sitelib}/Jokosher/*.py*
%dir %{python2_sitelib}/Jokosher/elements
%{python2_sitelib}/Jokosher/elements/*.py*
%dir %{python2_sitelib}/Jokosher/PlatformUtils
%{python2_sitelib}/Jokosher/PlatformUtils/*.py*
%dir %{python2_sitelib}/Jokosher/ui
%{python2_sitelib}/Jokosher/ui/*.py*
%{python2_sitelib}/%{name}-%{version}-py*.egg-info
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.glade
%{_datadir}/%{name}/*.png
%dir %{_datadir}/%{name}/extensions
%{_datadir}/%{name}/extensions/*
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/pixmaps/*
%dir %{_datadir}/%{name}/Instruments
%{_datadir}/%{name}/Instruments/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/pixmaps/%{name}*.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/omf/jokosher/jokosher-C.omf

%files help
%dir %{_datadir}/gnome
%dir %{_datadir}/gnome/help
%dir %{_datadir}/gnome/help/jokosher
%dir %{_datadir}/gnome/help/jokosher/C
%doc %{_datadir}/gnome/help/jokosher/C/*.xml
%dir %{_datadir}/gnome/help/jokosher/C/figures
%doc %{_datadir}/gnome/help/jokosher/C/figures/*.png

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.5
- Rebuilt for Fedora
* Sun May 02 2010 Toni Graffy <toni@links2linux.de> - 0.11.5-0.pm.1
- update to 0.11.5
* Wed Dec 08 2009 Toni Graffy <toni@links2linux.de> - 0.11.3-0.pm.1
- update to 0.11.3
* Sun Mar 22 2009 Toni Graffy <toni@links2linux.de> - 0.11.1-0.pm.1
- update to 0.11.1
* Fri Feb 27 2009 Toni Graffy <toni@links2linux.de> - 0.11-0.pm.1
- update to 0.11
- split off help subpackage, as this needs yelp and pulls in a lot
  of gnome packages
- split off lang subpackage
* Fri Aug 29 2008 Toni Graffy <toni@links2linux.de> - 0.10-0.pm.1
- update to 0.10
* Fri Oct 12 2007 Toni Graffy <toni@links2linux.de> - 0.9-0.pm.2
- rebuild for openSUSE-10.3
* Fri May 25 2007 Toni Graffy <toni@links2linux.de> - 0.9-0.pm.1
- update to 0.9
- repacked as tar.bz2
* Fri Nov 24 2006 Toni Graffy <toni@links2linux.de> - 0.2-0.pm.1
- update to 0.2
* Mon Oct 23 2006 Toni Graffy <toni@links2linux.de> - 0.1-0.pm.1
- build for packman
* Fri Jul 28 2006 oc2pus@arcor.de 0.1-0.oc2pus.1
- Initial build 0.1
