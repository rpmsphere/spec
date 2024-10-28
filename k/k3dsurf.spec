Name:          k3dsurf
Version:       0.6.2.4
Release:       10.1
Summary:       A program which generate 3D and 4D surfaces
Group:         Graphical Desktop/Applications/Educational
URL:           https://k3dsurf.sourceforge.net/
Source:        https://mesh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Source1:       %{name}.png
License:       GPL
BuildRequires: libpng-devel
BuildRequires: glibc-devel
BuildRequires: gcc-c++
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: qt3-devel
BuildRequires: libstdc++-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXmu-devel
BuildRequires: sane-backends-devel
BuildRequires: ghostscript-core ImageMagick

%description
K3DSurf is a program which generate 3D and 4D surfaces with Mathematical formulas
(Implicit or Explicit equations) with possibility of animation and morph effects.
It's also a "Modeler" for PovRay in the area of parametric surface.

%prep
%setup -q

%build
export QTDIR=%{_libdir}/qt-3.3
cd src
$QTDIR/bin/qmake
make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m755 bin/k3dsurf $RPM_BUILD_ROOT%{_bindir}/k3dsurf

cd icon
for png in catenoid_mini_16x16.png catenoid_mini_32x32.png catenoid_mini_64x64.png ; do
        for size in 16x16 32x32 64x64 ; do
                install -D -m 644 $png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps/catenoid_mini.png
        done
done
cd ..

cd src
for png in pov.xpm snapshot.xpm gear.xpm gedit.xpm; do 
        for size in 16x16 32x32 64x64 ; do
                convert -geometry $size $png $(echo $png | cut -d. -f 1-1).png
                install -D -m 644 $(echo $png | cut -d. -f 1-1).png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps/$(echo $png | cut -d. -f 1-1).png
        done
done
cd ..

install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

# Create the system menu entry
%{__mkdir_p}  $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=k3dsurf
GenericName=3D and 4D surfaces generation
Comment=3D and 4D surfaces generation
Name[it]=k3dsurf
GenericName[it]=Grafici di funzioni 3D e 4D
Comment[it]=Grafici di funzioni 3D e 4D
Exec=k3dsurf
Icon=%{name}
Terminal=0
Type=Application
StartupNotify=true
Categories=Application;Education;Mathematics;
EOF

%files
%{_bindir}/k3dsurf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}.png
%doc copying readme

%changelog
* Mon Jun 20 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.2.4
- Rebuilt for Fedora
* Mon Jul 27 2009 Automatic Build System <autodist@mambasoft.it> 0.6.2.4-1mamba
- automatic update by autodist
* Sun Jun 15 2008 gil <puntogil@libero.it> 0.6.2-1mamba
- update to 0.6.2
* Mon Jul 25 2005 Massimo Pintore <massimo.pintore@qilinux.it> 0.5.1-1qilnx
- package created by autospec
