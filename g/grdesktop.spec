Summary: A gtk2 frontend for rdesktop
Name: grdesktop
Version: 0.23
Release: 22.4
Group: Networking/Remote access
License: GPLv2+
Source0: %{name}-%{version}.tar.bz2
Patch0: grdesktop-0.23-desktopentry.patch
Patch1: grdesktop-0.23-format-strings.patch
Patch2: grdesktop-0.23-fix-desktop.patch
URL: http://www.nongnu.org/grdesktop/
Requires: rdesktop
BuildRequires: libgnomeui-devel
BuildRequires: ghostscript-core ImageMagick
BuildRequires: rarian-compat
BuildRequires: w3m udisks2

%description
grdesktop is a frontend, written in C using the GTK+2 toolkit, for
the remote desktop client (rdesktop).
It can save several connections (including their options), and browse
the network for available terminal servers.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure --with-keymap-path=%_datadir/rdesktop/keymaps
make

%install
%make_install
mv %buildroot%_datadir/locale/de/LC_MESSAGES/@GETTEXT_PACKAGE@.mo %buildroot%_datadir/locale/de/LC_MESSAGES/grdesktop.mo
mv %buildroot%_datadir/locale/es/LC_MESSAGES/@GETTEXT_PACKAGE@.mo %buildroot%_datadir/locale/es/LC_MESSAGES/grdesktop.mo
mv %buildroot%_datadir/locale/fr/LC_MESSAGES/@GETTEXT_PACKAGE@.mo %buildroot%_datadir/locale/fr/LC_MESSAGES/grdesktop.mo

%find_lang %name --with-gnome 
mkdir -p %buildroot%_datadir/icons/hicolor/{64x64/apps,32x32/apps,16x16/apps}
ln -s %_datadir/pixmaps/%name/icon.png %buildroot%_datadir/icons/hicolor/64x64/apps/%name.png
convert -scale 32x32 pixmaps/icon.png %buildroot%_datadir/icons/hicolor/32x32/apps/%name.png
convert -scale 16x16 pixmaps/icon.png %buildroot%_datadir/icons/hicolor/16x16/apps/%name.png

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_sysconfdir/gconf/schemas/grdesktop.schemas
%{_bindir}/grdesktop
%{_mandir}/man1/grdesktop.1*
%_datadir/application-registry/grdesktop.applications
%_datadir/applications/grdesktop.desktop
%_datadir/mime-info/grdesktop.keys
%_datadir/mime-info/grdesktop.mime
%{_datadir}/pixmaps/grdesktop/
%dir %_datadir/omf/grdesktop
%_datadir/omf/grdesktop/%name-C.omf
%_datadir/icons/hicolor/64x64/apps/%name.png
%_datadir/icons/hicolor/32x32/apps/%name.png
%_datadir/icons/hicolor/16x16/apps/%name.png

%changelog
* Thu Mar 26 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.23
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 0.23-12.mga5
+ Revision: 740260
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.23-11.mga5
+ Revision: 679934
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 0.23-10.mga4
+ Revision: 517159
- Mageia 4 Mass Rebuild
* Sat Jan 12 2013 dmorgan <dmorgan> 0.23-9.mga3
+ Revision: 361314
- Fix desktop file
  + umeabot <umeabot>
    - Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Wed Apr 06 2011 ennael <ennael> 0.23-8.mga1
+ Revision: 81308
- clean spec file
- imported package grdesktop
* Sat Jul 25 2009 Götz Waschk <waschk@mandriva.org> 0.23-8mdv2010.0
+ Revision: 399672
- fix format strings
- update license
  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick
* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.23-7mdv2009.0
+ Revision: 246636
- rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.23-5mdv2008.1
+ Revision: 148199
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Thu Sep 20 2007 Götz Waschk <waschk@mandriva.org> 0.23-5mdv2008.0
+ Revision: 91369
- fix desktop entry (bug #33760)
* Wed Jul 25 2007 Götz Waschk <waschk@mandriva.org> 0.23-4mdv2008.0
+ Revision: 55229
- Import grdesktop
* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 0.23-4mdv2007.0
- xdg menu
* Sun May 14 2006 Götz Waschk <waschk@mandriva.org> 0.23-3mdk
- Rebuild
- use mkrel
* Fri May 13 2005 Götz Waschk <waschk@mandriva.org> 0.23-2mdk
- drop obsolete gnome help file handling
- fix menu
* Fri Apr  2 2004 Götz Waschk <waschk@linux-mandrake.com> 0.23-1mdk
- fix installation of the locale files
- fix build
- new version
* Fri Feb  6 2004 Götz Waschk <waschk@linux-mandrake.com> 0.22-2mdk
- fix rdesktop keymap location
* Thu Feb  5 2004 Götz Waschk <waschk@linux-mandrake.com> 0.22-1mdk
- initial Mandrake package
* Tue Nov 12 2002 Che
- version upgrade
- prettyfied it a bit :P
* Fri Nov 01 2002 Che
- initial rpm release
