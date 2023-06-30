Name: 	 	gournal
Summary: 	GNOME hardwriting notepad
Version: 	0.5.1
Release: 	9.1
Source:		https://www.adebenham.com/debian/%{name}_%{version}-1.tar.bz2
URL:		https://www.adebenham.com/old-stuff/gournal/
License:	GPL
Group:		Applications/Productivity
BuildArch:	noarch

%description
Gournal is a note-taking application written for usage on Tablet-PCs.  It's
designed for usage with a stylus, not a mouse or keyboard.  It does not have
handwriting recognition but can be used in co-ordination with xstroke to
accept text.  The pages are saved as gzipped SVG files (not totally standard
yet but working on it).

Gournal looks/works just like a physical notebook with multiple pages.
Gournal has the following tools:
    * Fine/Normal/Medium/Think Pens
    * Eraser
    * Highliter
    * Typed Text
    * Time-stamp
    * Zoom
    * Infinite undo/redo
    * Delete entire strokes
    * Networkable pages
    * <Insert Images>
    * <Load a file as the background> 

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %{name} $RPM_BUILD_ROOT/%_bindir/
mkdir -p $RPM_BUILD_ROOT/%_datadir/%{name}
cp *.glade pixmaps/*.png $RPM_BUILD_ROOT/%_datadir/%{name}

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=Gournal
Comment=Handwriting notepad
Categories=Office;
EOF

install -Dm644 pixmaps/pencil.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGES README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jul 14 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.1
- Rebuilt for Fedora

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-8mdv2011.0
+ Revision: 619220
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.5.1-7mdv2010.0
+ Revision: 437802
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.5.1-6mdv2009.1
+ Revision: 350623
- 2009.1 rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.5.1-5mdv2009.1
+ Revision: 350291
- 2009.1 rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5.1-4mdv2009.0
+ Revision: 246526
- rebuild
- fix 'error: for key "Icon" in group "Desktop Entry" is an icon name with an
  extension, but there should be no extension as described in the Icon Theme
  Specification if the value is not an absolute path'

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.5.1-2mdv2008.1
+ Revision: 131674
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import gournal

* Sun Jan 22 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.5.1-2mdk
- Add BuildRequires: ImageMagick

* Wed Dec 07 2005 Lenny Cartier <lenny@mandriva.com> 0.5.1-1mdk
- 0.5.1

* Mon May 3 2004 Austin Acton <austin@mandrake.org> 0.3-1mdk
- initial package
