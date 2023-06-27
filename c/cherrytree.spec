%undefine _debugsource_packages
# get python version
%define __python /usr/bin/python2
%global py_ver %(if [ -f "%{__python}" ]; then %{__python} -c "import sys; sys.stdout.write(sys.version[:3])"; else echo 0; fi;)
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:           cherrytree
Version:        0.99.55
Release:        1
Summary:        Hierarchical note taking application
License:        GPLv3+
URL:            https://www.giuspen.com/cherrytree/
Source0:        https://www.giuspen.com/software/%{name}_%{version}.tar.xz
#BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python2-devel
BuildRequires:	libxml++-devel
BuildRequires:  gtksourceviewmm3-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  gspell-devel
BuildRequires:  fmt-devel
BuildRequires:  uchardet-devel
BuildRequires:  spdlog-devel
Requires:       python(abi) = %{py_ver}
Requires:       pygtk2
Requires:       pygobject2
Requires:       pygtksourceview
Requires:       python-enchant
Requires:       dbus-python
Requires:       python-appindicator
Requires:       /usr/bin/7za

%description
CherryTree is a hierarchical note taking application, featuring rich text and
syntax highlighting, storing all the data (including images) in a single XML
file with extension ".ctd".

%prep
%setup -q -n %{name}_%{version}

%build
#python2 setup.py build
export DISPLAY=:0
%cmake
%cmake_build -j1

%install
%cmake_install
#python2 setup.py install -O1 --root %{buildroot}
#py_byte_compile %{__python} %{buildroot}%{_datadir}/%{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/cherrytree.desktop

# don't include useless egg
rm -rf %{buildroot}%{python2_sitelib}

# these are no longer in use
rm -rf %{buildroot}%{_datadir}/application-registry/
rm -rf %{buildroot}%{_datadir}/mime-info/
%find_lang %{name}

