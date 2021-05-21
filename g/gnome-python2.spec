%define __python /usr/bin/python2
# Last updated for 2.28.0
# The order here corresponds to that in configure.ac,
# for easier comparison.  Please do not alphabetize.
%define pygtk_version                   2.10.3
%define pyorbit_version                 2.0.1
%define glib_version                    2.6.0
%define gtk_version                     2.6.0
%define libgnome_version                2.8.0
%define libgnomeui_version              2.8.0
%define libgnomecanvas_version          2.8.0
%define libgnomevfs_version             2.14.0
%define gconf_version                   2.11.1
%define libbonobo_version               2.8.0
%define libbonoboui_version             2.8.0
%define pygobject_version               2.17.0
%define python_version                  2.7.0

### Abstract ###

Name: gnome-python2
Version: 2.28.1
Release: 14
License: LGPLv2+
Group: Development/Languages
Summary: PyGNOME Python extension module
URL: http://download.gnome.org/sources/gnome-python/
#VCS: git:git://git.gnome.org/gnome-python
Source: http://download.gnome.org/sources/gnome-python/2.28/gnome-python-%{version}.tar.bz2

### Dependencies ###

Requires: pygtk2%{?_isa} >= %{pygtk_version}

### Build Dependencies ###

BuildRequires: libbonobo-devel >= %{libbonobo_version}
BuildRequires: libbonoboui-devel >= %{libbonoboui_version}
BuildRequires: libgnome-devel >= %{libgnome_version}
BuildRequires: libgnomeui-devel >= %{libgnomeui_version}
BuildRequires: pygtk2-devel >= %{pygtk_version}
BuildRequires: pyorbit-devel >= %{pyorbit_version}
BuildRequires: python2-devel >= %{python_version}

# added 2005-02-07, pkg last available in Fedora 3 and RHEL 4
Obsoletes: gnome-python2-nautilus <= 2.6.0

%description
The gnome-python package contains the source packages for the Python
bindings for GNOME called PyGNOME.

PyGNOME is an extension module for Python that provides access to the
base GNOME libraries, so you have access to more widgets, a simple
configuration interface, and metadata support.

%package gnome
Summary: Python bindings for libgnome
Group: Development/Languages
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gnomevfs%{?_isa} = %{version}-%{release}
# explicit just for the minimum version
Requires: libgnome%{?_isa} >= %{libgnome_version}
Requires: libgnomeui%{?_isa} >= %{libgnomeui_version}
# gnome.ui imports bonobo.ui (bz #689836)
Requires: %{name}-bonobo%{?_isa} = %{version}-%{release}

%description gnome
This module contains a wrapper that makes libgnome functionality available
from Python.


%package canvas
Summary: Python bindings for the GNOME Canvas
Group: Development/Languages
Requires: %{name}%{?_isa} = %{version}-%{release}
# explicit just for the minimum version
Requires: gtk2%{?_isa} >= %{gtk_version}
Requires: libgnomecanvas%{?_isa} >= %{libgnomecanvas_version}

%description canvas
This module contains a wrapper that allows use of the GNOME Canvas
in Python.

%package bonobo
Summary: Python bindings for interacting with Bonobo
Group: Development/Languages
Requires: %{name}%{?_isa} = %{version}-%{release}
# explicit just for the minimum version
Requires: libbonobo%{?_isa} >= %{libbonobo_version}
Requires: libbonoboui%{?_isa} >= %{libbonoboui_version}
Requires: pyorbit%{?_isa} >= %{pyorbit_version}
# this is provided by libbonobo
# bonobo.ui imports gnomecanvas (bz #689836)
Requires: %{name}-canvas%{?_isa} = %{version}-%{release}

%description bonobo
This module contains a wrapper that allows the creation of bonobo
components and the embedding of bonobo components in Python.

%package gconf
Summary: Python bindings for interacting with GConf
Group: Development/Languages
Requires: %{name}%{?_isa} = %{version}-%{release}
# explicit just for the minimum version
Requires: GConf2%{?_isa} >= %{gconf_version}

%description gconf
This module contains a wrapper that allows the use of GConf via Python.

