%global		snap r9671

Summary:	C++ user interface toolkit
Name:		fltk13
Version:	1.3.0
Release:	15.1
# see COPYING (or http://www.fltk.org/COPYING.php ) for exceptions details
License:	LGPLv2+ with exceptions	
Group:		System Environment/Libraries
URL:		http://www.fltk.org/
%if "%{?snap:1}" == "1"
Source0:        http://ftp.easysw.com/pub/fltk/snapshots/fltk-1.3.x-%{snap}.tar.bz2
%else
Source0:	http://ftp.easysw.com/pub/fltk/%{version}%{?pre}/fltk-%{version}%{?pre}-source.tar.gz
%endif
Source1: fltk-config.sh
## FIXME/TODO: upstream these asap -- Rex
Patch1:        	fltk-1.1.9-fltk_config.patch 
# libfltk_gl.so had undefined symbols
Patch3: 	fltk-1.1.x-r5750-undefined.patch
Patch5: 	fltk-1.1.8-fluid_desktop.patch
Patch8:         fltk-1.3.0-rh708185.patch
# http://www.fltk.org/str.php?L2599
Patch9:         fltk-1_v4.3.x-keyboard-x11.patch
# http://www.fltk.org/str.php?L2636
Patch10:        fltk-1_v2.3.x-clipboard.patch
Patch11:        fltk-1_v2.3.x-clipboard-x11.patch
Patch12:        fltk-1_v3.3.x-clipboard-xfixes.patch
# http://www.fltk.org/str.php?L2660
Patch13:        fltk-1_v4.3.x-cursor.patch
Patch20:        fltk-1_v4.3.x-cursor-abi.patch
# http://www.fltk.org/str.php?L2859
Patch14:        fltk-1.3.x-resize-expose.patch
# http://www.fltk.org/str.php?L2659
Patch15:        pixmap.patch
# http://www.fltk.org/str.php?L2802
Patch16:        fltk-1_v2.3.0-modal.patch
# http://www.fltk.org/str.php?L2816
Patch17:        fltk-1_v2.3.0-icons.patch
# http://www.fltk.org/str.php?L2860
Patch18:        fltk-1.3.x-screen_num.patch
Patch19:        fltk-1_v2.3.x-multihead.patch
BuildRequires: desktop-file-utils
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(gl) pkgconfig(glu) 
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(sm) 
BuildRequires: pkgconfig(xext) pkgconfig(xinerama) pkgconfig(xft) pkgconfig(xt) pkgconfig(x11) 
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xproto)
BuildRequires: xorg-x11-utils
BuildRequires: zlib-devel
BuildRequires: autoconf
#Provides: fltk = %{version}

%description
FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit.
It provides modern GUI functionality without the bloat, and supports
3D graphics via OpenGL and its built-in GLUT emulation.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: libstdc++-devel
Requires: pkgconfig(ice) pkgconfig(sm)
Requires: pkgconfig(xft) pkgconfig(xt) pkgconfig(x11)
#Provides: fltk-devel = %{version}

%description devel
%{summary}.

%package static
Summary: Static libraries for %{name}
Requires: %{name}-devel = %{version}-%{release}
#Provides: fltk-static = %{version}

%description static
%{summary}.

%package fluid
Summary: Fast Light User Interface Designer
Requires: %{name} = %{version}-%{release}
Requires: %{name}-devel
#Provides: fltk-fluid = %{version}

%description fluid
%{summary}, an interactive GUI designer for %{name}. 

%prep
%if 0%{?snap:1}
%setup -q -n fltk-1.3.x-%{snap}
%else
%setup -q  -n fltk-%{version}%{?pre}
%endif

%patch1 -p1 -b .fltk_config
%patch3 -p1 -b .undefined
%patch5 -p1 -b .fluid_desktop
%patch8 -p1 -b .rh708185
%patch9 -p1 -b .deadkeys
%patch10 -p1 -b .clipboard1
%patch11 -p1 -b .clipboard2
%patch12 -p1 -b .clipboard3
%patch13 -p1 -b .cursor
%patch20 -p1 -b .cursor-abi
%patch14 -p1 -b .resize-expose
%patch15 -p0 -b .pixmap
%patch16 -p1 -b .modal
%patch17 -p1 -b .icons
%patch18 -p1 -b .screen_num
%patch19 -p1 -b .multihead

# verbose build output
sed -i.silent '\,^.SILENT:,d' makeinclude.in

%build
# using --with-optim, so unset CFLAGS/CXXFLAGS
export CFLAGS="-fPIC -fpermissive"
export CXXFLAGS="-fPIC -fpermissive"

