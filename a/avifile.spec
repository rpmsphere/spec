Summary: Library used to play AVI streams
Name: avifile
Version: 0.7.48
Release: 1
License: GPL
Group: Applications/Multimedia
URL: https://avifile.sourceforge.net/
Source: https://dl.sf.net/avifile/avifile-0.7-%{version}.tar.bz2
Patch1: avifile-config.patch
Patch2: ftbfs-freebsd.patch
Patch3: ffmpeg.patch
Patch4: autotools.patch
Patch5: gcc45.patch
Patch6: fix-libav07-compat.patch
Patch7: fix-build-with-libav07.patch
Patch9: no-lame.patch
Patch10: ftbfs-gcc4.7.patch
Patch11: avifile-0.7.45-v4lxif.patch
Patch12: avifile-0.7.48-ac_lang.patch
BuildRequires: gcc-c++, autoconf, automake, libtool desktop-file-utils
BuildRequires: compat-ffmpeg-devel
BuildRequires: libstdc++-devel
BuildRequires: SDL-devel >= 1.1.3, esound-devel
BuildRequires: libvorbis-devel, libpng-devel libjpeg-turbo-devel
BuildRequires: libmad-devel, a52dec-devel, faad2-devel xvidcore-devel
BuildRequires: zlib-devel qt3-devel libXi-devel
BuildRequires: libv4l-devel
Obsoletes: avifile-utils <= 0.7.37
Provides:  avifile-utils

%description
Avifile is a library that allows you to read and write compressed AVI
files in most common video & audio formats (IndeoX Video, DivX, etc.)
under x86 Linux. Compression and decompression are performed with Win32
DLLs. It includes a simple AVI player and a Video4Linux capture program

To use this program, you will need to get the Win32 binaries from
%{url} and put uncompress them under /usr/lib/win32.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{name}-0.7-%{version}
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=AVI Player
Comment=Play your AVI files
Icon=avifile
Exec=aviplay
Terminal=false
MimeType=video/x-msvideo
Type=Application
Categories=Application;AudioVideo;
EOF

sed -i 's/__GNUC__ == 4/__GNUC__ >= 5 || __GNUC__ == 4/' lib/common/avm_output.cpp

%build
if [ -e %{_sysconfdir}/profile.d/qt.sh ] ; then
    source "%{_sysconfdir}/profile.d/qt.sh"
fi

find . -type f -exec grep 'linux/videodev.h' {} \; -exec perl -p -i -e "s|linux/videodev.h|libv4l1-videodev.h|g" {} \; -print

./autogen.sh

find . -type f -exec grep -- -lavcodec {} \; -exec perl -p -i -e "s|-lavcodec|-L%{_libdir}/compat-ffmpeg -lavcodec|g" {} \; -print

./configure --prefix=%{_prefix} --libdir=%{_libdir} \
	--program-prefix="%{?_program_prefix}" \
	--enable-static \
	--enable-quiet \
	--enable-release \
	--enable-win32 \
	--enable-x86opt \
	--disable-mmx \
	--disable-sdltest --with-sdl --without-lame

find . -name Makefile -exec %{__perl} -p -i -e "s|SDL_LIBS = 4 |SDL_LIBS = |g" {} \;

make clean

perl -p -i -e "s|CPPFLAGS =|CPPFLAGS = -I/usr/include/compat-ffmpeg|g" lib/Makefile
perl -p -i -e "s|FFMPEG_CFLAGS =|FFMPEG_CFLAGS = -I/usr/include/compat-ffmpeg|g" plugins/libffmpeg/Makefile
perl -p -i -e "s|-Wall|-Wall -Wno-narrowing|g" plugins/libmpeg_audiodec/Makefile

%ifarch %{arm}
find . -name Makefile\* -exec grep -- "-g -O2" {} \; -exec perl -p -i -e "s|-g -O2|%{optflags}|g" {} \; -print
%endif

make %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
make DESTDIR=%{buildroot} install

%{__install} -m0644 -D bin/test.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%{__install} -m0755 -d %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor "" \
	--dir %{buildroot}%{_datadir}/applications \
	avifile.desktop

%{__rm} -f doc/Makefile*

# clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}{,/avifile0.7,/avifile0.7/vidix}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%doc ChangeLog COPYING README doc/CREDITS doc/EXCEPTIONS doc/KNOWN_BUGS doc/README-DEVEL doc/TODO doc/VIDEO-PERFORMANCE doc/WARNINGS
%dir %{_libdir}/avifile*/
%{_bindir}/avibench
%{_bindir}/avicap
%{_bindir}/avicat
%{_bindir}/avimake
%{_bindir}/aviplay
%{_bindir}/avirec
%{_bindir}/avirecompress
%{_bindir}/avitype
%attr(4755, root, root) %{_bindir}/kv4lsetup
%{_libdir}/*.so.*
%{_libdir}/avifile*/*.so
%{_datadir}/avifile*/
%{_datadir}/pixmaps/*
%{_datadir}/applications/avifile.desktop
%{_mandir}/man?/*

%files devel
%{_bindir}/avifile-config
%{_includedir}/avifile
%{_includedir}/avifile-0.7
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/avifile*/*.a
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*
%exclude %{_libdir}/avifile*/*.la

%changelog
* Thu Jan 29 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.48
- Rebuild

* Sat Sep 14 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.48-1
- add optflags for building on arm

* Thu Jan 17 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.48-1
- use compat-ffmpeg-devel to build on > fc17

* Mon Jun  4 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.48-1
- build for fc17, updated to 0.7.48, borrowed patches from the Debian 
  9.1 and 12 tarballs, added patch for AC_LANG_*
- many fixes to the spec file, remove options for versions older than 12

* Thu May 31 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- add patch from debian for building with gcc-4.7 (patch7)
  https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=667107
  https://packages.ubuntu.com/quantal/libavifile-0.7c2

* Tue May 31 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- in >= fc15 the kernel no longer has the videodev.h include file, 
  add libv4l-devel dependency and fix include lines in all files
- add patch to add undefined define (missing in new include file)
  this is just a mindless hack...
- add patch for v4l2 includes

* Tue Nov  9 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- changed libjpeg-turbo-devel for fc14

* Tue Nov 24 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added xorg-x11-proto-devel and libXi build requirements
- fixed problems with const char * pointers and other small
  errors

* Tue Nov 25 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- updated for fc10 build
- ommit vidix shared libraries under x86_64

* Thu Jun 19 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- updated qt3-devel build req for fc9

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- updated desktop categories

* Tue Jun  5 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.45-3
- fix Makefile.am and include/Makefile.am for fc7 (patch3)

* Tue Dec 26 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.45-2
- added template gcc41 patch from here (patch2):
  https://bugs.donarmstrong.com/cgi-bin/bugreport.cgi?bug=395386
- readded patch1 for extra qualification in mp3encode.cpp
- a sed expression in configure gets confused when trying to deal
  with /usr/lib64 (the build system runs in a 64 bit machine) and 
  as a result sdl does not get recognized, fix by replacing it by
  hand (see perl hack above)

* Tue Dec 12 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.45-2
- rebuild on fc6 (fails)

* Wed Apr  5 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.45-1
- updated to 0.7.45
- added patch for fc5/gcc4.1 (patch1)

* Tue Jul  5 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added fc4/gcc4 patch

* Thu Apr 14 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.43-1
- man pages are just man pages, not doc
- add obsoletes for old avifile-utils

* Sun Apr 10 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- add missing buildrequires, do not build a package with lame or xvid
- disable mmx to be able to build
- do a maintainer-clean to fix ffmpeg subdir makefile:
  https://prak.org/pipermail/avifile/2003-July/006991.html
- enable exclusion of .la files
- needs ffmpeg-devel package in buildrequires
- no .la files generated in /usr/lib/*.la

* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 0.7.38-0
- Updated to release 0.7.38.

* Sat Aug 23 2003 Dag Wieers <dag@wieers.com> - 0.7.34-1
- Rebuild against xvidcore-0.9.2.

* Sat Apr 05 2003 Dag Wieers <dag@wieers.com> - 0.7.34-0
- Updated to release 0.7.34-20030319.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.7.26-1
- Build against new lame-3.93.1-1 package.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 0.7.26-0
- Initial package. (using DAR)
