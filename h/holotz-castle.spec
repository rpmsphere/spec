%undefine _debugsource_packages

Name:		holotz-castle
Version:	1.3.14
Release:	1
Summary:	A strategy platform scroller
License:	GPLv2+
Group:		Games/Arcade
URL:		https://www.mainreactor.net/holotzcastle/en/index_en.html
Source0:	https://www.mainreactor.net/holotzcastle/download/%{name}-%{version}-src.tar.gz
Source10:	hc-48x48.png
Source11:	hc-32x32.png
Source12:	hc-16x16.png
Source20:	holotz-castle-editor-48x48.png
Source21:	holotz-castle-editor-32x32.png
Source22:	holotz-castle-editor-16x16.png
Patch0:		holotz-castle-1.3.6-install.patch
Patch1:		holotz-castle-1.3.11-compile-fixes.patch
Patch2:		holotz-castle-1.3.14-compile-fixes.patch
BuildRequires:  gcc-c++
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:  mesa-libGLU-devel

%package -n %{name}-editor
License:	GPLv2+
Group:		Games/Arcade
Summary:	Holotz's Castle level editor
Requires:	%{name} == %{version}

%description
A great mystery is hidden beyond the walls of Holotz's Castle. Will you be
able to help Ybelle and Ludar to escape alive from the castle?

Test your dexterity with this tremendously exciting platform game!

%description -n %{name}-editor
This package contains a level editor for Holotz's Castle.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p0
%patch1 -p1
%patch2 -p1
sed -i -e 's|share/games|share|' -e 's|-Werror|-Wno-error|' -e 's|-L\.|-L. -lz|' src/Makefile
perl -pi -e s"|\r\n|\n|g" res/playlist.txt
rm -f res/savedata/empty.txt
sed -i -e 's|tmp > 0|tmp != NULL|' -e 's|0 >= (end|NULL == (end|' JLib/JLib/Util/JTextFile.cpp

%build
make

%install
rm -rf %{buildroot}
%makeinstall INSTALL_ROOT=%{buildroot}

install -d -m 755 %{buildroot}%{_mandir}/man6/
install -m 644 man/%{name}.6 %{buildroot}%{_mandir}/man6/
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
install -m 644 %{_sourcedir}/hc-48x48.png -D %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -m 644 %{_sourcedir}/hc-32x32.png -D %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 644 %{_sourcedir}/hc-16x16.png -D %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
#game

#game, xdg
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Holotz's Castle
Comment=%{Summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

#editor
install -m 644 man/%{name}-editor.6 %{buildroot}%{_mandir}/man6/
install -m 644 %{_sourcedir}/holotz-castle-editor-48x48.png -D %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}-editor.png
install -m 644 %{_sourcedir}/holotz-castle-editor-32x32.png -D %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}-editor.png
install -m 644 %{_sourcedir}/holotz-castle-editor-16x16.png -D %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}-editor.png

#editor, xdg
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}-editor.desktop << EOF
[Desktop Entry]
Name=Holotz's Castle Editor
Comment=Level editor for Holotz's Castle
Exec=%{name}-editor
Icon=%{name}-editor
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

%clean
rm -rf %{buildroot}

%files
%doc LICENSE.txt doc/*.txt
%attr(0755,root,games) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/game
%{_mandir}/man6/%{name}.6*
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files -n %{name}-editor
%doc LICENSE.txt
%attr(0755,root,games) %{_bindir}/%{name}-editor
%{_datadir}/%{name}/editor
%{_mandir}/man6/%{name}-editor.6*
%{_datadir}/icons/hicolor/64x64/apps/%{name}-editor.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}-editor.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}-editor.png
%{_datadir}/applications/%{name}-editor.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.14
- Rebuilt for Fedora
* Tue Sep 08 2009 Guillaume Bedot <littletux@mandriva.org> 1.3.14-1mdv2010.0
+ Revision: 433549
- New release 1.3.14
* Mon Jan 12 2009 Guillaume Bedot <littletux@mandriva.org> 1.3.13-1mdv2009.1
+ Revision: 328582
- Release 1.3.13
* Mon Sep 08 2008 Guillaume Bedot <littletux@mandriva.org> 1.3.12-1mdv2009.0
+ Revision: 282547
- Release 1.3.12 (with additional levels already included)
- Rediffed patch1
- Dropped unneeded buildrequires
- Fixed license, and some more cleanup
  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Fri Jan 11 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.3.10-1mdv2008.1
+ Revision: 148217
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Fri Aug 10 2007 Guillaume Bedot <littletux@mandriva.org> 1.3.10-1mdv2008.0
+ Revision: 61436
- Release 1.3.10
* Wed Apr 18 2007 Guillaume Bedot <littletux@mandriva.org> 1.3.9-1mdv2008.0
+ Revision: 14714
- New release 1.3.9
* Tue Aug 01 2006 Guillaume Bedot <littletux@mandriva.org> 1.3.8-3mdv2007.0
- patch from debian fixing warnings instead of ignoring them and endianess
 (trying to fix bug #24005)
* Mon Jul 31 2006 Guillaume Bedot <littletux@mandriva.org> 1.3.8-2mdv2007.0
- fix menu + xdg
* Wed Mar 15 2006 Guillaume Bedot <littletux@mandriva.org> 1.3.8-1mdk
- 1.3.8
* Sun Jan 22 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.3.7-2mdk
- Add BuildRequires: MesaGLU-devel
* Mon Nov 28 2005 Guillaume Bedot <littletux@mandriva.org> 1.3.7-1mdk
- New release
* Wed May 18 2005 Guillaume Bedot <littletux@mandriva.org> 1.3.6-2mdk
- Well, a package from David Black aka dblackia already existed in the club...
 the best of both is now kept in this new release, i hope.
- New descriptions, summary, and a additional icon, used for the editor 
 new menu entry.
- And finally, the package is split into game and editor packages.
* Tue May 17 2005 Guillaume Bedot <littletux@mandriva.org> 1.3.6-1mdk
- first package for Holotz Castle.

