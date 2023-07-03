%undefine _debugsource_packages

Name: 		pathological
Summary: 	Logical game
Version: 	1.1.3
Release: 	1
License: 	GPLv2+
Group: 		Games/Puzzles
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Don't install something to /usr/X11R6 - AdamW 2008/09
Patch0:		pathological-1.1.3-location.patch
# fix #35077
Patch1:     pathological-1.1.3-fix_encoding.patch
URL: 		https://pathological.sourceforge.net/
BuildRequires:	netpbm
BuildRequires:	ImageMagick
Requires:	pygame

%description
To solve a level, you fill each wheel with four marbles of matching 
colors. Various board elements such as teleporters, switches, filters, 
etc., make the game interesting and challenging. New levels can be 
created using your favorite text editor.

%prep
%setup -q  
%patch0 -p1 -b .location
%patch1 -p0
sed -i -e 's,/usr/lib,%{_libdir},g' -e 's,usr/games,usr/bin,g' -e 's,share/games,share,g' Makefile

%build
%__make

%install
rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

chmod 755 %{buildroot}%{_libdir}/%{name}/bin/*
rm -rf %{buildroot}%{_docdir}/%{name}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32}/apps
convert %{name}.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{name}.xpm %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=pathological
Name=Pathological
Name[zh_TW]=病態彈珠
Comment=Logic game
Comment[zh_TW]=Pathological 嘗試裝滿彈珠的邏輯遊戲
Categories=Game;LogicGame;
Icon=%{name}
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/%{name}.py

%clean
rm -rf %{buildroot}

%files
%doc README LICENSE
%{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/%{name}
%{_libdir}/%{name}/bin/*
%{_includedir}/X11/pixmaps/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_localstatedir}/games/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.3
- Rebuilt for Fedora
* Fri Apr 03 2009 Michael Scherer <misc@mandriva.org> 1.1.3-6mdv2009.1
+ Revision: 363942
- also fix the menu
* Fri Apr 03 2009 Michael Scherer <misc@mandriva.org> 1.1.3-5mdv2009.1
+ Revision: 363909
- fix the rm group
- fix bug 35077
* Sun Sep 07 2008 Adam Williamson <awilliamson@mandriva.org> 1.1.3-3mdv2009.0
+ Revision: 282295
- replace hardcoded /usr/lib in Makefile to fix x86-64 build
- buildrequires imagemagick
- generate fd.o icons from shipped .xpm file
- add location.patch: don't use /usr/X11R6
- clean up the docs mess
- s,$RPM_BUILD_ROOT,%%{buildroot}
- source location
- new license policy
- drop unncessary defines
  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - fix no-buildroot-tag
    - auto convert menu to XDG
    - BR netpbm
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import pathological
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Sun Mar 20 2005 Michael Scherer <misc@mandrake.org> 1.1.3-2mdk
- requires pygame, fix #12744
- fix spec
* Tue Feb 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-1mdk
- 1.1.3