%package gnomevfs
Summary: Python bindings for interacting with gnome-vfs
Group: Development/Languages
Requires: %{name}%{?_isa} = %{version}-%{release}
# explicit just for the minimum version
Requires: gnome-vfs2%{?_isa} >= %{libgnomevfs_version}
Requires: libbonobo%{?_isa} >= %{libbonobo_version}

%description gnomevfs
This module contains a wrapper that allows the use of gnome-vfs via python.

%package devel
Summary: Development files for building add-on libraries
Group: Development/Languages
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gnome-vfs2-devel%{?_isa} >= %{libgnomevfs_version}
#Requires: python2%{?_isa} >= %{python_version}
Requires: pkgconfig

%description devel
This package contains files required to build wrappers for GNOME add-on
libraries so that they interoperate with gnome-python2.

%prep
%setup -q -n gnome-python-%{version}
sed -i 's|python python2|python2|' configure

%build
%configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm {} \;

%files
%doc AUTHORS ChangeLog NEWS
%dir %{python2_sitearch}/gtk-2.0/gnome/
%dir %{_datadir}/pygtk/2.0/defs
%dir %{_datadir}/pygtk/2.0/argtypes

%files gnome
%{python2_sitearch}/gtk-2.0/gnome/__init__.*
%{python2_sitearch}/gtk-2.0/gnome/_gnome.so
%{python2_sitearch}/gtk-2.0/gnome/ui.so
%{_datadir}/pygtk/2.0/defs/ui.defs
%{_datadir}/pygtk/2.0/defs/gnome.defs
%{_datadir}/pygtk/2.0/defs/gnome-types.defs

