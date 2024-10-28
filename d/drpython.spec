%undefine _debugsource_packages
Name:           drpython
Summary:        Python editor and development environment
Version:        3.11.1
#Version:       3.11.4
Release:        8.1
Source:         https://prdownloads.sourceforge.net/drpython/%{name}-%{version}.zip
URL:            https://drpython.sourceforge.net/
License:        GPLv2
Group:          Development/Python
Requires:       python2-wxpython
BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
BuildArch:      noarch

%description
DrPython is a highly customizable, simple, and clean editing environment for
developing Python programs. It is intended primarily for use in schools, and
is a tribute to DrScheme.

%prep
%setup -q -n %{name}_%{version}
chmod 644 %name.py
#use xdg-open for the help instead of non existing mozilla
sed --in-place "s/mozilla/xdg-open/" drPreferences.py

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root=$RPM_BUILD_ROOT
echo 'python2 %python2_sitelib/%name/%name.pyw' >> $RPM_BUILD_ROOT/%_bindir/%name
chmod 755 $RPM_BUILD_ROOT/%_bindir/%name
rm -f $RPM_BUILD_ROOT/%_bindir/postinst.py

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Dr. Python
Comment=Python Editor and IDE
Exec=%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;IDE;
EOF

#icons
install -Dm644 documentation/%name.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%name.png

%files
%doc examples/ *.txt
%{_bindir}/%name
%python2_sitelib/%name
%python2_sitelib/DrPython-%{version}-py*.egg-info
%{_datadir}/pixmaps/%name.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.11.1
- Rebuilt for Fedora
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 1:3.11.1-3mdv2011.0
+ Revision: 592385
- rebuild for python 2.7
* Fri Feb 19 2010 Sandro Cazzaniga <kharec@mandriva.org> 1:3.11.1-2mdv2010.1
+ Revision: 508001
- fix licence tag
  + Frederik Himpe <fhimpe@mandriva.org>
    - Update to new version 3.11.1
* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 1:3.11.0-3mdv2009.1
+ Revision: 324225
- fix file list
  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick
* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1:3.11.0-3mdv2009.0
+ Revision: 244549
- rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Wed Feb 27 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.11.0-1mdv2008.1
+ Revision: 175672
- new version
* Fri Jan 18 2008 Alexander Kurtakov <akurtakov@mandriva.org> 165-2mdv2008.1
+ Revision: 154733
- fix help browser (use xdg-open instead of non-existing mozilla)
  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Thu May 24 2007 Adam Williamson <awilliamson@mandriva.org> 165-1mdv2008.0
