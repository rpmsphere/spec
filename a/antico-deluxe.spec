%define srcname anticodeluxe

Name: antico-deluxe
Version: 0.1.96
Release: 7.4
Summary: A Qt4 Window/Desktop manager
Source: https://anticodeluxe.googlecode.com/files/%srcname-%version.tar.bz2
Patch0: %srcname-0.1.96-link.patch
Patch1: antico-deluxe-0.1.96-alt-DSO.patch
Patch2: antico-deluxe-0.1.96-alt-glibc-2.16.patch
URL: https://code.google.com/p/anticodeluxe/
Group: Graphical desktop/Other
License: GPLv2 Artistic
BuildRequires: gcc-c++ alsa-lib-devel libao-devel qt4-devel libvorbis-devel

%description
Antico Deluxe is a fork of famous Antico WM/DE (https://antico.wordpress.com/),
with some new features added and many new planned.

The goal is to create very simple and fast Window/Desktop manager with very
aesthetic and familiar look and feel. A very few parameters are autoconfigured
(and can be changed) in few config files, avoiding unnecessary complications,
following the K.I.S.S. philosophy. Any other configurations like themes, icons
etc. should be avoided or minimal. Keeping in very small size while having
relatively rich feature set makes AnticoDeluxe very suitable for netbooks and
low-end computers. The overall look and feel have to be very close to MacOSX
look and feel, which is ORIGINAL WORK FROM APPLE INC.

%package devel
Summary: Antico Deluxe header files
Group: Development/C++
Requires: lib%name = %version-%release

%description devel
%name-devel contains the header files needed to develop
programs which make use of Antico Deluxe.

%prep
%setup -q -n %srcname
%patch 0 -p1
%patch 1 -p2
%patch 2 -p2

find -type f -name \*.pro | xargs sed -i "s|/usr/lib|%_libdir|g"

%build
export PATH=$PATH:%_qt4dir/bin
qmake-qt4 "QMAKE_CFLAGS+=%optflags -Wno-format-security" "QMAKE_CXXFLAGS+=%optflags -Wno-format-security" %name.pro
%make_build

%install
%make_install INSTALL_ROOT=%buildroot

%files
%doc AUTHORS CHANGELOG ROADMAP test BUGS README myxephyr
%dir %_datadir/themes/antico
%dir %_datadir/themes/antico/default
%_bindir/*
%_datadir/themes/antico/default/*
%_libdir/libame.so.*

%files devel
%dir %_includedir/ame
%_libdir/libame.so
%_includedir/ame/*

%changelog
* Tue Aug 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.96 
- Rebuilt for Fedora
* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.96-alt1.2
- Fixed build with glibc 2.16
* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.96-alt1.1
- Fixed build
* Tue May 12 2009 Boris Savelev <boris@altlinux.org> 0.1.96-alt1
- initial build for Sisyphus
