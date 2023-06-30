Summary:	A 3D adventure and roleplaying game
Name:		balazar
Version:	0.3.4
Release:	1
License:	GPL
Group:		Amusements/Games
Source:		https://download.gna.org/balazar/Balazar-%version.tar.bz2
Source10:	%{name}-16.png
Source11:	%{name}-32.png
Source12:	%{name}-48.png
URL:		https://home.gna.org/oomadness/en/balazar/
# or https://balazar.nekeme.net/
BuildRequires:	python2-devel, SDL-devel
Requires:	soya, python-imaging, pyogg, pyvorbis, pyopenal
Requires:	tofu, cerealizer
#pyrex=0.9.3, cal3d=0.9.1
BuildArch: noarch

%description
A 3D adventure and roleplaying game string Balazar the photo-mage.

%prep
%setup -q -n Balazar-%version

%build
python2 setup.py build

%install
rm -Rf $RPM_BUILD_ROOT

python2 setup.py install --root=$RPM_BUILD_ROOT
install -m 644 -D %{SOURCE10} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 644 -D %{SOURCE11} $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png
install -m 644 -D %{SOURCE12} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

mkdir $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Balazar
Name[zh_TW]=貝拉薩兄弟
Comment=%{summary}
Comment[zh_TW]=Balazar 類似瑪莉兄弟的遊戲
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;AdventureGame;
EOF

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%doc AUTHORS README LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%exclude %{_datadir}/Balazar-0.3.4-py2.?.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.4
- Rebuilt for Fedora
* Wed Nov 26 2008 milochen <milo_chen@mail2000.com.tw> 0.3.4-4.ossii
- initial ossii package
* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3.4-4mdv2009.0
+ Revision: 243160
- rebuild
- kill re-definition of %%buildroot on Pixel's request
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Wed Dec 05 2007 Emmanuel Andry <eandry@mandriva.org> 0.3.4-2mdv2008.1
+ Revision: 115724
- fix menu entry (bug #35851)
- New version
- drop old menu
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'
* Sat Jan 06 2007 Olivier Blin <oblin@mandriva.com> 0.3.1-5mdv2007.0
+ Revision: 104991
- use english website URL (John Keller)
* Sat Jan 06 2007 Olivier Blin <oblin@mandriva.com> 0.3.1-4mdv2007.1
+ Revision: 104709
- remove glew dependency, it is not required and libglew is already pulled by soya
- remove dependencies that are already required by soya
- remove python-pyrex dependency, it is not required for balazar to run
* Fri Jan 05 2007 Emmanuel Andry <eandry@mandriva.org> 0.3.1-3mdv2007.1
+ Revision: 104587
- Rebuild for python-pyrex
  package egg-info file
  + Eskild Hustvedt <eskild@mandriva.org>
    - Import balazar
* Mon Aug 28 2006 Emmanuel Andry <eandry@mandriva.org> 0.3.1-2mdv2007.0
- requires pyopenal
* Wed Jul 12 2006 Lenny Cartier <lenny@mandriva.com> 0.3.1-1mdv2007.0
- 0.3.1
- requires cerealizer
* Sun Jun 18 2006 Emmanuel Andry <eandry@mandriva.org> 0.3-1mdv2007.0
- 0.3
- xdg compliant
* Thu Oct 27 2005 Lenny Cartier <lenny@mandriva.com> 0.2-2mdk
- rebuild for latest allegro
* Mon Sep 12 2005 Guillaume Bedot <littletux@mandriva.org> 0.2-1mdk
- New release
- added some requires
* Wed Mar 02 2005 Guillaume Bedot <guillaume.bedot@cegetel.net> 0.1-1mdk
- First Mandrakelinux package
