%global debug_package %{nil}

Name: carve
Summary: A Qt-based cross-platform SVG Editor
Version: 0.05
Release: 5.1
Group: Applications/Multimedia
License: GPLv3
URL: https://launchpad.net/carve
#bzr branch lp:carve
Source0: %{name}.zip
BuildRequires: qt4-devel

%description
Carve includes an SVG-aware text editor, dockable DOM browser and Properties
panels, a preview window and the beginnings of a graphical editing mode.

%prep
%setup -q -n %{name}

%build
qmake-qt4
make %{?_smp_mflags}

%install
install -Dm755 Carve %{buildroot}%{_bindir}/%{name}
install -Dm644 images/Carve-48.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Carve
Comment=A Qt-based cross-platform SVG Editor
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Applications;Graphics;
EOF

%files
%doc README.txt HISTORY.txt LICENSE NOTICE
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.05
- Rebuild for Fedora
