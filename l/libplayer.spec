%undefine _debugsource_packages
%define major 2
%define libname libplayer
%define develname libplayer-devel

Name: libplayer
Version: 2.0.1
Release: 1
URL: http://libplayer.geexbox.org/
Source:	http://libplayer.geexbox.org/releases/%{name}-%{version}.tar.bz2
License: LGPLv2+
Summary: A multimedia A/V abstraction layer API
Group: System/Libraries
#BuildRequires: pkgconfig(libxine)
#BuildRequires: pkgconfig(libvlc)
Buildrequires: mplayer
BuildRequires: pkgconfig(gstreamer-0.10)
BuildRequires: pkgconfig(x11)
#BuildRequires: pkgconfig(gstreamer-plugins-base-0.10)

%description
libplayer is a multimedia A/V abstraction layer API. Its goal is to
interact with Enna Media Center.

libplayer provides a generic A/V API that relies on various multimedia
player for Linux systems. It currently supports MPlayer, xine VLC and
GStreamer only.

Its main goal is to provide an unique API that player frontends can use
to control any kind of multimedia player underneath. For example, it
provides a library to easily control MPlayer famous slave-mode.

%package test
Summary: A multimedia A/V abstraction layer API - test program
Group: System/Libraries

%description test
libplayer provides a generic A/V API that relies on various multimedia
player for Linux systems. It currently supports MPlayer, xine VLC and
GStreamer only.

This package contains test program for libplayer.

%package -n %{develname}
Summary: A multimedia A/V abstraction layer API
Group: System/Libraries
Provides: %{name}-devel = %{version}-%{release}
Requires: %libname = %version
Requires: pkgconfig(gstreamer-0.10)
#Requires: pkgconfig(gstreamer-plugins-base-0.10)

%description -n %{develname}
libplayer provides a generic A/V API that relies on various multimedia
player for Linux systems. It currently supports MPlayer, xine VLC and
GStreamer only.

This package contains the headers required for compiling software that uses
the libplayer library.

%prep
%setup -q

%build
export CFLAGS=-fPIC
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	--disable-static \
	--enable-shared \
	--disable-gstreamer \
	--enable-mplayer \
	--disable-vlc \
	--disable-xine
make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files test
%{_bindir}/*
%{_mandir}/man1/*

%files
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.1
- Rebuilt for Fedora
* Thu Sep 29 2011 trem <trem> 2.0.1-2.mga2
+ Revision: 150372
- add require gstreamer-0.10 and gstreamer-plugins-base-0.10 to package -devel
- add gstreamer-plugins-base-0.10 as BR
- use pkgconfig in BR instead of libfoo-devel
* Tue Sep 27 2011 trem <trem> 2.0.1-1.mga2
+ Revision: 149515
- imported package libplayer
* Mon Nov 08 2010 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 594974
- new version 2.0.1
* Sun Jul 25 2010 Funda Wang <fwang@mandriva.org> 2.0.0-0.20100724.1mdv2011.0
+ Revision: 558287
- 2.0.0 tarball
- 2.0 instead
* Sun Jul 25 2010 Funda Wang <fwang@mandriva.org> 1.0.0-1.20100724.1mdv2011.0
+ Revision: 558270
- New snapshot
* Sun Jan 03 2010 Funda Wang <fwang@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 485843
- import libplayer