%files canvas
%{python2_sitearch}/gtk-2.0/gnome/canvas.*
%{python2_sitearch}/gtk-2.0/gnomecanvas.so
%{_datadir}/pygtk/2.0/defs/canvas.defs
%defattr(644,root,root,755)
%doc examples/canvas/*

%files bonobo
%dir %{python2_sitearch}/gtk-2.0/bonobo/
%{python2_sitearch}/gtk-2.0/bonobo/__init__.*
%{python2_sitearch}/gtk-2.0/bonobo/*.so
%{_datadir}/pygtk/2.0/defs/bonobo*.defs
%{_datadir}/pygtk/2.0/argtypes/bonobo*
%defattr(644,root,root,755)
%doc examples/bonobo/*

%files gconf
%{python2_sitearch}/gtk-2.0/gconf.so
%{_datadir}/pygtk/2.0/defs/gconf.defs
%{_datadir}/pygtk/2.0/argtypes/gconf*
%defattr(644,root,root,755)
%doc examples/gconf/*

%files gnomevfs
%{python2_sitearch}/gtk-2.0/gnomevfs
%{python2_sitearch}/gtk-2.0/gnome/vfs*
%{_libdir}/gnome-vfs-2.0/modules/libpythonmethod.so
%doc %{_datadir}/gtk-doc/html/pygnomevfs
%defattr(644,root,root,755)
%doc examples/vfs/*

%files devel
%{_includedir}/gnome-python-2.0
%{_libdir}/pkgconfig/gnome-python-2.0.pc

# old versions did not have .pyc and .pyo files in their file list
# remove them now, or bad things will now happen because of the new
# paths.  This trigger must remain until upgrading from RHL 8.0 is no 
# longer supported.
%triggerun bonobo -- gnome-python2-bonobo < 1.99.14-5
rm -f %{python2_sitearch}/bonobo/__init__.{pyc,pyo}

%changelog
* Sun May 09 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.28.1
- Rebuilt for Fedora
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 2.28.1-14
- Mass rebuild 2014-01-24
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.28.1-13
- Mass rebuild 2013-12-27
* Fri May 03 2013 Colin Walters <walters@verbum.org> - 2.28.1-12
- Drop requires on bonobo-activation, since it is the same as libbonobo,
  but that package dropped the provides.
* Fri May 03 2013 Colin Walters <walters@verbum.org> - 2.28.1-11
- Rebuild against latest libbonobo
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Nov 29 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 2.28.1-7
- Drop unused/ancient -capplet subpackage definition remains.
- Add %%?_isa to all explicit dependencies on package names.
- Make pygtk2 dependency arch-specific (#749835).
* Fri Nov 25 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 2.28.1-6
- Fix missing deps in -gnome and -bonobo subpkg (#689836).
  gnome-python2-gnome should "Requires: gnome-python2-bonobo"
  gnome-python2-bonobo should "Requires: gnome-python2-canvas"
* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.1-5
- Rebuilt for glibc bug#747377
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.28.1-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Wed Jun 16 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 2.28.1-2.fc14
- Fix directory ownership issue with gtk-doc
- Update spec to drop redundant buildroot sections and python macro def
* Wed Mar 31 2010 Matthias Clasen <mclasen@redhat.com> - 2.28.1-1.fc13
- Update to 2.28.1
* Thu Jan 14 2010 Matthew Barnes <mbarnes@redhat.com> - 2.28.0-2.fc13
- Fix rpmlint warnings.
* Mon Sep 21 2009 Matthew Barnes <mbarnes@redhat.com> - 2.28.0-1.fc12
- Update to 2.28.0
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Jun 17 2009 Matthew Barnes <mbarnes@redhat.com> - 2.27.1-3.fc12
- Improve summary (RH bug #506526).
* Sun Jun 14 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.1-2.fc12
- Minor directory ownership cleanup
* Sat May 02 2009 Matthew Barnes <mbarnes@redhat.com> - 2.27.1-1.fc12
- Update to 2.27.1
* Sun Apr 12 2009 Matthew Barnes <mbarnes@redhat.com> - 2.26.1-1.fc11
- Update to 2.26.1
* Sat Mar 14 2009 Matthew Barnes <mbarnes@redhat.com> - 2.26.0-1.fc11
- Update to 2.26.0
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Fri Feb 20 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.90-2.fc11
- gnome-python2-gnome requires gnome-python2-gnomevfs (RH bug #486387).
* Sun Feb 01 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.90-1.fc11
- Update to 2.25.90
* Mon Jan 19 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.1-1.fc11
- Update to 2.25.1
* Sun Dec 21 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.3-4.fc11
- Don't require devel packages in a non-devel subpackage.
- gnome-python2 doesn't need gome-python2-gnomevfs (RH bug #477494).
* Fri Dec 19 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.3-3.fc11
- Add libgnome[ui] requirements to gnome subpackage.
* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.22.3-2
- Rebuild for Python 2.6
* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.3-1
- Update to 2.22.3
* Sun Sep 21 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.2-1.fc10
- Update to 2.22.2
* Mon Aug 25 2008 Daniel Drake <dsd@laptop.org> - 2.22.1-3.fc10
- Split libgnome bindings into their own package (RH bug #456122).
- Remove gnome-python2 dependency on gnome-python2-bonobo.
* Tue Jun 17 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.1-2.fc10
- Fix directory ownership (RH bug #451754).
* Mon Jun 16 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.1-1.fc10
- Update to 2.22.1
* Mon Apr 07 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.0-2.fc9
- Require pygtk2 explicitly (RH bug #441228).
* Sun Mar 09 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.0-1.fc9
- Update to 2.22.0
* Sat Feb 23 2008 Matthew Barnes <mbarnes@redhat.com> - 2.21.0-3.fc9
- Update to 2.21.1
* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 2.21.0-2.fc9
- Rebuild with GCC 4.3
* Mon Dec 03 2007 Matthew Barnes <mbarnes@redhat.com> - 2.21.0-1.fc9
- Update to 2.21.0
* Sat Nov 24 2007 Matthew Barnes <mbarnes@redhat.com> - 2.20.1-1.fc9
- Update to 2.20.1
* Sun Sep 16 2007 Matthew Barnes <mbarnes@redhat.com> - 2.20.0-1.fc8
- Update to 2.20.0
* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.19.2-3
- Rebuild for selinux ppc32 issue.
* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-2
- Update the license field
* Mon Jul 30 2007 Matthew Barnes <mbarnes@redhat.com> - 2.19.2-1.fc8
- Update to 2.19.2
* Sat Jul 07 2007 Matthew Barnes <mbarnes@redhat.com> - 2.19.1-1.fc8
- Update to 2.19.1
- Update versions of required packages.
- Remove the zvt subpackage, which was removed upstream long ago.
* Sun May 20 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.2-1
- Update to 2.18.2
* Mon Apr 09 2007 Matthew Barnes <mbarnes@redhat.com> - 2.18.1-1.fc7
- Update to 2.18.1
* Mon Mar 12 2007 Matthew Barnes <mbarnes@redhat.com> - 2.18.0-1.fc7
- Update to 2.18.0
* Mon Feb 26 2007 Matthew Barnes <mbarnes@redhat.com> - 2.17.92-2.fc7
- Rebuild
* Sun Feb 25 2007 Matthew Barnes <mbarnes@redhat.com> - 2.17.92-1.fc7
- Update to 2.17.92
* Mon Feb 05 2007 Matthew Barnes <mbarnes@redhat.com> - 2.17.2-2
- Rename spec file to gnome-python2.spec (RH bug #225834).
* Mon Jan 08 2007 Matthew Barnes <mbarnes@redhat.com> - 2.17.2-1
- Update to 2.17.2
* Sun Jan 07 2007 Matthew Barnes <mbarnes@redhat.com> - 2.17.1-1
- Update to 2.17.1
* Sun Dec 31 2006 Matthew Barnes <mbarnes@redhat.com> - 2.16.2-5
- Bonobo subpackage requires pyorbit >= 2.0.1, not 2.0.l (RH bug #150885).
* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.16.2-4
- rebuild for python 2.5
* Mon Nov 27 2006 Matthew Barnes <mbarnes@redhat.com> - 2.16.2-3.fc7
- More packaging tweaks based on suggestions by Patrice Dumas.
- No longer need BuildRequires for autoconf, automake, libtool.
* Fri Nov 17 2006 Matthew Barnes <mbarnes@redhat.com> - 2.16.2-2.fc7
- Fix some minor packaging bugs (RH bug #203532).
* Sun Nov  5 2006 Matthew Barnes <mbarnes@redhat.com> - 2.16.2-1.fc7
- Update to 2.16.2
* Sun Oct 29 2006 Matthew Barnes <mbarnes@redhat.com> - 2.16.0-2.fc6
- Clean up spec file.
- Remove unused patches.
- Add subpackage gnome-python2-devel (bug #203532).
* Tue Sep  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0
* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.91-1.fc6
- Update to 2.15.91
* Fri Aug  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.90-1.fc6
- Update to 2.15.90
* Fri Jul 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.4-2
- Fix gnome-vfs dependencies
* Thu Jul 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.4-1
- Update to 2.15.4
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.15.2-1.1
- rebuild
* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.2-1
- Update to 2.15.2
* Mon Mar 13 2006 Ray Strode <rstrode@redhat.com> - 2.12.4-1
- Update to 2.12.4
* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.12.3-1.2
- bump again for double-long bug on ppc(64)
* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.12.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes
* Wed Feb 06 2006 John (J5) Palmieri <johnp@redhat.com> - 2.12.3-1
- Update to 2.12.3
* Tue Dec 20 2005 Jesse Keating <jkeating@redhat.com> - 2.12.1-1.2
- rebuilt for new libgtop
* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> - 2.12.1-1.1
- rebuilt
* Wed Nov 09 2005 John (J5) Palmieri <johnp@redhat.com> - 2.12.1-1
- Update to 2.12.1
* Tue Aug 18 2005 John (J5) Palmieri <johnp@redhat.com> - 2.11.3-2
- Bump and rebuild for cairo ABI change
* Mon Jul 18 2005  John (J5) Palmieri <johnp@redhat.com> - 2.11.3
- update to upstream 2.11.3
* Fri Mar 11 2005 John (J5) Palmieri <johnp@redhat.com> - 2.10.0
- update to 2.10.0
- add a Requires line for gnome-python2-gnomevfs
* Mon Mar  7 2005 Jeremy Katz <katzj@redhat.com> - 2.9.5-1
- update to 2.9.5
* Mon Feb  7 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.4-2
- Remove unnecessary BuildRequires
* Mon Feb  7 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.4-1
- Update to 2.9.4
- Move some subpackages to gnome-python2-extra
- Obsolete gnome-python2-nautilus 
* Wed Jan 19 2005 Mark McLoughlin <markmc@redhat.com> - 2.6.0-5
- Backport wrapping for GConfEngine from upstream CVS
* Sun Nov  7 2004 Jeremy Katz <katzj@redhat.com> - 2.6.0-4
- rebuild against python 2.4
* Sun Oct 10 2004 Warren Togami <wtogami@redhat.com> - 2.6.0-3 
- #111008 fixes
  Fixes from Ville Skyttä
    Bad file permissions
    Unknown directories
    %%doc fixes
  Fixes from Toshio Kuratomi
    Update the BuildRequires
    Changed BuildRequires on gnome-panel to gnome-panel-devel
    Add Requires for python-abi
* Mon Oct  4 2004 GNOME <jrb@redhat.com> - 2.6.0-2
- fix gtkhtml2 to work in a lot of cases, #147404
* Mon Oct  4 2004 GNOME <jrb@redhat.com> - 2.6.0-1
- new version
* Wed Jul 14 2004 Jeremy Katz <katzj@redhat.com> - 2.0.2-1
- update to 2.0.2
* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Thu Dec 11 2003 Matt Wilson <msw@redhat.com> 2.0.0-3
- added BuildRequries: pyorbit-devel (#108566)
* Thu Nov  6 2003 Jeremy Katz <katzj@redhat.com> 2.0.0-3
- python 2.3
* Sun Oct 19 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add a %%clean specfile target
* Thu Oct  2 2003 Matt Wilson <msw@redhat.com> 2.0.0-2
- fix segv in gnome.ui.About() (#104396)
* Thu Sep  4 2003 Jeremy Katz <katzj@redhat.com> 2.0.0-1
- 2.0.0
* Wed Aug 20 2003 Jeremy Katz <katzj@redhat.com> 1.99.16-1
- update to 1.99.16
- add gnomeprint subpackage
- don't double include the gnome-vfs module (#102074)
* Tue Aug  5 2003 Elliot Lee <sopwith@redhat.com> 1.99.14-7
- Fix libtool
* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Thu Feb  6 2003 Matt Wilson <msw@redhat.com> 1.99.14-5
- added a trigger to remove left-over bonobo .pyc and .pyo files (#79652)
* Thu Feb  6 2003 Mihai Ibanescu <misa@redhat.com> 1.99.14-4
- rebuilt against new python
* Tue Jan 28 2003 Jeremy Katz <katzj@redhat.com> 1.99.14-3
- libdir-ify
* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt
* Fri Dec 27 2002 Jeremy Katz <katzj@redhat.com> 1.99.14-1
- update to 1.99.14
* Fri Dec 13 2002 Jeremy Katz <katzj@redhat.com>
- update to 1.99.13
- add gnomevfs subpackage
* Thu Oct 31 2002 Matt Wilson <msw@redhat.com>
- use %%configure
* Wed Oct 30 2002 Matt Wilson <msw@redhat.com>
- add gnome-python-2.0.pc to file list
* Wed Aug 28 2002 Matt Wilson <msw@redhat.com>
- bind gnome_client_set_*_command
* Wed Aug 28 2002 Tim Powers <timp@redhat.com>
- rebuilt
* Tue Aug 20 2002 Matt Wilson <msw@redhat.com>
- obsolete pygtk-applet (#69830)
* Thu Aug  1 2002 Jonathan Blandford <jrb@redhat.com>
- make the GnomeDruid's fields accessible from python
* Tue Jul 30 2002 Matt Wilson <msw@redhat.com>
- official 1.99.11 release
* Thu May 30 2002 Matt Wilson <msw@redhat.com>
- s/Gconf/GConf/
* Thu May 30 2002 Jeremy Katz <katzj@redhat.com>
- add gtkhtml2 and gconf subpackages
* Wed May 29 2002 Bill Nottingham <notting@redhat.com>
- add some defattrs
* Fri May 24 2002 Matt Wilson <msw@redhat.com>
- added bonobo, nautilus subpackages.  re-enabled applet subpackage
* Mon Nov 26 2001 Matt Wilson <msw@redhat.com>
- subpackages will need __init__ included in them
* Thu Oct 18 2001 Matt Wilson <msw@redhat.com>
- doesn't obsolete pygnome - it can be installed side-by-side
- added _gnomemodule.so to base package filelist
* Mon Oct 15 2001 Matt Wilson <msw@redhat.com>
- added __init__ files to gnome-python main package
* Mon Oct  8 2001 Matt Wilson <msw@redhat.com>
- new gnome-python package based on old pygtk package.
