Summary: A compiler/interpreter suite for developing images
Name: hgl
Version: 0.5.16
#Version: 0.5.42
Release: 1
License: BSD-2-clause
Group: Productivity/Graphics/Other
URL: http://hgl.rangun.de
Source: %{name}_%{version}~wheezy.tar.xz
Patch1: lua.patch
Patch2: example.hgl.patch
Patch3: netpbm.patch
BuildRequires: lua-devel
BuildRequires: gpgme-devel >= 1.1.5
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libcaca-devel >= 0.99
BuildRequires: netpbm-devel
BuildRequires: cppunit-devel >= 1.12
BuildRequires: compat-lua-devel
Patch5: lua-compat.patch
Patch4: hgl-fedora.patch
BuildRequires: giflib-devel >= 4.1.6
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: help2man
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: popt-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel >= 2.5.0
BuildRequires: libcurl-devel >= 7.16.2
BuildRequires: libxml2-devel >= 2.6.31
BuildRequires: libsmbclient-devel >= 3.0.28
BuildRequires: subversion
BuildRequires: bison
BuildRequires: flex
BuildRequires: doxygen >= 1.5.5
BuildRequires: graphviz
BuildRequires: ghostscript-core ImageMagick

%description
HGL is a compiler/interpreter suite for developing images. It features its own
simple but powerful language, an output format configurable by plugins, runtime
input handled by plugins, and easy integration into various environments like
Web servers or graphical applications. The input is taken from a source file,
which has to be compiled for quick and frequent access by the interpreter.
An interpreter then runs the compiled files, takes input from custom plugins
(if neccessary), and outputs its result via custom plugins.

%package -n libhgltypes2
Summary: compiler/interpreter suite for developing images (runtime libraries)
Group: Productivity/Graphics/Other
Obsoletes: libhgltypes0
Obsoletes: libhgltypes1
%description -n libhgltypes2
runtime libraries for compiler and interpreter

%package interpreter
Summary: compiler/interpreter suite for developing images (interpreter)
Group: Productivity/Graphics/Other
Requires: libhgltypes2 = %{version}
%description interpreter
the HGL interpreter

%package compiler
Summary: compiler/interpreter suite for developing images (compiler)
Group: Productivity/Graphics/Other
Requires: libhgltypes2 = %{version}
%description compiler
the HGL compiler

%package plugins
Summary: compiler/interpreter suite for developing images (plugins)
Group: Productivity/Graphics/Other
Requires: hgl-interpreter >= %{version}
%description plugins
all plugins for the HGL interpreter

%package tools
Summary: compiler/interpreter suite for developing images (tools)
Group: Productivity/Graphics/Other
Requires: libhgltypes2 >= %{version}
%description tools
all tools for the HGL interpreter

%package devel
Summary: compiler/interpreter suite for developing images (plugin development)
Group: Development/Libraries/Other
%description devel
development files

%prep
%setup -q
#patch1 -p1
%patch5 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2
sed -i '/AM_PATH_CPPUNIT/d' configure.ac

%build
autoreconf -fiv
%configure \
	--disable-maintainer-mode \
    --disable-dependency-tracking \
    --disable-silent-rules \
    --disable-dummy-plugins \
    --disable-doxygen-pdf \
    CPPFLAGS="-fvisibility=hidden -fvisibility-inlines-hidden -D_GLIBCXX_VISIBILITY=0 -DNDEBUG -I/usr/include/netpbm" \
    CXXFLAGS="$RPM_OPT_FLAGS -fipa-pta -fstrict-aliasing -std=gnu++98"
make

%install
%make_install
rm -rf %{buildroot}/%{_libdir}/hgl/plugins/*.la
rm -rf %{buildroot}/%{_libdir}/hgl/*.la
rm -rf %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_libdir}/*.so
rm -rf %{buildroot}/%{_libdir}/hgl/libhglcompiler.a
rm -rf %{buildroot}/%{_libdir}/hgl/libhglcompiler.so
rm -rf %{buildroot}/%{_libdir}/hgl/libhglinterpreter.a
rm -rf %{buildroot}/%{_libdir}/hgl/libhglinterpreter.so
rm -rf %{buildroot}/%{_libdir}/hgl/libhglcontrolcommand.a
rm -rf %{buildroot}/%{_libdir}/hgl/libhglcontrolcommand.so
rm -rf %{buildroot}/%{_libdir}/hgl/libhglimageoutput.so

%clean
rm -rf %{buildroot}

%post interpreter -p /sbin/ldconfig
%post compiler -p /sbin/ldconfig
%post -n libhgltypes2 -p /sbin/ldconfig

%postun interpreter -p /sbin/ldconfig
%postun compiler -p /sbin/ldconfig
%postun -n libhgltypes2 -p /sbin/ldconfig

%files -n libhgltypes2
%{_libdir}/libhgltypes*.so.*
%{_datadir}/locale/*/LC_MESSAGES/libhgltypes.mo

