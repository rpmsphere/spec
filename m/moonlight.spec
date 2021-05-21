%define libname libmoon
%define develname libmoon-devel
%define monover 2.6.1
%define monobasicver 2.6

Summary: Open Source implementation of Silverlight
Name: moonlight
Version: 2.4.1
Release: 9
Source0: http://ftp.novell.com/pub/mono/sources/moon/%version/%name-%{version}.tar.bz2
#gw these differ from the release tarballs
Source1: http://ftp.novell.com/pub/mono/sources/moon/%version/mono-%monover.tar.bz2
Source2: http://ftp.novell.com/pub/mono/sources/moon/%version/mono-basic-%monobasicver.tar.bz2
Patch: moon-2.0-format-strings.patch
Patch1: moon-2.0-fix-linkage.patch
#gw fix building with --no-undefined enabled
Patch5: mono-2.0-fix-linking.patch
Patch8: mono-2.6-format-strings.patch
Patch9:  bad-register.patch
Patch11: moonlight-2.3-firefox-4.0.patch
Patch12: moonlight-2.4.1-fix-build-ffmpeg.patch
Patch13: moonlight-2.4.1-fix-build-curl.patch
# /usr/include/xulrunner-9.0.1/nsStringAPI.h:1101:48: error: 'char16_t' was not declared in this scope
# TODO: investigate if libxul*.pc or mozilla-plugin.c should include -std=gnu++0x or if the char16_t
# is there by mistake (Anssi 01/2012)
Patch14: moonlight-firefox-char16_t.patch
License: LGPLv2
Group: System/Libraries
URL: http://www.mono-project.com/Moonlight
BuildRequires: gcc-c++
#BuildRequires: ffmpeg-devel
BuildRequires: libXtst-devel
BuildRequires: libXrandr-devel
BuildRequires: xulrunner-devel
BuildRequires: cairo-devel >= 1.6
BuildRequires: gnome-desktop-sharp-devel
BuildRequires: chrpath
BuildRequires: gtk2-devel
BuildRequires: ImageMagick-devel
BuildRequires: dbus-glib-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: ndesk-dbus-devel 
BuildRequires: curl-devel
BuildRequires: expat-devel
BuildRequires: bison
BuildRequires: zip
BuildRequires: links notification-daemon gtk-sharp2-doc
BuildRequires: python2 udisks2
Requires: %libname >= %version
Provides: moon
Obsoletes: moon
# Disable -devel as the lib is built against internal mono
Obsoletes: %develname < 2.4.1-3

%description
Moonlight is an open source implementation of Microsoft Silverlight
for Unix systems. It supports rich browser applications, similar to
Adobe Flash.

%package doc
Summary:	Documentation for %name
Group:		Development/Other
BuildArch:	noarch
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
This package provides API documentation for %name.

%package -n %libname
Group:System/Libraries
Summary: Open Source implementation of Silverlight

%description -n %libname
Moonlight is an open source implementation of Microsoft Silverlight
for Unix systems. It supports rich browser applications, similar to
Adobe Flash.

%if 1
%package -n %develname
Group:Development/C++
Summary: Open Source implementation of Silverlight
Requires: %libname = %version-%release
Provides: libmoon-devel = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
Moonlight is an open source implementation of Microsoft Silverlight
for Unix systems. It supports rich browser applications, similar to
Adobe Flash.
%endif

