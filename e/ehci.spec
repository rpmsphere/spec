Name: ehci
Summary: Enhanced human computer interface through webcam image processing library
Version: 0.7
Release: 1
Group: Development/Libraries
URL: http://code.google.com/p/ehci/
Source0: http://ehci.googlecode.com/files/%{name}-%{version}-src.zip
License: LGPL
BuildRequires: cmake, opencv-devel
BuildRequires: atlas

%description
This application is a webcam image processing library on top of OpenCV intended
to generate events from user's head, hand and body movements. This library is
also intended to track objects so that augmented reality can be made. In order
to enhance human computer interaction, the application is going to use a single
webcam, without the needs to use FTIR or Diffused Illumination techniques.

Besides tracking positions, this library will also be able to provide higher
level events and gestures like get 3d user position, and open hand gestures.
Collision with virtual objects is also considered in augmented reality.

%package        devel
Summary:        Development files for Ehci
Group:          Development/Libraries/C and C++
Requires:      %{name}

%description    devel
Development files for Ehci.

%prep
%setup -q -n %{name}
sed -i 's|/include|/include /usr/include/opencv2|' src/CMakeLists.txt
sed -i -e 's|CvMatr32f|float*|' -e 's|CvVect32f|float*|' include/ehci.h src/ehci.cpp
sed -i '1i #include <opencv2/imgproc.hpp>\n#include <opencv2/calib3d/calib3d_c.h>' src/ehci.cpp

%build
cmake -DBUILD_SHARED_LIBS=ON -DOpenCV_DIR=%{_libdir}/cmake/OpenCV .
%make_build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_libdir}
install -m755 src/libEhci.so %{buildroot}%{_libdir}
install -Dm644 include/ehci.h %{buildroot}%{_includedir}/ehci.h

%files
%{_libdir}/lib*

%files devel
%{_includedir}/*

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7
- Rebuilt for Fedora
