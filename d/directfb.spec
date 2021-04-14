%global major_ver 1.6
%global minor_ver .3

Summary: Graphics abstraction library for the Linux Framebuffer Device
Name: directfb
Version: %{major_ver}%{minor_ver}
Release: 6.1
Group: System Environment/Libraries
License: LGPLv2+
URL: http://www.directfb.org/
Source0: http://www.directfb.org/downloads/Core/DirectFB-%{major_ver}/DirectFB-%{version}.tar.gz
Source1: 85-directfb.rules
Patch2: DirectFB-1.5.3-fix_v4l1.patch
Patch3: DirectFB-1.6.1-lm.patch
Patch4: DirectFB-1.6.1-gcc-atomics-on-arm.patch
Patch5: DirectFB-1.5.3-add-missing-davinci-files.patch
Patch6: DirectFB-1.5.3-vdpau.patch
Patch8: DirectFB-1.6.1-mesa-libgbm-stridefix.patch
Patch9: DirectFB-1.6.1-FusionID-fix-git21c3684.patch

BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: libjpeg-devel
BuildRequires: libmng-devel
BuildRequires: freetype-devel
%{?_with_sdl:BuildRequires: SDL-devel}
BuildRequires: libdrm-devel
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: libsysfs-devel
BuildRequires: libv4l-devel
BuildRequires: libvdpau-devel
BuildRequires: libvncserver-devel
%{?_with_fusion:BuildRequires: linux-fusion-devel}
%{?_with_fusion:Requires: linux-fusion}
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGLES-devel
%if 0%{?fedora} >= 17
BuildRequires: mesa-libgbm-devel
%endif
BuildRequires: tslib-devel

%description
DirectFB is a thin library that provides hardware graphics acceleration,
input device handling and abstraction, integrated windowing system with
support for translucent windows and multiple display layers on top of the
Linux Framebuffer Device.

It is a complete hardware abstraction layer with software fallbacks for
every graphics operation that is not supported by the underlying hardware.
DirectFB adds graphical power to embedded systems and sets a new standard
for graphics under Linux.

Non-default rpmbuild options:
--with fusion:   Enable linux-fusion support
--with sdl:      Enable SDL experimental support

%package devel
Summary: Development files for DirectFB
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: zlib-devel
Requires: libsysfs-devel
%{?_with_fusion:Requires: linux-fusion-devel}

%description devel
Development files for DirectFB.

%prep
%setup -q -n DirectFB-%{version}
%patch2 -p1 -b .fix_v4l1
%patch3 -p1 -b .lm
%patch4 -p1 -b .arm-atomics
%patch5 -p1 -b .davinci
%patch6 -p1 -b .vdpau
%if 0%{?fedora} >= 18
#patch8 -p1 -b .stride
%endif
%patch9 -p1 -b .fusionID

#Disable ppc asm since compilation fails (and it seems better to use glibc)
sed -i.noppcasm -e 's/want_ppcasm=yes/want_ppcasm=no/'g configure.in configure

# Fix file-not-utf8
for i in ChangeLog README NEWS AUTHORS ; do
cp -pr $i $i.not-utf8
iconv -f ISO_8859-1 -t UTF8 $i.not-utf8 > $i
touch -r $i.not-utf8 $i
rm $i.not-utf8
done

#Remove old headers
rm interfaces/IDirectFBVideoProvider/{videodev.h,videodev2.h}

%build
%configure \
    --with-gfxdrivers=all \
%{?_with_sdl:--enable-sdl} \
    --enable-zlib \
%{?_with_fusion:--enable-multi} \
    --enable-unique \
    --enable-video4linux2 \
    --with-tests

# Remove rpath for 64bit
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

