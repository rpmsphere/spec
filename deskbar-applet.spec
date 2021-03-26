%define name deskbar-applet
%define version 2.32.0
%define release %mkrel 9

%define _requires_exceptions pkgconfig\(.*\)

Summary: All-in-one search bar for the GNOME panel
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/deskbar-applet/%{name}-%{version}.tar.bz2
Patch1: deskbar-applet-2.25.3-seamonkey.patch
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/DeskbarApplet
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel
BuildRequires: pygtk2.0-devel
BuildRequires: gnome-python-extras
BuildRequires: gnome-python-applet
BuildRequires: gnome-python-devel
BuildRequires: evolution-data-server-devel
BuildRequires: gnome-desktop-devel
BuildRequires: dbus-python
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: gnome-doc-utils docbook-dtd42-xml
BuildRequires: gnome-python-devel
BuildRequires: firefox
BuildRequires: scrollkeeper
BuildRequires: chrpath
Requires: gnome-python-extras
Requires: gnome-python-gconf
Requires: gnome-python-applet
Requires: python-elementtree
Requires: dbus-python
Requires(post): scrollkeeper
Requires(postun): scrollkeeper
Suggests: libmozilla-firefox

%description
The Deskbar is an all-in-one search bar. It is a Linux/Gnome panel
applet that is similar to Google's (Windows only) Deskbar
It supports the search in Mozilla Firefox and Epiphany.

%prep
%setup -q
%patch1 -p1 -b .seamonkey

%build
%configure2_5x --disable-scrollkeeper --disable-schemas-install
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std pythondir=%py_platsitedir
%find_lang %name
%find_lang deskbar --with-gnome
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done
cat deskbar.lang >> %name.lang

find  %buildroot -name \*.so |xargs chrpath -d

%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas %name
%update_icon_cache hicolor
%update_scrollkeeper

%preun
%preun_uninstall_gconf_schemas %name

%postun
%clean_icon_cache hicolor
%clean_scrollkeeper

