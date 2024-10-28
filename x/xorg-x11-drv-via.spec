%undefine _debugsource_packages

Summary:   Xorg X11 via video driver
Name:      xorg-x11-drv-via
Version:   5.76.52.92.009
Release:   1
URL:       http://linux.via.com.tw/support/downloadFiles.action
License:   opensource
Group:     User Interface/X Hardware Support
Source0:   5.76.52.92-opensource-009-005f78-20150730.tar.gz
BuildRequires: xorg-x11-server-devel
BuildRequires: xorg-x11-server-source
BuildRequires: libXvMC-devel
BuildRequires: libdrm-devel
BuildRequires: systemd-devel
BuildRequires: libXfont-devel
Requires: via_chrome9-kmod

%description 
VIA Chrome Linux Xserver driver.

%prep
%setup -q -n 5.76.52.92-opensource-009-005f78-20150730
#sed -i '/mibstore.h/d' XServer/uxa/uxa-priv.h
#sed -i '1i #include <xorg-server.h>' XServer/src/xf86drmVIA.c
cp /usr/share/xorg-x11-server-source/hw/xfree86/dri/{sarea.h,dri.h,dristruct.h} XServer/src
sed -i 's|xf86Info.disableRandR|FALSE|' XServer/src/via_driver_kms.c XServer/src/via_driver.c
sed -i -e '4340s|,pReadmask||' -e '4379s|, pReadmask||' XServer/src/via_driver.c
sed -i '986s|, pReadmask||' XServer/src/via_video.c

%build
cd XServer
chmod +x configure
sh autogen.sh --prefix=/usr --disable-static --enable-dri
sed -i 's|^CFLAGS =|CFLAGS = -Wl,--allow-multiple-definition|' Makefile */Makefile
make

%install
cd XServer
make install DESTDIR=$RPM_BUILD_ROOT
%ifarch x86_64
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64
%endif
mkdir -p $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d
cat > $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/10-via.conf <<EOF
Section "Device"
        Identifier "Card0"
        Driver "via"
EndSection
EOF

%files
%doc Readme
%{_libdir}/xorg/modules/drivers/via_drv.so
%{_mandir}/man4/via.4*
%{_datadir}/X11/xorg.conf.d/10-via.conf

%changelog
* Mon Oct 05 2015 Wei-Lun Chao <bluebat@member.fsf.org> 5.76.52.92.009
- Using source from VIA
* Fri Jan 5 2007 Soren Sandmann <sandmann@redhat.com> 0.2.1-9
- Remove blank-on-init.patch since it causes lockups (#217624)
* Wed Nov 8 2006 Soren Sandmann <sandmann@redhat.com> 0.2.1-8
- blank-on-init.patch, patch to blank framebuffer before starting X. (#210297).
* Mon Oct 2 2006 Adam Jackson <ajackson@redhat.com> 0.2.1-7
- via-0.2.1-build-fix.patch: De-pollute glibc's headers of X #defines.
* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 0.2.1-6
- rebuilt for unwind info generation, broken in gcc-4.1.1-21
* Wed Sep 20 2006 Adam Jackson <ajackson@redhat.com> 0.2.1-5
- via-0.2.1-assert.patch: include assert.h so we don't crash at runtime.
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild
* Mon Jun 19 2006 Mike A. Harris <mharris@redhat.com> 0.2.1-4
- Updated via.xinf to fix numerous errors an inaccuracies (#195806)
- Conditionalized DRI support by adding with_dri macro.
* Fri May 26 2006 Mike A. Harris <mharris@redhat.com> 0.2.1-3
- Updated sdk dependency to pick up proto-devel automatically. (#192167)
* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 0.2.1-2
- Rebuild for 7.1 ABI fix.
* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 0.2.1-1
- Update to 0.2.1 from 7.1RC1.
* Wed Feb 22 2006 Mike A. Harris <mharris@redhat.com> 0.1.33.2-2
- Install via.xinf, which was inadvertently left out of packaging (#182506)
* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 0.1.33.2-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes
* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 0.1.33.2-1
- Updated xorg-x11-drv-via to version 0.1.33.2 from X11R7.0
* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 0.1.33.1-1
- Updated xorg-x11-drv-via to version 0.1.33.1 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.
- Re-enabled the XvMC libs, etc.
- Updated libdrm dependency to >= 2.0-1
* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 0.1.32-1
- Updated xorg-x11-drv-via to version 0.1.32 from X11R7 RC2
- Add rpm macro with_xvmc, and disable it by default, as upstream does not
  build the via XvMC modules in RC2.
* Fri Nov 04 2005 Mike A. Harris <mharris@redhat.com> 0.1.31.1-1
- Updated xorg-x11-drv-via to version 0.1.31.1 from X11R7 RC1
- Fix *.la file removal.
- Added "BuildRequires: libXvMC-devel" dependency.
- Added "BuildRequires: libdrm-devel >= 1.0.5-1" dependency as it is required
  to build this version of the via driver aparently.
- Added xorg-x11-drv-via-0.1.31.1-buildfix-CVSHEAD.patch to fix the driver
  to actually build.
- Added 'devel' subpackage for XvMC .so
* Tue Oct 04 2005 Mike A. Harris <mharris@redhat.com> 0.1.31-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86, x86_64
* Fri Sep 02 2005 Mike A. Harris <mharris@redhat.com> 0.1.31-0
- Initial spec file for via video driver generated automatically
  by my xorg-driverspecgen script.
