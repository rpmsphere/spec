%define oname YafaRay
# NOTE: Please update the version and rebuild this package if blender is updated:
%define blender_addons %{_datadir}/blender/2.83/scripts/addons/
%define addon_name %{name}_v3
# Disable automatic compilation of Python files in extra directories
%global _python_bytecompile_extra 0
%define __provides_exclude_from ^%{python3_sitearch}/.*\\.so|%{_libdir}/%{name}-plugins/.*\\.so

Name:           yafaray
Version:        3.4.4
Release:        2
Summary:        A free open-source raytracing render engine
Group:          Graphics/3D
License:        LGPLv2+
URL:            http://www.yafaray.org
Source0:        https://github.com/YafaRay/Core/archive/v%{version}/Core-%{version}.tar.gz
Source1:        https://github.com/YafaRay/Blender-Exporter/archive/v%{version}/Blender-Exporter-%{version}.tar.gz
Source2:        %{name}-blender.metainfo.xml
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  swig

# Name was changed in 2014
Provides:       yafray = %{version}

# libyafarayqt.so moved from Blender subpackage to main package
Conflicts:      yafaray-blender < 3.3.0-8

%description
YafaRay is a free open-source raytracing render engine.

Raytracing is a rendering technique for generating realistic images by
tracing the path of light through a 3D scene. A render engine consists of
a "faceless" computer program that interacts with a host 3D application
to provide very specific raytracing capabilities "on demand". Blender 3D
is the host application of YafaRay.

%package blender
Summary:        Blender integration scripts
Group:          Graphics/3D
License:        GPLv2+

Requires:       %{name} >= %{version}-%{release}
Requires:       blender

%description blender
YafRay uses a python-coded settings interface to set lighting and rendering
parameters. This settings interface is launched by an entry automatically
added to the Blender Render menu.

%prep
%autosetup -p1 -a 1 -n Core-%{version}

# Fix for python 3.6+
sed -i 's|3.5|%{python3_version}|' CMakeModules/FindYafPythonLibs.cmake src/bindings/CMakeLists.txt

# TODO: Patch to use LIB_SUFFIX and PR upstream
sed -i -e 's|set(YAF_LIB_DIR lib)|set(YAF_LIB_DIR %{_lib})|g' CMakeLists.txt
sed -i -e 's|set(YAF_TARGET_TYPE ARCHIVE DESTINATION ${CMAKE_INSTALL_PREFIX}/lib RUNTIME)|\
    set(YAF_TARGET_TYPE ARCHIVE DESTINATION ${CMAKE_INSTALL_PREFIX}/%{_lib} RUNTIME)|g' CMakeLists.txt

mv Blender-Exporter-%{version} %{addon_name}

# Fix setup for standalone + Blender install
sed -i -e "s|PLUGIN_PATH =.*|PLUGIN_PATH = os.path.join('%{_prefix}', '%{_lib}', '%{name}-plugins')|" %{addon_name}/__init__.py
sed -i -e "s|@YAFARAY_BLENDER_EXPORTER_VERSION@|%{version}|g" %{addon_name}/__init__.py

mv %{addon_name}/tests %{addon_name}_tests

%ifarch aarch64
sed -i 's|fsqrt(n)|sqrtf(n)|' include/utilities/mathOptimizations.h
%endif

%build
%cmake \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
    -DUSER_RELEASE_OPTIMIZATION_FLAGS="%{optflags} -O3 -ffast-math -pthread" \
    -DWITH_QT=ON \
    -DYAF_BINDINGS_PY_DIR=%{python3_sitearch} \
    -DYAF_PY_VERSION=%{python3_version}

%cmake_build

%install
%cmake_install

install -d %{buildroot}%{blender_addons}
cp -pr %{addon_name} %{buildroot}%{blender_addons}

# FIXME workaround for: https://github.com/K-3D/k3d/issues/15
ln -s %{_bindir}/%{name}-xml %{buildroot}%{_bindir}/yafray

install -D -m644 %{_sourcedir}/%{name}-blender.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo/%{name}-blender.metainfo.xml

# Let RPM pick docs in the file section
rm -rf %{buildroot}%{_docdir}/%{name}

# We don't ship those for now, it doesn't seem built to be used
# as a shared library.
rm -fr %{buildroot}%{_includedir}/%{name}

# Manually invoke the python byte compile macro for each path that needs byte
# compilation.
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/blender/

