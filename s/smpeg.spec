%global __os_install_post %{nil}
%define svn 390
#define svn 412

Summary: SDL MPEG Library
Name: smpeg
Version: 0.4.5
# svn co svn://svn.icculus.org/smpeg/trunk smpeg
Release: 27.1
Source: %{name}-%{svn}.tar.gz
License: LGPL
Group: System Environment/Libraries
Patch1: smpeg-0.4.4-automake15.patch
Patch2: smpeg-autoconf253.patch
Patch3: smpeg-gtv.patch
Patch4: smpeg-0.4.4-plaympeg.patch
URL: https://icculus.org/smpeg
BuildRequires: gcc-c++, SDL-devel

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder
and SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to 
create a general purpose MPEG video/audio player for the Linux OS. 

%package devel
Summary: Libraries, includes and more to develop SMPEG applications.
Group: Development/Libraries/C/Multimedia
Requires: %{name} = %{version}

%description devel
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder
and SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to 
create a general purpose MPEG video/audio player for the Linux OS. 

This is the libraries, include files and other resources you can use
to develop SMPEG applications.

%package tools
Summary: Command line tools for working with %name
Group: Command Line Applications/Multimedia
Requires: %name = %version-%release

%description tools
Command line tools for working with %name

%package static
Summary: Libraries for linking statically to %name
Group: Development/Libraries/C/Multimedia/Static
Requires: %name-devel = %version-%release

%description static
Libraries for linking statically to %name

%prep
%setup -q -n %name
##%patch 1 -p1 -b .am15~
##%patch 2 -p1 -b .ac253~
%patch 3 -p1 -b .gtv~
%patch 4 -p1 -b .plaympeg~
cp -f /usr/share/libtool/build-aux/config.* .
sed -i -e 's|unsigned int xlen,ylen;|int xlen,ylen;|' -e 's|unsigned int linbits;|int linbits;|' MPEGaudio.h
sed -i 's|answer + 4|"%s", answer + 4|' plaympeg.c

%build
cp -f /usr/share/automake*/depcomp . || :
cat >acinclude.m4 <<EOF #HACK
AC_DEFUN([AC_TYPE_SOCKLEN_T],
[AC_CACHE_CHECK([for socklen_t], ac_cv_type_socklen_t,
[
  AC_TRY_COMPILE(
  [#include <sys/socket.h>],
  [socklen_t len = 42; return len;],
  ac_cv_type_socklen_t=yes,
  ac_cv_type_socklen_t=no)
])
  if test $ac_cv_type_socklen_t != yes; then
    AC_DEFINE(socklen_t, int)
  fi
])
AC_DEFUN([AM_PATH_GTK], [return 1])
EOF
touch INSTALL NEWS AUTHORS ChangeLog
./autogen.sh
##libtoolize --force
#autoreconf
%configure --disable-debug --disable-gtk-player --disable-opengl-player --with-sdl-prefix=%_prefix
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT/usr/share/aclocal
install -m 644 smpeg.m4 $RPM_BUILD_ROOT/usr/share/aclocal

%files
%doc CHANGES COPYING README
%{_libdir}/lib*.so*

%files tools
##%{_bindir}/gtv
%{_bindir}/plaympeg
%exclude %{_mandir}/man1/gtv*
%{_mandir}/man1/plaympeg*

%files devel
%{_bindir}/smpeg-config
%{_includedir}/*
%{_datadir}/aclocal/*

%files static
%{_libdir}/lib*.a
%{_libdir}/lib*.la

%changelog
* Wed Apr 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.5
- Rebuilt for Fedora
* Thu Mar 13 2008 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.5-0.370.2ark
- Remove bogus arts dependency
* Mon Sep 24 2007 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.5-0.370.1ark
- Update to SVN snapshot
- Split out -static -and -tools packages
* Fri Oct 10 2004 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.5-0.20041008.1ark
- Update to CVS snapshot
* Mon Aug 26 2002 Ark Linux Team <arklinux@arklinux.org> 0.4.4-19ark
- automated rebuild
* Sun Aug 18 2002 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.4-18ark
- Force linking with libgcc_s
* Sat Aug 17 2002 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.4-17ark
- automated rebuild
* Fri Aug  9 2002 Bernhard Rosenkraenzer <bero@arklinux.org> 0.4.4-16ark
- Remove gtv - we have xine and mplayer
