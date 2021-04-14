Name:		industrial-gnome-theme
Version: 0.2.34
Release: 9.1
License:	GPL
URL:		http://www.ximian.com/
Source0:	ximian-artwork-%version.tar.bz2
Source1:    Industrial-index.theme
BuildRequires:	gtk+-devel
BuildRequires:	gtk2-devel
BuildRequires:  intltool
BuildArch: noarch
Summary:	The Default Style for Ximian Desktop
Group: Graphical desktop/GNOME
Requires: gnome-icon-theme
Requires: gtk2-engines
Provides: ximian-artwork

%description
This contains the default style configuration for the Ximian Desktop.
This package contains Industrial themes for GNOME2, gdm xmms and galeon.

%prep
%setup -q -n ximian-artwork-%version
libtoolize --force
aclocal
intltoolize --force
autoconf
automake --add-missing

%build
%configure
make

%install
%makeinstall
rm -rf %buildroot%{_libdir}/gtk
# GTK2 industrial engine is now in gtk-engines2
rm %buildroot%{_libdir}/gtk-2.0/engines/*
rm -rf %buildroot%{_datadir}/themes/Industrial/gtk-2.0
mv %buildroot%{_datadir}/pixmaps/backgrounds %buildroot%{_datadir}/backgrounds
cp %{SOURCE1} %buildroot%{_datadir}/themes/Industrial/index.theme

%clean
rm -fr %buildroot

%files
%doc COPYING
%{_datadir}/themes/*
%{_datadir}/pixmaps/*
%{_datadir}/backgrounds/ximian
%{_datadir}/gdm/themes/*
%{_datadir}/galeon/themes/*
%{_datadir}/xmms/Skins/*
%{_datadir}/icons/Industrial

%changelog
* Tue Mar 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.34
- Rebuilt for Fedora
* Tue Jul 26 2011 Götz Waschk <waschk@mandriva.org> 0.2.34-6mdv2012.0
+ Revision: 691697
- rebuild
* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2.34-5mdv2011.0
+ Revision: 242992
- rebuild
- kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Tue Sep 04 2007 Götz Waschk <waschk@mandriva.org> 0.2.34-3mdv2008.0
+ Revision: 79089
- call libtoolize to fix build
- Import ximian-artwork
* Sun Sep  3 2006 Götz Waschk <waschk@mandriva.org> 0.2.34-3mdv2007.0
- fix icon cache handling
* Wed Apr 26 2006 Götz Waschk <waschk@mandriva.org> 0.2.34-2mdk
- fix build
- use mkrel
* Mon Apr 25 2005 Götz Waschk <waschk@mandriva.org> 0.2.34-1mdk
- fix build
- New release 0.2.34
* Tue Dec 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.2.26-4mdk 
- Don't ship gtk2 industrial engine/theme, it is now in gtk-engines2
* Sat Apr  3 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2.26-3mdk
- autoconf 2.5 macro
- rebuild for new gtk
* Tue Aug  5 2003 Götz Waschk <waschk@linux-mandrake.com> 0.2.26-2mdk
- depend on gnome-icon-theme
- remove files already in gnome-icon-theme
* Fri Jun 13 2003 Götz Waschk <waschk@linux-mandrake.com> 0.2.26-1mdk
- adapt for Mandrake
* Fri May 23 2003 Ximian, Inc.
- Version: 0.2.34-0.ximian.6.1
- Summary: New build.
- New automated build.
* Wed May 21 2003 Ximian, Inc.
- Version: 0.2.25-0.ximian.5.1
- Summary: New build.
- New automated build.
* Sat Apr 26 2003 Ximian, Inc.
- Version: 0.2.19-0.ximian.1
- Summary: New build.
- New automated build.
* Thu Mar 20 2003 Ximian, Inc.
- Version: 0.2.16-0.ximian.2
- Summary: New build.
- New automated build.
* Tue Feb 11 2003 Ximian, Inc.
- Version: 0.2.14-0.ximian.1
- Summary: New build.
- New automated build.
* Fri Feb 7 2003 Ximian, Inc.
- Version: 0.2.13-0.ximian.1
- Summary: New build.
- New automated build.
* Tue Jan 21 2003 Ximian, Inc.
- Version: 0.2.11-1.ximian.1
- Summary: Tweaked handle and scrollbar code.
- Fixes GtkVPaneds and GtkHPaned.  Fixed scrollbars for
          mozilla/galeon.  Fixed scrollbar and handle colors.
* Tue Jan 21 2003 Ximian, Inc.
- Version: 0.2.10-1.ximian.1
- Summary: New GtkPaned code.
- Fixes GtkVPaneds and GtkHPaned.
* Tue Jan 21 2003 Ximian, Inc.
- Version: 0.2.9-1.ximian.1
- Summary: Galeon theme.
- Adds galeon theme.
* Fri Oct 25 2002 Ximian, Inc.
- Version: 0.2.0-1.ximian.1
- Summary: New build.
- New automated build.
* Tue Oct 22 2002 Ximian, Inc.
- Version: 0.1.5-1.ximian.1
- Summary: New build.
- New automated build.
* Tue Oct 15 2002 Ximian, Inc.
- Version: 0.1.4.2-1.ximian.1
- Summary: New build.
- New automated build.
* Fri Oct 11 2002 Ximian, Inc.
- Version: 0.1.4-1.ximian.1
- Summary: New build.
- New automated build.
* Fri Oct 4 2002 Ximian, Inc.
- Version: 0.1.3-1.ximian.1
- Summary: New build.
- New automated build.
* Fri Oct 4 2002 Ximian, Inc.
- Version: 0.1.2-1.ximian.1
- Summary: New build.
- New automated build.
* Wed Oct 2 2002 Ximian, Inc.
- Version: 0.1.1-1.ximian.1
- Summary: New build.
- New automated build.
* Mon Sep 30 2002 Ximian, Inc.
- Version: 0.1.0-1.ximian.1
- Summary: New build.
- New automated build.
* Fri Sep 27 2002 Ximian, Inc.
- Version: 0.0.8-1.ximian.1
- Summary: New build.
- New automated build.
* Thu Sep 26 2002 Ximian, Inc.
- Version: 0.0.7.1-1.ximian.1
- Summary: New build.
- New automated build.
* Mon Sep 23 2002 Ximian, Inc.
- Version: 0.0.6.1-1.ximian.1
- Summary: New build.
- New automated build.
* Fri Sep 20 2002 Ximian, Inc.
- Version: 0.0.6-1.ximian.1
- Summary: New build.
- New automated build.
* Fri Sep 20 2002 Ximian, Inc.
- Version: 0.0.5.2-1.ximian.1
- Summary: New build.
- New automated build.
* Thu Sep 19 2002 Ximian, Inc.
- Version: 0.0.5.1-1.ximian.1
- Summary: New build.
- New automated build.
* Fri Sep 13 2002 Ximian, Inc.
- Version: 0.0.5-1.ximian.1
- Summary: New build.
- New automated build.
* Thu Sep 12 2002 Ximian, Inc.
- Version: 0.0.4.1-1.ximian.1
- Summary: New build.
- New automated build.
* Wed Sep 11 2002 Ximian, Inc.
- Version: 0.0.4-1.ximian.1
- Summary: New build.
- New automated build.
* Mon Sep 9 2002 Ximian, Inc.
- Version: 0.0.3-1.ximian.1
- Summary: New build.
- New automated build.
* Wed Aug 28 2002 Ximian, Inc.
- Version: 0.0.2-1.ximian.1
- Summary: New build.
- New automated build.
* Fri Aug 23 2002 Ximian, Inc.
- Version: 0.0.1-1.ximian.1
- Summary: New build.
- New automated build.
