%undefine _debugsource_packages

Summary:        Emulate keyboard or mouse actions with a joystick
Name:           qjoypad
Version:        4.1.0
Release:        16.1
Source0:        https://downloads.sourceforge.net/project/qjoypad/qjoypad/%{name}-4.1/%{name}-%{version}.tar.gz
Group:          System/Kernel and hardware
License:        GPLv2+
URL:            https://qjoypad.sourceforge.net/
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel
BuildRequires:  libX11-devel
BuildRequires:  libXtst-devel
BuildRequires:  ghostscript-core ImageMagick

%description
QJoyPad converts input from a gamepad or joystick into key-presses or mouse 
actions, letting you control any X program with your game controller.
It comes with a convenient and easy-to-use interface.

%prep
%setup -q
sed -i 's|qmake|qmake-qt4|' src/config
perl -pi -e 's,^doc\.extra,#doc\.extra,' src/qjoypad.pro
sed -i '/icons\.extra/s,\$\${icons\.path},\$\(INSTALL_ROOT\)\$\${icons\.path},g' src/qjoypad.pro

%build
cd src
./config --prefix=%{_prefix}
sed -i 's|-lXtst|-lX11 -lXtst|' Makefile
%__make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall INSTALL_ROOT=$RPM_BUILD_ROOT -C src

#icons for the menu
rm -r $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -D -m 644 icons/gamepad4-64x64.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=QJoyPad
Comment=Emulate keyboard or mouse actions with a joystick
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Qt;Settings;
EOF

%files
%doc README.txt LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.0
- Rebuilt for Fedora
* Sun Jan 16 2011 anssi <anssi> 4.1.0-4.mga1
+ Revision: 20176
- remove old scripts
- fix license tag
- rename desktop file
- remove old category from the desktop file
- imported package qjoypad
* Wed Dec 08 2010 Funda Wang <fwang@mandriva.org> 4.1.0-3mdv2011.0
+ Revision: 615295
- BR imagemagick
  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages
  + Ahmad Samir <ahmadsamir@mandriva.org>
    - use icons from the tarball directly
* Tue Mar 09 2010 Ahmad Samir <ahmadsamir@mandriva.org> 4.1.0-1mdv2010.1
+ Revision: 516838
- new upstream release 4.1.0
- build against qt4
- clean spec
- fix license
- drop patch
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 3.4.1-4mdv2010.0
+ Revision: 442558
- rebuild
* Sat Apr 11 2009 Anssi Hannula <anssi@mandriva.org> 3.4.1-3mdv2009.1
+ Revision: 366361
- rebuild
* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 3.4.1-2mdv2009.1
+ Revision: 360033
- fix 100%% cpu usage (sleep longer, sleep.patch, from azriek.fr,
  fixes bug #40886)
* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 3.4.1-1mdv2009.0
+ Revision: 218435
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.4.1-1mdv2008.1
+ Revision: 140742
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %$RPM_BUILD_ROOT on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'
* Thu Feb 08 2007 Anssi Hannula <anssi@mandriva.org> 3.4.1-1mdv2007.0
+ Revision: 118219
- buildrequires libxtst-devel
- 3.4.1
- drop patch0, applied upstream
- Import qjoypad
* Sat Jul 29 2006 Anssi Hannula <anssi@mandriva.org> 3.4-1mdv2007.0
- 3.4
- fix menu
- xdg menu
- use default pixmaps
- mkrel
* Sat Jun 19 2004 Guillaume Bedot <littletux@zarb.org> 3.3-2mdk
- Fixed groups.
* Sat Jun 19 2004 Guillaume Bedot <littletux@zarb.org> 3.3-1mdk
- First package
