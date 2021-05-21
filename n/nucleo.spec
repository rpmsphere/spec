Name:           nucleo
Version:        0.7.6
Release:        1
Summary:        Toolkit for exploring new uses of video
Group:          Development/Tools
License:        LGPLv2+
URL:            http://insitu.lri.fr/~roussel/projects/nucleo
Source0:        http://insitu.lri.fr/metisse/download/nucleo/%{name}-%{version}.tar.bz2
Patch:		nucleo-0.7.3-imgconvert-header.patch
BuildRequires:  libGL-devel libGLU-devel
BuildRequires:  libjpeg-devel libpng-devel libexif-devel freetype-devel

%description
Nucleo is a toolkit for exploring new uses of video and new human-computer
interaction techniques.

%package devel
Summary:        Files necessary for developing with %{name}
Group:          Development/Libraries
Requires:       pkgconfig
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains files required to build applications that make
use of nucleo.

%prep
%setup -q
%patch -p1
#sed -i '1i #include <cstdio>' nucleo/core/URI.cxx nucleo/core/TimeStamp.cxx nucleo/network/udp/UdpSocket.cxx nucleo/helpers/Phone.cxx
sed -i '1i #include <getopt.h>' nucleo/utils/AppUtils.cxx
sed -i '1i #include <unistd.h>' nucleo/network/udp/UdpSocket.cxx nucleo/network/NetworkUtils.cxx
sed -i '/gnutls_.*_set_priority/d' nucleo/network/xmpp/XmppConnection.cxx
sed -i '1i #include <string.h>' nucleo/image/encoding/PNGenc.cxx
sed -i 's|png\.h|libpng12/png.h|' nucleo/image/encoding/PNGenc.cxx
sed -i 's|linux/videodev.h|libv4l1-videodev.h|' nucleo/image/source/v4lImageSource.H
sed -i '1i #include <unistd.h>' nucleo/image/sink/novImageSink.cxx nucleo/image/sink/bufferedImageSink.cxx
sed -i '1i #include <unistd.h>' nucleo/helpers/Phone.cxx
sed -i -e 's|url_fclose|avio_close|' -e 's|PKT_FLAG_KEY|AV_PKT_FLAG_KEY|' nucleo/plugins/ffmpeg/ffmpegImageSink.cxx

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING.LESSER LICENSE NEWS README
%{_bindir}/nBundle
%{_bindir}/nTest
%{_bindir}/videoClient
%{_bindir}/videoServer
%{_libdir}/libNucleo.so.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so

%files devel
%{_bindir}/%{name}-config
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/libNucleo.so
%{_libdir}/pkgconfig/%{name}.pc
%exclude %{_libdir}/*.la
%exclude %{_libdir}/%{name}/*.la

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.6
- Rebuilt for Fedora
* Mon Jun 12 2006 Christopher Stone <chris.stone@gmail.com> 0.5-7
- Remove %%makeinstall macro
* Fri Jun 09 2006 Christopher Stone <chris.stone@gmail.com> 0.5-6
- devel subpackage now Requires pkgconfig
- Remove %%{name} from devel description
* Sat Jun 03 2006 Christohper Stone <chris.stone@gmail.com> 0.5-5
- Make spec file compatible with FC4
* Sat Jun 03 2006 Christopher Stone <chris.stone@gmail.com> 0.5-4
- Add libX11 and libXt to BuildRequires
* Thu Jun 01 2006 Christopher Stone <chris.stone@gmail.com> 0.5-3
- Remove INSTALL from %%doc
* Sun May 21 2006 Christopher Stone <chris.stone@gmail.com> 0.5-2
- Add optional BuildRequires
* Sat May 20 2006 Christopher Stone <chris.stone@gmail.com> 0.5-1
- Initial RPM release
