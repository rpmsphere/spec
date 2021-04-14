%undefine _debugsource_packages

Name: xnc
Summary: X filemanager with many functions
Version: 5.0.4
Release: 35.1
Source0: %{name}-%{version}.src.tar.bz2
Patch0: xnc-gcc44.patch
Patch1: xnc-5.0.4-str-fmt.patch
Patch2: xnc-5.0.4-link.patch
URL: http://www.xnc.dubna.su  
Group:  File tools
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXt-devel
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: libpng12-devel
BuildRequires: ghostscript-core ImageMagick gcc-c++
License: GPL

%description
X Northern Captain allows the user to navigate through many filesystems,
manipulate files, archives, execute commands in builtin shell, view
and edit images, text and binary files...

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
sed -i 's|abs(|fabs(|' src/bookmark.cxx src/plugins/five/fivegui.cxx src/plugins/aqua/aquagui.cxx
sed -i 's|<png\.h>|<libpng12/png.h>|' src/lib/image2/sdl_image/IMG_png.c

%build
cp /usr/share/automake-*/config.guess .
export CFLAGS=-Wno-narrowing
export LDFLAGS=-Wl,--allow-multiple-definition
./configure --prefix=/usr --mandir=/usr/share/man --libdir=%{_libdir} --with-gnu-ld --with-x
make

%install
rm -fr %{buildroot}
make DESTDIR=%{buildroot} install 
rm -fr %{buildroot}%{_datadir}/doc
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS INSTALL INSTALL-bin.xnc LICENSE  release.news 
%doc README README.keys TODO WHATS_NEW   
%_bindir/*
%_libdir/xnc
%_mandir/man1/*
%{_datadir}/applications/xnc-gnome2.desktop
%exclude %{_datadir}/applnk/System/X_Northern_Captain.desktop
%exclude %{_datadir}/gnome/apps/Applications/xnc.desktop
%{_datadir}/pixmaps/*

%changelog
* Sun Mar 10 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0.4
- Rebuilt for Fedora
* Fri Jan 07 2011 Funda Wang <fwang@mandriva.org> 5.0.4-10mdv2011.0
+ Revision: 629549
- add more BR
- fix build
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild
  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 5.0.4-6mdv2008.1
+ Revision: 135913
- really fix build
- further fix build
- fix build
- revert r135564
- auto-convert XDG menu entry
- adatp to new docdir
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import xnc
* Fri Jan 13 2006 Anssi Hannula <anssi@mandriva.org> 5.0.4-6mdk
- fix BuildRequires
* Sun Jan 08 2006 Anssi Hannula <anssi@mandriva.org> 5.0.4-5mdk
- fix x86_64 build
* Wed Jan 05 2005 Lenny Cartier <lenny@mandriva.com> 5.0.4-4mdk
- rebuild
* Mon Aug 23 2004 Charles A Edwards <eslrahc@mandrake.org> 5.0.4-3mdk
- rebuild for new menu
* Wed Jun 16 2004 Charles A Edwards <eslrahc@mandrake.org> 5.0.4-2mdk
- rebuild
- quiet setup
- fix Section in menu
* Fri Jan 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 5.0.4-1mdk
- 5.0.4
* Mon Sep 01 2003 Lenny Cartier <lenny@mandrakesoft.com> 5.0.2-4mdk
- owns datadir/xnc-version
* Wed Jul 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 5.0.2-3mdk
- buildrequires from Michael Scherer
* Tue May 06 2003 Lenny Cartier <lenny@mandrakesoft.com> 5.0.2-2mdk
- buildrequires
* Thu Feb 06 2003 Lenny Cartier <lenny@mandrakesoft.com> 5.0.2-1mdk
- 5.0.2
- use versioning when installing files
* Thu Jan 9 2003 Charles A Edwards <eslrahc@bellsouth.net> 5.0.0-1mdk
- 5.0.0
- convert src tar.gz to tar.bz2 
- icons
- menu entry
- add files
- spec clean-up--get rid of stuff we don't need anymore
* Fri Sep 06 2002 Lenny Cartier <lenny@mandrakesoft.com> 4.4.7-3mdk
- rebuild
* Fri May 31 2002 Lenny Cartier <lenny@mandrakesoft.com> 4.4.7-2mdk
- rebuild against new libstdc++
- clean spec ( macros )
* Thu Apr 25 2002 Lenny Cartier <lenny@mandrakesoft.com> 4.4.7-1mdk
- updated by Charles A Edwards <eslrahc@bellsouth.net>
