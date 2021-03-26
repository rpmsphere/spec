%define CImg_version 139

Name:           wxcam
Version:        1.0.7
Release:        1
Summary:        Webcam application for linux
License:        GNU General Public License version 2 or later (GPLv2 or later)
Group:          Productivity/Graphics/Other
URL:            http://wxcam.sourceforge.net
Source0:        http://downloads.sourceforge.net/wxcam/wxcam-%{version}.tar.bz2
# Header Cimg.h taken from version 1.3.9 of the CImg-library
# This file is licensed under the "CeCILL free software license" 
# See http://cimg.sourceforge.net/ for more information 
Source1:        CImg-%{CImg_version}.h.bz2
Source2:        Licence_CeCILL_V2-en.txt
Source3:	%{name}-1.0.7.zh_CN.po
Source4:        %{name}-1.0.7.zh_TW.po
Source5:	%{name}.png
Source100:      %{name}.changes
Patch0:         wxcam-CImg.h.diff
Patch1:         %{name}-%{version}-fix_no_return_in_nonvoid_function.patch
Buildrequires:  gcc-c++ pkgconfig perl-XML-Parser
BuildRequires:  gtk2-devel libglade2-devel libtiff-devel libjpeg-devel 
Buildrequires:  xvidcore-devel mjpegtools-devel intltool wxGTK-devel

%description
wxCam is a webcam application for linux. It supports video recording (in an
avi uncompressed and Xvid format), snapshot taking, and some special commands
for philips webcams, so you can also use the program for astronomy purposes.
It supports video4linux 1 drivers, so it should work on a very large number
of devices. 

%prep
%setup -q

bzcat %{SOURCE1} > src/CImg.h
cp %{SOURCE2} License_CImg

%patch0 -p0
%patch1 -p0

# set some reasonable permissions for documentation files
chmod 0644 COPYING

echo -e 'zh_CN\nzh_TW' >> po/LINGUAS
cp %{SOURCE3} po/zh_CN.po
cp %{SOURCE4} po/zh_TW.po
cp %{SOURCE5} %{name}.png

sed -i 's|linux/videodev.h|libv4l1-videodev.h|' src/v4l.h src/device.h

%build
%configure --prefix=/usr --docdir=%{_defaultdocdir}

%__make %{?_smp_mflags} V=1

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -r "%{buildroot}/usr/doc"

%find_lang %{name}

%files -f %{name}.lang
%doc License_CImg README COPYING AUTHORS ChangeLog INSTALL NEWS
%{_bindir}/wxcam
%{_datadir}/applications/wxcam.desktop
%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %{buildroot}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.7
- Rebuild for Fedora
- Rebuild for OSSII
* Mon Dec 27 2010 packman@links2linux.de -1.0.7
- updated to 1.0.7
  better support for MJPEG webcams
  some bugfixes in gain and shutter speed (for philips webcams)
* Sun Aug  8 2010 packman@links2linux.de - 1.0.6
- updated to 1.0.6
- CImg.h updated to 1.3.9
- reversed BuildRequires for openSUSE 11.3
  wxWidgets-devel is now packaged for openSUSE 11.3 by Packman
- added intltool to BuildRequires
- patches updated
- minor improvements on spec file
* Wed Jul 21 2010 packman@links2linux.de - 1.0.4
- fixed BuildRequires for openSUSE 11.3
* Wed Jan 20 2010 Axel Koellhofer <axel@links2linux.de> - 1.0.4-0.pm.0
- updated to version 1.0.4
- adapted spec from H. Graeber for recent openSUSE versions
- spec cleanup
- removed obsolete BuildRequire for revel
* Sun Sep 30 2007 Herbert Graeber <herbert@links2linux.de> - 0.9.4
- update to version 0.9.4
* Sun Sep  9 2007 Herbert Graeber <herbert@links2linux.de> - 0.9.1
- Add patch for wxWidgets from packman
- Initial version 0.9.1