%configure \
  --with-links \
  --with-optim="%{optflags}" \
  --enable-largefile \
  --enable-shared \
  --enable-threads \
  --enable-xdbe \
  --enable-xinerama \
  --enable-xft

make %{?_smp_mflags}

%install
make install install-desktop DESTDIR=$RPM_BUILD_ROOT 

# omit examples/games: 
make -C test uninstall-linux DESTDIR=$RPM_BUILD_ROOT
rm -f  $RPM_BUILD_ROOT%{_mandir}/man?/{blocks,checkers,sudoku}*

# we only apply this hack to multilib arch's
%ifarch x86_64 %{ix86} ppc64 ppc s390x s390 sparc64 sparc
%global arch %(uname -i 2>/dev/null || echo undefined)
mv $RPM_BUILD_ROOT%{_bindir}/fltk-config \
   $RPM_BUILD_ROOT%{_bindir}/fltk-config-%{arch}
install -p -m755 -D %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/fltk-config
%endif

# docs
rm -rf __docs
mv $RPM_BUILD_ROOT%{_docdir}/fltk __docs

## unpackaged files
# errant docs
rm -rf $RPM_BUILD_ROOT%{_mandir}/cat*

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/fluid.desktop

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc ANNOUNCEMENT CHANGES COPYING CREDITS README
%{_libdir}/libfltk.so.1.3
%{_libdir}/libfltk_forms.so.1.3
%{_libdir}/libfltk_gl.so.1.3
%{_libdir}/libfltk_images.so.1.3

%files devel
%doc __docs/*
%{_bindir}/fltk-config
%{?arch:%{_bindir}/fltk-config-%{arch}}
%{_includedir}/FL/
%{_includedir}/Fl
%{_libdir}/libfltk.so
%{_libdir}/libfltk_forms.so
%{_libdir}/libfltk_gl.so
%{_libdir}/libfltk_images.so
%{_mandir}/man1/fltk-config.1*
%{_mandir}/man3/fltk.3*

%files static
%{_libdir}/libfltk.a
%{_libdir}/libfltk_forms.a
%{_libdir}/libfltk_gl.a
%{_libdir}/libfltk_images.a

%post fluid
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun fluid
if [ $1 -eq 0 ] ; then
  update-desktop-database -q &> /dev/null
  touch --no-create %{_datadir}/icons/hicolor &> /dev/null
  gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans fluid
update-desktop-database -q &> /dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files fluid
%{_bindir}/fluid
%{_mandir}/man1/fluid.1*
%{_datadir}/applications/fluid.desktop
%{_datadir}/icons/hicolor/*/*/*
# FIXME, add according to new mime spec
%{_datadir}/mimelnk/*/*.desktop

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.3.0-9
- rebuild due to "jpeg8-ABI" feature drop

