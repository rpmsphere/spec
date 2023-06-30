%undefine _debugsource_packages

Name:           eko
Version:        7.0.1
Release:        1
Summary:        Simple sound editor
License:        GPL-3.0
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://semiletov.org/eko/#about
Source0:        semiletov.org/eko/dloads/%{name}-%{version}.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  portaudio-devel
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)

%description
EKO understands all popular sound formats and useful in simple editing(cut/copy/paste)
with a minimum FX processing. External fx currently are not supported.

Features:
  * real-time FX rack
  * generators of sine, nouse
  * channel converter
  * RMS and level analysis
  * DC offset corrector
  * reverese
  * handy editing
  * color palettes
  * hotkeys customizations

%prep
%setup -q

# Fix files is compiled without RPM_OPT_FLAG
find . -type f -name \*.pro | while read FILE; do
echo "QMAKE_CXXFLAGS += %optflags" >> "$FILE"; done

%build
qmake-qt5 %{name}.pro PREFIX=%{buildroot}/usr
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Eko
GenericName=Eko Sound Editor
GenericName[ru]=Звуковой редактор Eko
Comment=Edit sound files
Comment[ru]=Редактирование звуковых файлов
Exec=eko
Icon=eko
Terminal=false
Type=Application
Categories=Application;AudioVideo;Audio;
EOF

%files
%doc AUTHORS ChangeLog COPYING NEWS* TODO
%{_bindir}/eko
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/eko.png

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 7.0.1  
- Rebuilt for Fedora
* Tue Jul 21 2015 avvissu@yandex.ru
- Update o 2.1.0:
  * misc fixes
- Update patches:
  * eko-2.0.0_include.patch -> eko-2.1.0_include.patch
* Wed May  6 2015 avvissu@yandex.ru
- Initial release
