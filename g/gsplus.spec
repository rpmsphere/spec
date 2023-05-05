Name:           gsplus
Version:        0.14
Release:        3.20201110
Summary:        An Apple IIgs Emulator
License:        GPLv2
URL:            http://apple2.gs/plus/
Source0:        %{name}-git.zip
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  perl
BuildRequires:  re2c
BuildRequires:  readline-devel
BuildRequires:  SDL2_image-devel       

%description
A cross-platform Apple IIgs emulator

%prep
%setup -qc

%build
# We say no shared LIBS because they are only local to gsplus and not useful otherwise
%cmake gsplus-master -DCMAKE_BUILD_TYPE:STRING=Release -DWITH_ATBRIDGE:BOOL=OFF -DWITH_HOST_FST:BOOL=ON -DWITH_RAWNET:BOOL=ON -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

# Create a desktop file
cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=GSPlus
Comment=%{summary}
Exec=gsplus -resizeable
Icon=gsplus
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;Emulator;
EOF

%install
# No installer so must do it manually
chrpath -d %{__cmake_builddir}/bin/GSplus
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{__cmake_builddir}/bin/GSplus %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sv GSplus %{name}
popd

pushd gsplus-master/assets
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{32x32,64x64,128x128,256x256,512x512}/apps
install -pm 0644 gsp_icon_32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -pm 0644 gsp_icon_64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -pm 0644 gsp_icon_128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -pm 0644 gsp_icon_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -pm 0644 gsp_icon_512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
popd

# Install the .desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
                     %{name}.desktop
                     
%files
%license gsplus-master/COPYRIGHT.txt gsplus-master/LICENSE.txt
%doc gsplus-master/doc/{README.txt,gsplusmanual.pdf}
%{_bindir}/GSplus
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/{32x32,64x64,128x128,256x256,512x512}/apps/%{name}.png

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.14
- Rebuilt for Fedora
* Wed Dec 30 2020 RPMBuilder - 0.14-3.20201110
- SPEC modernisation and cleanups
- Allow building of debug packages
* Thu Dec 24 2020 RPMBuilder - 0.14-2.20201110
- Added resizeable to default icon launch option
* Tue Nov 10 2020 RPMBuilder - 0.14-1.20201110
- Initial RPM release
