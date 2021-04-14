Name: 		grpn
Version: 	1.5.2
Release: 	1
License: 	GPL
Summary: 	RPN calculator for X built using the GIMP Toolkit
URL: 		http://lashwhip.com/grpn.html
Group: 		Sciences/Mathematics
Source: 	https://fossies.org/linux/misc/legacy/%{name}-%{version}.tar.gz
BuildRequires:  gtk2-devel

%description 
GRPN is a RPN calculator for the X Window system built using the GIMP
Toolkit (GTK). GRPN works with real numbers, complex numbers,
matrices, and complex matrices. Numbers can be displayed in 4
different radix modes, and complex numbers can be displayed in either
Cartesian or polar form.

%prep
%setup -q

%build
cd src
make

%install
install -Dm755 src/grpn $RPM_BUILD_ROOT%{_bindir}/grpn
install -Dm644 src/grpn.1 $RPM_BUILD_ROOT%{_mandir}/man1/grpn.1
install -Dm644 src/debian/grpn.desktop %buildroot%{_datadir}/applications/%{name}.desktop
install -Dm644 src/debian/grpn.xpm %buildroot%{_datadir}/pixmaps/%{name}.xpm

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%doc src/CHANGES src/LICENSE src/README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Tue Nov 27 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.2
- Rebuilt for Fedora
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1.2-8mdv2010.0
+ Revision: 429323
- rebuild
* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.1.2-7mdv2009.0
+ Revision: 246643
- rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.1.2-5mdv2008.1
+ Revision: 131682
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import grpn
* Wed May 10 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1.2-5mdk
- Fix build on x86-64
* Tue Jan 10 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1.2-4mdk
- rebuild
* Mon Aug 16 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.1.2-3mdk
- Rebuild
* Fri Jul 18 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 1.1.2-2mdk
- Rebuild
* Mon Apr 08 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.2-1mdk
- 1.1.2
* Sat Jan 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.1-5mdk
- Fix menu entry
* Tue Jul 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.1-4mdk
- s/Copyright/License/g
* Mon Jun 18 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.1.1-3mdk
- New office menu structure
* Wed Jan 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.1-2mdk
- rebuild
* Mon Sep 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1.1-1mdk
- menus
- macros
- BM
- v1.1.1
* Thu Apr 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-2mdk
- fix group
* Thu Feb 24 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build 
* Mon Jun 21 1999 Tom Faska <tom@ubertas.com>
- Initial RPM for grpn-1.1.0
