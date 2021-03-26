%define _default_patch_fuzz 2

# debug make the package bigger
%define debug_package %{nil}

# set wantvdpau to 1 if you want to build packages with NVidia VDPAU
# hardware video rendering offload support
# (and pay attention to the dependencies)
%define wantvdpau 1

# set wantpulse to 1 if you wish to compile with pulseaudio support
%define wantpulse 0

Name: boxee
Version: 0.9.23.15885
Release: 1
URL: http://www.boxee.tv 
Source: %{name}-sources-%{version}.tar.bz2
Source1: boxee.desktop
Source2: boxee.png
Summary: Fedora Linux port
License: GPLv2 with exceptions
Group: Applications/Multimedia

BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_mixer-devel
BuildRequires: fontconfig-devel
BuildRequires: fribidi-devel
BuildRequires: glibc-devel
BuildRequires: hal-devel
BuildRequires: glew-devel
BuildRequires: libstdc++-devel
BuildRequires: glib2-devel
BuildRequires: libjasper-devel
BuildRequires: libjpeg-devel
BuildRequires: libogg-devel
BuildRequires: libpng-devel
BuildRequires: libstdc++-devel
BuildRequires: e2fsprogs-devel
BuildRequires: libvorbis-devel
BuildRequires: lzo-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: tre-devel
BuildRequires: boost-devel
BuildRequires: bzip2-devel
BuildRequires: freetype-devel
BuildRequires: libXinerama-devel
BuildRequires: fontconfig-devel
BuildRequires: mysql-libs
BuildRequires: mysql-devel
BuildRequires: jasper-devel
BuildRequires: faac-devel
BuildRequires: enca-devel
BuildRequires: cmake
BuildRequires: gperf
BuildRequires: nasm
BuildRequires: libXmu-devel
BuildRequires: pcre-devel
BuildRequires: gcc-c++
BuildRequires: sqlite-devel
BuildRequires: curl-devel
BuildRequires: libmad-devel
BuildRequires: libcdio-devel
BuildRequires: ftgl-devel
BuildRequires: avahi-devel
BuildRequires: ffmpeg-devel

# new with svn 23241
BuildRequires: libsamplerate-devel
BuildRequires: libmms-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel

# new leading up to svn23581
BuildRequires: faad2-devel
BuildRequires: flac-devel
BuildRequires: libtiff-devel
BuildRequires: libcurl-devel
BuildRequires: libass-devel
BuildRequires: lame-devel
BuildRequires: libsmbclient-devel

# For Boxee
BuildRequires: automake >= 1.10
BuildRequires: xulrunner

%if %{fedora} == 15
BuildRequires: kcbench-data
%endif

# nvidia vdpau
%if %{wantvdpau}
BuildRequires: libvdpau-devel
%endif

BuildRequires: python-devel, zip, rsync, libtool, gettext
AutoReq: off
Requires: libmms, mysql-libs

Requires: libvorbis >= 1.2
Requires: libmad >= 0.15
Requires: libogg >= 1.1
# xorg-x11-utils is needed for xpdyinfo binary that xbmc will try to run on startup - thanks ctatman
Requires: xorg-x11-utils
Requires: ftgl
Requires: avahi

# new leading up to svn23581
Requires: faac
Requires: faad2 >= 2.7-16
Requires: flac
Requires: lame

# Patches
Patch1: boxee-0.9.14.6992-run-boxee-desktop_feodra.patch
Patch2: boxee-0.9.20.10263-config_libmysql_path.patch
Patch3: boxee-0.9.21.11497-fix_Para_py.patch
Patch4: boxee-0.9.23-fix_for_gcc-4_6.patch
Patch5: boxee-0.9.23-find-smbno_h.patch
Patch6: boxee-0.9.21.12563-fix_python_a-include_ThreadPolicy.patch

