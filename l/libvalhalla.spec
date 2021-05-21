Name: libvalhalla
Version: 2.0.0
Release: 5
URL: http://libvalhalla.geexbox.org/
Source:	http://libvalhalla.geexbox.org/releases/%{name}-%{version}.tar.bz2
Patch0: add-lrt-to-ldflags.patch
Patch1: fix-curl-includes.patch
Patch2: fix_ftbfs_libav_0.7.patch
License: LGPLv2+
Summary: A media scanner
Group: System Environment/Libraries
BuildRequires: sqlite-devel
BuildRequires: ffmpeg-devel
BuildRequires: curl-devel
BuildRequires: libxml2-devel
BuildRequires: libexif-devel
BuildRequires: libgcrypt-devel

%description
libvalhalla is a library written in C. It is a media scanner, that stores
various information in an SQLite database and relies on FFmpeg (libavformat
and libavutil) and libcurl. It features many Internet grabbers that allows
automatic download of covers, lyrics, informations on media files, tags
retrival in video and music files and so on.

%package test
Summary: A media scanner
Group: System/Tools

%description test
libvalhalla is a library written in C. It is a media scanner, that stores
various information in an SQLite database and relies on FFmpeg (libavformat
and libavutil) and libcurl. It features many Internet grabbers that allows
automatic download of covers, lyrics, informations on media files, tags
retrival in video and music files and so on.

%package devel
Summary: A media scanner
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
libvalhalla is a library written in C. It is a media scanner, that stores
various information in an SQLite database and relies on FFmpeg (libavformat
and libavutil) and libcurl. It features many Internet grabbers that allows
automatic download of covers, lyrics, informations on media files, tags
retrival in video and music files and so on.

This package contains the headers required for compiling software that uses
the libvalhalla library.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
##%patch2 -p1
sed -i 's|CODEC_TYPE_|AVMEDIA_TYPE_|' src/parser.c src/grabber_ffmpeg.c

%build
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	--disable-static \
	--enable-shared
make %{_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -fr %{buildroot}/%{_mandir}

%clean
rm -rf %{buildroot}

%files test
%{_bindir}/*

%files
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Jun 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> 2.0.0-5
- Add patches from Debian
- modified patch for libav

* Sun Apr 17 2011 Firefly <firefly@opendesktop.org.tw> 2.0.0-2
- Fix DSO error.

* Mon Dec 6 2010 Firefly <firefly@opendesktop.org.tw> 2.0.0-1
- release 2.0.0
- remove man page(s).