%files interpreter
%config %{_sysconfdir}/hglrc
%{_bindir}/hgl
%{_libdir}/hgl/libhglinterpreter-*.so
%{_libdir}/hgl/libhglimageoutput-*.so
%{_mandir}/man1/hgl.1.*
%dir %{_datadir}/hgl/examples
%{_datadir}/hgl/examples/mandelbrot.*
%{_datadir}/hgl/examples/example.hglz
%{_datadir}/hgl/examples/example.png
%{_datadir}/hgl/examples/Coat_of_Arms_of_Germany.hglz
%{_datadir}/hgl/examples/cathy-doppelgaenger.hglz
%{_datadir}/hgl/examples/cathys-bedroom.hglz
%{_datadir}/hgl/examples/progress.sh
%doc %{_datadir}/doc/hgl/README.interpreter
%dir %{_datadir}/hgl
%{_datadir}/hgl/stdlib.hglz
%{_datadir}/locale/*/LC_MESSAGES/hgl.mo

%files compiler
%config %{_sysconfdir}/hglcrc
%{_bindir}/hglc
%{_libdir}/hgl/libhglcompiler-*.so
%{_datadir}/hgl/examples/example.hgl
%{_datadir}/hgl/examples/complex.hgl.bz2
%dir %{_datadir}/hgl/examples/flags
%{_datadir}/hgl/examples/flags/*.hgl
%{_datadir}/hgl/examples/Coat_of_Arms_of_Germany.hgl.bz2
%{_datadir}/hgl/examples/wales-dragon.hgl.bz2
%{_datadir}/hgl/examples/cathys-bedroom.hgl.bz2
%{_datadir}/hgl/examples/Flag_of_Turkmenistan.hgl.bz2
%{_datadir}/hgl/examples/simple-alpha-blending.hgl
%doc %{_datadir}/doc/hgl/README.precision
%doc %{_datadir}/doc/hgl/README.lua
%{_mandir}/man1/hglc.1.*
%{_datadir}/locale/*/LC_MESSAGES/hglc.mo

%files plugins
%dir %{_libdir}/hgl
%dir %{_libdir}/hgl/plugins
%{_libdir}/hgl/libhglcontrolcommand-*.so
%{_libdir}/hgl/plugins/*.so
#%{_datadir}/hgl/examples/Coat_of_Arms_of_Germany.gif
%{_datadir}/hgl/examples/cathys-bedroom.png
#%{_datadir}/hgl/examples/Flag_of_Algeria.ppm
%{_datadir}/hgl/examples/Flag_of_Samoa.svg
%{_datadir}/locale/*/LC_MESSAGES/hgl-ioplugins.mo
%{_datadir}/locale/*/LC_MESSAGES/hgl-csplugins.mo
%dir %{_datadir}/doc/hgl
%doc %{_datadir}/doc/hgl/README.svg
%doc %{_datadir}/doc/hgl/README.ControlSources

%files tools
%{_bindir}/svg2hgl
%{_datadir}/hgl/examples/home.hgl
%{_datadir}/hgl/examples/home.svg
%{_datadir}/hgl/examples/Coat_of_Arms_of_Germany.svg
%{_datadir}/hgl/examples/Flag_of_Turkmenistan.svg
%doc %{_datadir}/doc/hgl/README.svg2hgl
%{_datadir}/locale/*/LC_MESSAGES/hgl-svg2hgl.mo
%{_mandir}/man1/svg2hgl.1.*

%files devel
%dir %{_includedir}/hgl
%{_includedir}/hgl
%{_libdir}/hgl/libhglcontrolinterface.a
%{_libdir}/hgl/libhgldecompiler.a
%{_libdir}/libhgltypes.a
%doc %{_datadir}/doc/hgl/libhgltypes-doc
%doc %{_datadir}/doc/hgl/libhgltypes.tag
%doc %{_datadir}/doc/hgl/plugin-api-doc
%doc %{_datadir}/doc/hgl/plugin.tag

%changelog
* Sun Jan 19 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.16
- Rebuild for Fedora
