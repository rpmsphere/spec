%define pre     20050612

Name:           xconq
Version:        7.5.0
Release:        21.1
Summary:        General turn-based 2D strategy game system
URL:            https://xconq.org
License:        GPL
Group:          Games/Strategy
Source0:        https://prdownloads.sourceforge.net/xconq/%{name}-%{version}-0pre.0.%{pre}.tar.bz2
Patch0:         xconq-7.5.0-0pre.0.20050612-makefile.patch
Patch1:         %{name}-7.5.0.tclpath.patch
Patch2:         xconq-7.5.0-64bit-fix.patch
Patch3:         xconq-7.5.0-0pre.0.20050612-fix-format-errors.patch
BuildRequires:  paragui-devel
BuildRequires:  freetype-devel
BuildRequires:  SDL-devel
BuildRequires:  ncurses-devel
BuildRequires:  ncurses-static
BuildRequires:  tk-devel
BuildRequires:  tcl-devel
BuildRequires:  texinfo
BuildRequires:  ghostscript-core ImageMagick
BuildRequires:  libXaw-devel

%description
Xconq is a general strategy game system.  It is a complete system that
includes all the components: a portable engine, graphical interfaces
for Unix/Linux/X11, Macintosh, and Windows, multiple AIs, networking
for multi-player games, and an extensive game library.

In addition to Xconq's "standard" game, which is similar to the
classic Empire/Empire Deluxe games of years ago, the game library
includes games for ancient civilizations, the Peloponnesian War, the
Roman Civil War, Frederician strategy, Napoleonic strategy, Gettysburg
at a brigade scale, the Russian revolution, the Normandy invasion,
WWII at scales from tactical to grand strategic, Beirut street
fighting, voyages of discovery, African exploration, and many others,
including space and fantasy games.

As befits its emphasis on strategy, Xconq's forte is turn-based play
using overhead or isometric views of a tiled world.  The world is 
basically two-dimensional, although varying elevations are available 
for games that need elevation effects or line-of-sight.  Xconq is 
especially interesting for games about unusual or lesser-known strategic
situations; it is unique in providing a single system for modelling
the conflicts and strategies of any period in history.

%package        tcltk
Summary:        The Tcl/Tk user interface for the Xconq game system
Group:          Games/Strategy
Requires:       %{name} = %{version}

%description    tcltk
The Tcl/Tk user interface for the Xconq game engine relies on a mixture of 
Tcl scripts and C code to provide a multi-windowed user experience. This 
is presently the one which most players use.

%package        curses
Summary:        The curses (console) user interface for the Xconq game system
Group:          Games/Strategy
Requires:       %{name} = %{version}

%description    curses
The Curses user interface is for running games in the Xconq engine on a 
text console. It is quick, but lacking the more complete experience and 
conveniecne of a graphical user interface.

%package        sdl
Summary:        The SDL user interface for the Xconq game system
Group:          Games/Strategy
Requires:       %{name} = %{version}

%description    sdl
The SDL user interface is in its infancy and much development needs to be 
done on it. However, it is a more modern game interface following the 
single-window paradigm, and it is speedy.

%prep
%setup -q -n %{name}-%{version}-0pre.0.%{pre}
%patch 0 -p1 -b .makefile
%patch 1 -p0 -b .tclpath
%patch 2 -p1 -b .64bit
%patch 3 -p1 -b .format
sed -i 's|color < 0|color == NULL|' tcltk/tkmap.c

%build
%configure      --disable-freetypetest \
                --disable-paraguitest \
                --bindir=%{_bindir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir} \
                --datadir=%{_datadir}/%{name} \
                --with-tclconfig=%{_libdir} \
        --with-tkconfig=%{_libdir} \
                --enable-alternate-scoresdir=%{_localstatedir}/lib/games/%{name}

