%undefine _debugsource_packages

Summary:	A simple-in-use GTK-based text editor
Name:		teagtk
Version:	18.0.0
Release:	16.1
Group:		Editors
License:	GPLv2+
URL:		https://semiletov.org/tea/
Source0:	https://ovh.dl.sourceforge.net/sourceforge/tea-editor/%{name}-%{version}.tar.bz2
BuildRequires:  python3-scons python3-devel gtk3-devel gtksourceview3-devel
BuildRequires:  aspell-devel zziplib

%description
Teagtk is a simple-in-use GTK-based text editor.

%prep
%setup -q
sed -i -e 's|/usr/local|/usr|' -e 's|-lm|-lm -Wl,--allow-multiple-definition|' SConstruct

%build
scons

%install
scons --install-sandbox=%{buildroot} install
%find_lang %{name}
install -Dm755 %{name} %{buildroot}/%{_bindir}/%{name}

# icons
install -Dm644 images/tea_icon.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=TeaGTK
Comment=A simple-in-use GTK-based text editor
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Gtk;TextEditor;Utility;
EOF

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/pixmaps/%name.png
%{_datadir}/applications/*

%changelog
* Mon Apr 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 18.0.0
- Rebuilt for Fedora
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 0:17.6.6-2mdv2010.0
+ Revision: 445388
- rebuild
* Mon Sep 01 2008 Frederik Himpe <fhimpe@mandriva.org> 0:17.6.6-1mdv2009.0
+ Revision: 278584
- update to new version 17.6.6
* Sat Jul 12 2008 Funda Wang <fundawang@mandriva.org> 0:17.6.5-1mdv2009.0
+ Revision: 234073
- update to new version 17.6.5
* Fri Jun 27 2008 Funda Wang <fundawang@mandriva.org> 0:17.6.3-1mdv2009.0
+ Revision: 229384
- New version 17.6.3
- tea has been renamed to teagtk
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Wed Jun 04 2008 Funda Wang <fundawang@mandriva.org> 0:17.6.1-1mdv2009.0
+ Revision: 214936
- update to new version 17.6.1
* Sun Mar 09 2008 Funda Wang <fundawang@mandriva.org> 0:17.6.0-1mdv2008.1
+ Revision: 182406
- update to new version 17.6.0
* Fri Jan 25 2008 Funda Wang <fundawang@mandriva.org> 0:17.5.4-1mdv2008.1
+ Revision: 157956
- update to new version 17.5.4
* Sat Jan 12 2008 Funda Wang <fundawang@mandriva.org> 0:17.5.3-1mdv2008.1
+ Revision: 149262
- clearify LICENSE
- update to new version 17.5.3
  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix description
* Wed Jan 09 2008 Funda Wang <fundawang@mandriva.org> 0:17.5.2-1mdv2008.1
+ Revision: 147166
- update to new version 17.5.2
* Wed Jan 09 2008 Funda Wang <fundawang@mandriva.org> 0:17.5.1-1mdv2008.1
+ Revision: 147044
- update to new version 17.5.1
* Sun Dec 30 2007 Funda Wang <fundawang@mandriva.org> 0:17.5.0-1mdv2008.1
+ Revision: 139538
- New version 17.5.0
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
* Thu Dec 13 2007 Jérôme Soyer <saispo@mandriva.org> 0:17.4.1-1mdv2008.1
+ Revision: 119228
- New release
* Mon Nov 12 2007 Funda Wang <fundawang@mandriva.org> 0:17.4.0-1mdv2008.1
+ Revision: 108062
- New version 17.4.0
* Fri Oct 19 2007 Funda Wang <fundawang@mandriva.org> 0:17.3.5-1mdv2008.1
+ Revision: 100348
- update to new version 17.3.5
* Sun Oct 14 2007 Funda Wang <fundawang@mandriva.org> 0:17.3.3-1mdv2008.1
+ Revision: 98202
- New version 17.3.3
* Sun Oct 14 2007 Funda Wang <fundawang@mandriva.org> 0:17.3.2-1mdv2008.1
+ Revision: 98139
- New version 17.3.2
* Tue Oct 09 2007 Funda Wang <fundawang@mandriva.org> 0:17.3.1-1mdv2008.1
+ Revision: 96123
- gtksouorceview2 is default now
- BR aspell
- New version 17.3.1
* Wed Sep 05 2007 Funda Wang <fundawang@mandriva.org> 0:17.2.2-1mdv2008.0
+ Revision: 79687
- drop unused files
- New version 17.2.2
- New version 17.2.1
* Sat Aug 25 2007 Funda Wang <fundawang@mandriva.org> 0:17.2.0-1mdv2008.0
+ Revision: 71149
- New versiono 17.2.0.
- BR gtksourceview 2.0
* Tue Aug 07 2007 Funda Wang <fundawang@mandriva.org> 0:17.1.4-1mdv2008.0
+ Revision: 59637
- New version 17.1.4
* Thu Jul 26 2007 Funda Wang <fundawang@mandriva.org> 0:17.1.0-1mdv2008.0
+ Revision: 55782
- BR old version of gtksourceveiw
- BR new version of gtksourceview
- New version 17.1.0
* Thu Jul 12 2007 Funda Wang <fundawang@mandriva.org> 0:17.0.1-1mdv2008.0
+ Revision: 51559
- BR gtksourceview 1.0
- New version
* Wed May 02 2007 Lenny Cartier <lenny@mandriva.org> 0:16.1.1-1mdv2008.0
+ Revision: 20558
- Update to 16.1.1
* Fri Mar 02 2007 Lenny Cartier <lenny@mandriva.com> 16.0.4-1mdv2007.0
+ Revision: 130947
- Update to 16.0.4
* Tue Feb 27 2007 Lenny Cartier <lenny@mandriva.com> 0:16.0.2-2mdv2007.1
+ Revision: 126259
- xdg menu
* Mon Feb 26 2007 Lenny Cartier <lenny@mandriva.com> 0:16.0.2-1mdv2007.1
+ Revision: 125929
- Update to 16.0.2
* Fri Nov 17 2006 Lenny Cartier <lenny@mandriva.com> 0:14.3.1-1mdv2007.1
+ Revision: 85152
- Update to 14.3.0
* Tue Nov 14 2006 Lenny Cartier <lenny@mandriva.com> 0:14.3.0-1mdv2007.1
+ Revision: 83994
- Update to 14.3.0
- Import tea
* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 0:14.0-1mdv2007.0
- 14.0
* Fri May 12 2006 Thierry Vignaud <tvignaud@mandriva.com> 13.2-2mdk
- fix buildrequires
* Wed May 10 2006 Lenny Cartier <lenny@mandriva.com> 13.2-1mdk
- 13.2
* Wed May 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 13.0-2mdk
- fix buildrequires (thus fixing x86_64 build)
* Fri Apr 28 2006 Lenny Cartier <lenny@mandriva.com> 0:13.0-1mdk
- 13.0
* Wed Feb 01 2006 Lenny Cartier <lenny@mandriva.com> 0:12.0-1mdk
- 12.0
* Tue Jul 05 2005 Lenny Cartier <lenny@mandriva.com> 0:10.1-1mdk
- 10.1
* Sun Apr 03 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 8.2-1mdk
- first spec for mdk
