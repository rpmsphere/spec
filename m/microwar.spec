%define	_name	MicroWar
Name:			microwar
Version:		2.0rc3
Release:		1
Summary:		A space invaders style arcade game
Summary(zh_TW):	一款太空入侵者類型的大型遊戲
Group:			Amusements/Games
License:		BSD License
URL:			http://microwar.sourceforge.net/
Source0:		MW20rc3-source.zip
Patch0:			%{_name}-configobj.patch
Requires:		python2-pygame
BuildArch:		noarch

%description
MicroWar is 'Space Invaders' style arcade game, in the cruel world of
micro-compter industry. You're a Macintosh faced to invading Wintel hordes 
year after year, kill more PC. Bonuses let you improve your Mac performances 
or restore life...

%description -l zh_TW
在微電腦工業的殘酷世界中，MicroWar 是"宇宙侵略者"類型的大型機台遊戲，
你是面對著年復一年成群來襲的 Wintel 的 Macintosh。殺死愈多 PC，紅利讓你增進
你的 Macintosh 效能或是恢復生命

%prep
%setup -q -n %{_name}-%{version}
%patch0 

# fix error filename to execute correctly
%__mv data/sprites/mac-IIci.png data/sprites/mac-IICi.png
%__mv data/sounds/Generic.ogg data/sounds/generic.ogg 

rm -rf ../__MACOSX

%install
rm -rf $RPM_BUILD_ROOT

# .py and data
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}/data
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}/data/backgrounds
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}/data/fonts
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}/data/sounds
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}/data/sprites
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}/doc
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}/licence
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}/English.lproj
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}/English.lproj/MainMenu.nib
%__install -m 644 *.py $RPM_BUILD_ROOT%{_datadir}/%{_name}
%__install -m 644 data/*.ini \
	$RPM_BUILD_ROOT%{_datadir}/%{_name}/data
%__install -m 644 data/backgrounds/*.jpg \
	$RPM_BUILD_ROOT%{_datadir}/%{_name}/data/backgrounds
%__install -m 644 data/fonts/*.ttf \
	$RPM_BUILD_ROOT%{_datadir}/%{_name}/data/fonts
%__install -m 644 data/sounds/*.ogg \
	$RPM_BUILD_ROOT%{_datadir}/%{_name}/data/sounds
%__install -m 644 data/sprites/*.png \
	$RPM_BUILD_ROOT%{_datadir}/%{_name}/data/sprites
%__install -m 644 doc/*.html \
	$RPM_BUILD_ROOT%{_datadir}/%{_name}/doc
%__install -m 644 doc/history.txt \
	-D $RPM_BUILD_ROOT%{_datadir}/%{_name}/doc/history.txt
%__install -m 644 licence/*.txt \
	$RPM_BUILD_ROOT%{_datadir}/%{_name}/licence/
%__install -m 644 English.lproj/mwar.icns \
	-D $RPM_BUILD_ROOT%{_datadir}/%{_name}/English.lproj/mwar.icns
%__install -m 644 English.lproj/MainMenu.nib/*.nib \
	$RPM_BUILD_ROOT%{_datadir}/%{_name}/English.lproj/MainMenu.nib

# bin
%__install -d $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/bash
cd %{_datadir}/%{_name}
python2 microwar.py
EOF
%__chmod 755 $RPM_BUILD_ROOT%{_bindir}/%{name}

# icon
%__install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
%__install -m 644 data/sprites/saucer-left.png -D \
	$RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

# .desktop
%__install -d $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=MicroWar
Comment=A space invaders style arcade game
Comment[zh_TW]=一款太空入侵者類型的大型遊戲
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/%{_name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 13 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0rc3
- Rebuilt for Fedora
* Thu Aug 26 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 2.0rc3-3
- add %dist
- add %BuildArch
- add %description of zh_TW
- fix .py files and data files install directory
- fix Exec within .desktop file
* Tue Aug 24 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 2.0rc3-2
- fix the name of src.rpm
* Mon Aug 23 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 2.0rc3-1
- Build RPM for OX
