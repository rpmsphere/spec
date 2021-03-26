%define	name	civil
%define	Name	Civil
%define	version	0.83
%define	title	Civil
%define	longtitle	American civil war simulation
%define	title_editor	Civil Editor
%define	longtitle_editor	Civil scenario editor
Name:		%{name}
Version:	%{version}
Release:	1
Summary:	%{longtitle}
License:	GPL
Group:		Games/Strategy
URL:		http://civil.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/civil/%{name}-%{version}.tar.bz2
Patch0:		civil-0.83-python24.patch.bz2
Patch1:		civil-0.83-remove-broken-pygame-check.patch
Requires:	SDL >= 1.2
Requires:	python >= 2.1
Requires:	pygame >= 1.5.3
Requires:	%{name}-graphics = %{version}
Requires:	%{name}-sounds = %{version}
BuildRequires:	python-devel
BuildRequires:	ImageMagick

%description
Civil is a game that simulates battles in the American Civil War. It is 
playable by two players over a network. Civil aims to be able to recreate
battles in great detail.

%package	graphics
Summary:	Civil graphics
Group:		Games/Strategy
Requires:	%{name} = %{version}

%description	graphics
Graphics for Civil, a simulation of the American Civil War.

%package	sounds
Summary:	Civil sounds
Group:		Games/Strategy
Requires:	%{name} = %{version}

%description	sounds
Sounds for Civil, a simulation of the American Civil War.

%package	scenarios
Summary:	Civil sample scenarios
Group:		Games/Strategy
Requires:	%{name} = %{version}

%description	scenarios
Some example scenarios for Civil, a simulation of the American Civil
War.

%package	editor
Summary:	Civil scenario editor
Group:		Games/Strategy
Requires:	%{name} = %{version}
Requires:	python-PQueue

%description	editor
Scenario editor for civil, a simulation of the American Civil War.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .pygame
# fix perms
for file in AUTHORS BUGS ChangeLog INSTALL LICENSE README TODO; do
    chmod 644 $file; 
done

# clean-up build files included in tarball
rm -rf src/map/los/build

# remove useless shellbang 
sed -i -e '1d' src/civil{,-editor,-ai,-lounge}.py
sed -i 's|, s$|,|' src/old/setup_players.py

%build
%configure --bindir=%{_bindir} --datadir=%{_datadir}/%{name}
%__make

%install
rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install
# help
install -d %{buildroot}%{_datadir}/%{name}/doc/help
install -m 644 doc/help/*.xml %{buildroot}%{_datadir}/%{name}/doc/help

# icons
install -D -m 644 gfx/periphery/civil-icon-48x48.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# drop provided desktop files, they are too much buggy
rm -rf %{buildroot}%{_datadir}/applnk/Games/TacticStrategy/*.desktop

install -d -m 755 %{buildroot}%{_datadir}/applications
cat >  %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{title}
Comment=%{longtitle}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Application;Game;ArcadeGame;
Name[zh_TW]=南北戰爭
Comment[zh_TW]=南北戰爭
EOF

cat >  %{buildroot}%{_datadir}/applications/%{name}-editor.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{title_editor}
Comment=%{longtitle_editor}
Exec=%{name}-editor
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Application;Game;ArcadeGame;
Name[zh_TW]=南北戰爭編輯器
Comment[zh_TW]=南北戰編輯器
EOF

#ln -s %{_libdir}/python%{pyver}/site-packages/ccivil.so %{buildroot}/%{_datadir}/%{name}/src/map/los/
ln -s %{_libdir}/python2.7/site-packages/ccivil.so %{buildroot}/%{_datadir}/%{name}/src/map/los/

chmod ogu+x %{buildroot}/%{_datadir}/%{name}/src/civil-server.py

# no longer works, miss some xml nodes
rm -f %{buildroot}/%{_datadir}/%{name}/scenarios/chakie_test.civil

%clean
rm -rf %{buildroot} 

%files
%doc AUTHORS BUGS ChangeLog INSTALL LICENSE README TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-ai
%{_bindir}/%{name}-lounge
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/src
%{_datadir}/%{name}/doc
%{python_sitearch}/*
%{_mandir}/man6/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files graphics
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/gfx

%files sounds
%{_datadir}/%{name}/sound

%files scenarios
%{_datadir}/%{name}/scenarios

%files editor
%{_bindir}/%{name}-editor
%{_datadir}/applications/%{name}-editor.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.83
- Rebuild for Fedora

* Fri Oct 31 2008 milochen <milo_chen@mail2000.com.tw> 0.83-9.ossii
- initial ossii package

* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.83-9mdv2007.0
+ Revision: 96498
- Rebuild against new python
- Import civil

* Mon Sep 11 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.83-8mdv2007.0
- drop broken pygame check (P1)
- cosmetics

* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.83-7mdv2007.0
- xdg menu

* Wed May 10 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.83-6mdk
- patch 0: make it work with python-2.4

* Wed Dec 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.83-5mdk
- %%mkrel
- spec cleanup
- remove some useless shellbangs

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 0.83-4mdk
- Rebuild for new python

* Mon Nov 01 2004 Michael Scherer <misc@mandrake.org> 0.83-3mdk
- Buildrequires

* Tue Sep 28 2004 Michael Scherer <misc@mandrake.org> 0.83-2mdk 
- fix #11740, and other bugs

* Thu Aug 26 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.83-1mdk 
- new version

* Fri Jul 09 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.82-5mdk 
- rpmbuildupdate aware
- fixed menu category

* Mon Jan 12 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.82-4mdk
- buildrequires (slbd)

* Sat Aug 30 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 0.82-3mdk
- rebuild for latest python
- this is not a noarch package, they are python extension inside

* Mon Jun 16 2003 Per ?yvind Karlsen <peroyvind@sintrax.net> 0.82-2mdk
- fix problem with help files (from David Coe <david.coe@dsl.pipex.com>)

* Wed Jun 11 2003 Per ?yvind Karlsen <peroyvind@sintrax.net> 0.82-1mdk
- 0.82
- quiet setup
- rm -rf %{buildroot} in the correct stage

* Sat Jan 04 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.81-2mdk
- rebuild

* Mon Sep 09 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.81-1mdk  
- 0.8.1
- splitted package to takes cares of poor guys with low bandwidth
- fixed missing doc files

* Wed Sep 04 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.80-3mdk  
- require pygame >= 1.5.3 
- menu entry

* Sat Aug 31 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.80-2mdk  
- scenario included in main package
- included missing fonts
- requires python-PQueue

* Sat Aug 31 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.80-1mdk
- first mdk release
