%undefine _debugsource_packages

Name:           imagicom
Version:        1.3
Release:        18.1
Summary:        Beesoft Image Commander
License:        GPLv2+
Group:          File tools
URL:            https://www.beesoft.org/index.php?id=imagicom
Source:         https://www.beesoft.org/download/%{name}_%{version}_src.tar.gz
BuildRequires:  qt4-devel
BuildRequires:  ImageMagick6-c++-devel

%description
Image Commander is a simple application for bulk picture processing.
It's appearance is very similar to a standard two-panel file manager.
Users can perform a various set of operations on the chosen images.
Settings applied to every image can be saved for future use/reference.
The application allows a preview of a modified image on every stage of
processing. When the required modifications for all files are set the
user can execute a batch process by pressing F5 key.

%prep
%setup -q -n imagicom
sed -i 's|MaxRGB|65535|' Parsery.cpp QBtMagic.cpp

%build
qmake-qt4
sed -i 's|-I/usr/include/ImageMagick|-I/usr/include/ImageMagick-6|' Makefile
sed -i 's|-lMagick++ -lMagickWand -lMagickCore|-lMagick++-6.Q16 -lMagickCore-6.Q16 -lMagickWand-6.Q16|' Makefile
make CXXFLAGS+="-fPIC"

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

# menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Image Commander
Comment=Beesoft Commander for Images
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Graphics;Qt;
EOF

# icon
install -Dm644 img/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Feb 06 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
