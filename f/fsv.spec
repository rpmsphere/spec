Name: fsv
Version: 0.9
Release: 18.1
Group: File tools
License: LGPL
URL: http://fsv.sourceforge.net/
Summary: 3D File System Visualizer
Source: %{name}-%{version}.tar.bz2
Buildrequires: gtk+-devel mesa-libGLU-devel glib-devel
Buildrequires: gtkglarea-devel 

%description
fsv (pronounced effessvee) is a file system visualizer in cyberspace. It
lays out files and directories in three dimensions, geometrically
representing the file system hierarchy to allow visual overview and
analysis. fsv can visualize a modest home directory, a workstation's hard
drive, or any arbitrarily large collection of files, limited only by the
host computer's memory and hardware constraints.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}  --with-doc-dir=$RPM_DOC_DIR/%{name}
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT%{_prefix} docdir=`pwd`/doc.rpm
install -Dm 644 fsv.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/fsv
install -Dm 644 src/xmaps/fsv-icon.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/fsv.xpm

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=fsv
Name=Fsv
Comment=3D file browser
Icon=fsv
Categories=System;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc doc.rpm/*
%config(noreplace) %{_sysconfdir}/X11/wmconfig/fsv
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%changelog
* Fri May 08 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9
- Rebuild for Fedora
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-17mdv2011.0
+ Revision: 618363
- the mass rebuild of 2010.0 packages
* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.9-16mdv2010.0
+ Revision: 428927
- rebuild
* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9-15mdv2009.0
+ Revision: 245436
- rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Thu Jan 03 2008 Thierry Vignaud <tv@mandriva.org> 0.9-13mdv2008.1
+ Revision: 141939
- auto-convert XDG menu entry
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- import fsv
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Thu Apr 06 2006 Lenny Cartier <lenny@mandriva.com> 0.9-12mdk
- fix url
* Thu Jan 13 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.9-11mdk
- rebuild
* Thu Nov 27 2003 Michael Scherer <misc@mandrake.org> 0.9-10mdk
- more macro
- fix 32/64 bit library issues
* Tue Apr 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9-9mdk
- buildrequires
* Thu Jan 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9-8mdk
- rebuild
* Tue Jan 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.9-7mdk
- icon
* Wed Sep 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.9-6mdk
- fix requires
* Tue Jul 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.9-5mdk
- rebuild
* Mon Mar 19 2001  Lenny Cartier <lenny@mandrakesoft.com> 0.9-4mdk
- rebuild
* Tue Aug 31 2000  Lenny Cartier <lenny@mandrakesoft.com> 0.9-3mdk
- BM
- macros
- menu
* Wed Apr 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.9-2mdk
- fix group
- fix files section
* Wed Feb 09 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.9-1mdk
- new in contribs
- mandrake adaptations
- strange way to manage files :)
