%undefine _debugsource_packages
Name:           aoi
Version:        3.2.0
Release:        1
Summary:        3D modeling and rendering studio Written in Java
URL:            http://www.artofillusion.org
Group:          Graphics/3D
Source0:        https://sourceforge.net/projects/aoi/files/ArtOfIllusion-source/3.2/ArtOfIllusion-3.2.0.zip
Source1:        jmf-2_1_1e-alljava.zip
Patch1:         aoi-2.8.1-mga-encoding.patch
License:        GPLv2+
BuildArch:      noarch
BuildRequires:  java-devel-openjdk
BuildRequires:  lua
BuildRequires:  ant
#BuildRequires:  ant-nodeps
#BuildRequires:  jogl2
BuildRequires:  bsh
#BuildRequires:  jama
BuildRequires:  dos2unix
#BuildRequires:  buoy
BuildRequires:  xml-commons-apis
BuildRequires:  xerces-j2
Requires:       java >= 1.5

%description
Art of Illusion is a free, open source 3D modeling and rendering studio.
Many of its capabilities rival those found in commercial programs.
Highlights include subdivision surface based modeling tools,
skeleton based animation, and a graphical language 
for designing procedural textures and materials.

%files
%doc *.md
%attr(755,root,root) %{_bindir}/%{name}
%attr(644,root,root) %{_datadir}/%{name}/ArtOfIllusion.jar
%attr(755,root,root) %{_datadir}/%{name}/Plugins
%attr(644,root,root) %{_datadir}/applications/%{name}.desktop
%attr(644,root,root) %{_datadir}/pixmaps/%{name}.png

%prep
%setup -q -a1 -n ArtOfIllusion-%{version}
# We only use this jar for build, not inclued in %%files.
mv JMF-2.1.1e/lib/jmf.jar .
#patch1 -p1 -b .aoi-2.8.1-mga-encoding.patch

%build
export CLASSPATH="."
%ant -buildfile ArtOfIllusion.xml

%install
# Installs the jar
%__install -dm 755 %{buildroot}%{_datadir}/%{name}/Plugins
%__install -m 644 Live_Application/ArtOfIllusion.jar %{buildroot}%{_datadir}/%{name}

# Install the script
cat > %{name} <<EOF
#!/bin/sh
AOI_CLASSPATH=/usr/share/java/buoy.jar:/usr/share/java/buoyx.jar:/usr/share/java/jama.jar:/usr/share/java/jogl.jar:/usr/share/java/bsh.jar:/usr/share/aoi/ArtOfIllusion.jar:/usr/share/java/gluegen.jar:
java -cp \$AOI_CLASSPATH artofillusion.ArtOfIllusion
EOF
%__install -dm 755 %{buildroot}%{_bindir}
%__install -m 755 %{name} %{buildroot}%{_bindir}

# convert win32 EOL to unix EOL
dos2unix License.md
dos2unix Readme.md

# icons
%__install -d -m755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 InstallerSrc/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# desktopfile
%__install -d -m755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Art of Illusion
GenericName=3D modelling and rendering studio
Comment=3D modelling and rendering studio Written in Java
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Graphics;
EOF

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.0
- Rebuilt for Fedora
* Fri Jan 11 2013 umeabot <umeabot> 2.8.1-4.mga3
+ Revision: 345626
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Mon Dec 31 2012 barjac <barjac> 2.8.1-3.mga3
+ Revision: 336463
- update group
- clean spec
- fix build - patched odd characters in comments
* Wed May 11 2011 dmorgan <dmorgan> 2.8.1-2.mga1
+ Revision: 97125
- Add some provives
* Wed May 11 2011 dmorgan <dmorgan> 2.8.1-1.mga1
+ Revision: 97102
- imported package aoi
