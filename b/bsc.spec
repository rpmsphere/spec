%undefine _debugsource_packages

Name:       	bsc
Version:    	4.1.0
Release:    	8.1
Summary:    	Beesoft Commander file manager
License:    	GPLv2+
Group:      	File tools
URL:        	http://www.beesoft.org/index.php?id=bsc
Source:     	http://www.beesoft.org/download/%{name}_%{version}_src.tar.bz2
BuildRequires:	qt4-devel
BuildRequires:	ghostscript-core ImageMagick

%description
Beesoft Commander is a file manager (like Norton Commander) for Linux. It is
based on Qt4-GUI.

%prep
%setup -q -n bsc

%build
qmake-qt4 QMAKE_CXXFLAGS+="-fPIC"
make

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 0755 %{name} %{buildroot}%{_datadir}/%{name}
install -m 0644 help.en.html %{buildroot}%{_datadir}/%{name}
cp -R img %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -s  ../../%{_datadir}/%{name}/%{name} %{name}
popd 

# menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Beesoft Commander
Comment=Beesoft Commander file manager
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=System;FileManager;Qt;
EOF

# icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48}/apps
convert -resize 16x16 BeesoftCommander.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
convert -resize 48x48 BeesoftCommander.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install BeesoftCommander.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Thu Feb 06 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.0
- Rebuilt for Fedora
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1.0-2mdv2011.0
+ Revision: 616864
- the mass rebuild of 2010.0 packages
* Wed May 20 2009 Jérôme Brenier <incubusss@mandriva.org> 4.1.0-1mdv2010.0
+ Revision: 378097
- new version 4.1.0 based on Qt4
- specfile modified accordingly
- license fixed (GPLv2+)
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Fri Apr 27 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2.27-1mdv2008.0
+ Revision: 18795
- Import bsc
