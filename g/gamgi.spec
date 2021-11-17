%undefine _debugsource_packages

Name:		gamgi
Version:	0.17.4g
Release:	1
Summary:	Package to construct, view and analyse atomic structures
Group:		Sciences/Chemistry
License:	GPLv2	
URL:		http://www.gamgi.org
Source0:	http://www.gamgi.org/src/%{name}-all-%{version}.tar.gz
Patch1:		gamgi_ttfpath.patch
BuildRequires:	cairo-devel pango-devel atk-devel gtk2-devel expat-devel freetype-devel 
BuildRequires:	mesa-libGL-devel mesa-libGLU-devel gtkglext-devel
BuildRequires:	ghostscript-core ImageMagick desktop-file-utils
BuildRequires:	harfbuzz-devel
Requires:	netpbm-progs bitstream-vera-sans-fonts bitstream-vera-sans-mono-fonts
Requires:	dejavu-sans-fonts dejavu-sans-mono-fonts dejavu-serif-fonts

%description
GAMGI (General Atomistic Modelling Graphic Interface) aims to be useful for: 
  1) the scientific community working in atomistic modelling, who needs a graphic interface to build and analyse atomic structures
  2) the scientific community at large, who needs a graphic interface to study atomic structures and to prepare images for presentations
  3) teaching the atomic structure of matter in schools and universities, even inviting students to run GAMGI at home
  4) science promotion, in exhibitions and science museums.

GAMGI can determine any point group of symmetry, can build crystals for any space group of symmetry, can build Random Close Packing structures, Voronoi and coordination polyhedra for arbitrary structures. GAMGI comes with comprehensive atomic data, including ionic radius and isotopic data. GAMGI can handle an arbitrary number of independent windows, layers (with different referentials, projections, viewports and visibilities), lights (directional, positional and spot), 3D text fonts (extruded and stroked). Actions can be performed in a single object or in a list of objects previously selected. GAMGI comes with detailed but concise documentation, just one click away for each task.

%prep
%setup -q -n %{name}%{version}
%patch1 -p1 -b .ttf
%ifarch x86_64 aarch64
sed -i 's|/usr/lib|/usr/lib64|g' src/make_local
%endif
sed -i 's|-I/usr/include/pango-1.0|-I/usr/include/pango-1.0 -I/usr/include/harfbuzz -I%{_libdir}/glib-2.0/include -I%{_libdir}/gtk-2.0/include -I%{_libdir}/gtkglext-1.0/include|' src/make_local
sed -i 's|-ldl|-ldl -Wl,--allow-multiple-definition|' src/make_rules

%build
cd src
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm 755 src/%{name} $RPM_BUILD_ROOT/%{_bindir}

install -dm 755 $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -af dat/* $RPM_BUILD_ROOT/%{_datadir}/%{name}

# menu 
mkdir -p %{buildroot}%{_datadir}/applications

cat > %{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=GAMGI
Comment=Visualize and analyse atomic structures
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Education;
EOF

install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 doc/icon/gamgi316.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
convert %{buildroot}%{_datadir}/pixmaps/%{name}.png -resize 48 \
%{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
gzip doc/man/page
cp doc/man/page.gz $RPM_BUILD_ROOT/%{_mandir}/man1/gamgi.1.gz

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop
    
%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS CONTRIBUTORS SUPPORTERS doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.gz

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.17.4g
- Rebuilt for Fedora
* Sun Jan 27 2013 josef radinger <cheese@nosuchhost.net> - 0.16.3-1
- bump version
* Mon Nov 5 2012 josef radinger <cheese@nosuchhost.net> 
- 0.16.2-2
- fix build of x86_64-packages
* Sat Nov 3 2012 josef radinger <cheese@nosuchhost.net> 
- 0.16.2-1
- bump version
* Sat Oct 13 2012 josef radinger <cheese@nosuchhost.net> 
- 0.16.1-3
- modify ttfpath 
* Sat Oct 13 2012 josef radinger <cheese@nosuchhost.net> 
- 0.16.1-2
- add Requires
* Sat Oct 13 2012 josef radinger <cheese@nosuchhost.net> 
- 0.16.1-1
- init version
