%global __os_install_post %{nil}
%undefine _debugsource_packages

Name: webcamoid
Version: 9.1.1
Release: 1
Summary: The full webcam and multimedia suite
Group: Applications/Multimedia
License: GPLv3+
URL: https://github.com/hipersayanX/webcamoid
Source0: %{name}-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: qt5-qtquickcontrols2-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: ffmpeg-devel
BuildRequires: libv4l-devel

%description
Webcamoid is a full featured webcam capture application.
Features:
    * Take pictures and record videos with the webcam.
    * Manages multiple webcams.
    * Written in C++/Qt.
    * Custom controls for each webcam.
    * Add funny effects to the webcam.
    * +60 effects available.
    * Effects with live previews.
    * Translated to many languages.
    * Use custom network and local files as capture devices.
    * Capture from desktop.

%prep
%setup -q
sed -i -e 's|lupdate|lupdate-qt5|' -e 's|lrelease|lrelease-qt5|' StandAlone/Translations/CMakeLists.txt

%build
#ifarch aarch64
#export CC=clang CXX=clang++
#endif
#qmake-qt5 LIBDIR=%{_libdir} LICENSEDIR=%{_defaultdocdir}/webcamoid
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr .
make

%install
rm -rf %{buildroot}
#make INSTALL_ROOT=%{buildroot} install
%make_install
#mkdir -p %{buildroot}%{_mandir}/man1
#mv %{buildroot}%{_mandir}/webcamoid.1.gz %{buildroot}%{_mandir}/man1/webcamoid.1.gz

%files
%{_bindir}/webcamoid
%{_datadir}/applications/webcamoid.desktop
%{_datadir}/icons/hicolor/*/apps/webcamoid.*
#{_defaultdocdir}/webcamoid
%{_mandir}/man1/webcamoid.1*
%{_libdir}/avkys
%{_libdir}/libavkys.so*
#{_libdir}/qt5/qml/AkQml
%{_datadir}/licenses/webcamoid/COPYING
%{_datadir}/metainfo/io.github.webcamoid.Webcamoid.metainfo.xml
%{_datadir}/webcamoid

%changelog
* Sun Nov 17 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 9.1.1
- Rebuilt for Fedora
* Mon Feb 23 2015 Gonzalo Exequiel Pedone <hipersayan DOT x AT gmail DOT com> 6.2.0-1
- Final Release.
