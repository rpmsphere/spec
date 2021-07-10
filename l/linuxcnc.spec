%define __python /usr/bin/python3
%define rtai 0

Name: linuxcnc
Version: 2.8.2
Release: 1
Summary: LinuxCNC controls CNC machines
Summary(ru_RU.UTF-8): Программа управления ЧПУ станков
License: GPLv2+ and LGPLv2
Group: Engineering
URL: https://github.com/LinuxCNC/linuxcnc
Source0: %name-%version.tar.gz
Source1: aarch64-io.h
Patch1: fix_install-alt.patch
BuildRequires: gcc-c++ imake libGL-devel libGLU-devel libXaw-devel libXinerama-devel libXmu-devel libXt-devel ncurses-devel readline-devel
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(libmodbus) pkgconfig(libudev) pkgconfig(libusb-1.0)
BuildRequires: tcl-devel tk-devel kmod bwidget tkimg tclx python3-tkinter ghostscript-core ImageMagick libxslt groff procps psmisc
BuildRequires: python3-devel python3-lxml boost-python3-devel pycairo-devel pygtk2-devel intltool
BuildRequires: libtirpc-devel bwidget
#BuildRequires: graphviz dblatex docbook-xsl netcat texlive-lang-cyrillic texlive-lang-french texlive-lang-spanish texlive-lang-german asciidoc-a2x source-highlight
Requires: tcl-%name = %version
Requires: %name-data = %version

%description
LinuxCNC is software that runs on Linux, on most standard PCs, that can
interpret G-code and run a CNC machine. It was originally developed on a
milling machine, but support was added for lathes and many other types of
machine. It can be used with mills, lathes, plasma cutters, routers, robots,
and so on. 

%description -l ru_RU.UTF-8
LinuxCNC это программа, которая работает на ОС Linux на большинстве стандартных
ПК, которые могут интерпретировать G-код и запустить станок с ЧПУ. Изначально он
был разработан для фрезерного станка, но поддержка была добавлена и для токарных
станков и многих других типов машин. Он может быть использован с токарными
станками, станками плазменной резки, маршрутизаторами, роботами, и так далее.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for %name

%package data
Summary: Data files for %name
Buildarch: noarch
Group: Engineering

%description data
Data files for %name

%package -n tcl-%name
Summary: Tcl files for %name
Group: Development/Tcl
Requires: bwidget
Provides: tcl(Hal) tcl(Linuxcnc) tcl(Ngcgui)

%description -n tcl-%name
Tcl files for %name

%package -n python-%name
Summary: Python files for %name
Group: Development/Python

%description -n python-%name
Python files for %name

%prep
%setup -q
%patch1 -p1
sed -i 's|INCLUDES := .|INCLUDES := . /usr/include/tirpc|' src/Makefile
sed -i 's|LDFLAGS := |LDFLAGS := -ltirpc |' src/Makefile
%ifarch aarch64
cp %SOURCE1 src/rtapi/io.h
sed -i 's|<sys/io.h>|"io.h"|' src/rtapi/uspace_rtapi_app.cc src/rtapi/rtapi_io.h src/rtapi/rtapi_pci.cc src/rtapi/rtai_ulapi.c
%endif

%build
cd src
autoreconf -ifv
%configure --disable-build-documentation \
           --enable-non-distributable=yes \
           --with-boost-python=boost_python39 \
           --disable-python \
           --without-libmodbus \
           %if %rtai == 1
           --with-realtime=/patch/to/rtai
           %else
           --with-realtime=uspace
           %endif
           
%make_build

%install
cd src
%make_install SITEPY=%python_sitelib
%ifarch x86_64 aarch64
mv %buildroot/usr/lib/* %buildroot/usr/lib64/
chmod -R +x %buildroot/usr/lib64/*
sed -i 's|/usr/lib/|/usr/lib64/|' %buildroot/usr/bin/%name
%endif
cd ..

mv %buildroot%_datadir/gtksourceview-2.0 %buildroot%_datadir/gtksourceview-3.0

%if %rtai == 1
    mv %buildroot%_sysconfdir/init.d/* %buildroot%_initdir
%else
    rm -fR %buildroot%_sysconfdir/init.d/*
%endif

install -d -m755 %buildroot%_datadir/applications
cp debian/extras/usr/share/applications/linuxcnc.desktop %buildroot%_datadir/applications
cp debian/extras/usr/share/applications/linuxcnc-latency.desktop %buildroot%_datadir/applications
cp debian/extras/usr/share/applications/linuxcnc-pncconf.desktop %buildroot%_datadir/applications
cp debian/extras/usr/share/applications/linuxcnc-stepconf.desktop %buildroot%_datadir/applications

#fix desktop categories
sed 's/X-CNC/Development;Engineering/' -i %buildroot%_datadir/applications/*

### == desktop file documentation
cat > %buildroot%_datadir/applications/%name-documentation.desktop << END
[Desktop Entry]
Name=LinuxCNC Documentation
Name[ru_RU]= Документация LinuxCNC 
Comment=LinuxCNC Documentation
Comment[ru_RU]=Документация LinuxCNC
Exec=%_bindir/xdg-open %_docdir/%name
Icon=linuxcncicon
Terminal=false
Type=Application
Categories=Development;Engineering;
END

#install rules
install -d -m755 %buildroot%_udevrulesdir
cp debian/extras/lib/udev/rules.d/* %buildroot%_udevrulesdir

for x in 16 32 48; do
    mkdir -p %buildroot%_datadir/icons/hicolor/$x'x'$x/apps
	convert linuxcncicon.png -resize $x'x'$x \
	        %buildroot%_datadir/icons/hicolor/$x'x'$x/apps/linuxcncicon.png
done
%find_lang %name
%find_lang gmoccapy

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_docdir}/linuxcnc/examples/sample-configs/sim/axis/vismach/VMC_toolchange/vmcgui
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/* %{buildroot}%{python_sitearch}/*.py %{buildroot}%{python_sitearch}/*/*.py
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{python_sitearch}/*.py %{buildroot}%{python_sitearch}/*/*.py

%files -f %name.lang 
%_bindir/*
%_libdir/%name
%_sysconfdir/%name
%if %rtai == 1
%_initdir/realtime
%endif
%_udevrulesdir/*.rules
%_datadir/applications/%{name}*.desktop
%exclude %_datadir/applications/%name-documentation.desktop
%_sysconfdir/X11/app-defaults/*
%_datadir/axis/tcl
%_datadir/%name/hallib
%_datadir/%name/ncfiles
%_libdir/*.so.*
%exclude %_libdir/*.a

%files data -f gmoccapy.lang
%_datadir/%name
%exclude %_datadir/%name/hallib
%exclude %_datadir/%name/ncfiles
%dir %_datadir/axis
%_datadir/axis/images
%_datadir/glade3
%_datadir/gmoccapy
%_datadir/gscreen
%_datadir/gtksourceview-3.0/*
%_datadir/icons/hicolor/*/*
%_mandir/man?/*
%_datadir/applications/%name-documentation.desktop
%_docdir/%name

%files -n tcl-%name
%_libdir/tcltk/%name

%files -n python-%name
%python_sitearch/*

%files devel
%_includedir/%name
%_libdir/*.so

%changelog
* Mon Jul 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.14
- Rebuilt for Fedora
* Fri Jul 22 2016 Anton Midyukov <antohami@altlinux.org> 2.7.5-alt1
- New version 2.7.5
- Fix repocop warning.
* Thu May 12 2016 Anton Midyukov <antohami@altlinux.org> 2.7.4-alt1.20160506.1
- Initial build for Alt Linux Sisyphus
