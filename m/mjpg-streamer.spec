%global debug_package %{nil}

Summary: Stream webcam video to HTTP
Name: mjpg-streamer
Version: 0.r182
Release: 22.1
License: GPLv2
Group: Video
Source0: %{name}-code-182.zip
Source1: %{name}.desktop
Source2: %{name}.png
Source3: %{name}-udp-client.desktop
Source4: mjpg_streamer.1
Source5: mjpg_streamer_udp_client.1
Source6: mstreamer.1
Source7: mjpg_streamer.sysconfig
Source8: videodev.h
Patch0: %{name}.Makefile.patch
#Patch1: {name}.encoder.patch
Patch2: %{name}.start.sh.patch
#Patch3: {name}.httpd.c.patch
#Patch4: {name}.autofocus.patch
Patch5: %{name}.uvc.patch
Patch6: %{name}.control.patch
Patch7: %{name}.outputhttp.patch
#Patch8: {name}.utils.h.patch
#Patch9: {name}.outputviewer.patch
URL: http://mjpg-streamer.sourceforge.net/
BuildRequires: libv4l-devel libjpeg-devel SDL-devel unzip
BuildRequires: qt4-devel
BuildRequires: ghostscript-core ImageMagick
BuildRequires: desktop-file-utils
Requires: SDL procps
#Source44: import.info

%description
MJPG-streamer takes JPGs from Linux-UVC compatible webcams, from local files
or other input plugins and streams them as M-JPEG via HTTP to webbrowsers,
VLC and other software. It is the successor of uvc-streamer, a Linux-UVC
streaming application with Pan/Tilt.

Control the application with mstreamer <start|stop|status> from the command
line or use the desktop menu in KDE.

%prep
%setup -q -n %{name}-code-182
cd %{name}
#patch0 -p0
#patch1 -p0
%patch2 -p0
#patch3 -p0
#patch4 -p0
#patch5 -p0
%patch6 -p0
%patch7 -p0
#patch8 -p0
#patch9 -p0
cp -a %{S:4} .
cp -a %{S:5} .
#cp -a %{S:6} .
cp -a %{S:8} .
# Fix wrong address in www/LICENCE.txt (not needed)
rm www/LICENSE.txt

sed -i 's|videodev\.h|videodev2.h|' mjpg_streamer.c plugins/*/*.h plugins/*/*.c ../uvc-streamer/*
sed -i '/linux\/stat.h/d' utils.c
sed -i 's|-Wall|-Wall -Wl,--allow-multiple-definition|' Makefile plugins/*/Makefile

%build
cd %{name}
%{__make} %{?jobs:-j%jobs} %{?_smp_mflags} USE_LIBV4L2=true RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
cd ../udp_client
qmake-qt4 -o Makefile udp_client.pro
make
cd ../uvc-streamer
make

%install
cd %{name}
install -d %{buildroot}%{_bindir}
install -m 755 mjpg_streamer %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}
install -m 755 *.so %{buildroot}%{_libdir}
install -d %{buildroot}%{_datadir}/%{name}/www
install -m 644 www/* %{buildroot}%{_datadir}/%{name}/www
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1} %{SOURCE3}
install -d %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_mandir}/man1
install -m 644 *.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}/etc/sysconfig
install -m 644 %{SOURCE7} %{buildroot}/etc/sysconfig/mjpg-streamer
cd ../udp_client
install -m 755 udp_client %{buildroot}%{_bindir}/mjpg_streamer_udp_client
cd ../uvc-streamer
install -m 755 uvc_stream %{buildroot}%{_bindir}/uvc_stream
sed -i -e '/^OnlyShowIn/d' `find %{buildroot}%{_datadir}/applications -name '*.desktop'`



%clean
rm -rf %{buildroot}

%files
%doc %{name}/README %{name}/CHANGELOG %{name}/LICENSE %{name}/start.sh
%doc %{_mandir}/man1/mjpg_streamer.1.gz
%doc %{_mandir}/man1/mjpg_streamer_udp_client.1.gz
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/www
%{_bindir}/mjpg_streamer
%{_bindir}/mjpg_streamer_udp_client
%{_bindir}/uvc_stream
%{_libdir}/*.so
%{_datadir}/%{name}/www/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-udp-client.desktop
%{_datadir}/pixmaps/%name.png
# The format has changed; otherwise use config(noreplace)
%config /etc/sysconfig/mjpg-streamer

%changelog
* Mon Mar 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.r182
- Rebuild for Fedora
* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> r137-alt1_102.2
- converted from openSUSE Build Service (Projects > home:vodoo)
