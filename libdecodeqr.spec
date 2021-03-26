Name:           libdecodeqr
Version:        0.9.4
Release:        8.1
Summary:        Decoding QR 2D barcodes
Group:          Applications/Engineering
License:        LGPL
URL:            https://github.com/josephholsten/libdecodeqr
Source0:        http://cloud.github.com/downloads/josephholsten/libdecodeqr/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++, opencv-devel, lapack-devel
BuildRequires:  atlas

%description
libdecodeqr is a C/C++ library for decoding QR code based on
JIS X 0510 and ISO/IEC18004.
This library is able to decode various image formats whether it's
taken from a file, webcam, scanner, or any other image formats
available.

%package        devel
Summary:        QR Code decoding library - Development files
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that decode qrencode.

%prep
%setup -q
sed -i -e 's/__BEGIN__/__CV_BEGIN__/' -e 's/__END__/__CV_END__/' libdecodeqr/imagereader.cpp
sed -i 's|cvWarpPerspectiveQMatrix|cvGetPerspectiveTransform|' libdecodeqr/imagereader.cpp
sed -i '1i #include <opencv2/imgproc.hpp>' examples/webcam/webcam.cpp

%build
export CXXFLAGS='-O2 -g -fpermissive -fPIC'
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README
%{_libdir}/libdecodeqr.so.*

%files devel
%doc examples/*
%{_includedir}/*.h
%{_libdir}/libdecodeqr.la
%{_libdir}/libdecodeqr.so

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.4
- Rebuild for Fedora