* Tue Dec 04 2012 Adam Tkac <atkac redhat com> - 1.3.0-8
- fix ABI breakage caused by fltk-1_v4.3.x-cursor.patch (#883026)

* Thu Nov 29 2012 Adam Tkac <atkac redhat com> - 1.3.0-7
- add xcursor BR

* Wed Aug 22 2012 Adam Tkac <atkac redhat com> - 1.3.0-6
- update to 1.3.x snap r9671
- add some not-yet-accepted patches needed by tigervnc

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Rex Dieter <rdieter@fedoraproject.org> 1.3.0-3
- rebuild (libpng)
- pkgconfig-style deps

* Thu Aug 25 2011 Rex Dieter <rdieter@fedoraproject.org> 1.3.0-2
- fltk-config inconsistency on ARM (#733421)

* Fri Jun 24 2011 Rex Dieter <rdieter@fedoraproject.org> 1.3.0-1
- 1.3.0 (final)
- --with-links

* Fri May 27 2011 Adam Tkac <atkac redhat com> - 1.3.0-0.2.rc5
- fltk-config: don't emit unneeded -l<library> flags (#708185)

* Wed May 25 2011 Adam Tkac <atkac redhat com> - 1.3.0-0.1.rc5
- update to 1.3.0rc5
- patches no longer needed
  - fltk-1.1.9-test.patch
  - fltk-1.1.9-rpath.patch
  - fltk-1.1.10-pkgconfig_xft.patch
  - fltk-1.1.10-fluid_target.patch
- regenerated other patches to match current source

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.10-5
- FTBFS fltk-1.1.10-4.fc15: ImplicitDSOLinking (#660884)

* Wed Sep 29 2010 jkeating - 1.1.10-4
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.10-3
- verbose build output (hint from mschwendt)

* Tue Sep 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.10-2
- drop BR: man , fixes FTBFS (#631212)

* Sun Feb 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.10-1
- fltk-1.1.10
- FTBFS fltk-1.1.10-0.1.rc3.fc13: ImplicitDSOLinking (#564877)

* Tue Dec 08 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.10-0.1.rc3
- fltk-1.1.10rc3

* Mon Dec 07 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.9-7
- real -static subpkg (#545145)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 28 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.9-5
- fltk-fluid duplicate .desktop file (#508553)
- optimize scriptlets

* Wed May 13 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.9-4
- unbreak fltk-config --ldstaticflags (#500201)
- (another?) gcc44 patch
- -devel: +Provides: %%name-static
- fix multiarch conflicts (#341141)

* Wed Mar 04 2009 Caolán McNamara <caolanm@redhat.com> - 1.1.9-3
- fix uses of strchr wrt. constness

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 01 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.9-1
- fltk-1.1.9

* Sat Mar 29 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.8-1
- fltk-1.1.8 (final)

* Tue Feb 29 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.8-0.8.r6027
- fltk-1.1.x-r6027

* Mon Feb 11 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.8-0.7.r5989 
- respin (gcc43)

* Wed Dec 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.6.r5989
- --enable-largefile
- fltk-1.1.x-r5989 snapshot (1.1.8 pre-release)

* Mon Aug 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.5.r5750
- License: LGPLv2+ with exceptions

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.4.r5750
- License: LGPLv2+ (with exceptions)

* Sun Apr 29 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.3.r5750
- *really* fix --rpath issue, using non-empty patch this time (#238284)

* Sun Apr 29 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.2.r5750
- nuke --rpath (#238284)

* Thu Apr 05 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.8-0.1.r5750
- fltk-1.1.x-r5750 snapshot (1.1.8 pre-release)
- --enable-xinerama
- patch for undefined symbols in libfltk_gl

* Wed Apr  4 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.7-9.r5555
- Always apply fltk-config patch (#199656)
- Update fltk-1.1.7-config.patch

* Wed Dec 13 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.7-8.r5555
- more 64bit hackage to workaround broken Makefile logic (#219348)

* Wed Dec 13 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.7-7.r5555
- fltk-1.1.x-r5555 snapshot, for 64bit issues (#219348)
- restore static libs (they're tightly coupled with fltk-config)
- cleanup %%description's

* Mon Dec 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.7-6
- move tests to %%check section

* Mon Dec 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.7-5
- use included icon/.desktop files
- fix up fltk-config (#199656)

* Mon Dec 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.7-3
- follow icon spec
- omit static libs

* Wed Sep 06 2006 Michael J. Knox <michael[AT]knox.net.nz> - 1.1.7-2
- rebuild for FC6

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.7-1
- Upstream update

* Thu Nov 17 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.6-4
- Fixed BR and -devel Requires for modular X

* Sun Nov 13 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.6-3
- Update BuildRequires as well

* Sun Nov 13 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.6-2
- Update Requires for -devel

* Thu Oct 27 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.6-1
- Upstream update

* Thu Aug 18 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.1.4-10
- Fixed BR/Requires for x86_64

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Nov 20 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.8
- Hopefully fixed Xft flags for rh80

* Thu Nov 20 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.7
- Fixed typo

* Thu Nov 20 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.6
- Added xft.pc build dependency
- Added BuildReq:man

* Sun Nov  9 2003 Ville Skyttä <ville.skytta@iki.fi> 0:1.1.4-0.fdr.4
- Spec file cleanup
- Enabled xft and threads

* Tue Oct 28 2003 Dams <anvil[AT]livna.org> - 0:1.1.4-0.fdr.3
- Added missing symlink in includedir

* Wed Oct  1 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.2
- Removed comment after scriptlets

* Wed Oct  1 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.1
- Updated to final 1.1.4

* Wed Sep 24 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.0.4.rc1
- Fixed documentation path in configure

* Fri Aug 29 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.0.3.rc1
- Fixed typo in desktop entry
- Added missing BuildRequires ImageMagick and desktop-file-utils

* Fri Aug 29 2003 Dams <anvil[AT]livna.org> 0:1.1.4-0.fdr.0.2.rc1
- Moved fluid to its own package
- Added missing Requires for devel package

* Sat Aug 16 2003 Dams <anvil[AT]livna.org>
- Initial build.