+ Revision: 30589
- generate and package fd.o icons
- install correctly: use setup.py and install to python2_sitelib
- new version 165
- Import drpython
* Tue Sep 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 161-2mdv2007.0
- XDG
* Sun May 07 2006 Jerome Soyer <saispo@mandriva.org> 161-1mdk
- New release 161
* Thu Oct 13 2005 Lenny Cartier <lenny@mandriva.com> 3.10.13-1mdk
- 3.10.13
* Tue Mar 01 2005 Jerome Soyer <saispo@mandrake.org> 3.10.12-1mdk
- 3.10.12
* Wed Feb 23 2005 Jerome Soyer <saispo@mandrake.org> 3.10.10-1mdk
- 3.10.10
* Sun Feb 20 2005 Jerome Soyer <saispo@mandrake.org> 3.10.7-1mdk
- 3.10.7
* Fri Feb 18 2005 Jerome Soyer <saispo@mandrake.org> 3.10.6-1mdk
- 3.10.6
* Tue Feb 15 2005 Jerome Soyer <saispo@mandrake.org> 3.10.4-1mdk
- 3.10.4
* Mon Feb 14 2005 Jerome Soyer <saispo@mandrake.org> 3.10.3-1mdk
- 3.10.3
* Sun Feb 13 2005 Jerome Soyer <saispo@mandrake.org> 3.10.2-1mdk
- 3.10.2
* Sat Feb 12 2005 Jerome Soyer <saispo@mandrake.org> 3.10.1-1mdk
- 3.10.1
* Fri Feb 11 2005 Jerome Soyer <saispo@mandrake.org> 3.10.0-1mdk
- 3.10.0
* Wed Feb 09 2005 Jerome Soyer <saispo@mandrake.org> 3.9.10-1mdk
- 3.9.10
* Tue Feb 08 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.9.9-1mdk
- 3.9.9
* Fri Feb 04 2005 Jerome Soyer <saispo@mandrake.org> 3.9.6-1mdk
- 3.9.6
* Sat Jan 29 2005 Jerome Soyer <saispo@mandrake.org> 3.9.5-1mdk
- 3.9.5
* Tue Jan 25 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.9.4-1mdk
- 3.9.4
* Sun Jan 23 2005 Jerome Soyer <saispo@mandrake.org> 3.9.2-1mdk
- 3.9.2
* Wed Jan 12 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.8.5-1mdk
- 3.8.5
* Fri Jan 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.8.3-1mdk
- 3.8.3
* Thu Jan 06 2005 Jerome Soyer <saispo@mandrake.org> 3.8.2-1mdk
- 3.8.2
* Sat Jan 01 2005 Jerome Soyer <saispo@mandrake.org> 3.8.0-1mdk
- 3.8.0
- Happy New Year !
* Fri Dec 24 2004 Jerome Soyer <saispo@mandrake.org> 3.7.9-1mdk
- 3.7.9
* Mon Dec 20 2004 Jerome Soyer <saispo@mandrake.org> 3.7.8-1mdk
- 3.7.8
* Fri Dec 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.7.6-1mdk
- 3.7.6
* Mon Dec 06 2004 Jerome Soyer <saispo@mandrake.org> 3.7.3-1mdk
- 3.7.3
- Build with new Python
* Tue Nov 30 2004 Jerome Soyer <saispo@mandrake.org> 3.7.0-1mdk
- 3.7.0
* Tue Nov 09 2004 Jerome Soyer <saispo@mandrake.org> 3.6.10-1mdk
- 3.6.10
* Sat Nov 06 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.6.9-1mdk
- 3.6.9
- install documentation in the right path
* Fri Oct 29 2004 Jerome Soyer <saispo@mandrake.org> 3.6.6-1mdk
- 3.6.6
* Wed Oct 27 2004 Jerome Soyer <saispo@mandrake.org> 3.6.5-1mdk
- 3.6.5
* Tue Oct 26 2004 Jerome Soyer <saispo@mandrake.org> 3.6.4-1mdk
- 3.6.4
* Sat Oct 23 2004 Jerome Soyer <saispo@mandrake.org> 3.6.3-1mdk
- 3.6.3
* Fri Oct 22 2004 Jerome Soyer <saispo@mandrake.org> 3.6.2-1mdk
- 3.6.2
* Thu Oct 21 2004 Jerome Soyer <saispo@mandrake.org> 3.6.1-1mdk
- 3.6.1
* Tue Oct 19 2004 Jerome Soyer <saispo@mandrake.org> 3.6.0-1mdk
- 3.6.0
* Mon Oct 11 2004 Jerome Soyer <saispo@mandrake.org> 3.5.9-1mdk
- 3.5.9
* Sat Oct 09 2004 Jerome Soyer <saispo@mandrake.org> 3.5.8-1mdk
- 3.5.8
* Wed Oct 06 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.5.6-1mdk
- 3.5.6
* Thu Sep 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.5.3-1mdk
- 3.5.3
* Thu Sep 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.5.0-1mdk
- 3.5.0
* Mon Sep 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.7-1mdk
- 3.4.7
* Wed Sep 08 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.5-1mdk
- 3.4.5
* Wed Sep 01 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.3-1mdk
- 3.4.3
* Thu Aug 26 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0
* Fri Aug 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.3.7-1mdk
- 3.3.7
* Fri Aug 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.3.3-1mdk
- 3.3.3
* Mon Aug 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2
* Mon Aug 2 2004 Austin Acton <austin@mandrake.org> 3.3.0-1mdk
- 3.3.0
* Thu Jul 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.2.0-1mdk
- 3.2.0
* Fri Jun 25 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.0.7-1mdk
- 3.0.7
* Tue Jun 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.0.6-1mdk
- 3.0.6
* Sat Jun 19 2004 Austin Acton <austin@mandrake.org> 3.0.4-1mdk
- 3.0.4
* Mon Jun 14 2004 Austin Acton <austin@mandrake.org> 3.0.1-1mdk
- 3.0.1
- new menu
* Fri Apr 2 2004 Austin Acton <austin@mandrake.org> 2.3.5-1mdk
- 2.3.5
* Sun Feb 22 2004 Austin Acton <austin@mandrake.org> 2.2.7-1mdk
- 2.2.7
* Fri Feb 21 2004 Austin Acton <austin@mandrake.org> 2.2.6-1mdk
- 2.2.6
* Sun Feb 15 2004 Austin Acton <austin@mandrake.org> 2.2.3-1mdk
- 2.2.3
* Mon Feb 9 2004 Austin Acton <austin@mandrake.org> 2.2.1-1mdk
- 2.2.1
* Sun Feb 8 2004 Austin Acton <austin@mandrake.org> 2.1.4-2mdk
- oops, make it run (James Sparenberg)
- put in /usr/share
* Wed Jan 28 2004 Austin Acton <austin@mandrake.org> 2.1.4-1mdk
- 2.1.4
* Sat Jan 24 2004 Austin Acton <austin@mandrake.org> 2.1.0-1mdk
- 2.1.0
* Sat Jan 17 2004 Austin Acton <austin@mandrake.org> 2.0.3-1mdk
- 2.0.3
* Wed Jan 14 2004 Franck Villaume <fvill@freesurf.fr> 2.0.2-2mdk
- BuildRequires : ImageMagick
* Thu Jan 8 2004 Austin Acton <austin@linux.ca> 2.0.2-1mdk
- initial package
