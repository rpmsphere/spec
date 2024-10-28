Name:          qgifer
Version:       0.2.3rc2
Release:       1
Summary:       A video-based animated GIF creator
Group:         Applications/Multimedia
License:       GPLv3
#URL:           https://sourceforge.net/projects/qgifer/
URL:           https://github.com/Apkawa/QGifer
Source0:       %{name}-%{version}-source.tar.gz
BuildRequires: cmake, giflib-devel, qt-devel, kdelibs4-devel, opencv-devel, qca2
BuildRequires: atlas, udisks2

%description
QGifer is a tool for extracting part of a video to an animated GIF file.

%prep
%setup -q -n %{name}-%{version}-source
#sed -i 's|-lopencv_core |-lopencv_core -lopencv_videoio |' CMakeLists.txt
#sed -i -e 's|MakeMapObject|GifMakeMapObject|' -e 's|FreeMapObject|GifFreeMapObject|' src/palettewidget.h
#sed -i -e 's|FALSE|false|' -e 's|FreeMapObject|GifFreeMapObject|' -e '/PrintGifError/d' src/gifcreator.cpp
sed -i '168,175d' src/palettewidget.cpp #bug in giflib-5.1.9
sed -i -e '26i #include <opencv2/core/cvdef.h>\n#include <opencv2/videoio/legacy/constants_c.h>' src/frameplayer.h

%build
%cmake
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/pixmaps
sed -i 's|/usr/share/icons/||' %{buildroot}%{_datadir}/applications/qgifer.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/qgifer.desktop
%{_datadir}/doc/qgifer
%{_datadir}/pixmaps/qgifer.xpm
%exclude %{_datadir}/menu/qgifer
%{_datadir}/qgifer

%changelog
* Thu Aug 29 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3rc2
- Rebuilt for Fedora
* Mon Jun 10 2013 David Vásquez <davidjeremias82 AT gmail DOT com> 0.2.1
- Initial rpm
