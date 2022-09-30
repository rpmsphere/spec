%undefine _debugsource_packages
%define	oname Qtcam

Summary:	Open Source Linux Webcamera Software
Name:		qtcam
# For version: see src/qml/qtcam/about/release.ini
Version:	25.0.2
Release:	1
License:	GPLv3+
Group:		Video
URL:		http://www.e-consystems.com/opensource-linux-webcam-software-application.asp
# While being actively develoed, there are no official releases:
# make the tarball directly from https://github.com/alexzk1/qtcam
Source0:	%{name}-master.zip
Source1:	%{oname}.desktop
BuildRequires:  gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick
BuildRequires:	qt5-qtbase-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libturbojpeg)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	qt5-qtdeclarative-devel
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:  libevdev-devel
BuildRequires:  qt5-qtmultimedia-devel

%description
Qtcam is a free, Open Source Linux Webcamera Software with more than 10 image
control settings, extension settings and Color space switching.

%prep
%setup -q -n %{name}-master
#sed -i 's|CODEC_FLAG2_FAST|AV_CODEC_FLAG2_FAST|' src/h264decoder.cpp
#sed -i 's|CODEC_FLAG_GLOBAL_HEADER|AV_CODEC_FLAG_GLOBAL_HEADER|' src/videoencoder.cpp

%build
cd src
%qmake_qt5
#sed -i 's|-isystem /usr/include |-I/usr/include/ffmpeg |' Makefile
sed -i 's|-I/usr/include |-I/usr/include -I/usr/include/ffmpeg |' Makefile
%make_build SUBLIBS="-lpulse -levdev -lturbojpeg -lusb-1.0 -lavcodec -lasound -lavutil -lavformat -lv4l2 -lv4lconvert -ludev -lswscale"

%install
#make_install -C src
install -Dm755 src/%{oname} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/qml
cp -a src/qml/%{name} %{buildroot}%{_datadir}/qml

# Add menu entry
desktop-file-install %{SOURCE1} \
	--dir=%{buildroot}%{_datadir}/applications

# Prepare and install icons
for size in 256x256 128x128 96x96 64x64 48x48 32x32 22x22 16x16 ; do
	install -dm 0755 %{buildroot}%{_datadir}/icons/hicolor/$size/apps
	convert -strip -resize $size src/qml/qtcam/icon/images/icon.jpg \
		%{buildroot}%{_datadir}/icons/hicolor/$size/apps/%{name}.png
done

%files
%doc LICENSE README ChangeLog
%{_bindir}/%{name}
%{_datadir}/qml/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sun Sep 18 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 25.0.2
- Rebuilt for Fedora
* Mon Oct 16 2017 Giovanni Mariani <mc2374@mclink.it> 16.0.1-1
- (86d3ea1) Updated to release 16.0.1, added P0 to fix installation path, updated S1 and Breqs, cleaned specfile
