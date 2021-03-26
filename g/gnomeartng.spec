Summary:	The successor of Gnome-Art 
Name:		gnomeartng
Version:	0.7.0
Release:	20.4
URL:		http://gnomeartng.plasmasolutions.de/
Source0:  	http://download.berlios.de/gnomeartng/%{name}-%{version}.tar.gz
License:	GPL
Group:		User Interface/Desktops
BuildArch:      noarch
BuildRequires:  libpng-devel
BuildRequires:	libpng12
BuildRequires:  mono-devel, gnome-sharp-devel
BuildRequires:  udisks2

%description
With this application you're able to change your gnome look and feel completely.
It is the successor of Gnome-Art and lets you change your Gnome-themes (icon-, 
wallpaper-, splash-,...-themes) with one click.

%prep
%setup -q

%build
mcs `pkg-config --libs gtk-sharp-2.0 glade-sharp-2.0 gnome-sharp-2.0 gconf-sharp-2.0` \
%if %{fedora}>22
    -r:/usr/lib/mono/4.5/Mono.Posix.dll \
%else
    -r:/usr/lib/mono/2.0/Mono.Posix.dll \
%endif
    -resource:gui.glade -resource:legacy-icon-mapping.xml \
    -r:ICSharpCode.SharpZipLib -r:System.Windows.Forms.dll -recurse:./src/*.cs -out:GnomeArtNg.exe

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af locale images GnomeArtNg.exe $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cat > $RPM_BUILD_ROOT%{_bindir}/gnomeartng << EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec mono GnomeArtNg.exe
EOF

# desktop menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/gnomeartng.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Gnome-Art Next Gen
Comment=Changes your gnome look and feel completely.
Exec=gnomeartng
Icon=gnomeartng
Terminal=false
Type=Application
Categories=GNOME;GTK;Graphics;
EOF

# icon
install -Dm 644 images/Icon.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.svg

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README VERSION TODO
%attr(755,root,root) %{_bindir}/gnomeartng
%{_datadir}/%{name}*
%{_datadir}/pixmaps/*.svg
%{_datadir}/applications/*.desktop

%changelog
* Mon Mar 21 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.0
- Rebuild for Fedora
* Thu Jul 16 2009 Slick50 <lxgator@gmail.com> 0.7.0-1pclos2009
- 0.7.0
* Wed Mar 11 2009 Slick50 <lxgator@gmail.com> 0.6.0-2pclos2007
- rebuild
* Thu Jul 31 2008 Slick50 <slick50@linuxgator.org> 0.6.0-1pclos2007
- 0.6.0
* Mon Jun 30 2008 Slick50 <slick50@linuxgator.org> 0.5.1-1pclos2007
- 0.5.1
* Fri Jun 13 2008 Slick50 <slick50@linuxgator.org> 0.4.5-1pclos2007
- Initial build