#Fix some relative fonts for dfbinspector.c
ln -s ../fonts/dejavu/DejaVuSans.ttf %{buildroot}%{_datadir}/%{name}-%{version}/decker.ttf

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/dfbfx
%{_bindir}/dfbg
%{_bindir}/dfbdump
%{_bindir}/dfbinfo
%{_bindir}/dfbinput
%{_bindir}/dfblayer
%{_bindir}/dfbpenmount
%{_bindir}/dfbscreen
## new with 1.2.0
%{_bindir}/dfbinspector
## new with 1.2.6
%{_bindir}/dfbmaster
#{_bindir}/dfbsummon
%{_bindir}/mkdfiff
%{_bindir}/mkdgiff
# uwmdump Unique WM
%{_bindir}/uwmdump
## New with 1.4.3
%{_bindir}/coretest_blit2
%{_bindir}/dfbtest_blit2
%{_bindir}/dfbtest_mirror
%{_bindir}/dfbtest_window_flip_once
## New with 1.4.1
%{_bindir}/dfbtest_blit
%{_bindir}/dfbtest_reinit
%{_bindir}/dfbtest_scale
%{_bindir}/dfbtest_sync
%{_bindir}/dfbtest_window
%{_bindir}/direct_stream
%{_bindir}/direct_test
%{_bindir}/fusion_fork
%{_bindir}/fusion_reactor
%{_bindir}/fusion_skirmish
%{_bindir}/fusion_stream
%{_bindir}/pxa3xx_dump
## New with 1.4.11
%{_bindir}/dfbtest_fillrect
%{_bindir}/dfbtest_font
%{_bindir}/fusion_call
%{_bindir}/mkdgifft
#New with 1.5.0
%{_bindir}/dfbtest_init
%{_bindir}/dfbtest_water
%{_bindir}/dfbtest_windows_watcher
# Dropped in 1.6
# %{_bindir}/fluxcomp
%{_bindir}/fusion_call_bench
#New with 1.5.3
%ifarch %{arm}
%{_bindir}/c64xdump
%endif
%{_bindir}/dfbtest_stereo_window
%{_bindir}/dfbtest_gl1
%{_bindir}/dfbtest_gl2
%{_bindir}/dfbtest_gl3
# New with 1.6
%{_bindir}/dfbtest_blit_multi
%{_bindir}/dfbtest_clipboard
%{_bindir}/dfbtest_flip
%{_bindir}/dfbtest_input
%{_bindir}/dfbtest_old_gl2
%{_bindir}/dfbtest_prealloc
%{_bindir}/dfbtest_resize
%{_bindir}/dfbtest_scale_nv21
%{_bindir}/dfbtest_surface_compositor
%{_bindir}/dfbtest_surface_updates
%{_bindir}/dfbtest_video
%{_bindir}/dfbtest_waitserial
%{_bindir}/dfbtest_window_cursor
%{_bindir}/dfbtest_window_flip
%{_bindir}/dfbtest_window_surface
# New with 1.6.3
%{_bindir}/dfbdumpinput
%{_bindir}/dfbtest_blit_threads
%{_bindir}/dfbtest_surface_compositor_threads
%ifarch %{arm}
%{_libdir}/libdavinci_c64x.so.*
%endif
%{_libdir}/libdirectfb-*.so.*
%{_libdir}/libdirect-*.so.*
%{_libdir}/libfusion-*.so.*
%{_libdir}/libuniquewm*.so.*
%{_libdir}/directfb-%{major_ver}-0/
%{_datadir}/directfb-%{version}/
%{_mandir}/man1/dfbg.1*
%{_mandir}/man5/directfbrc.5*
%{_sysconfdir}/udev/rules.d/85-directfb.rules

