Name:           ogre
Version:        1.8.1
Release:        23.1
Summary:        Object-Oriented Graphics Rendering Engine
# MIT with exceptions - main library
# CC-BY-SA - devel docs
# Freely redistributable without restriction - most of samples content
# MIT      - shaders for DeferredShadingMedia samples
# Public Domain - Some of the build files, samples and plugins
License:        MIT with exceptions and CC-BY-SA and Freely redistributable without restriction
Group:          System Environment/Libraries
URL:            http://www.ogre3d.org/
# This is modified http://downloads.sourceforge.net/ogre/ogre-v%(echo %{version} | tr . -).tar.bz2
# with non-free files striped (see ogre-make-clean.sh):
# Update local glew copy to 1.6.0
# - Non-free licensed headers under RenderSystems/GL/include/GL removed
# - Non-free chiropteraDM.pk3 under Samples/Media/packs removed
# - Non-free fonts under Samples/Media/fonts removed
# - Non-free textures under Samples/Media/materials/textures/nvidia
Source0:        %{name}-%{version}-clean.tar.bz2
Patch0:         ogre-1.7.2-rpath.patch
#Patch1:         ogre-1.6.0-system-glew.patch
# Upstream patch to GLEW applied to new version
Patch1:         ogre-1.6.0rc1-glew.patch
Patch2:         ogre-1.8.1-system-tinyxml.patch
Patch3:         ogre-1.7.2-fix-ppc-build.patch
Patch5:         ogre-1.8.1-build-rcapsdump.patch
Patch6:         ogre-thread.patch
Patch7:         ogre-1.8.1-dynlib-allow-no-so.patch
Patch8:         ogre-1.8.1-cmake-freetype.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  zziplib-devel freetype-devel
BuildRequires:  libXaw-devel libXrandr-devel libXxf86vm-devel libGLU-devel
BuildRequires:  ois-devel freeimage-devel openexr-devel
BuildRequires:  glew-devel
BuildRequires:  boost-devel
# BuildRequires:  poco-devel
BuildRequires:  tinyxml-devel
BuildRequires:  cmake
BuildRequires:  cppunit-devel

%description
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier and more
intuitive for developers to produce applications utilizing
hardware-accelerated 3D graphics. The class library abstracts all the
details of using the underlying system libraries like Direct3D and
OpenGL and provides an interface based on world objects and other
intuitive classes.

%package paging
Summary:        OGRE component for terrain paging
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description paging
Provides paging functionality. In essence it allows worlds to be rendered
and loaded at the same time.

%package property
Summary:        OGRE component for property introspection
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description property
OGRE's property system allows you to associate values of arbitrary type with
names, and have those values exposed via a self-describing interface.

%package rtss
Summary:        OGRE RT Shader System component
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description rtss
The Real Time Shader System, or RTSS for short, is a component of Ogre. This
component is used to generate shaders on the fly based on object material
properties, scene setup and other user definitions.

%package terrain
Summary:        OGRE component for terrain rendering
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description terrain
OGRE's terrain component provides rendering of terrain represented by
heightmaps.

%package utils
Summary:        OGRE production pipeline utilities
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}

%description utils
Contains OgreXMLConverter, it can take .mesh.xml files and convert them into
their binary variant.
Also provides OgreMeshUpgrader that can load old Ogre .mesh files and upgrade
them to the latest version.

%package devel
Summary:        Ogre header files and documentation
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-paging = %{version}-%{release}
Requires:       %{name}-property = %{version}-%{release}
Requires:       %{name}-rtss = %{version}-%{release}
Requires:       %{name}-terrain = %{version}-%{release}
Requires:       pkgconfig
# Requires:       poco-devel
Requires:       boost-devel
Requires:       cmake

%description devel
This package contains the header files for Ogre.
Install this package if you want to develop programs that use Ogre.


%package devel-doc
Summary:        Ogre development documentation
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildRequires:  doxygen

%description devel-doc
This package contains the Ogre API documentation and the Ogre development
manual. Install this package if you want to develop programs that use Ogre.


%package samples
Summary:        Ogre samples executables and media
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}, dejavu-sans-fonts

