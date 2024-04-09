Name:		loemu
Version:	0.3.1
Release:	2.1
Summary:	A simple python front-end for various emulators
License:	GPLv2+
Group:		Emulators
URL:		http://loemu.pegueroles.com/
Source0:	http://loemu.pegueroles.com/dists/%{name}-%{version}.tar.gz
Source10:	loemu-32.png
Source40:	loemu-0.3.0-fr.po.tar.bz2 
Patch0:		loemu-0.3.0-default-config.patch
BuildRequires:	python2-devel
BuildRequires:	pygtk2-libglade
BuildRequires:	python2-libxml2
BuildRequires:  python2-libxslt
BuildRequires:	unzip
BuildRequires:	intltool
#Requires:	libxslt-python
#Requires:	pygtk2-libglade
#Suggests:	sdlmame
#Suggests:	snes9x
#Suggests:	zsnes
#Suggests:	xmame
BuildArch:	noarch

%description
Loemu provides a simple frontend for various emulators.

It currently supports game emulation with xmame, sdlmame and snes9x.
But the design of loemu allows the support of more emulators adding specific 
emulator configuration files. 

This package is in PLF because of Mandriva policy regarding emulators.

%prep
%setup -q
%patch0 -p0
tar -xvjf %{_sourcedir}/loemu-0.3.0-fr.po.tar.bz2

%build
sed -i '7,24d' setup.py
DISPLAY=:0 python2 setup.py build 

%install
rm -rf %{buildroot}
DISPLAY=:0 python2 setup.py install --root=%{buildroot}

#xdg menu
#icon
install -d -m 755 %{buildroot}/%{_datadir}/pixmaps
install -m 644 %{_sourcedir}/loemu-32.png %{buildroot}/%{_datadir}/pixmaps/loemu.png
#menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/loemu.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Loemu
Name[zh_TW]=遊戲機模擬器
Comment=%{summary}
Comment[zh_TW]=Python 編寫的簡易遊戲機模擬器
Exec=loemu
Icon=loemu
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc README
%{_bindir}/*
%{_datadir}/loemu
%{_datadir}/locale/*/LC_MESSAGES/loemu.mo
%{_datadir}/pixmaps/loemu.png
%{_datadir}/applications/loemu.desktop
%{python2_sitelib}/loemu*

%clean
rm -rf %{buildroot}

%changelog
* Mon Mar 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
* Tue Oct 21 2008 Guillaume Bedot <littletux@zarb.org> 0.3.1-2plf2009.1
- removed sdlmame related files (catver, nplayers) :
 up-to date version will now be in sdlmame package
- updated patch0 to reflect this change
- rpm spec policy proposal related changes
- drop old README.urpmi.update
* Tue Mar  4 2008 Guillaume Bedot <littletux@zarb.org> 0.3.1-1plf2008.1
- 0.3.1
* Fri Feb  8 2008 Guillaume Bedot <littletux@zarb.org> 0.3.0-2plf2008.1
- nplayers & catver update
* Mon Jan 28 2008 Guillaume Bedot <littletux@zarb.org> 0.3.0-1plf2008.1
- 0.3.0
* Thu Dec 06 2007 Guillaume Bedot <littletux@zarb.org> 0.2.1-2plf2008.1
- fix 2007.0 build
* Tue Nov 27 2007 Guillaume Bedot <littletux@zarb.org> 0.2.1-1plf2008.1
- 0.2.1
- french translation and patch update
* Sat Jul 14 2007 Guillaume Bedot <littletux@zarb.org> 0.2.0-4plf2008.0
- changed the path from the real sdlmame binary to the wrapper
- buildreq intltool
* Sun Jun 24 2007 Guillaume Bedot <littletux@zarb.org> 0.2.0-3plf2008.0
- french translation fixes
* Thu Jun 21 2007 Guillaume Bedot <littletux@zarb.org> 0.2.0-2plf2008.0
- Added a french translation 
* Tue Jun 19 2007 Guillaume Bedot <littletux@zarb.org> 0.2.0-1plf2008.0
- Release 0.2.0
- Updated custom config (added nplayers.ini), warning when updating
* Mon May 21 2007 Guillaume Bedot <littletux@zarb.org> 0.1.1-2plf2008.0
- Req and buildreq fixes
- Custom config : catver.ini + allow cheats
* Wed May 16 2007 Guillaume Bedot <littletux@zarb.org> 0.1.1-1plf2008.0
- First package for PLF
