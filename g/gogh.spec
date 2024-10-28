%define pkg_name Gogh

Name: gogh
Version: 0.1.2.1
Release: 1
Summary: A GNU/Linux bitmap graphics editor
Group: Applications/Multimedia
License: GPLv2+ with exceptions
URL: https://www.goghproject.com
Source0: https://www.goghproject.com/%{pkg_name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: pygtk2-devel
BuildRequires: python2-setuptools
BuildRequires: gettext
Requires: python2-setuptools
Requires: pygtk2
Requires: gnome-python2
Requires: PyXML
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
Gogh is a GNU/Linux bitmap graphics editor. It is designed to work with pressure-sensitive input devices, like a Wacom tablet.
Gogh is currently under development, hovewer it is functional and has the following features:

    * Support for pressure sensitive devices - brush width and opacity may vary with pressure.
    * Pen, Smudge and Eraser brush types
    * Multiple layers with adjustable opacity
    * Zoom
    * Image resize (trim/append), image scale
    * Almost every action is undoable - even resizing the image and deleting layers
    * Images can be saved in Gogh format, or converted to PNG and JPEG formats
    * Color picker

%prep
%setup -q -n %{pkg_name}-%{version}

%build
python2 setup.py build

%install
%__rm -rf %{buildroot}
python2 setup.py install --skip-build --root=%{buildroot}
%__mkdir_p %{buildroot}%{python2_sitelib}/gogh/glade
%__cp gogh *.py* *.xml %{buildroot}%{python2_sitelib}/gogh/
%__cp glade/* %{buildroot}%{python2_sitelib}/gogh/glade
%__mkdir_p %{buildroot}%{_datadir}/locale/ru_RU/LC_MESSAGES
%__cp po/ru_RU/LC_MESSAGES/gogh.mo %{buildroot}%{_datadir}/locale/ru_RU/LC_MESSAGES/
%{__cat} > %{buildroot}%{_bindir}/gogh << EOF
#!/bin/sh
%{python2_sitelib}/gogh/gogh
EOF
%__mkdir_p %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/pixmaps
%__cp glade/gogh-symbol16.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%__cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=%{pkg_name}
Name[zh_TW]=梵谷調色盤
Comment=Bitmap graphics editor
Comment[zh_TW]=Gogh 點陣圖形編輯程式
Exec=%{name}
Icon=%{name}.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=GTK;Application;Graphics;
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{python2_sitelib}/%{name}/%{name}

%post
update-desktop-database &> /dev/null ||:
update-mime-database %{_datadir}/mime &> /dev/null ||:

%postun
update-desktop-database &> /dev/null ||:
update-mime-database %{_datadir}/mime &> /dev/null ||:

%files
%doc COPYING README
#%exclude %{python2_sitelib}/Jokosher/Profiler.py
%{python2_sitelib}/gogh*
%{python2_sitelib}/Gogh*
%{_bindir}/gogh
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Mar 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2.1
- Rebuilt for Fedora
* Wed Mar 4 2009 Wind <yc.yan@ossii.com.tw>
- Rebuild for ossii
* Mon Aug 20 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-5
- update license tag
* Mon Jun 18 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-4
- change menu entry location
* Sat Jun  9 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-3
- desktop file fixes
* Sat Jun  9 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-2
- Add yelp requires - fixes #243402
* Wed May 16 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-1
- 0.9 final
* Sat Apr 21 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-0.3.rc1
- rc1
- remove redundant directories
* Thu Apr  5 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-0.2.20070405svn
- update to svn 20070405
- added python macros
* Mon Mar 26 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-0.1.20070325svn
- Naming cleanups
* Sun Mar 25 2007 Christopher Brown <snecklifter@gmail.com> - 0-0.1.20070325svn
- naming convention changes
- dependency cleanups
- macro tidying
* Thu Mar 22 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-3.20070322svn
- updated to r1342
* Fri Mar 16 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-2.20070316svn
- r1340
- package naming guidelines
- desktop file install
- file listing and cleansing
* Sun Mar 11 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-1.20070311svn
- add ladspa dependency
* Thu Mar  8 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-1.20070308svn
- omf registration and handling
* Wed Mar  7 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-1.20070306svn
- update to r1337
- add find_lang macro
- added scrollkeeper gettext and python2-setuptools as dependencies
- added post and postun scripts
- added svn snapshot comment
* Sun Feb 25 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-1.20070225svn
- svn tagging and cleanups
* Mon Feb 19 2007 Christopher Brown <snecklifter@gmail.com> - 0.9-1
- rebuilding for 0.9 release
* Sun Sep 10 2006 Christopher Brown <snecklifter@gmail.com> - 0.1-7
- include files in source for security
* Sun Sep 10 2006 Christopher Brown <snecklifter@gmail.com> - 0.1-6
- alsaaudio patches and file permission issues
* Sun Aug 20 2006 Christopher Brown <snecklifter@gmail.com> - 0.1-5
- added patches against 0.1 release
* Thu Jul 27 2006 Christopher Brown <snecklifter@gmail.com> - 0.1-4
- remove alsaaudio dependency
- added python_dir for Extras
* Thu Jul 27 2006 Christopher Brown <snecklifter@gmail.com> - 0.1-3
- Add noarch flag and plenty of requires
- change copy file method
* Wed Jul 19 2006 Christopher Brown <snecklifter@gmail.com> - 0.1-2
- 0.1 final release with docs
* Mon Jul 17 2006 Christopher Brown <snecklifter@gmail.com> - 0.1-1
- python_dir updates and tag removal in extras submission process
* Sat Jul 15 2006 Christopher Brown <snecklifter@gmail.com> - 0.1-1
- Cleaned up file list
- Added init stuff
* Fri Jul 14 2006 Christopher Brown <snecklifter@gmail.com> - 0.1-1
- Updated to latest svn
- Updated file list
- Changed version in readiness for release
* Sun Jun 18 2006 Christopher Brown <snecklifter@gmail.com> - 0.1-20060618svn
- Added .desktop and requires information
- Updated name to meet Fedora Extras convention (hopefully)
* Sun Jun 18 2006 Christpher Brown <snecklifter@gmail.com> - 0.0.400-1
- rpmlint updates
* Sat Jun 17 2006 Christopher Brown <snecklifter@gmail.com> - 0.0.397-1
- Initial build.
