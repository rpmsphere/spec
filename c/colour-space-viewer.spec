%global debug_package %{nil}

Name: colour-space-viewer
Summary: Visualises different colour space cubes in 3 projections
Version: 0.rev7
Release: 6.1
Group: Development/Tools
License: GPLv3
URL: http://code.google.com/p/colour-space-viewer/
Source0: %{name}-%{version}.zip
BuildRequires: qt-devel
BuildRequires: boost-devel

%description
Colour space viewer is a tiny program which just visualises different
colour spaces. Some people have difficulties with understanding what
colourspaces are and what their components really mean. This program
shows three dissections of colourcubes and allows a user to move these
dissections.

%prep
%setup -q -n %{name}

%build
qmake-qt4
make %{?_smp_mflags}
cat > %{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Colour Space Viewer
Comment=Visualises different colour space cubes in 3 projections
Icon=colour-space-viewer
Exec=colour-space-viewer
Type=Application
Terminal=false
Categories=Utility;
EOF

%install
install -Dm755 colour_space_viewer %{buildroot}%{_bindir}/%{name}
install -Dm644 icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Jan 07 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.rev7
- Rebuild for Fedora
