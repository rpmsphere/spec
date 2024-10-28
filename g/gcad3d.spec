%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages
%define oname gCAD3D
%ifarch x86_64 aarch64
%define ARCH 64
%else
%define ARCH 32
%endif

Name:           gcad3d
Version:        2.40
Release:        10.1
Summary:        A 3D CAD CAM application
Group:          Graphics/3D
License:        GPLv3
URL:            https://www.gcad3d.org
Source0:        https://www.gcad3d.org/download/%{oname}_%{version}-src.zip
Source1:        examples.gz
BuildRequires: gtk3-devel
BuildRequires: ctags
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel

%description
gCAD3D is a 3D CAD CAM application that features an integrated 3D OpenGL
viewer, a program interpreter for geometry and NC-commands in 3D, an
integrated NC-processor, and a programming interface for user programs.

It can
-Import and display data from Iges, Step, wire frame and solid objects
-Create and modify wire frame elements
-Create surfaces
-Create simple solid bodies
-Assemble user-created ancillary programs
-Export wire frame elements as DXF and Iges
-Export surfaces as Vrml-1, Vrml-2, obj, tw Iges

%prep
%setup -q -n mnt/serv1/Devel/%{name}
mkdir -p binLinux%{ARCH}/plugins
echo export gcad_dir_dev=$PWD/ >> src/options.sh
echo export gcad_dir_bin=$PWD/binLinux%{ARCH}/ >> src/options.sh

%build
cd src/APP
./do complete

%install
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=gCAD3D
Exec=%{name}
Icon=%{_datadir}/%{name}/icons/%{oname}.xpm
Comment=A 3D CAD CAM application
Comment[ru]=3D CAD CAM приложение
GenericName=3D CAD CAM design tool
GenericName[ru]=3D САПР
Type=Application
Categories=Graphics;
Terminal=false
EOF

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a icons %{SOURCE1} %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_libdir}
cp -a binLinux%{ARCH} %{buildroot}%{_libdir}/%{name}
rm %{buildroot}%{_libdir}/%{name}/xa_gui.so
ln -s %{name}/xa_gui_gtk3.so %{buildroot}%{_libdir}/xa_gui.so
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/%{name}/%{oname} %{buildroot}%{_bindir}/%{name}

%files
%doc README TODO LICENSE* doc/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}
%{_libdir}/xa_gui.so
%{_datadir}/%{name}

%changelog
* Mon Aug 27 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.40
- Rebuilt for Fedora
* Tue Jan 06 2015 alexl <alexl> 2.01-4.mga5
+ Revision: 808843
- added GenericName in desktop file
* Wed Oct 15 2014 umeabot <umeabot> 2.01-3.mga5.nonfree
+ Revision: 750676
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 2.01-2.mga5.nonfree
+ Revision: 679431
- Mageia 5 Mass Rebuild
* Tue Apr 22 2014 alexl <alexl> 2.01-1.mga5.nonfree
+ Revision: 617436
- imported package gcad3d
* Tue Mar 12 2013 symbianflo <symbianflo@mandrivausers.ro> 2.01-2
+ Revision: 52e6111
- LOG update to 2.01, add,fix gui-libs