%description
Boxee is a free, open-source software platform that integrates personal media 
with Internet media along with social networking. boxee’s social networking 
component allows users to share information about what they’re listening to or 
watching with other Boxee users or friends on social networks like twitter, 
facebook, etc.

It is based on the Award winning open-source project XBMC, and also 
incorporates the XUL framework (which is the basis for the Mozilla browser).

%prep 
%setup -q -n %{name}-sources-%{version}

# Patch this shit up
%patch1 -p1 -b .rn-bxe-dsktp_fedora
%patch2 -p1 -b .config_libmysql_path
%patch3 -p1 -b .fix_Para
%patch4 -p1 -b .gcc-4_6

%if %{fedora} == 15
%patch5 -p1 -b .smbno
%endif

# run boostrap, needed to get a configure
./bootstrap

%ifarch x86_64
CFLAGS="-I/usr/lib64/dbus-1.0/include -I/usr/lib64/glib-2.0/include -D_FORTIFY_SOURCE=2"
LDFLAGS="-L/usr/lib64/mysql -lm -lcrypto -lXext -lmms"
INCLUDES="-I/usr/lib64/dbus-1.0/include -I/usr/include/ffmpeg -I/usr/include/cdio++ -I/usr/include/cdio" 
%else
CFLAGS="-I/usr/lib/dbus-1.0/include -I/usr/lib/glib-2.0/include -D_FORTIFY_SOURCE=2"
LDFLAGS="-L/usr/lib/mysql -lm -lcrypto -lXext -lmms"
INCLUDES="-I/usr/lib/dbus-1.0/include -I/usr/include/ffmpeg -I/usr/include/cdio++ -I/usr/include/cdio" 
%endif
export CFLAGS
export LDFLAGS
export INCLUDES
mv "language/English (US)" language/English

%ifarch x86_64
cp %{_includedir}/python2.7/{pyconfig.h,pyconfig-64.h} %{_builddir}/%{name}-sources-%{version}/xbmc/lib/libPython/Python/Include/.
%else
cp %{_includedir}/python2.7/{pyconfig.h,pyconfig-32.h} %{_builddir}/%{name}-sources-%{version}/xbmc/lib/libPython/Python/Include/.
%endif

# I know this is ugly as hell, but It's all i've got till I can learn the correct way to fix this
cp %{_builddir}/%{name}-sources-%{version}/xbmc/{ThreadPolicy.cpp,ThreadPolicy.h} %{_builddir}/%{name}-sources-%{version}/xbmc/lib/libPython/.
%patch6 -p1 -b .fix_python_a

%configure \
%if %{wantvdpau}
  --enable-vdpau \
%else
  --disable-vdpau \
%endif
%if %{wantpulse}
  --enable-pulse \
%else
  --disable-pulse \
%endif
  --enable-goom

%build

%ifarch x86_64
  CFLAGS="-I/usr/lib64/dbus-1.0/include -I/usr/lib64/glib-2.0/include -D_FORTIFY_SOURCE=2" \
  LDFLAGS="-L/usr/lib64/mysql -lm -lcrypto -lXext -lmms" \
  INCLUDES="-I/usr/lib64/dbus-1.0/include -I/usr/include/ffmpeg -I/usr/include/cdio++ -I/usr/include/cdio" \
  make 
  make -C %{_builddir}/%{name}-sources-%{version} give_me_my_mouse_back
