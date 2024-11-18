%undefine _debugsource_packages
%global _name diffimg

Name: diffimg-xbee
Summary: Simple image comparison tool
Version: 2.3.0
Release: 1
Group: Applications/Multimedia
License: GPLv2
URL: https://sourceforge.net/projects/diffimg/
Source0: https://codeload.github.com/lingo/diffimg-xbee/tar.gz/%{version}-lingo#/diffimg-xbee-%{version}-lingo.tar.gz
BuildRequires: dos2unix
BuildRequires: qt4-devel
BuildRequires: qwt5-qt4-devel
BuildRequires: opencv-devel
BuildRequires: cmake atlas

%description
DiffImg is a simple image comparison tool which take two images with the same
size as input. Some statitics are computed and the positions where pixel differ
are displayed as a color mask.

%prep
%setup -q -n %{_name}-xbee-%{version}-lingo
#dos2unix tounix.sh
#sh ./tounix.sh
#sed -i 's|lib -lperceptualdiff|lib|' build/apps.pro
#sed -i 's|-lopencv_core|-lopencv_core -lopencv_imgcodecs -lperceptualdiff|' build/apps.pro
sed -i 's|-Wall|-Wall -I/usr/include/opencv4|' build/CMakeLists.txt
sed -i 's|opencv_core|opencv_core opencv_imgcodecs|' build/CMakeLists.txt
#sed -i 's|opencv2/imgproc/imgproc.hpp|opencv4/opencv2/imgproc/imgproc.hpp|' 3rdparty/perceptualdiff/OpenCVImageLoader.cpp
sed -i -e 's|CV_BGR2RGB|cv::COLOR_BGR2RGB|' -e 's|CV_RGB2RGBA|cv::COLOR_RGB2RGBA|' -e 's|CV_RGBA2RGB|cv::COLOR_RGBA2RGB|' -e 's|CV_BGR2HSV|cv::COLOR_BGR2HSV|' \
  3rdparty/perceptualdiff/OpenCVImageLoader.cpp src/MiscFunctions.cpp
sed -i -e 's|CV_RGB2GRAY|cv::COLOR_RGB2GRAY|' -e 's|CV_LOAD_IMAGE_UNCHANGED|cv::IMREAD_UNCHANGED|' src/metrics/BaseMetric.cpp src/metrics/PerLuminanceMetric.cpp

%build
cd build
#qmake-qt4 -recursive INSTALL_PREFIX=$RPM_BUILD_ROOT/usr %{_name}.pro
%cmake . -DCMAKE_CXX_FLAGS="-I/usr/include/opencv4 -fPIE"
%cmake_build

%install
rm -rf $RPM_BUILD_ROOT
cd build
#make install
%cmake_install
# remove doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{_name}/*.txt
sed -i -e 's|%{buildroot}||' -e 's|/usr/share/pixmaps/%{_name}-xbee.png|%{_name}|' %{buildroot}%{_datadir}/applications/%{_name}.desktop
mv %{buildroot}%{_bindir}/%{_name} %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_mandir}/man1/%{_name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
%doc *.txt
%{_bindir}/*
%{_datadir}/%{_name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_mandir}/man*/*

%changelog
* Mon May 06 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.0
- Rebuilt for Fedora
