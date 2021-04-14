%undefine _debugsource_packages
Name:           font-manager
Version:        0.8.4
Release:        1
Summary:        A simple font management application for Gtk+ Desktop Environments
Group:          Applications/Publishing
License:        GPLv3+
URL:            http://code.google.com/p/%{name}
Source0:        https://github.com/FontManager/master/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  cairo-devel fontconfig-devel freetype-devel glib2-devel 
BuildRequires:  intltool json-glib-devel libappstream-glib
BuildRequires:  pango-devel sqlite-devel yelp-tools gtk3-devel meson
BuildRequires:  vala gobject-introspection-devel libgee-devel libxml2-devel
#BuildRequires:  file-roller nemo-python-devel gucharmap-devel nautilus-python-devel

%description
Font Manager is intended to provide a way for average users to easily
manage desktop fonts, without having to resort to command line tools
or editing configuration files by hand. While designed primarily with
the Gnome Desktop Environment in mind, it should work well with other
Gtk+ desktop environments.

Font Manager is NOT a professional-grade font management solution.

%prep
%setup -q

%build
#configure --disable-schemas-compile --with-nautilus --with-nemo
meson --prefix=/usr build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %name

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc README.md COPYING CHANGELOG
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/help/*/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/gnome-shell/search-providers/org.gnome.FontManager.SearchProvider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Font*.png

%changelog
* Sun Apr 4 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.4
- Rebuilt for Fedora
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Dec 23 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.7.2-3
- add nemo sub-package
- move nautilus-python requires to nautilus sub-package
* Tue Aug 18 2015 Jean-Francois Saucier <jsaucier@gmail.com> - 0.7.2-2
- Update to new upstream version, based on Jerry Casiano spec file
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.5.7-11
- Add an AppData file for the software center
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Sat Aug 04 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.5.7-6
- Fix FTBFS for gcc-4.7
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Sun Jan 15 2012 Ian Weller <iweller@redhat.com> - 0.5.7-4
- Requires: python-reportlab
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sun Jan  2 2011 Jean-Francois Saucier <jsaucier@gmail.com> - 0.5.7-1
- Update to the new upstream version
* Wed Sep 29 2010 jkeating - 0.5.6-2
- Rebuilt for gcc bug 634757
* Wed Sep 15 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.5.6-1
- Rebuild new version
* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Thu Jul  8 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.5.5.4-1
- Rebuild the new version
* Fri Jun 18 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.5.4-5
- Include upstream patch for debuginfo and compilation issue
* Tue Jun  8 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.5.4-4
- Fix library issue
- Fix compilation issue with Fedora
- Fix the creation of a useful debuginfo package
* Thu Jun  3 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.5.4-3
- Include some fixes by upstream for the compilation error on x86_64
* Thu Jun  3 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.5.4-2
- Fix the compilation error on x86_64
- Fix some BuildRequires for the new version
* Wed Jun  2 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.5.4-1
- Update to new upstream version
* Wed Apr 14 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.4.4-1
- Update to new upstream version
* Sun Jan 17 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.4.3-1
- Update to new upstream version
- Remove patches as they are not necessary anymore
- Adjust python optimization
* Wed Jan  6 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.4.2-5
- Fix license string
- Fix upstream Makefile to include *.py file with *.pyc and *.pyo
* Sun Jan  3 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.4.2-4
- Fix permission problem on .desktop file directly with a patch
* Sun Jan  3 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.4.2-3
- Fix permission problem on .desktop file
- Fix wildcards problem in file section
* Sun Jan  3 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.4.2-2
- Fix as per the recommendations on bug #551878
* Sat Jan  2 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.4.2-1
- Initial build for Fedora