%else
  CFLAGS="-I/usr/lib/dbus-1.0/include -I/usr/lib/glib-2.0/include -D_FORTIFY_SOURCE=2"
  LDFLAGS="-L/usr/lib/mysql -lm -lcrypto -lXext -lmms" \
  INCLUDES="-I/usr/lib/dbus-1.0/include -I/usr/include/ffmpeg -I/usr/include/cdio++ -I/usr/include/cdio" \
  make 
  make -C %{_builddir}/%{name}-sources-%{version} give_me_my_mouse_back
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/boxee/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/boxee/plugins/{music,pictures,video}
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
find language media screensavers scripts skin sounds UserData visualisations system -type d -not -iregex ".*svn.*" -exec mkdir -p $RPM_BUILD_ROOT/usr/share/boxee/"{}" \; -printf " -- %f                           \r"
install -m755 Boxee $RPM_BUILD_ROOT/usr/bin/Boxee
install -m755 give_me_my_mouse_back $RPM_BUILD_ROOT/usr/bin/give_me_my_mouse_back
install -m755 run-boxee-desktop.in $RPM_BUILD_ROOT/usr/bin/run-boxee-desktop
install -m755 xbmc-xrandr $RPM_BUILD_ROOT/usr/bin/xbmc-xrandr
install -m644 %{_sourcedir}/boxee.desktop $RPM_BUILD_ROOT/usr/share/applications/boxee.desktop
install -m644 %{_sourcedir}/boxee.png $RPM_BUILD_ROOT/usr/share/pixmaps/boxee.png
cp -a media/{boxee_screen_saver,defaultrss.png,downloadrss.png,Fonts,icon32x32-linux.png,icon.png,weather.rar} $RPM_BUILD_ROOT/usr/share/boxee/media/.
cp -f screensavers/*.xbs $RPM_BUILD_ROOT/usr/share/boxee/screensavers
cp -a scripts/{autoexec.py,Lyrics,OpenSubtitles,RTorrent} $RPM_BUILD_ROOT/usr/share/boxee/scripts
cp -a --parents skin/boxee/{720p,colors,Fonts,media,skin.xml,sounds} $RPM_BUILD_ROOT/usr/share/boxee/
cp -a language/* $RPM_BUILD_ROOT/usr/share/boxee/language
cp -f UserData/{rtorrent.rc,shortcuts.xml.in.linux,sources.xml.in.diff.linux,sources.xml.in.linux} $RPM_BUILD_ROOT/usr/share/boxee/UserData
cp -a visualisations/{opengl_spectrum.vis,projectM,projectM.presets,ProjectM.vis,Waveform.vis} $RPM_BUILD_ROOT/usr/share/boxee/visualisations
%ifarch x86_64
cp -a system/{asound.conf,hdhomerun-x86_64-linux.so,ImageLib-x86_64-linux.so,keymaps,libexif-x86_64-linux.so,libid3tag-x86_64-linux.so,Lircmap.xml,playercorefactory.xml,players,python,scrapers,shaders} $RPM_BUILD_ROOT/usr/share/boxee/system/.
%else
cp -a system/{asound.conf,hdhomerun-i486-linux.so,ImageLib-i486-linux.so,keymaps,libexif-i486-linux.so,libid3tag-i486-linux.so,Lircmap.xml,playercorefactory.xml,players,python,scrapers,shaders} $RPM_BUILD_ROOT/usr/share/boxee/system/.
%endif
rm -rf `find $RPM_BUILD_ROOT/usr/share/boxee/system |grep -E "\.dll|\.DLL|osx|\.exe|_cocoa|\.tiff|\.dylib|\.chk|\.jnilib|\.rsrc|mangle|maccharset.properties|searchplugins|shlibsign|ssltunnel|_speedups.so|upnpserver.xml|X10-Lola-IRSSmap.xml"`
rm -rf $RPM_BUILD_ROOT/usr/share/boxee/system/players/flashplayer/{xulrunner,xulrunner-i486-linux-jaunty,xulrunner-win32}
rm -rf $RPM_BUILD_ROOT/usr/share/boxee/system/players/flashplayer/xulrunner-x86_64-linux/bin
rm -rf $RPM_BUILD_ROOT/usr/share/boxee/system/players/dvdplayer/etc 
rm -rf $RPM_BUILD_ROOT/usr/share/boxee/system/python/{Dlls,python24.dll,python24.zip,python24.zlib,readme.txt,spyce}
mv $RPM_BUILD_ROOT/usr/share/boxee/system/python/Lib $RPM_BUILD_ROOT/usr/share/boxee/system/python/lib
%ifarch x86_64
rm -rf `find $RPM_BUILD_ROOT/usr/share/boxee |grep -E "i486"`
%else
rm -rf `find $RPM_BUILD_ROOT/usr/share/boxee |grep -E "x86_64"`
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%if %{fedora} == 14 || 15
ln -s %{_lib}/libcrypto.so.1.0.0d %{_libdir}/libcrypto.so.0.9.8
ln -s %{_libdir}/libssl.so.1.0.0d %{_libdir}/libssl.so.0.9.8
%endif
mkdir -p /usr/local/bin
ln -s /usr/bin/python /usr/local/bin/python

%post 
%if %{fedora} == 14 && %{_arch} == x86_64
ln -s %{_libdir}/xulrunner-1.9.2 %{_datadir}/boxee/system/players/flashplayer/xulrunner-x86_64-linux/bin
%endif

%if %{fedora} == 15 && %{_arch} == x86_64
ln -s %{_libdir}/xulrunner-2 %{_datadir}/boxee/system/players/flashplayer/xulrunner-x86_64-linux/bin
%endif

%preun
rm -rf %{_libdir}/libcrypto.so.0.9.8
rm -rf %{_libdir}/libssl.so.0.9.8

%if %{fedora} == 14 || 15 && %{_arch} == x86_64
rm -rf %{_datadir}/boxee/system/players/flashplayer/xulrunner-x86_64-linux/bin
%endif
rm -f /usr/local/bin/python

%files
%defattr(-,root,root)
   %{_bindir}/Boxee
   %{_bindir}/give_me_my_mouse_back
   %{_bindir}/run-boxee-desktop
   %{_bindir}/xbmc-xrandr
   %{_datadir}/applications/boxee.desktop
   %{_datadir}/pixmaps/boxee.png
   %{_datadir}/boxee

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Jun 17 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Thu Jun 02 2011 Justin Payne - 0.9.23.15885-0.2.b
- Build for F14 and F15
- Drop support in spec file for F12 and F13
- Patch to build with gcc-4.6
- Patch to find smbfs headers no longer in kernel-headers

* Thu Dec 2 2010 Justin Payne - 0.9.23.15885-0.1.b
- Updated to new sources

* Mon Aug 30 2010 Justin Payne - 0.9.22.13692-0.1.b
- Updated to new sources

* Sat Jul 10 2010 Justin Payne - 0.9.21.12563-0.1.b
- Updated to new sources

* Thu Jun 24 2010 Justin Payne - 0.9.21.11497-0.2.b
- Cleaned up spec file
- Fedora 13 build
- Dropped support for EOL Fedora releases 10 and 11
- Fixed the old Para.py syntax errors

* Thu May 05 2010 Justin Payne - 0.9.21.11497-0.1.b
- Updated beta sources
- Thanks for changing the source file name again guys

* Wed Jan 27 2010 Justin Payne - 0.9.20.10408-0.2.b
- Pulled rtorrent out of this package.
- Symlink to system xulrunner. Why keep bundling these pre-built libraries?

* Wed Jan 27 2010 Justin Payne - 0.9.20.10408-0.1.b
- New Beta sources released. Thanks for renaming the
  tarball guys :-(

* Sat Jan 23 2010 Justin Payne - 0.9.20.10263-0.2.b
- Added runtime option for new lirc path [thanks sp00ge]

* Fri Jan 08 2010 Justin Payne - 0.9.20.10263-0.1.b
- Build Beta 
- Changes to spec file for x86_64

* Thu Dec 10 2009 Justin Payne - 0.9.14.6992-0.2.a
- Changes to BuildRequires for ftgl and f12 install support

* Sun Nov 07 2009 Justin Payne - 0.9.14.6992-0.1.a
- Initial port of Boxee Alpha 0.9.14.6992 to Fedora