%files -f %{name}.lang
%doc changelog.txt license.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
#%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/*.1*
%{_datadir}/metainfo/*
%{_includedir}/gmock
%{_includedir}/gtest
%{_libdir}/cmake/GTest
%{_libdir}/libg*
%{_libdir}/pkgconfig/*

%changelog
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.99.55
- Rebuilt for Fedora
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Mon Jul 09 2018 Oliver Haessler <oliver@redhat.com> - 0.38.5-3
- switched from Python 3 to Python 2
* Mon Jul 09 2018 Oliver Haessler <oliver@redhat.com> - 0.38.5-2
- fixed python versioning for Fedora based on the change from 
https://fedoraproject.org/wiki/Changes/Move_usr_bin_python2_into_separate_package
* Wed Jul 04 2018 Oliver Haessler <oliver@redhat.com> - 0.38.5-1
- Update to 0.38.5 including the following bugfixes:
- bugfix – when save on exit is enabled and write to disk fails, changes are lost (#358)
- bugfix – superscript and subscript tags not recognized when copied from external source (#355)
- bugfix – workaround for bug in locale module (#368)
- added syntax highlighting for go language
- implemented support for opening a text file from the command line with cherrytree
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.38.2-4
- Rebuilt for Python 3.7
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.38.2-2
- Remove obsolete scriptlets
* Tue Sep 05 2017 Oliver Haessler <oliver@redhat.com> - 0.38.2-1
- Update to 0.38.2 including the following bugfixes:
- bugfix in import from cherrytree file (links broken)
- bugfix in export to HTML (‘#’ in node name)
- left arrow key press with focus on an already collapsed tree node, now moves the selection to the node parent
- automatic syntax highlighting nodes – added right click menus cut & copy as plain text
- bugfix in recent filenames, problem with underscore character
- bugfix in import from keynote
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Wed Jun 28 2017 Oliver Haessler <oliver@redhat.com> - 0.38.1-1
- Update to 0.38.1
* Sat Apr 08 2017 Oliver Haessler <oliver@redhat.com> - 0.38.0-1
- Update to 0.38.0
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Mon Oct 03 2016 Oliver Haessler <oliver@redhat.com> - 0.37.5
- Update to 0.37.5
* Mon Aug 29 2016 Oliver Haessler <oliver@redhat.com> - 0.37.4
- Update to 0.37.4
* Wed Aug 10 2016 Oliver Haessler <oliver@redhat.com> - 0.37.3
- Update to 0.37.3
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Fri Jul 08 2016 Oliver Haessler <oliver@redhat.com> - 0.37.2
- Update to 0.37.2
* Fri May 27 2016 Oliver Haessler <oliver@redhat.com> - 0.37.0
- Update to 0.37.0
* Wed Mar 30 2016 Oliver Haessler <oliver@redhat.com> - 0.36.9-1
- Update to 0.36.9
* Tue Mar 22 2016 Oliver Haessler <oliver@redhat.com> - 0.36.8-1
- Update to 0.36.8
* Mon Feb 29 2016 Oliver Haessler <oliver@redhat.com> - 0.36.6-1
- Update to 0.36.6
* Tue Feb 23 2016 Oliver Haessler <oliver@redhat.com> - 0.36.5-1
- Update to 0.36.5
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Tue Jan 26 2016 Oliver Haessler <oliver@redhat.com> - 0.36.4-2
- added new check for using python34-devel on EPEL 7
* Tue Jan 26 2016 Oliver Haessler <oliver@redhat.com> - 0.36.4-1
- Update to 0.36.4
- changed BR: python3-devel to use the python3_pkgversion macro to build on EPEL7
* Thu Jan 14 2016 Oliver Haessler <oliver@redhat.com> - 0.36.3-1
- Update to 0.36.3
* Thu Dec  3 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.36.0-1
- BR: python3-devel to get py_byte_compile macro
* Mon Nov 23 2015 Pavel Kovar <kovar.pavel@gmail.com> - 0.36.0-1
- Update to 0.36.0
- Requires python-appindicator
- py_byte_compile step added
- desktop-file-validate added
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Oct 26 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.35.2-1
- Update to 0.35.2
* Sun Oct 12 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.35.1-1
- Update to 0.35.1
* Tue Sep 09 2014 Rex Dieter <rdieter@fedoraproject.org> 0.33.4-2
- update mime scriptlet
* Sun Jun  8 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.33.4-1
- Update to 0.33.4
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Feb  1 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.32-1
- Update to 0.32.0
* Fri Sep 27 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.30.5-1
- Update to 0.30.5, license changed to GPLv3+
- Requires python-enchant
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Wed May 29 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.29.4-1
- Update to 0.29.4
* Fri Feb  8 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.29.2-1
- Update to 0.29.2
* Sat Jan 12 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.29-1
- Update to 0.29
* Wed Dec 19 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.28.5-1
- Update to 0.28.5
* Thu Oct 11 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.28-1
- Update to 0.28 (#859463, #860086, #861571, #861780)
* Sat Sep 29 2012 ZhiQiang Fan <mr.zqfan@gmail.com> - 0.27.1-1
- Update to 0.27.1 (#834037)
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Wed Jun 13 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.26.2-1
- Update to 0.26.2
* Sun May 27 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.26-1
- Update to 0.26
* Sun Mar  4 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.25.4-1
- Update to 0.25.4
* Sat Feb 18 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.25.3-1
- Update to 0.25.3
* Wed Jan 25 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.25.2-1
- Update to 0.25.2
* Sun Jan 22 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.25.1-1
- Update to 0.25.1
* Mon Jan 16 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.25-1
- Update to 0.25
* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Sat Dec 31 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.24-1
- Update to 0.24
* Thu Nov  3 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.23.1-1
- Update to 0.23.1
- Add manuall python(abi) requirement
* Thu Jun 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.22.1-1
- Update to 0.22.1
* Mon Apr 25 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.21-1
- Update to 0.21
* Tue Mar 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.20.1-1
- Update to 0.20.1
* Tue Mar 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.20.1-1
- Update to 0.20
* Sat Jan 22 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19.3-2
- Omit %%{_datadir}/application-registry/ and %%{_datadir}/mime-info/
* Fri Jan 21 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19.3-2
- Remove useless egg and manually add python(abi) requirement
* Mon Jan 17 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19.3-1
- Update to 0.19.3
* Sat Jan 15 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19.2-1
- Update to 0.19.2
- Drop cherrytree.glade.h again
- Make sure cherrytree.desktop is not executable
* Tue Jan 11 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19.1-1
- Update to 0.19.1
- Use setup.py instead of manual installation
- BR python2-devel instead of python-devel
* Tue Jan 04 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19-2
- Drop cherrytree.glade.h
* Mon Jan 03 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19-1
- Update to 0.19
* Wed Dec 29 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.18.1-1
- Update to 0.18.1
* Mon Dec 20 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.17.1-1
- Inital package
