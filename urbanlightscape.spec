Name:           urbanlightscape
Version:        1.3.0
Release:        3.1
License:        GPL-2.0+
Summary:        Improve Lighting, Correct Exposure, Add Synthetic Light to Photos
URL:            http://www.indii.org/software/urbanlightscape
Group:          Productivity/Graphics/Bitmap Editors
Source0:        http://www.indii.org/files/%{name}/releases/%{name}-%{version}.tar.gz
Source1:        http://www.indii.org/images/%{name}_128.png
BuildRequires:  ImageMagick
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  wxGTK-devel

%description
Urban Lightscape is a photo filter for exposure correction,
localized brightness adjustments, dodging and burning, and the
introduction of synthetic lighting to a photo. A simple
"double-click-and-drag" paradigm is used to place control points on
a photo, and clever edge detection localises and interpolates
lightness adjustments around and between these points. Results are
rapid, with additional controls for more subtle refinements.

%prep
%setup -q

%build
%configure --disable-assert
make %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall
# Create desktop file.
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=Urban Lightscape
GenericName=Correct Exposure, Lighting, Brightness
GenericName[ru]=Коррекция экспозиции, яркости, света
Type=Application
Exec=urbanlightscape %f
Icon=urbanlightscape
Categories=Graphics;Photography;
Comment=Improve lighting, Correct Exposure, Add Synthetic Light to Photos
Comment[ru]=Коррекция экспозиции, яркости, света
StartupNotify=true
Terminal=false
MimeType=image/gif;image/jpeg;image/png;image/tiff;image/x-bmp;image/x-portable-pixmap;image/x-pcx;image/x-targa;image/x-xpm;
EOF
install -Dm 0644 %{name}.desktop \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Install icons of various sizes.
install -Dm 0644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
for size in 96x96 64x64 48x48 32x32 22x22 16x16 ; do
    install -dm 0755 \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}/apps
    convert -resize ${size} %{SOURCE1} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Mon Oct 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0
- Rebuild for Fedora
* Sat Apr  7 2012 lazy.kent@opensuse.org
- Update to 1.1.0.
- Performance improvements when interacting with control points.
* Sun Mar 18 2012 lazy.kent@opensuse.org
- Update to 1.0.4.
- Fixed zoom-fit function.
- Fixed GCC 4.6 compile errors.
* Tue Mar 13 2012 lazy.kent@opensuse.org
- Initial package created - 1.0.3.
