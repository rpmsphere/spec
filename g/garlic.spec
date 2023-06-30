Name: 		garlic
Version: 	1.6
Release: 	12.1
Summary: 	Free molecular viewer and editor
License: 	GPL
Group: 		Sciences/Chemistry
Source0: 	%{name}-%{version}.tar.bz2
Source1: 	%{name}-%{version}-doc.tar.bz2
Source2:	%{name}.1.bz2
URL: 		https://garlic.mefos.hr/sources
BuildRequires: 	libX11-devel

%description
Garlic is a full-featured molecular viewer and editor. It is
intended mainly for biological macromolecules (proteins and DNA)
in PDB format. It can also render high-quality images for
presentations or publishing.

%prep
%setup -q -a 1
mv garlic-%version doc
sed -i 's|^CCOPT.*|CCOPT = %{optflags}|' Makefile
rm -rf doc/mouse/.xvpics/
sed -i 's|usr/X11R6/lib|usr/X11R6/%{_lib}|g' Makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m755 garlic $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/%{name}
install -m644 .garlicrc *.pdb $RPM_BUILD_ROOT/%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
cp %SOURCE2 $RPM_BUILD_ROOT/%{_mandir}/man1
install -Dm644 %{name}.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.xpm

# menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=garlic
Categories=Education;Science;Chemistry;
Name=Garlic
Icon=%{name}
Comment=3D Molecule Viewer
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README HISTORY BUGS *.script doc
%{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 1.6-6mdv2011.0
+ Revision: 635488
- simplify BR
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-5mdv2011.0
+ Revision: 618425
- the mass rebuild of 2010.0 packages
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.6-4mdv2010.0
+ Revision: 429105
- rebuild
  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick
* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.6-3mdv2009.0
+ Revision: 245630
- rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.6-1mdv2008.1
+ Revision: 131556
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import garlic
* Thu Apr 06 2006 Lenny Cartier <lenny@mandriva.com> 1.6-1mdk
- 1.6
* Tue Nov 08 2005 Austin Acton <austin@mandriva.org> 1.4-2mdk
- lib64 fix
* Mon Feb 16 2004 Austin Acton <austin@mandrake.org> 1.4-1mdk
-1.4
* Wed Jul 2 2003 Austin Acton <aacton@yorku.ca> 1.3-1mdk
- 1.3
- fix group
- fix URL
- cleanup spec
- add manpage
* Thu Mar 20 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.2-3mdk
- removed .xvpics thumbnails
- added it's own icons
- add missing BuildRequires
* Sun Nov 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.2-2mdk
- add menu macros
- from Austin Acton <aacton@yorku.ca> :
	- add menu entry and threaded build
	- expand description
* Fri Sep 20 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2-1mdk
- first mdk package
