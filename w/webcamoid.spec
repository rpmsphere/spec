%undefine _debugsource_packages

Name: webcamoid
Version: 8.8.0
Release: 1
Summary: The full webcam and multimedia suite
Group: Applications/Multimedia
License: GPLv3+
URL: https://github.com/hipersayanX/webcamoid
Source0: %{name}-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: ffmpeg-devel
BuildRequires: libv4l-devel
Requires: qt5-qtmultimedia
Requires: ffmpeg-libs
Requires: libv4l

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

%build
%ifarch aarch64
export CC=clang CXX=clang++
%endif
qmake-qt5 Webcamoid.pro \
    LIBDIR=%{_libdir} \
    LICENSEDIR=%{_defaultdocdir}/webcamoid
make

%install
rm -rf %{buildroot}
make INSTALL_ROOT=%{buildroot} install
#mkdir -p %{buildroot}%{_mandir}/man1
#mv %{buildroot}%{_mandir}/webcamoid.1.gz %{buildroot}%{_mandir}/man1/webcamoid.1.gz

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/webcamoid
%{_datadir}/applications/webcamoid.desktop
%{_datadir}/icons/hicolor/*/apps/webcamoid.*
%{_defaultdocdir}/webcamoid
%{_mandir}/man1/webcamoid.1*
%{_libdir}/avkys
%{_libdir}/libavkys.so*
%{_libdir}/qt5/qml/AkQml

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 8.8.0
- Rebuilt for Fedora
* Mon Feb 23 2015 Gonzalo Exequiel Pedone <hipersayan DOT x AT gmail DOT com> 6.2.0-1
- Final Release.