%files
%license LICENSES
%doc AUTHORS CHANGELOG README
%doc tests/*
%{_bindir}/yafray
%{_bindir}/%{name}-xml
%{_datadir}/%{name}/
%{_libdir}/%{name}-plugins/
%{_libdir}/libyafaray_v3_core.so
%{_libdir}/libyafaray_v3_plugin.so
%{_libdir}/libyafarayqt.so

%files blender
%doc %{addon_name}_tests/*
%{blender_addons}/%{addon_name}/
%{_datadir}/metainfo/%{name}-blender.metainfo.xml
%{python3_sitearch}/_yaf*.so
%{python3_sitearch}/yaf*.py*
%{python3_sitearch}/__pycache__/*

%changelog
* Tue Sep 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.4.4
- Rebuilt for Fedora
* Thu Jun 04 2020 daviddavid <daviddavid> 3.4.4-2.mga8
+ Revision: 1590320
- rebuild for new blender 2.83
* Sun May 10 2020 daviddavid <daviddavid> 3.4.4-1.mga8
+ Revision: 1582457
- new version: 3.4.4
* Sun May 03 2020 wally <wally> 3.4.0-2.mga8
+ Revision: 1578128
- rebuild for boost 1.73.0
* Sat Mar 28 2020 daviddavid <daviddavid> 3.4.0-1.mga8
+ Revision: 1561416
- new version: 3.4.0
* Wed Feb 19 2020 umeabot <umeabot> 3.3.0-21.mga8
+ Revision: 1544939
- Mageia 8 Mass Rebuild
+ daviddavid <daviddavid>
- rebuild for new blender 2.82
* Sun Jan 26 2020 wally <wally> 3.3.0-20.mga8
+ Revision: 1483453
- rebuild for boost 1.72.0
* Sat Jan 25 2020 daviddavid <daviddavid> 3.3.0-19.mga8
+ Revision: 1482893
- rebuild for new opencv 4.2.0
+ wally <wally>
- build with new cmake macros
* Sun Nov 24 2019 daviddavid <daviddavid> 3.3.0-18.mga8
+ Revision: 1462626
- rebuild for new blender 2.81
* Tue Sep 17 2019 daviddavid <daviddavid> 3.3.0-17.mga8
+ Revision: 1443138
- backport upstream fixes for python 3.8 compatibility
- rebuild fpr python3.8
* Tue Apr 02 2019 umeabot <umeabot> 3.3.0-16.mga7
+ Revision: 1385307
- Qt5 Rebuild
* Sat Mar 02 2019 daviddavid <daviddavid> 3.3.0-15.mga7
+ Revision: 1371029
- backport upstream patch to port to Qt5 (mga#24413)
- backport some others upstream fixes
* Thu Jan 10 2019 daviddavid <daviddavid> 3.3.0-14.mga7
+ Revision: 1354080
- rebuild for new Python 3.7
* Tue Oct 16 2018 wally <wally> 3.3.0-13.mga7
+ Revision: 1321117
- rebuild for new boost 1.68.0
* Tue Oct 16 2018 daviddavid <daviddavid> 3.3.0-12.mga7
+ Revision: 1320943
- rebuild for new ilmbase and openexr 2.3.0
* Sun Sep 23 2018 umeabot <umeabot> 3.3.0-11.mga7
+ Revision: 1302009
- Mageia 7 Mass Rebuild
* Tue Aug 07 2018 wally <wally> 3.3.0-10.mga7
+ Revision: 1248799
- add back pycache and bytecompile blender plugin .py files under /usr/share/blender 'manually'
* Thu Aug 02 2018 wally <wally> 3.3.0-9.mga7
+ Revision: 1246955
- build only on ix86 anf x86_64
* Mon Jul 23 2018 akien <akien> 3.3.0-8.mga7
+ Revision: 1244969
- Fix incorrect installation of Blender plugin
- Blender plugin is GPLv2+, not LGPLv2+
- Move Qt library to main package, it's not related to Blender plugin
- Package test scenes in doc folders
- Add metainfo file from Fedora
* Thu Jul 05 2018 daviddavid <daviddavid> 3.3.0-7.mga7
+ Revision: 1241785
- update files list (no more __pycache__ reference)
* Sun May 27 2018 wally <wally> 3.3.0-6.mga7
+ Revision: 1232433
- rebuild for openexr 2.2.1
* Thu Apr 12 2018 daviddavid <daviddavid> 3.3.0-5.mga7
+ Revision: 1218055
- rebuild for new opencv 3.4.1
* Sat Jan 13 2018 wally <wally> 3.3.0-4.mga7
+ Revision: 1192620
- build without -std=c++11
- rebuild for new ilmbase
* Mon Dec 25 2017 wally <wally> 3.3.0-3.mga7
+ Revision: 1184720
- rebuild for new boost
* Tue Nov 21 2017 tv <tv> 3.3.0-2.mga7
+ Revision: 1178107
- rebuild for boost 1.65
* Tue Oct 03 2017 daviddavid <daviddavid> 3.3.0-1.mga7
+ Revision: 1167699
- honor user OPTIMIZATION_FLAGS thus fixing empty debugsourcefiles.list
- new version: 3.3.0
- update Source URL
- switch to cmake and python3
- fix blender addons path
* Sat Feb 06 2016 umeabot <umeabot> 0.1.1-7.mga6
+ Revision: 941820
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 0.1.1-6.mga5
+ Revision: 748613
- Second Mageia 5 Mass Rebuild
* Sun Sep 28 2014 alexl <alexl> 0.1.1-5.mga5
+ Revision: 731445
- added symlink /usr/bin/yafray
* Tue Sep 16 2014 umeabot <umeabot> 0.1.1-4.mga5
+ Revision: 690815
- Mageia 5 Mass Rebuild
* Sun Aug 24 2014 luigiwalser <luigiwalser> 0.1.1-3.mga5
+ Revision: 667002
- rebuild for ilmbase and OpenEXR
* Thu May 01 2014 luigiwalser <luigiwalser> 0.1.1-2.mga5
+ Revision: 619157
- rebuild for ilmbase
* Wed Apr 16 2014 alexl <alexl> 0.1.1-1.mga5
+ Revision: 615318
- version 0.1.1 with blender integration
- rename yafray in yafaray
- rename yafray in yafaray
* Tue Apr 15 2014 alexl <alexl> 0.0.9-1.mga5
+ Revision: 615152
- imported package yafray
