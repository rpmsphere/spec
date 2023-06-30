Summary: Base library of Galago
Name: galago
Version: 0.5.2
Release: 14.1
Source0: https://www.galago-project.org/files/releases/source/libgalago/lib%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
URL: https://www.galago-project.org/
BuildRequires: dbus-glib-devel
BuildRequires: gtk-doc
BuildRequires: w3m

%description
This is the base library of the Galago desktop presence framework.

%package devel
Group: Development/C
Summary: Base library of Galago - headers
Requires: %{name} = %version-%release

%description devel
This is the base library of the Galago desktop presence framework.

%prep
%setup -q -n lib%{name}-%{version}

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall MKINSTALLDIRS=`pwd`/mkinstalldirs
rm -rf $RPM_BUILD_ROOT%_datadir/autopackage
%find_lang lib%name
find $RPM_BUILD_ROOT -name '*.la' | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files -f lib%name.lang
%doc AUTHORS NEWS
%{_libdir}/lib*.so.*

%files devel
%doc ChangeLog 
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libgalago.pc
%{_includedir}/libgalago
%{_datadir}/gtk-doc/html/libgalago

%changelog
* Sun Sep 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.2
- Rebuilt for Fedora
* Tue Feb 15 2011 ahmad <ahmad> 0.5.2-11.mga1
+ Revision: 52032
- drop old/unneeded scriptlets
- don't ship .la
- imported package libgalago
* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-10mdv2011.0
+ Revision: 602546
- rebuild
* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.5.2-9mdv2010.1
+ Revision: 540031
- rebuild so that shared libraries are properly stripped again
* Thu Apr 22 2010 Matthew Dawkins <mattydaw@mandriva.org> 0.5.2-8mdv2010.1
+ Revision: 537952
- dropped major from devel pkg name
  disabled static build
* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-7mdv2010.1
+ Revision: 520788
- rebuilt for 2010.1
* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5.2-6mdv2010.0
+ Revision: 425545
- rebuild
* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.5.2-5mdv2009.1
+ Revision: 351404
- rebuild
* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.5.2-4mdv2009.0
+ Revision: 222565
- rebuild
  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.5.2-3mdv2008.1
+ Revision: 150563
- rebuild
* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.5.2-2mdv2008.1
+ Revision: 148492
- rebuild
- kill re-definition of %%$RPM_BUILD_ROOT on Pixel's request
- do not package big ChangeLog
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Mon Oct 30 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.5.2-1mdv2007.0
+ Revision: 73766
- New version 0.5.2
- import libgalago-0.5.1-3mdv2007.0
* Tue Aug 08 2006 Götz Waschk <waschk@mandriva.org> 0.5.1-3mdv2007.0
- fix buildrequires
* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 0.5.1-2mdv2007.0
- Rebuild with latest dbus
* Thu Jul 13 2006 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdv2007.0
- update file list
- fix installation
- New release 0.5.1
* Sat Apr 22 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdk
- new major
- New release 0.5.0
* Wed Jan 25 2006 Götz Waschk <waschk@mandriva.org> 0.3.3-3mdk
- rebuild for new dbus
- use mkrel
* Thu Oct 27 2005 Götz Waschk <waschk@mandriva.org> 0.3.3-2mdk
- rebuild for new dbus
* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 0.3.3-1mdk
- new URL
- New release 0.3.3
* Sat Jun 18 2005 Götz Waschk <waschk@mandriva.org> 0.3.2-3mdk
- description (Buchan)
* Fri Jun 17 2005 Götz Waschk <waschk@mandriva.org> 0.3.2-2mdk
- add provides to the library package
* Fri Jun 17 2005 Götz Waschk <waschk@mandriva.org> 0.3.2-1mdk
- initial package