%prep
%setup -q -n %name-%version -a 1 -a 2
%patch -p1
%patch1 -p1 -b .fix-linking
%patch11 -p1
%patch12 -p1 -b .ffmpeg
%patch13 -p1 -b .curl
%patch14 -p1
autoreconf -fi
cd mono-%monover
%patch5 -p1 -b .linking
%patch8 -p1 -b .format-strings
%patch9
cd ../mono-basic-%monobasicver/vbnc/vbnc
#gw rename source file with parenthesis
sed -i -e "s^(^^" -e "s^)^^" vbnc.exe.sources
for x in source/Parser/Parser\(*.vb;do
  mv "$x" $(echo "$x" | sed -e "s^(^^" -e "s^)^^")
done

%build
export CFLAGS+=" -fPIC -std=gnu89"
cd mono-%monover
./configure --prefix=%{_builddir}/%name-%version/install \
            --with-mcs-docs=no \
            --with-ikvm-native=no

make EXTERNAL_MCS=false EXTERNAL_RUNTIME=false
make install
# libtool is evil, if the .la is present things get jacked up
find %{_builddir}/%name-%version/install -name \*.la -delete
cd ..
# Configure against the junk install of mono
export PATH=%{_builddir}/%name-%version/install/bin:${PATH}
export LD_LIBRARY_PATH=%{_builddir}/%name-%version/install/lib:${LD_LIBRARY_PATH}
export PKG_CONFIG_PATH=%{_builddir}/%name-%version/install/lib/pkgconfig:${PKG_CONFIG_PATH}
# And then we build moonlight
%configure --without-testing --without-performance --without-examples \
  --disable-debug --disable-sanity \
  --with-ff3=no \
  --with-cairo=system \
  --with-mcspath=`pwd`/mono-%monover/mcs --with-mono-basic-path=`pwd`/mono-basic-%monobasicver --with-curl=system \
  --disable-desktop-support --enable-sdk
# We need the system gac for gtk-sharp
# Only if we're linking to the junk mono
export MONO_GAC_PREFIX=%{_builddir}/%name-%version/install:/usr
#gw parallel build does not work in 2.0
%if %{fedora}>20
sed -i '/G_GNUC_INTERNAL void g_ptr_array_insert /d' src/utils.h
%endif
make

%install
%makeinstall
mkdir -p %buildroot%_libdir/mozilla/plugins
export PATH=%{_builddir}/%name-%version/install/bin:${PATH}
export LD_LIBRARY_PATH=%{_builddir}/%name-%version/install/lib:${LD_LIBRARY_PATH}
export PKG_CONFIG_PATH=%{_builddir}/%name-%version/install/lib/pkgconfig:${PKG_CONFIG_PATH}
%{__make} install DESTDIR=$RPM_BUILD_ROOT
# Copy the custom libmono.so.0 for the plugin to use
install -m 755 %{_builddir}/%name-%version/install/lib/libmono.so.0 $RPM_BUILD_ROOT%{_libdir}/moonlight/
%if %{fedora} < 18
# Make the loader pull in the correct libmono
chrpath -r  %{_libdir}/moonlight $RPM_BUILD_ROOT%{_libdir}/moonlight/plugin/libmoon*.so
ln -s %_libdir/moonlight/plugin/libmoonloader.so %buildroot%_libdir/mozilla/plugins
rm -f %buildroot%_libdir/moon/plugin/README
%endif

# Remove files from -devel
%if 0
rm -f %buildroot%_bindir/munxap
rm -f %buildroot%_libdir/%name/munxap.exe*
rm -f %buildroot%_libdir/libmoon.so
rm -f %buildroot%_datadir/pkgconfig/%{name}*.pc
%endif
find $RPM_BUILD_ROOT -name '*.la' -delete

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%files
%doc README TODO
%_bindir/*
##%if 0%{fedora} > 16
##%_prefix/lib/mono/%name
##%_prefix/lib/mono/gac/*
##%else
##%_libdir/mono/%name
##%_libdir/mono/gac/*
##%endif
%_prefix/lib/%name/2.0*
%if %{fedora} < 18
%_libdir/mozilla/plugins/libmoon*
%endif
%_libdir/%name/plugin
%_libdir/%name/*.exe*
##%_datadir/man/man1/*

%files -n %libname
%_libdir/libmoon.so.*
%_libdir/%name/libmono.so.*

%if 1
%files -n %develname
%_bindir/munxap
%_libdir/%name/munxap.exe*
%_libdir/libmoon.so
##%_datadir/pkgconfig/%{name}*.pc
%endif

##%files doc
##%_prefix/lib/monodoc/sources/%name-gtk*

%changelog
* Tue Jul 03 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.1
- Rebuilt for Fedora
* Sat Feb 18 2012 tv <tv> 2.4.1-9.mga2
+ Revision: 210482
- rebuild for new xulrunner
* Mon Jan 09 2012 anssi <anssi> 2.4.1-8.mga2
+ Revision: 193603
- add missing buildrequires on expat-devel (it was probably pulled in
  implicitely before)
- build firefox plugin using -std=gnu++0x to fix char16_t build error
  in xulrunner headers (firefox-char16_t.patch)
* Wed Dec 07 2011 fwang <fwang> 2.4.1-7.mga2
+ Revision: 178055
- drop all .la files
* Sun Dec 04 2011 pterjan <pterjan> 2.4.1-6.mga2
+ Revision: 176551
- Do not BuildRequire mono-devel, we need to use embedded copy
- Fix build for recent libcurl
- Add explicit link to libX11
- Fix ffmpeg patch
- Move the ffmpeg at the right place, it is for moonlight sources not mono
  + dmorgan <dmorgan>
    - Fix build with new ffmpeg
    - Rebuild against new ffmpeg
    - Add tarball
    - Fix sha1.lst file
    - Rebuild against new ffmpeg
  + fwang <fwang>
    - rebuild for new ffmpeg
* Wed Apr 20 2011 pterjan <pterjan> 2.4.1-3.mga1
+ Revision: 89246
- Remove useless -devel
* Tue Apr 19 2011 pterjan <pterjan> 2.4.1-2.mga1
+ Revision: 88107
- Update mono-basic-2.6.tar.bz2
* Sun Apr 17 2011 dmorgan <dmorgan> 2.4.1-1.mga1
+ Revision: 87318
- Try to fix linkage ( spturtle)
- Update to moonlight 2.4.1
- imported package moonlight
