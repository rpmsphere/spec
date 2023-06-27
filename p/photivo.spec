%undefine _debugsource_packages

Name: photivo
Version: 20200406
Release: 1
Summary: Photo processor
Group: Graphics
License: GPLv3+
URL: http://photivo.org
Source: %{name}-master.zip
BuildRequires: gcc-c++ libgomp qt4-devel libtool-ltdl-devel
BuildRequires: exiv2-devel lensfun-devel fftw3-devel liblqr-1-devel
BuildRequires: GraphicsMagick-c++-devel libjpeg-devel libtiff-devel libpng-devel bzip2-devel
BuildRequires: lcms-devel lcms2-devel xz-devel LibRaw-devel
BuildRequires: gimp-devel urw-fonts

%description
Photivo is a free and open source photo processor. It handles RAW files
as well as bitmap files in a non-destructive 16 bit processing pipe with
gimp workflow integration and batch mode.

Photivo tries to provide the best algorithms available; even if this
implies some redundancy. So, to my knowledge, it offers the most
flexible and powerful denoise, sharpen and local contrast (fake HDR)
algorithms in the open source world. (If not, let's port them )
Although, to get the desired results, there may be a quite steep
learning curve.

Photivo is just a developer, no manager and no Gimp. It is intended to
be used in a workflow together with digiKam/F-Spot/Shotwell and Gimp. It
needs a quite strong computer and is not aimed at beginners.

%package gimp
Summary: Photivo plugin for Gimp
Group: Graphics
Requires: %name = %version-%release

%description gimp
Photivo is a free and open source photo processor. It handles RAW files
as well as bitmap files in a non-destructive 16 bit processing pipe with
gimp workflow integration and batch mode.

This package provides Photivo plugin for Gimp.

%prep
%setup -q -n %{name}-master
sed -i 's|lensfun\.h|lensfun/lensfun.h|' Sources/ptConstants.h Sources/ptImage.h Sources/ptImage_Lensfun.cpp Sources/ptLensfun.h
sed -i 's|exiv2/xmp.hpp|exiv2/xmp_exiv2.hpp|' Sources/ptImageHelper.h
sed -i '31i #include<cstdlib>' Sources/ptDefines.h
sed -i 's|-march=i686||' CMakeLists.txt photivoProject/photivoProject.pro

%build
#qmake-qt5 PREFIX=%_prefix CONFIG-=debug CONFIG+=WithGimp
#make
%{cmake}
%{cmake_build}

%install
#make INSTALL_ROOT=%buildroot install
#install -pD -m755 ptGimp %buildroot%_libdir/gimp/2.0/plug-ins/ptGimp
%{cmake_install}
# install utilities
#install -pD -m755 ptClear %buildroot%_bindir/PtClear
#chmod 755 %buildroot%_bindir/ptClear
#ln -s ptClear %buildroot%_bindir/%name-clear
#install -pD -m755 ptCreateAdobeProfiles %buildroot%_bindir/ptCreateAdobeProfiles
#ln -s ptCreateAdobeProfiles  %buildroot%_bindir/%name-CreateAdobeProfiles
#install -pD -m755 ptCreateCurves %buildroot%_bindir/ptCreateCurves
#ln -s ptCreateCurves  %buildroot%_bindir/%name-CreateCurves
# fix permissions under %_datadir/%name
find %buildroot%_datadir/%name -type f -print0|xargs -r0 chmod 644 --
rm -rf %buildroot$HOME/.local
chmod +x %buildroot%_bindir/*

%files
%doc README
%_bindir/*
%_datadir/%name
%_datadir/applications/*
%_datadir/pixmaps/photivo-appicon.png

#files gimp
#_libdir/gimp/2.0/plug-ins/*

%changelog
* Sun May 14 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 20200406
- Rebuilt for Fedora
* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 0-alt10.f1a2a2889c33
- update to current snapshot
- built against libexiv2.so.13
* Tue Oct 29 2013 Yuri N. Sedunov <aris@altlinux.org> 0-alt9.99e7c7510b70
- update to current snapshot
* Fri Apr 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0-alt8.6256ff175312
- built current snapshot
* Thu Jan 24 2013 Yuri N. Sedunov <aris@altlinux.org> 0-alt7.50b234e492b
- rebuilt against libexiv2.so.12
* Wed Nov 21 2012 Yuri N. Sedunov <aris@altlinux.org> 0-alt6.50b234e492b
- built current snapshot
* Mon Feb 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0-alt5.0c5babd64674
- built current snapshot
* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0-alt4.571a226abd23
- built current snapshot
* Sat Jul 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0-alt3.bac78754fba4
- built current snapshot
* Sun May 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0-alt2.60f1eb32cced
- built current snapshot
* Fri Apr 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0-alt1.a02c90cbbe57.2
- built current snapshot
* Thu Mar 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0-alt1
- first build for Sisyphus
