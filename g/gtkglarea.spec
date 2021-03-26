Summary:	OpenGL widget for GTK+ 1.2
Name:		gtkglarea
Version:	1.2.3
Release: 	18.1
License:	LGPL
Group:		System/Libraries
URL:		http://www.student.oulu.fi/~jlof/gtkglarea/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		gtkglarea-1.2.3-fix-underquoted-calls.patch
patch1:		gtkglarea-1.2.3.printf.patch
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+)
BuildRequires:	libtool

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawingArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

%package devel
Summary:	Development libraries for GtkGLArea
Group:		Development/GNOME and GTK+
Requires:	%{name}

%description devel
Libraries and includes files you can use for GtkGLArea development.

%prep
%setup -q
%patch0 -p1 -b .underquoted
%patch1 -p1 -b .printf

%build
autoreconf -fis
%configure
make

%install
%make_install

%files
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/lib*.so.*

%files devel
%doc docs/*.txt
%{_libdir}/*.so
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_includedir}/*
%{_datadir}/aclocal/*

%changelog
* Tue Feb 10 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.3
- Rebuild for Fedora

* Mon Nov 10 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-14mdv2009.1
+ Revision: 301800
- bump release
- try to fix build

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.3-11mdv2008.1
+ Revision: 170878
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jul 21 2007 Adam Williamson <awilliamson@mandriva.com> 1.2.3-10mdv2008.0
+ Revision: 54351
- rebuild for 2008
- ew, don't symlink to a different major!
- bunzip2 patch
- new devel policy
- Import gtkglarea

* Thu Jun 08 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.3-9mdv2007.0
- fix buildrequires
- add missing %%build section
- fix underquoted calls (P0)

* Tue Dec 27 2005 Lenny Cartier <lenny@mandriva.com> 1.2.3-8mdk
- rebuild

* Fri Aug 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.3-7mdk
- rebuild

* Thu Jul 24 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.2.3-6mdk
- rebuild

* Thu Jan 16 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2.3-5mdk
- fix files list

* Sat Aug  3 2002 Stefan van der Eijk <stefan@eijk.nu> 1.2.3-4mdk
- BuildRequires

* Tue Jul 23 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.2.3-3mdk
- Rebuild with latest gcc3.1
- Sanitize specfile (silentify %%setup)
- BuildRequires: Mesa-devel. Where is Mesa-common-devel gone?

* Thu Jan 17 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.2.3-2mdk
- remove empty doc file

* Tue Oct 16 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.3-1mdk
- new version

* Thu Sep 13 2001 Stefan van der Eijk <stefan@eijk.nu> 1.2.2-10mdk
- BuildRequires: gtk+-devel

* Sat Jul 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-9mdk
- rebuild

* Sun May 27 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.2-8mdk
- have Provides more suitable to lib policy
- fix problems reported by rpmlint

* Thu Apr 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-7mdk
- fix provides & obsoletes

* Sat Mar 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-6mdk
- split

* Thu Jan 11 2001 David BAUDENS <baudens@mandrakesoft.com> 1.2.2-5mdk
- BuildRequires: Mesa-common-devel

* Wed Nov 08 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-4mdk
- rebuild for gcc-2.96

* Thu Jul 27 2000 Pixel <pixel@mandrakesoft.com> 1.2.2-3mdk
- remove duplicate lib in gtkglarea and gtkglarea-devel + cleanup, BM

* Tue Apr 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-2mdk
- add ldconfig in devel post

* Thu Mar 21 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-1mdk
- clean specfile
- v1.2.2

* Wed Dec 08 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
 - rebuild linking against Mesa 3.1cvs (uses OpenGL naming of libs instead
   of libMesa*.so stuff)
    
* Mon Nov 01 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- 1.2.1
	 
* Tue Feb 09 1999 Pablo Saratxaga <srtxg@chanae.alphanet.ch>
 - First try at an RPM  
