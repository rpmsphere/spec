%undefine _debugsource_packages

Name:           cobras
Version:        0.18
Release:        11.1
Summary:        Beesoft IDE
License:        GPLv2+
Group:          File tools
URL:            https://www.beesoft.org/index.php?id=bsc
Source:         https://www.beesoft.org/download/%{name}_%{version}_src.tar.gz
BuildRequires:  qt4-devel
BuildRequires:  ghostscript-core ImageMagick

%description
Cobras is an IDE for linux programmers.

%prep
%setup -q -n cobras

%build
qmake-qt4 QMAKE_CXXFLAGS+="-fPIC"
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
install -m644 *.ts %{buildroot}%{_datadir}/%{name}

# menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Cobras
Comment=Beesoft IDE
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;Qt;
EOF

# icon
install -Dm644 img/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Feb 06 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.18
- Rebuilt for Fedora
