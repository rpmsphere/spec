Summary:	Advanced archive manager for the Xfce
Name:		squeeze
Version:	0.2.3
Release:	19.1
License:	GPLv2+
Group:		Archiving/Compression
URL:		http://squeeze.xfce.org
Source0:	http://archive.xfce.org/src/apps/%{name}/0.2/%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.2.1-TreeView-border.patch
Patch1:		%{name}-0.2.1-recent-documents.patch
BuildRequires:	pkgconfig(thunar-vfs-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	desktop-file-utils
BuildRequires:	dos2unix

%description
Squeeze is a modern and advanced archive manager for 
the Xfce Desktop Environment.Its design adheres to the 
Xfce philosophy, which basically means Squeeze is both 
fast and easy to use.

%package devel
Summary:	Development files for squeeze
Group:		Development/Other

%description devel
Development files for squeeze.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
dos2unix TODO

%build
%define Werror_cflags %nil
export LDFLAGS=-Wl,--allow-multiple-definition
%configure \
	--disable-static \
	--enable-gslices \
	--enable-pathbar \
	--enable-toolbar \
	--enable-iter-slices

make CFLAGS+=-Wno-format-security

%install
%makeinstall
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog NEWS TODO
%doc %{_datadir}/gtk-doc/html/*
%{_bindir}/squeeze
%{_libexecdir}/thunar-archive-plugin/squeeze.tap
%{_datadir}/applications/squeeze.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%exclude %{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/pixmaps/squeeze/*.png
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/libsqueeze-0.2.la

%changelog
* Sat Aug 03 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3
- Rebuild for Fedora
* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.3-9mdv2010.1
+ Revision: 543280
- rebuild for mdv 2010.1
* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.2.3-8mdv2010.0
+ Revision: 445226
- rebuild
* Sun Mar 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.3-7mdv2009.1
+ Revision: 353006
- use define Werror_cflags %%nil
* Thu Nov 13 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-6mdv2009.1
+ Revision: 302730
- rebuilt against new libxcb
* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.3-5mdv2009.1
+ Revision: 294927
- rebuild for new Xfce4.6 beta1
* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-4mdv2009.0
+ Revision: 260992
- rebuild
* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-3mdv2009.0
+ Revision: 253079
- rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
* Thu Feb 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.3-1mdv2008.1
+ Revision: 176019
- new version
- drop patch 2, merged upstream
* Mon Feb 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.2-3mdv2008.1
+ Revision: 170068
- Patch2: fix sigsev against glib-2.15 (xfce upstream bug #3772)
- obsolete old library
* Mon Jan 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.2-1mdv2008.1
+ Revision: 146262
- fix file list
- drop patch 2 as it has been merged upstream
- api varsion has changed from 1 to 0.2 so in this case old library has to be obsoleted
- fix libification
- new version
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Thu Dec 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-8mdv2008.1
+ Revision: 119169
- add patch 0 (missing links for library)
- new license policy
- do not package COPYING file
* Tue Sep 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-7mdv2008.0
+ Revision: 79568
- add more configure options
* Tue Sep 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-6mdv2008.0
+ Revision: 79364
- provide patch 0 (border in TreeView)
  provide patch 1 (adds support for recent documents)
- new devel library policy
- drop X-MandrivaLinux
* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-4mdv2008.0
+ Revision: 33092
- obsoletes libsqueeze0
* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-3mdv2008.0
+ Revision: 32982
- revert libname
- add %%post and %%postun for library
* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-2mdv2008.0
+ Revision: 32815
- tune up the dessktop file
* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-1mdv2008.0
+ Revision: 32789
- correct libname
- Import squeeze