%files devel
%defattr(-,root,root,-)
%doc docs/html/*.html docs/html/*.png
%exclude %{_bindir}/directfb-config
%{_bindir}/directfb-csource
%{_includedir}/directfb/
%{_includedir}/directfb-internal/
%{_libdir}/pkgconfig/direct.pc
%{_libdir}/pkgconfig/directfb.pc
%{_libdir}/pkgconfig/directfb-internal.pc
%{_libdir}/pkgconfig/fusion.pc
%ifarch %{arm}
%{_libdir}/libdavinci_c64x.so
%endif
%{_libdir}/libdirectfb.so
%{_libdir}/libdirect.so
%{_libdir}/libfusion.so
%{_libdir}/libuniquewm.so
%{_mandir}/man1/directfb-csource.1*

%changelog
* Thu Jan 02 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.3
- Rebuilt for Fedora
* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.6.2-3
- rebuild due to "jpeg8-ABI" feature drop
* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.6.2-2
- rebuild against new libjpeg
* Sat Sep 22 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.6.2-1
- Update to 1.6.2
* Mon Sep 17 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.6.1-2
- Drop vt tweak
- Change BR to pkgconfig(glu)
* Mon Sep 17 2012 Tom Callaway <spot@fedoraproject.org> - 1.6.1-1
- update to 1.6.1
- include udev rules
* Thu Aug 30 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.5.3-9
- Fix vdpau plugin - rhbz#852740
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Sat May 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.5.3-7
- Add ARM atomics patch to fix compilation on ARMv5tel
* Fri Apr 27 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.5.3-6
- Backport fix for ARM
* Thu Apr 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.5.3-5
- Fix rhbz#781874 - MMX is selectable at runtime
* Sat Jan 14 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.5.3-4
- Fix build with libpng 1.5 (patch from Gentoo).
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.5.3-2
- Rebuild for new libpng
* Fri Aug 19 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.5.3-1
- Update to 1.5.3
- Add BR libvdpau-devel
- Add BR mesa-{EGL,GLU,GLES}-devel libdrm-devel
- Fix asm on %%{ix86}
- Remove v4l internal headers
- Remove autoreconf call
* Sun Aug 07 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.5.2-1
- Update to 1.5.2
* Sun Jul 17 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.5.1-1
- Update to 1.5.1
* Thu Jul 14 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.5.0-1
- Update to 1.5.0
- Drop not upstreamed libv4l patches
* Wed Nov 24 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.4.11-1
- Update to 1.4.11
* Mon Apr 19 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3
* Mon Aug 31 2009 kwizart < kwizart at gmail.com > - 1.4.2-3
- Update to 1.4.2
- Add dfbtest_sync and pxa3xx_dump
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Thu Jul 16 2009 kwizart < kwizart at gmail.com > - 1.4.1-1
- Update to 1.4.1
* Mon Jun 30 2009 kwizart < kwizart at gmail.com > - 1.4.0-1
- Update to 1.4.0
- Add BR libGL-devel
* Mon Jun 30 2009 kwizart < kwizart at gmail.com > - 1.2.8-4
- Built with tslib
* Mon May 11 2009 kwizart < kwizart at gmail.com > - 1.2.8-3
- Improve tty patch
- Conditionalize SDL experimental support.
* Thu May  7 2009 kwizart < kwizart at gmail.com > - 1.2.8-2
- Change default tty to tty1
* Tue Apr 21 2009 kwizart < kwizart at gmail.com > - 1.2.8-1
- Update to 1.2.8
- Disable mmx/sse on x86
* Thu Feb 12 2009 kwizart < kwizart at gmail.com > - 1.2.7-3
- Force autoreconf + re tag
* Tue Jan 20 2009 kwizart < kwizart at gmail.com > - 1.2.7-1
- Update to 1.2.7
- Fix decker.ttf path
- Add libv4l2 support
- Fix doc encoding
* Wed Oct 22 2008 kwizart < kwizart at gmail.com > - 1.2.6-3
- Disable the sorelease downgrade
- Exclude directfb-config - Fix multiarch conflicts #341011.
* Mon Oct 20 2008 kwizart < kwizart at gmail.com > - 1.2.6-2
- Disable ppc asm
- Drop the asm/type.h patch (fixed upstream)
* Mon Sep 29 2008 kwizart < kwizart at gmail.com > - 1.2.6-1
- Update to 1.2.6
* Wed Jul 16 2008 kwizart < kwizart at gmail.com > - 1.2.0-1
- Update to 1.2.0 (final)
- Add BR libvncserver-devel
- Enable Unique WM
- Enabled multi (Requires linux-fusion kernel module)
* Sat Jun 21 2008 kwizart < kwizart at gmail.com > - 1.2.0-0.1.rc1
- Update to 1.2.0-rc1
* Sat Jun 21 2008 kwizart < kwizart at gmail.com > - 1.1.1-1
- Update to 1.1.1
- Add --enable-multi 
* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 1.0.0-3
- Rebuild for new BuildID feature.
* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 1.0.0-2
- Update License field.
* Mon Apr  9 2007 Matthias Saou <http://freshrpms.net/> 1.0.0-1
- Update to 1.0.0 final.
- No longer disable MMX on x86_64, it builds again.
- Disable /usr/lib64 rpath on 64bit.
* Fri Feb  2 2007 Matthias Saou <http://freshrpms.net/> 1.0.0-0.1.rc3
- Update to 1.0.0-rc3.
* Wed Jan 17 2007 Matthias Saou <http://freshrpms.net/> 1.0.0-0.1.rc2
- Update to 1.0.0-rc2.
- Include sysfs patch from Eric Moret (#204568).
- Require sysfs devel package in the devel sub-package.
- Spec file cleanup.
- Update asmtypes patch, required to get this rc2 to build.
- Disable MMX on x86_64 since some asm code fails to build otherwise.
- No longer pass an explicit list of drivers to configure since default is all.
* Thu Oct 19 2006 Matthias Saou <http://freshrpms.net/> 1.0.0-0.1.rc1
- Update to 1.0.0-rc1.
- Include the new mkdfiff program (DirectFB Fast Image File Format).
* Thu Sep 14 2006 Matthias Saou <http://freshrpms.net/> 0.9.25.1-3
- FC6 rebuild.
- Remove gcc-c++ build requirement, it's a default now.
- End directory lines in %%files with slashes to identify them more easily.
- Add types patch to fix 64bit build on FC6.
- Add linux-compiler patch to remove obsolete kernel header include.
- Add ppc patch to remove other obsolete kernel header include.
* Sun Jun 09 2006 Warren Togami <wtogami@redhat.com> 0.9.25.1-2
- buildreq sysfsutils-devel became libsysfs-devel
* Sat May 13 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.25.1-1
- new upstream version
* Sun Mar 05 2006 Thomas Vander Stichele <thomas at apestaart dot org> 0.9.24-5
- rebuild for fedora extras 5
* Fri Nov 25 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.24-4
- Merge FC-4 and devel specfiles for easier maintainance and consistence.
- Incorperate improvements suggested by Ville Skyttä in bug 162358.
* Thu Nov 24 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.24-3
- Remove "remove custom CFLAGS" patch, this only adds -ffast-math,
  which IMHO is unlikely to be the cause of the build problems, especially
  since a local x86_64 mockbuild works fine. Try to build it hoping that the
  real cause is gone now, since Dan's build did succeed.
* Tue Nov 15 2005 Dan Williams <dcbw@redhat.com> 0.9.24-2
- Try removing custom CFLAGS to see if build makes it through x86_64
* Sun Nov 13 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.24-1
- 0.9.22 Has build troubles on PPC, upgrade to 0.9.24 which will most
  likely fix this (Only a build will tell for sure).
- Re-enable sis315 since this is fixed in 0.9.24, add r200.
* Mon Oct 17 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.22-2.fc5
- increase release field to be equal to FC4 release field, to avoid upgrade
  problems.
- force rebuild since directfb is missing from extra-devel repository.
* Thu Jun 30 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.22-2.fc4
- increment release because of new source upload
* Tue Jun 19 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.22-1.fc5
- incorporate changes from Ville
- update to new upstream release
* Wed Jun 15 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.22-1.fc4
- new upstream release
- add libdirect and libfusion shared libraries
* Fri Dec 31 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.21-0.fdr.1
- new upstream release
- added new binaries and libraries
- remove epochs
* Fri Jan 02 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0:0.9.20-0.fdr.1: new version
* Sat Sep 13 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0:0.9.18-0.fdr.3:
  - readd epochs
  - disable sse, make mmx optional
* Tue Aug 19 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.18-0.fdr.2:
  - incorporated Anvil's suggestions
* Sun Jul 06 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.18-0.fdr.1: initial rpm release