%description samples
This package contains the compiled (not the source) sample applications coming
with Ogre.  It also contains some media (meshes, textures,...) needed by these
samples. The samples are installed in %{_libdir}/Samples/*.so and can be run
using SampleBrowser.

%prep
%setup -q
%patch0 -p1 -z .rpath
%patch1 -p0 -z .glew
%patch2 -p1 -z .sys-tinyxml
%patch3 -p1 -z .ppc
%patch5 -p0 -z .build-rcapsdump
%patch6 -p0 -z .thread
%patch7 -p0 -z .dynlib-allow-no-so
%patch8 -p1 -z .cmake-freetype

# remove execute bits from src-files for -debuginfo package
chmod -x `find RenderSystems/GL -type f` \
  `find Samples/DeferredShading -type f` Samples/DynTex/src/DynTex.cpp
#  Samples/Common/bin/resources.cfg
# Remove spurious execute bits from some Media files
chmod -x `find Samples/Media/DeferredShadingMedia -type f`
# create a clean version of the api docs for %%doc
mkdir api
find . \( -wholename './Docs/api/html/*.html' -or \
  -wholename './Docs/api/html/*.gif' -or -wholename './Docs/api/html/*.png' \
  -or -wholename './Docs/api/html/*.css' \) -exec cp --target-directory='api' '{}' +
for i in api/OgreParticleEmitter_8h_source.html \
         api/classOgre_1_1ParticleSystem.html \
         api/classOgre_1_1DynLib.html \
         api/classOgre_1_1ParticleEmitter.html; do
  iconv -f ISO_8859-2 -t UTF8 $i > api/tmp
  touch -r $i api/tmp
  mv api/tmp $i
done
# Add mit.txt symlink for links in License.html
rm -r Docs/licenses/*
ln -s ../COPYING Docs/licenses/mit.txt
# remove included tinyxml headers to ensure use of system headers
rm Tools/XMLConverter/include/tiny*


%build
mkdir build
cd build
%cmake .. -DOGRE_FULL_RPATH=0 -DCMAKE_SKIP_RPATH=1 -DOGRE_LIB_DIRECTORY=%{_lib} -DOGRE_BUILD_RTSHADERSYSTEM_EXT_SHADERS=1 -DOGRE_BUILD_PLUGIN_CG=0
make %{?_smp_mflags}

%install
cd build
make DESTDIR=$RPM_BUILD_ROOT install

# Create config for ldconfig
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/OGRE" > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

# Install the samples
mkdir -p $RPM_BUILD_ROOT%{_libdir}/OGRE/Samples
install -p -m 644 lib/Sample_*.so $RPM_BUILD_ROOT%{_libdir}/OGRE/Samples
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/OGRE
for cfg in plugins.cfg quakemap.cfg resources.cfg samples.cfg; do
  install -p -m 644 inst/bin/release/$cfg \
    $RPM_BUILD_ROOT%{_sysconfdir}/OGRE/
done

# Swap out reference to non-free quake map that was removed
cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/OGRE/quakemap.cfg
Archive: /usr/share/OGRE/media/packs/ogretestmap.zip 
Map: ogretestmap.bsp
EOF

# Fixing bug with wrong case for media
mv ../Samples/Media/PCZAppMedia/ROOM_NY.mesh ../Samples/Media/PCZAppMedia/room_ny.mesh
mv ../Samples/Media/PCZAppMedia/ROOM_PY.mesh ../Samples/Media/PCZAppMedia/room_py.mesh
install -p -m 755 bin/SampleBrowser $RPM_BUILD_ROOT%{_bindir}/SampleBrowser

mkdir -p $RPM_BUILD_ROOT%{_datadir}/OGRE/
cp -a ../Samples/Media $RPM_BUILD_ROOT%{_datadir}/OGRE/media
rm -f $RPM_BUILD_ROOT%{_datadir}/OGRE/media/CMakeLists.txt

ln -s ../../../../fonts/dejavu/DejaVuSans-Bold.ttf \
  $RPM_BUILD_ROOT%{_datadir}/OGRE/media/fonts/bluebold.ttf
ln -s ../../../../fonts/dejavu/DejaVuSans.ttf \
  $RPM_BUILD_ROOT%{_datadir}/OGRE/media/fonts/bluehigh.ttf
ln -s ../../../../fonts/dejavu/DejaVuSansCondensed.ttf \
  $RPM_BUILD_ROOT%{_datadir}/OGRE/media/fonts/bluecond.ttf
ln -s ../../../../fonts/dejavu/DejaVuSans.ttf \
  $RPM_BUILD_ROOT%{_datadir}/OGRE/media/fonts/solo5.ttf

# cmake macros should be in the cmake directory, not an Ogre directory
mkdir -p $RPM_BUILD_ROOT%{_datadir}/cmake/Modules
mv $RPM_BUILD_ROOT%{_libdir}/OGRE/cmake/* $RPM_BUILD_ROOT%{_datadir}/cmake/Modules

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING
%doc Docs/ChangeLog.html Docs/License.html Docs/licenses Docs/ReadMe.html Docs/style.css Docs/ogre-logo*.gif
%{_libdir}/libOgreMain.so.*
%{_libdir}/OGRE

%{_datadir}/OGRE
%dir %{_sysconfdir}/OGRE
%exclude %{_bindir}/SampleBrowser
%exclude %{_libdir}/OGRE/Samples
%exclude %{_libdir}/OGRE/cmake
%exclude %{_datadir}/OGRE/media
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/*

%files paging
%defattr(-,root,root,-)
%{_libdir}/libOgrePaging.so.*

%files property
%defattr(-,root,root,-)
%{_libdir}/libOgreProperty.so.*

%files rtss
%defattr(-,root,root,-)
%{_libdir}/libOgreRTShaderSystem.so.*

%files terrain
%defattr(-,root,root,-)
%{_libdir}/libOgreTerrain.so.*

%files utils
%defattr(-,root,root,-)
%{_bindir}/OgreMeshUpgrader
%{_bindir}/OgreXMLConverter
%{_bindir}/rcapsdump

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*Ogre*.so
%{_datadir}/cmake/Modules/*
%{_includedir}/OGRE
%{_libdir}/pkgconfig/*.pc

%files devel-doc
%defattr(-,root,root,-)
%doc api Docs/manual Docs/shadows Docs/vbo-update Docs/style.css

%files samples
%defattr(-,root,root)
%{_bindir}/SampleBrowser
%{_libdir}/OGRE/Samples
%{_datadir}/OGRE/media
%{_sysconfdir}/OGRE/plugins.cfg
%{_sysconfdir}/OGRE/quakemap.cfg
%{_sysconfdir}/OGRE/resources.cfg
%{_sysconfdir}/OGRE/samples.cfg


%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.8.1-11
- Rebuild for boost 1.55.0
- Fix detection of libfreetype (ogre-1.8.1-cmake-freetype.patch)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 1.8.1-9
- Update ogre-thread.patch to exclude -mt suffix from Boost.Thread and
  Boost.System DSO's.

* Sat Jul 27 2013 Petr Machata <pmachata@redhat.com> - 1.8.1-8
- Rebuild for boost 1.54.0

* Sat Apr 20 2013 Bruno Wolff III <bruno@wolff.to> - 1.8.1-7
- cmake scripts need to be at the top level
- Fix MODULES/Modules oops

* Sat Apr 20 2013 Bruno Wolff III <bruno@wolff.to> - 1.8.1-6
- Avoid opening plugins twice

* Sat Apr 20 2013 Bruno Wolff III <bruno@wolff.to> - 1.8.1-5
- Allow for plugin names to not end in .so - bz 573672
- Put cmake files in cmake directory instead of an Ogre directory

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.8.1-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.8.1-3
- Rebuild for Boost-1.53.0

* Sun Dec 09 2012 Bruno Wolff III <bruno@wolff.to> - 1.8.1-2
- Consuming packages using threads need to link to boost_system-mt

* Fri Nov 30 2012 Martin Preisler <mpreisle@redhat.com> - 1.8.1-1
- Update to upstream 1.8.1

* Fri Nov 30 2012 Martin Preisler <mpreisle@redhat.com> - 1.8.0-1
- Update to upstream 1.8.0
- Split the components into a subpackages
- Split utils into a subpackage
- Put cmake modules into the -devel subpackage

* Tue Oct 02 2012 Jon Ciesla <limburgher@gmail.com> - 1.7.4-5
- Fix FTBFS on ARM, based on debian's patch.

* Fri Aug 10 2012 Bruno Wolff III <bruno@wolff.to> - 1.7.4-4
- Fix for boost 1.50

* Sat Jul 21 2012 Bruno Wolff III <bruno@wolff.to> - 1.7.4-3
- Fix issue with utilSSE hack breaking under gcc 4.7 (bug 842041)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 01 2012 Bruno Wolff III <bruno@wolff.to> - 1.7.4-1
- Update to upstream 1.7.4
- This is a minor bugfix update from 1.7.3

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-6
- Rebuilt for c++ ABI breakage

* Tue Jan 17 2012 Bruno Wolff III <bruno@wolff.to> - 1.7.3-5
- Rebuild for ois 1.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.3-3
- Rebuild for boost soname bump

* Fri Jul 22 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.3-2
- Rebuild for boost 1.47

* Sat May 14 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.3-1
- Upstream update to 1.7.3
- Changelog at http://www.ogre3d.org/2011/05/08/ogre-1-7-3-cthugha-released#more-1284

* Mon Apr 04 2011 Jon Ciesla <limb@jcomserv.net> - 1.7.2-14
- Re-rebuilding for boost 1.46.1, 2011-03-15 rebuild got 1.46.0.

* Tue Mar 15 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-13
- Rebuild for boost 1.46.1 update

* Sun Mar 06 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-12
- Fix broken pkgconfig files

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-10
- With ogre 1.7, cegui is no longer a build dependency.

* Sun Feb 06 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-9
- Rebuild for boost soname bump.

* Tue Jan 11 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-8
- Fix config for replacement for quake map.

* Mon Jan 10 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-7
- Exclude CMakeLists.txt from Media
- Install Samples media where Ogre expects it.
- Ogre expects the *.cfg files in /etc/OGRE

* Fri Jan 07 2011 Tom Callaway <spot@fedoraproject.org> - 1.7.2-6
- BuildRequires: boost-devel for threading, Remove poco-devel from BR

* Wed Jan 05 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-5
- Drop ttb requirement entirely.

* Wed Jan 05 2011 Dan Horák <dan[at]danny.cz> - 1.7.2-4
- tbb is available only on selected architectures

* Wed Jan 05 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-3
- Use SampleBrowser instead of out of date ogre-samples script

* Mon Jan 03 2011 Bruno Wolff III <bruno@wolff.to> - 1.7.2-2
- ogre-devel requires poco-devel to make sure references to poco headers works.

* Tue Dec 21 2010 Tom Callaway <spot@fedoraproject.org> - 1.7.2-1
- move to 1.7.2

* Sat Nov 28 2009 Bruno Wolff III <bruno@wolff.to> - 1.6.4-5
- Get upstream fixes since 1.6.4 release. This includes a couple of crash bugs.

* Mon Nov 23 2009 Bruno Wolff III <bruno@wolff.to> - 1.6.4-4
- Allow CEGIUOgreRenderer to find needed libraries

* Sat Nov 21 2009 Bruno Wolff III <bruno@wolff.to> - 1.6.4-3
- Spec file cleanups

* Tue Nov 17 2009 Bruno Wolff III <bruno@wolff.to> - 1.6.4-2
- Rebuild for ois 1.2

* Mon Sep 28 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.6.4-1
- New upstream release 1.6.4

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 16 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.6.2-1
- New upstream release 1.6.2
- Exceptions added to License
- Reenabling OpenEXR plugin, as it fixed now

* Fri Mar 06 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.6.1-5
- Add licenses of samples to License tag

* Mon Mar 02 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.6.1-4
- Update Ogre-Samples to work properly without CgProgramManager plugin

* Fri Feb 27 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.6.1-3
- Fixing PPC build

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 10 2009 Alexey Torkhov <atorkhov@gmail.com> 1.6.1-1
- New upstream release 1.6.1

* Tue Jan 20 2009 Hans de Goede <hdegoede@redhat.com> 1.6.0-5
- Adjust font requires for font rename (rh 480465)

* Sat Jan 10 2009 Hans de Goede <hdegoede@redhat.com> 1.6.0-4
- use regular (full) instead of lgc dejavu fonts for the demos (rh 477434)

* Sat Dec 27 2008 Hans de Goede <hdegoede@redhat.com> 1.6.0-3
- Remove non-free fonts from samples subpackage (rh 477434)

* Wed Dec  3 2008 Hans de Goede <hdegoede@redhat.com> 1.6.0-2
- Rebuild for new cegui

* Thu Nov 06 2008 Alexey Torkhov <atorkhov@gmail.com> 1.6.0-1
- New upstream release 1.6.0
- Updated samples running script
- Removed non-free quake map from samples media
- Added docs license in License tag

* Sat Sep 21 2008 Alexey Torkhov <atorkhov@gmail.com> 1.6.0-0.1.rc1
- New upstream release 1.6.0rc1
- Disabling broken OpenEXR plugin, it is not updated for long time and doesn't
  compile. FreeImage now have EXR support
- Updated private GLEW sources to 1.5.0 due to license issues and compiling
  against it instead of system ones, as it is patched by upstream

* Fri Jul 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.9-2
- Rebuild for new cegui

* Wed Jul  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.9-1
- New upstream release 1.4.9

* Thu May 22 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.8-2
- Rebuild for new cegui
- Use system tinyxml (bz 447698)

* Tue May 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.8-1
- New upstream release 1.4.8
- Warning as always with a new upstream ogre release this breaks the ABI
  and changes the soname!

* Sun Mar 30 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.7-2
- Switch to freeimage as imagelibrary, as upstream is abandoning DevIL support
  (bz 435399)
- Enable the openexr plugin

* Sun Mar 16 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.7-1
- New upstream release 1.4.7
- Warning as always with a new upstream ogre release this breaks the ABI
  and changes the soname!

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.6-5
- Autorebuild for GCC 4.3

* Thu Jan 24 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-4
- Install 2 additional header files for ogre4j (bz 429965)

* Tue Jan 22 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-3
- Rebuild for new glew

* Sat Jan 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-2
- Oops I just found out that ogre contains private copies of GL and GLEW
  headers, which fall under the not 100% SGI Free Software B and GLX Public
  License licenses, remove these (even from the tarbal!) and use the system
  versions instead

* Sat Dec 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-1
- New upstream release 1.4.6
- Warning as always with a new upstream ogre release this breaks the ABI
  and changes the soname!

* Wed Nov 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.5-3
- Fix building of ogre with an older version of ogre-devel installed
  (bz 382311)

* Mon Nov 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.5-2
- Ogre-Samples now takes the name of which samples to run as arguments, if no
  arguments are provided, it will run all of them like it used too (bz 377011)
- Don't install a useless / broken plugins.cfg in the Samples folder,
  Ogre-Samples will generate a correct one when run (bz 377011)

* Mon Oct  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.5-1
- New upstream release 1.4.5

* Fri Sep 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.4-1
- New upstream release 1.4.4 (bz 291481)

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.2-2
- Update License tag for new Licensing Guidelines compliance

* Sat Jun 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.2-1
- New upstream release 1.4.2
- Warning as always with a new upstream ogre release this breaks the ABI
  and changes the soname!
- Warning this release also breaks the API!

* Thu May 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.5-2
- Fix building on ppc64

* Fri Feb 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.5-1
- New upstream release 1.2.5

* Fri Jan 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.3-2
- Rebuild for new cairomm
- Added a samples sub-package (suggested by Xavier Decoret)

* Fri Oct 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.3-1
- New upstream release 1.2.3
- Warning as always with a new upstream ogre release this breaks the ABI
  and changes the soname!

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.2-2.p1
- FE6 Rebuild

* Thu Jul 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.2-1.p1
- New upstream release 1.2.2p1
- Drop integrated char_height patch
- Drop ogre-1.2.1-visibility.patch since this is fixed with the latest gcc
  release, but keep it in CVS in case things break again.
- Add a patch that replaces -version-info libtool argument with -release,
  which results in hardcoding the version number into the soname. This is
  needed because upstream changes the ABI every release, without changing the
  CURRENT argument passed to -version-info .
- Also add -release when linking libCEGUIOgreRenderer.so as that was previously
  unversioned.

* Tue Jul 18 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.1-3
- Add ogre-1.2.1-visibility.patch to fix issues with the interesting new
  gcc visibility inheritance.

* Fri Jul  7 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.1-2
- Make -devel package Requires on the main package fully versioned.
- Move libOgrePlatform.so out of %%{_libdir} and into the OGRE plugins dirs as
  its not versioned and only used through dlopen, so its effectivly a plugin.  

* Thu Jun 15 2006 Hans de Goede 1.2.1-1
- Initial FE packaging attempt, loosely based on a specfile created by
  Xavier Decoret <Xavier.Decoret@imag.fr>
