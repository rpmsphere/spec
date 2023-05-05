Name:           hotshots
Version:        2.2.0
Release:        6.1
License:        GPLv2+
Summary:        Screenshot and Annotation Tool
URL:            https://sourceforge.net/projects/hotshots/
Group:          Productivity/Graphics/Other
Source0:        http://sourceforge.net/projects/hotshots/files/%{version}/HotShots-%{version}-src.zip
BuildRequires:  ghostscript-core ImageMagick
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqxt-devel
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtNetwork)
BuildRequires:  pkgconfig(QtXml)
BuildRequires:  libqxt-devel

%description
HotShots is an application for capturing screens and saving them in
a variety of image formats as well as adding annotations and graphical
data (arrows, lines, texts, ...).

%prep
%setup -qn HotShots-%{version}-src
sed -i 's/\r$//' *.txt
sed -i 's|(abs(|(std::abs(|' src/editor/items/BaseItem.cpp

%build
cd build
qmake-qt4 \
    QMAKE_CFLAGS+="%{optflags}" \
    QMAKE_CXXFLAGS+="%{optflags}" \
    QMAKE_STRIP="true" \
    INSTALL_PREFIX=%{_prefix} \
    MYAPP_INSTALL_TRANS=%{_datadir}/%{name}/lang
make %{?_smp_mflags}

%install
pushd build
make INSTALL_ROOT=%{buildroot} install
popd
# Remove docs as we use hotshot-1.1.0-docs_path.patch
rm -rf %{buildroot}%{_datadir}/%{name}/*.txt
# Remove pixmap. Install icons of various sizes into icons/hicolor.
rm -f %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm 0644 res/%{name}.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
for size in 96x96 64x64 48x48 32x32 22x22 16x16 ; do
    install -dm 0755 \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
    convert -strip -resize ${size} res/%{name}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done
sed -i 's|/.*/||' %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_mandir}/man?/*
%{_datadir}/%{name}

%changelog
* Sun Mar 26 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.0
- Rebuilt for Fedora
* Tue May 21 2013 lazy.kent@opensuse.org
- Update to 1.1.1.
  * Features:
    + Ability to force a background color for clipboard/web copy.
    + Ability to launch Internet browser when uploading is done.
    + Add Polish translation.
    + Some cosmetic changes.
    + Add an image uploading service (tof.canardpc.com/).
    + Use external Qxt library on Linux.
  * Bugs:
    + Correct untimely exit when HotShots is minimized.
    + Change default style on Linux platform.
    + Correct a problem with transparency for clipboard/web copy.
    + Correct invalid bounding rect when item are outside
    background image.
- BuildRequires: libqxt-devel.
- Install icons of various sizes into icons/hicolor (BuildRequires:
  ImageMagick, hicolor-icon-theme). Add %%icon_theme_cache_post/un
  macros.
* Sun May 12 2013 lazy.kent@opensuse.org
- Initial package created - 1.1.0.
- Add hotshots-1.1.0-desktop.patch: fix desktop file.
- Add hotshots-1.1.0-docs_path.patch: change path to docs.
- Add hotshots-1.1.0-lang_path.patch: change path to translations.