sed -i 's|-Wall|-Wall -Wno-narrowing -fpermissive -std=gnu++11|' Makefile */Makefile */*/Makefile

LDFLAGS="%optflags" \
make    all \
        all-cconq \
    all-sdlconq \
        info

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_datadir}/games
install -d -m 755 %{buildroot}%{_localstatedir}/lib/games
%make_install \
        install-cconq \
    install-sdlconq \
        install-info \
        bindir=%{buildroot}%{_bindir} \
    mandir=%{buildroot}%{_mandir} \
    infodir=%{buildroot}%{_infodir} \
        datadir=%{buildroot}%{_datadir}/%{name} \
        scoresdir=%{buildroot}%{_localstatedir}/lib/games/%{name}

mv %{buildroot}%{_bindir}/{x,tk}conq
mv %{buildroot}%{_mandir}/man6/{x,tk}conq.6

# icons
install -d %{buildroot}%{_datadir}/pixmaps
convert images/default.gif -resize 48x48! %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}-tcltk.desktop << EOF
[Desktop Entry]
Name=Xconq Tk interface
Comment=%{Summary}, Tk interface
Exec=tkconq
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}-sdl.desktop << EOF
[Desktop Entry]
Name=Xconq SDL interface
Comment=%{Summary}, SDL interface
Exec=sdlconq
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

for i in sdlconq tkconq; do
mv %{buildroot}%{_bindir}/${i} %{buildroot}%{_bindir}/${i}.bin
cat <<EOF >  %{buildroot}%{_bindir}/${i}
#!/bin/bash
cd  %{_datadir}/%{name}/lib
exec %{_bindir}/${i}.bin 
EOF
done;

%files
%doc README ChangeLog NEWS doc/*.html changelogs
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%dir %attr(-,games,games) %{_localstatedir}/lib/games/%{name}
%{_infodir}/*

%files tcltk
%attr(2755,root,games) %{_bindir}/tkconq*
%{_bindir}/imfapp
%{_bindir}/imf2x
%{_bindir}/x2imf
%{_mandir}/man6/tkconq.6*
%{_datadir}/applications/%{name}-tcltk.desktop

%files curses
%attr(2755,root,games) %{_bindir}/cconq*
%{_mandir}/man6/cconq.6*

%files sdl
%attr(2755,root,games) %{_bindir}/sdlconq*
%{_datadir}/applications/%{name}-sdl.desktop

%changelog
* Tue Feb 24 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 7.5.0
- Rebuilt for Fedora
* Wed Dec 08 2010 Funda Wang <fwang@mandriva.org> 7.5.0-1.20050612.8mdv2011.0
+ Revision: 616052
- fix more makefile
  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages
* Tue Apr 13 2010 Thierry Vignaud <tv@mandriva.org> 7.5.0-1.20050612.7mdv2010.1
+ Revision: 534511
- rebuild
* Sun Apr 12 2009 Michael Scherer <misc@mandriva.org> 7.5.0-1.20050612.5mdv2009.1
+ Revision: 366478
- oups, forgot to include the binary
- fix 38354 by correcting menu
* Sat Apr 11 2009 Michael Scherer <misc@mandriva.org> 7.5.0-1.20050612.4mdv2009.1
+ Revision: 366293
- remove old bzip patch ( already uncompressed )
- fix bug 49542 and 49544
* Wed Mar 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 7.5.0-1.20050612.3mdv2009.1
+ Revision: 348661
- fix format errors
- fix build with latest tk
  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick
* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 7.5.0-1.20050612.2mdv2009.0
+ Revision: 218426
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
- adapt to %%_localstatedir now being /var instead of /var/lib (#22312)
* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 7.5.0-1.20050612.2mdv2008.1
+ Revision: 140953
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 7.5.0-1.20050612.2mdv2008.0
+ Revision: 82059
- rebuild for new soname of tcl
  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'
* Mon Jun 18 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 7.5.0-1.20050612.1mdv2008.0
+ Revision: 41015
- ?\194?\164#"?\194?\164#" buildrequires
- fix buildrequires
- fix buildrequires
- fix 64 bit build (P2)
- drop debian menu
- a bit more new snapshot..
- Import xconq
* Fri Aug 25 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 7.5.0-1.20050117.7mdv2007.0
- fix macros for menu
- xdg menu
- cleanups
* Wed Jan 04 2006 Oden Eriksson <oeriksson@mandriva.com> 7.5.0-0.20050117.6mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps
* Thu Dec 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 7.5.0-0.20050117.5mdk
- fix buildrequires
- patch tk version to find tkconq.tcl correctly (fix #20363)
* Wed Dec 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 7.5.0-0.20050117.4mdk
- buildrequires
* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 7.5.0-0.20050117.3mdk
- %%mkrel
- fix doc files encoding and perms
- relax requires versioning
* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 7.5.0-0.20050117.2mdk
- BuildRequires fix
* Fri Jan 21 2005 Guillaume Rousse <guillomovitch@mandrake.org> 7.5.0-0.20050117.1mdk 
- new version
* Sun Jan 16 2005 Guillaume Rousse <guillomovitch@mandrake.org> 7.5.0-0.20050108.1mdk 
- new version
* Sun Nov 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 7.5.0-0.20041126.1mdk 
- new version
- fix info pages installation
- menus
- disable parallel build
- use %%{_bindir} and %%{_datadir} instead of %%{_bindir} and %%{_datadir}
* Wed Nov 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 7.5.0-0.20041119.1mdk 
- first mdk release, from an heavily modified spec file from Eric McDonald <eric_mcdonald@users.sourceforge.net>