%files -f %name.lang
%defattr(-,root,root)
%doc README NEWS TODO AUTHORS
%_sysconfdir/gconf/schemas/deskbar-applet.schemas
%_libdir/bonobo/servers/*
%_libdir/%name/
%py_platsitedir/*deskbar*
%_libdir/pkgconfig/%name.pc
%_datadir/%name
%_datadir/icons/hicolor/*/apps/*
%dir %_datadir/omf/*/
%_datadir/omf/*/*-C.omf


%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 2.32.0-7mdv2011.0
+ Revision: 677662
- rebuild to add gconftool as req

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.32.0-6
+ Revision: 663763
- mass rebuild

* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-5mdv2011.0
+ Revision: 592973
- rebuild
- rebuild for new python 2.7

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581341
- update to new version 2.32.0

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-3mdv2011.0
+ Revision: 568222
- rebuild for new e-d-s

* Mon Jun 21 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.1-2mdv2010.1
+ Revision: 548451
- Rebuild with latest eds

  + Götz Waschk <waschk@mandriva.org>
    - disable schemas installation at build time

* Tue May 04 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 541964
- disable beagle support
- update to new version 2.30.1

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528786
- update to new version 2.30.0

* Tue Feb 23 2010 Götz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 510197
- update to new version 2.29.91

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 2.29.90-1mdv2010.1
+ Revision: 502893
- update to new version 2.29.90

* Tue Oct 06 2009 Thierry Vignaud <tv@mandriva.org> 2.28.0-3mdv2010.0
+ Revision: 454735
- do not package huge ChangeLog

* Fri Sep 25 2009 Olivier Blin <oblin@mandriva.com> 2.28.0-2mdv2010.0
+ Revision: 448873
- disable beagle on arches without it (from Arnaud Patard)

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 447257
- update to new version 2.28.0

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437467
- update to new version 2.27.92

* Mon Aug 24 2009 Götz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 420469
- update to new version 2.27.91

* Mon Aug 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 414417
- update to new version 2.27.90

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 401416
- update to new version 2.27.5

* Mon Jul 13 2009 Götz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 395622
- update to new version 2.27.4

* Mon Jun 15 2009 Götz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 386124
- update to new version 2.27.3

* Mon May 25 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 379682
- update to new version 2.27.2

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374186
- new version

* Mon Apr 20 2009 Götz Waschk <waschk@mandriva.org> 2.26.1-3mdv2009.1
+ Revision: 368403
- fix python dir (bug #50035)

* Wed Apr 15 2009 Götz Waschk <waschk@mandriva.org> 2.26.1-2mdv2009.1
+ Revision: 367280
- fix file list
- update to new version 2.26.1

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356860
- update to new version 2.26.0

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 347518
- update to new version 2.25.92

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341235
- update to new version 2.25.91

* Mon Feb 02 2009 Götz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 336524
- update to new version 2.25.90

* Mon Jan 19 2009 Götz Waschk <waschk@mandriva.org> 2.25.5-1mdv2009.1
+ Revision: 331373
- update to new version 2.25.5

* Tue Jan 06 2009 Götz Waschk <waschk@mandriva.org> 2.25.4-1mdv2009.1
+ Revision: 325234
- update to new version 2.25.4

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 2.25.3-2mdv2009.1
+ Revision: 319527
- rebuild with python 2.6

* Fri Dec 19 2008 Götz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 316135
- new version
- update the patch

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 309315
- update to new version 2.25.2
- remove gnomevfs dep

* Tue Nov 04 2008 Götz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 299715
- update to new version 2.25.1

* Tue Oct 21 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295919
- update to new version 2.24.1

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287266
- new version

* Tue Sep 09 2008 Götz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282908
- new version
- remove workaround patch for x86_64 crash

* Tue Sep 02 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-2mdv2009.0
+ Revision: 278834
- work around iurt bug
- bump
- new version

* Tue Aug 19 2008 Götz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273557
- new version

* Tue Aug 05 2008 Götz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263722
- new version

* Tue Jul 22 2008 Götz Waschk <waschk@mandriva.org> 2.23.5-1mdv2009.0
+ Revision: 240042
- new version

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.4-1mdv2009.0
+ Revision: 231164
- new version

* Mon Jun 30 2008 Götz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 230366
- new version
- update license

* Tue May 27 2008 Götz Waschk <waschk@mandriva.org> 2.22.2.1-1mdv2009.0
+ Revision: 211565
- new version

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 192477
- new version

* Tue Mar 11 2008 Götz Waschk <waschk@mandriva.org> 2.22.0.1-1mdv2008.1
+ Revision: 185935
- new version

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183688
- new version

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 174988
- new version
- update the patch

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165735
- remove rpath
- fix buildrequires
- new version

* Tue Jan 29 2008 Götz Waschk <waschk@mandriva.org> 2.21.90.1-1mdv2008.1
+ Revision: 159990
- new version

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 159495
- new version

* Mon Jan 14 2008 Götz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 151813
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 2.21.4-2mdv2008.1
+ Revision: 132161
- BR gnome-python-devel

* Mon Dec 17 2007 Götz Waschk <waschk@mandriva.org> 2.21.4-1mdv2008.1
+ Revision: 131631
- fix buildrequires
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 04 2007 Götz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 115208
- new version
- rediff patch 1

* Wed Nov 14 2007 Götz Waschk <waschk@mandriva.org> 2.21.2-1mdv2008.1
+ Revision: 108576
- new version

* Thu Oct 18 2007 Funda Wang <fwang@mandriva.org> 2.20.1-2mdv2008.1
+ Revision: 99857
- Rebuild against FF 2.0.0.7

* Mon Oct 15 2007 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 98628
- fix buildrequires
- new version

* Tue Sep 18 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89450
- new version
- drop patches 2,3

* Tue Sep 04 2007 Götz Waschk <waschk@mandriva.org> 2.19.92-3mdv2008.0
+ Revision: 79210
- replace some hard deps by suggests (bug #33126)

* Tue Sep 04 2007 Götz Waschk <waschk@mandriva.org> 2.19.92-2mdv2008.0
+ Revision: 79178
- add fixes from svn for the gdm logout and evo address book search

* Mon Sep 03 2007 Götz Waschk <waschk@mandriva.org> 2.19.92-1mdv2008.0
+ Revision: 78555
- new version

* Mon Aug 27 2007 Götz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 71939
- new version

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 2.19.90.1-1mdv2008.0
+ Revision: 63316
- new version
- update patch 1

* Tue Aug 07 2007 Götz Waschk <waschk@mandriva.org> 2.19.6.1-1mdv2008.0
+ Revision: 59769
- new version
- drop patch 2

* Mon Aug 06 2007 Götz Waschk <waschk@mandriva.org> 2.19.6-1mdv2008.0
+ Revision: 59327
- rename patch1, it only handles seamonkey now
- relax dep on firefox
- update file list
- patch to fix build problem
- new version
- update the patch

* Tue Jul 31 2007 Götz Waschk <waschk@mandriva.org> 2.19.5-2mdv2008.0
+ Revision: 57224
- rebuild

* Tue Jul 10 2007 Götz Waschk <waschk@mandriva.org> 2.19.5-1mdv2008.0
+ Revision: 50857
- new version
- rediff patch 1

* Fri Jun 15 2007 Götz Waschk <waschk@mandriva.org> 2.19.3-2mdv2008.0
+ Revision: 39888
- rebuild for new ff
- new version

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 13821
- new version


* Fri Mar 23 2007 Frederic Crozat <fcrozat@mandriva.com> 2.18.0-3mdv2007.1
+ Revision: 148531
- Force rebuild with correct firefox version this time

* Fri Mar 23 2007 Götz Waschk <waschk@mandriva.org> 2.18.0-2mdv2007.1
+ Revision: 148361
- rebuild for new firefox

* Wed Mar 14 2007 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 143475
- new version
- update seamonkey version

* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 2.17.93-1mdv2007.1
+ Revision: 142049
- new version

* Thu Mar 08 2007 Frederic Crozat <fcrozat@mandriva.com> 2.17.92-2mdv2007.1
+ Revision: 137721
- Disable pkgconfig auto dependencies

* Wed Feb 28 2007 Götz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 127236
- new version

* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 2.17.91-2mdv2007.1
+ Revision: 126287
- rebuild for new firefox

* Mon Feb 12 2007 Götz Waschk <waschk@mandriva.org> 2.17.91-1mdv2007.1
+ Revision: 118848
- new version

* Tue Jan 23 2007 Götz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.1
+ Revision: 112239
- new version

* Thu Jan 11 2007 Götz Waschk <waschk@mandriva.org> 2.17.5.1-1mdv2007.1
+ Revision: 107454
- fix buildrequires
- new version
- handle scrollkeeper

* Mon Jan 08 2007 Götz Waschk <waschk@mandriva.org> 2.17.2-4mdv2007.1
+ Revision: 106100
- rebuild

* Fri Dec 15 2006 Götz Waschk <waschk@mandriva.org> 2.17.2-3mdv2007.1
+ Revision: 97465
- depend on beagle-gui

* Thu Dec 07 2006 Götz Waschk <waschk@mandriva.org> 2.17.2-2mdv2007.1
+ Revision: 92021
- remove old stuff
- fix patch for new firefox

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 2.17.2-1mdv2007.1
+ Revision: 88262
- fix file list
- new version

* Wed Nov 22 2006 Götz Waschk <waschk@mandriva.org> 2.16.2-2mdv2007.1
+ Revision: 86435
- bot rebuild
- new version

* Thu Nov 09 2006 Götz Waschk <waschk@mandriva.org> 2.16.1-3mdv2007.1
+ Revision: 79283
- bot rebuild
- rebuild for new firefox

* Mon Oct 23 2006 Götz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.1
+ Revision: 71693
- Import deskbar-applet

* Mon Oct 23 2006 Götz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.1
- unpack patch
- New version 2.16.1

* Tue Sep 19 2006 Frederic Crozat <fcrozat@mandriva.com> 2.16.0-3mdv2007.0
- Drop conflicts, replaced by requires on firefox lib package

* Sun Sep 17 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-2mdv2007.0
- rebuild for new firefox

* Tue Sep 05 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Wed Aug 30 2006 Götz Waschk <waschk@mandriva.org> 2.15.92.1-1mdv2007.0
- New release 2.15.92.1

* Fri Aug 25 2006 Götz Waschk <waschk@mandriva.org> 2.15.92-1mdv2007.0
- remove menu entry
- New release 2.15.92

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 2.15.91-1mdv2007.0
- New release 2.15.91

* Fri Aug 04 2006 Götz Waschk <waschk@mandriva.org> 2.15.90.1-1mdv2007.0
- rebuild for new firefox

* Sun Jul 30 2006 Götz Waschk <waschk@mandriva.org> 2.15.90.1-4mdv2007.0
- rebuild for new firefox

* Fri Jul 28 2006 Götz Waschk <waschk@mandriva.org> 2.15.90.1-3mdv2007.0
- don't use Xvfb anymore

* Fri Jul 28 2006 Götz Waschk <waschk@mandriva.org> 2.15.90.1-2mdv2007.0
- fix deps

* Thu Jul 27 2006 Götz Waschk <waschk@mandriva.org> 2.15.90.1-1mdv2007.0
- fix buildrequires
- drop patch 2
- New release 2.15.90.1

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-2mdv2007.0
- patch for new e-d-s

* Tue Jul 25 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-1
- New release 2.15.90

* Wed Jul 12 2006 Götz Waschk <waschk@mandriva.org> 2.15.4-1mdv2007.0
- new macros
- fix menu
- New release 2.15.4

* Tue Jun 20 2006 Austin Acton <austin@mandriva.org> 2.15.3-2mdv2007.0
- requires dbus-python

* Wed Jun 14 2006 Götz Waschk <waschk@mandriva.org> 2.15.3-1mdv2007.0
- update file list
- New release 2.15.3

* Wed Jun 07 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.2.1-1mdv2007.0
- Release 2.15.2.1

* Mon Jun 05 2006 Götz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.1
- Rebuild

* Mon May 29 2006 Götz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- fix buil
- New release 2.14.2

* Thu May 04 2006 Götz Waschk <waschk@mandriva.org> 2.14.1.1-3mdk
- rebuild for new firefox

* Sat Apr 22 2006 Götz Waschk <waschk@mandriva.org> 2.14.1.1-2mdk
- rebuild for new firefox

* Tue Apr 18 2006 Götz Waschk <waschk@mandriva.org> 2.14.1.1-1mdk
- New release 2.14.1.1

* Sun Apr 16 2006 Götz Waschk <waschk@mandriva.org> 2.14.1-2mdk
- seamonkey instead of mozilla
- rebuild for new e-d-s

* Tue Apr 11 2006 Götz Waschk <waschk@mandriva.org> 2.14.1-1mdk
- New release 2.14.1

* Tue Mar 14 2006 Götz Waschk <waschk@mandriva.org> 2.14.0.1-1mdk
- New release 2.14.0.1

* Sun Mar 12 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- New release 2.14.0

* Tue Feb 28 2006 Götz Waschk <waschk@mandriva.org> 2.13.92-1mdk
- New release 2.13.92

* Tue Feb 14 2006 Götz Waschk <waschk@mandriva.org> 2.13.91-1mdk
- New release 2.13.91

* Sun Feb 05 2006 Götz Waschk <waschk@mandriva.org> 2.13.90.1-1mdk
- rediff the patch
- New release 2.13.90.1

* Fri Feb 03 2006 Götz Waschk <waschk@mandriva.org> 2.13.90-2mdk
- rebuild for new mozilla-firefox

* Tue Jan 31 2006 Götz Waschk <waschk@mandriva.org> 2.13.90-1mdk
- fix build
- fix buildrequires
- New release 2.13.90

* Mon Jan 23 2006 Götz Waschk <waschk@mandriva.org> 0.8.8-3mdk
- update file list for new python dirs

* Tue Jan 17 2006 Götz Waschk <waschk@mandriva.org> 0.8.8-2mdk
- fix buildrequires

* Mon Jan 16 2006 Götz Waschk <waschk@mandriva.org> 0.8.8-1mdk
- New release 0.8.8

* Tue Jan 10 2006 Götz Waschk <waschk@mandriva.org> 0.8.7-2mdk
- rebuild for new mozilla-firefox

* Tue Jan 03 2006 Götz Waschk <waschk@mandriva.org> 0.8.7-1mdk
- update the patch
- New release 0.8.7

* Mon Dec 12 2005 Götz Waschk <waschk@mandriva.org> 0.8.6.1-1mdk
- New release 0.8.6.1

* Fri Dec 09 2005 Götz Waschk <waschk@mandriva.org> 0.8.6-1mdk
- update file list
- fix deps
- fix source URL
- rediff the patch
- New release 0.8.6
- use mkrel

* Tue Nov 15 2005 Götz Waschk <waschk@mandriva.org> 0.8.5-1mdk
- New release 0.8.5

* Tue Nov 01 2005 Götz Waschk <waschk@mandriva.org> 0.8.4-1mdk
- New release 0.8.4

* Sun Oct 30 2005 Götz Waschk <waschk@mandriva.org> 0.8.3-1mdk
- New release 0.8.3

* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 0.8.2-2mdk
- rebuild for new mozilla

* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 0.8.2-1mdk
- New release 0.8.2

* Tue Oct 25 2005 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdk
- update file list
- fix buildrequires
- drop patch 0
- New release 0.8.0

* Fri Oct 21 2005 Götz Waschk <waschk@mandriva.org> 0.6-5mdk
- fix firefox path (bug #19363)

* Sat Oct 15 2005 Götz Waschk <waschk@mandriva.org> 0.6-4mdk
- fix deps
- make it actually work with libexecdir == libdir

* Sat Oct 15 2005 Götz Waschk <waschk@mandriva.org> 0.6-3mdk
- fix summary, thanks to nitpicking Dick Gevers :-)

* Sat Oct 15 2005 Götz Waschk <waschk@mandriva.org> 0.6-2mdk
- fix buildrequires

* Sat Oct 15 2005 Götz Waschk <waschk@mandriva.org> 0.6-1mdk
- initial package

