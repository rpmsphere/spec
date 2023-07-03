%global pkgname xdm

Summary: X.Org X11 xdm - X Display Manager
Name: xorg-x11-%{pkgname}
Version: 1.1.12
Release: 1
# NOTE: Remove Epoch line if/when the package ever gets renamed.
Epoch: 1
License: MIT
URL: https://www.x.org
Source0: ftp://ftp.x.org/pub/individual/app/xdm-%{version}.tar.bz2
Source1: Xsetup_0
Source10: xdm.init
Source11: xdm.pamd

# Following are Fedora specific patches
Patch11: xdm-1.0.5-sessreg-utmp-fix-bug177890.patch

# FIXME Most likely not needed
Patch14: xdm-1.1.10-libdl.patch

# send a USER_LOGIN event like other login programs do.
Patch15: xdm-1.1.10-add-audit-event.patch

# systemd unit file update
Patch16: xdm-service.patch

# Include <crypt.h> if needed.
Patch17: xdm-1.1.11-include_crypt_h.patch

# FIXME: Temporary build dependencies for autotool dependence.
BuildRequires: make
BuildRequires: autoconf, automake, libtool

BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-xtrans-devel
BuildRequires: libXaw-devel
BuildRequires: libXmu-devel
BuildRequires: libXt-devel
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: libXext-devel
BuildRequires: libXpm-devel
BuildRequires: libX11-devel
# FIXME: There's no autotool dep on libXdmcp currently, but it fails with the
# following:
# configure: error: Library requirements (xdmcp) not met; consider adjusting
# the PKG_CONFIG_PATH environment variable if your libraries are in a
# nonstandard prefix so pkg-config can find them.
BuildRequires: libXdmcp-devel
# FIXME: There's no autotool specified dep on this currently, but everything
# explodes looking for X11/Xauth.h without it:
BuildRequires: libXau-devel
BuildRequires: libXinerama-devel
BuildRequires: pam-devel
# Add TrueType support (resolves bug #551908)
BuildRequires: libXft-devel
# Add libaudit support
BuildRequires: audit-libs-devel
# systemd support
BuildRequires: systemd-rpm-macros systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# FIXME:These old provides should be removed
Provides: xdm

Requires: pam

# We want to use the system Xsession script
Requires: xorg-x11-xinit
Requires: sessreg

%description
X.Org X11 xdm - X Display Manager

%prep
%setup -q -n %{pkgname}-%{version}

%patch11 -p0 -b .redhat-sessreg-utmp-fix-bug177890
#%_patch14 -p1 -b .add-needed
#%patch15 -p1 -b .add-audit-events
%patch16 -p1 -b .systemd
#%patch17 -p1 -b .crypt_h

%build
autoreconf -v --install
%configure \
	--disable-static \
        --with-libaudit \
        --with-xdmlibdir=%{_libexecdir} \
	--with-xdmconfigdir=%{_sysconfdir}/X11/xdm \
	--with-xdmscriptdir=%{_sysconfdir}/X11/xdm \
	--with-pixmapdir=%{_datadir}/xdm/pixmaps \
	--enable-xdmshell

make %{?_smp_mflags}

%install
echo looking for xdmshell
find . -name \*xdmshell\*
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
echo looking for xdmshell
find $RPM_BUILD_ROOT -name \*xdmshell\*

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm/Xsetup_0

# Install pam xdm config files
{
   mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
   install -p -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/xdm
}

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm/Xsession
(cd $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm; ln -sf ../xinit/Xsession .)

# we need to crate /var/lib/xdm to make authorization work (bug
# 500704)
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/xdm

%post
%systemd_post xdm.service

%preun
%systemd_preun xdm.service

%postun
%systemd_postun xdm.service

%files
%doc AUTHORS COPYING README.md ChangeLog
%{_bindir}/xdm
%{_bindir}/xdmshell
%dir %{_sysconfdir}/X11/xdm
# NOTE: The Xaccess file from our "xinitrc" package had no customizations,
# and was out of sync with upstream, so we ship the upstream one now.
%config %{_sysconfdir}/X11/xdm/Xaccess
%config %{_sysconfdir}/X11/xdm/Xresources
%config %{_sysconfdir}/X11/xdm/Xservers
%config %{_sysconfdir}/X11/xdm/xdm-config
%{_sysconfdir}/X11/xdm/GiveConsole
%{_sysconfdir}/X11/xdm/TakeConsole
%config %{_sysconfdir}/X11/xdm/Xreset
%{_sysconfdir}/X11/xdm/Xsession
%config %{_sysconfdir}/X11/xdm/Xsetup_0
%config %{_sysconfdir}/X11/xdm/Xstartup
%config %{_sysconfdir}/X11/xdm/Xwilling
# NOTE: For security, upgrades of this package will install the new pam.d
# files and make backup copies by default.  'noreplace' is intentionally avoided
# here.
%config %{_sysconfdir}/pam.d/xdm
# NOTE: We intentionally default to OS supplied file being favoured here on
# OS upgrades.
%{_datadir}/X11/app-defaults/Chooser
%dir %{_datadir}/xdm
%dir %{_datadir}/xdm/pixmaps
%{_datadir}/xdm/pixmaps/xorg-bw.xpm
%{_datadir}/xdm/pixmaps/xorg.xpm
%dir %{_sharedstatedir}/xdm
%{_libexecdir}/chooser
%{_libexecdir}/libXdmGreet.so
%{_mandir}/man?/*
# systemd unit file
%{_unitdir}/xdm.service

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.12
- Rebuilt for Fedora
* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
* Wed Apr 28 2021 Peter Hutterer <peter.hutterer@redhat.com> 1:1.1.11-26
- Add Requires for sessreg, our patched GiveConsole needs it
* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
* Thu Nov  5 11:00:40 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 1:1.1.11-24
- Add BuildRequires for make
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> 1:1.1.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Thu Mar 21 2019 Adam Jackson <ajax@redhat.com> - 1.1.11-20
- Rebuild for xtrans 1.4.0
* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1:1.1.11-18
- Rebuilt for libcrypt.so.2 (#1666033)
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Sun Jan 21 2018 Björn Esser <besser82@fedoraproject.org> - 1:1.1.11-15
- Add patch to include <crypt.h> if needed
* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1:1.1.11-14
- Rebuilt for switch to libxcrypt
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jan 28 2016 Peter Hutterer <peter.hutterer@redhat.com>
- Remove unnecessary defattr
* Wed Jan 20 2016 Peter Hutterer <peter.hutterer@redhat.com>
- s/define/global/
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Tue Aug  7 2012 Lennart Poettering <lpoetter@redhat.com> - 1:1.1.11-4
- Display Manager Rework
- https://fedoraproject.org/wiki/Features/DisplayManagerRework
- https://bugzilla.redhat.com/show_bug.cgi?id=846143
* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Mon Sep 26 2011 Matěj Cepl <mcepl@redhat.com> - 1.1.11-1
- New upstream release (#741101)
- Added support for systemd
* Fri Apr 01 2011 Adam Jackson <ajax@redhat.com> 1.1.10-1
- xdm 1.1.10
- move chooser to %%_libexecdir
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sat Sep 25 2010 Parag Nemade <paragn AT fedoraproject.org> - 1:1.1.6-21
- Merge-review cleanup (#226650)
* Wed Mar 24 2010 Matěj Cepl <mcepl@redhat.com> - 1:1.1.6-20
- Updated patch by sgrubb, this time tested with actual user
* Fri Mar 19 2010 Matěj Cepl <mcepl@redhat.com> - 1:1.1.6-19
- Work with audit system (fixes #469357). Patch by Steve Grubb.
- --disable-xprint is not needed anymore, it is disabled by
  default
* Sat Mar 06 2010 Stephen Beahm <stephenbeahm@comcast.net> 1:1.1.6-18
- Fix typo introduced in rev 15 to address (#551908).
* Fri Mar 05 2010 Matěj Cepl <mcepl@redhat.com> - 1:1.1.6-17
- Fixed bad directory ownership of /usr/share/X11
* Tue Feb 16 2010 Adam Jackson <ajax@redhat.com> 1.1.6-16
- xdm-1.1.6-add-needed.patch: Fix FTBFS from --no-add-needed
* Fri Jan 29 2010 Matěj Cepl <mcepl@redhat.com> - 1:1.1.6-15
- Add BR libXft-devel for TrueType support (#551908)
* Mon Aug 03 2009 Adam Jackson <ajax@redhat.com> 1.1.6-14
- Un-Requires xorg-x11-filesystem
* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Mon Jul 20 2009 Adam Jackson <ajax@redhat.com> 1.1.6-12
- Fix FTBFS due to Xaw xprint build macro disappearing. (#511508)
* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> 1.1.6-11
- Remove xserver PAM config file, it belongs (unsurprisingly) in
  xserver. (#500469)
* Tue Jun 23 2009 Matěj Cepl <mcepl@redhat.com> - 1:1.1.6-10
- return lost patch for fixing bug 470348.
* Thu May 14 2009 Matěj Cepl <mcepl@redhat.com> - 1:1.1.6-8
- Create /var/lib/xdm to make authorization work (bug 500704)
* Sat Mar 14 2009 Matěj Cepl <mcepl@redhat.com> - 1.1.6-7
- Make XDM work with SELinux (fix bug 388431)
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.6-6.0.bug388431test.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Thu Oct 30 2008 Soren Sandmann <ssp@redhat.com> 1.1.6-5
- Fix xdm.pamd (bug 388431)
* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.1.6-4
- Fix license tag.
* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:1.1.6-3
- Autorebuild for GCC 4.3
* Fri Aug 24 2007 Ray Strode <rstrode@redhat.com> 1:1.1.6-2
- Use system Xsession script (bug 244264)
* Fri Aug 17 2007 Dave Airlie <airlied@redhat.com> 1:1.1.6-1
- Update to 1.1.6
* Sat Aug 11 2007 Dave Airlie <airlied@redhat.com> 1:1.1.5-1
- Update to 1.1.5
* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 1:1.1.3-1
- Update to 1.1.3
* Mon Jul 24 2006 Mike A. Harris <mharris@redhat.com> 1:1.0.5-5.fc6
- Added xdm-1.0.5-sessreg-utmp-fix-bug177890.patch to restore GiveConsole to
  what we shipped in 6.8.2, and also fix bug (#177890)
* Wed Jul 19 2006 Mike A. Harris <mharris@redhat.com> 1:1.0.5-4.fc6
- Remove app-defaults dir from file manifest, as it is owned by libXt (#174021)
* Mon Jul 17 2006 Mike A. Harris <mharris@redhat.com> 1:1.0.5-3.fc6
- Added pam_keyinit.so support to xdm.pamd and xserver.pamd (#198631)
- Flag pam.d{xdm,xserver} as attr(0644,root,root) replaceable config files.
- Flag app-defaults/Chooser as a replaceable config file.
- Add conditional {dist} flag to Release field.
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1:1.0.5-2
- rebuild
* Wed Jun 28 2006 Mike A. Harris <mharris@redhat.com> 1:1.0.5-1
- Updated xdm to version 1.0.5.
- Remove xdm-1.0.4-setuid.diff as it is integrated in 1.0.5
* Wed Jun 21 2006 Mike A. Harris <mharris@redhat.com> 1:1.0.4-4
- Add missing documentation to doc macro.
- Clean cruft out of specfile.
* Tue Jun 20 2006 Mike A. Harris <mharris@redhat.com> 1:1.0.4-3
- Added xdm-1.0.4-setuid.diff to fix potential security issue (#196094)
- Added temporary "BuildRequires: autoconf, automake, libtool" dependencies
  for mock builds, for as long as we need to run autotools at compile time.
* Tue May 30 2006 Adam Jackson <ajackson@redhat.com> 1:1.0.4-2
- Fix BuildRequires (#191858)
* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 1:1.0.4-1
- Updated to version 1.0.4
* Fri Mar 31 2006 Adam Jackson <ajackson@redhat.com> 1:1.0.3-1
- Updated to version 1.0.3.  Forcibly relibtoolize to avoid present and future
  bogons on libXdmGreet.so losing the .so extension.
* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1:1.0.1-1.2
- bump again for double-long bug on ppc(64)
* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1:1.0.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes
* Mon Jan 09 2006 Mike A. Harris <mharris@redhat.com> 1:1.0.1-1
- Updated xdm to version 1.0.1 from X11R7.
- Added --with-xdmscriptdir option to ./configure to put scripts in /etc
- Updated xdm-1.0.1-redhat-xdm-config-fix.patch to work with xdm 1.0.1
* Thu Nov 24 2005 Mike A. Harris <mharris@redhat.com> 1:0.99.3-6
- Updated xdm.pamd to work with recent pam changes, and bumped the minimum
  pam requirement up to 0.78-0 for FC5 builds. (#170661)
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", as the xdm package
  puts files into /usr/lib/X11, so we have to make sure it is not a symlink.
- Removed "filesystem" package dependency, as xorg-x11-filesystem carries
  that dependency now, so it can be updated in one spot.
- Added missing "BuildRequires: pkgconfig".
- Added xdm-0.99.3-xdm-app-defaults-in-datadir.patch to force app-defaults
  files to install into _datadir instead of _libdir.
- Added xdm-0.99.3-xdm-scripts-in-configdir.patch to put the xdm scripts in
  _sysconfdir, and removed older xdm-0.99.3-xdm-configdir.patch which hacked
  up Makefile.in.  Fixes a typo that caused Xreset to not get installed
  properly also.
* Mon Nov 14 2005 Jeremy Katz <katzj@redhat.com> 1:0.99.3-5
- require newer filesystem package (#172610)
* Mon Nov 14 2005 Jeremy Katz <katzj@redhat.com> 1:0.99.3-4
- install scripts into /etc/X11/xdm instead of %%{_libdir} (#173081)
- use our Xsetup_0 instead of xorg one (#173083)
* Sat Nov 12 2005 Mike A. Harris <mharris@redhat.com> 1:0.99.3-3
- Added "Obsoletes: xinitrc", as xdm now provides files that were previously
  part of that package.  xorg-x11-xinit now provides the xinitrc scripts.
* Sat Nov 12 2005 Mike A. Harris <mharris@redhat.com> 1:0.99.3-2
- Rebuild against new libXaw 0.99.2-2, which has fixed DT_SONAME.
- Added xdm-0.99.3-redhat-xdm-config-fix.patch which merges in an
  xdm-config fix present in the forked Red Hat xdm-config from the FC4
  xinitrc package, which invokes Xwilling with "-s /bin/bash" instead
  of "-c" to fix bug (#86505).
- Removed ancient xdm rpm preinstall script, as it should be unnecessary now.
* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 1:0.99.3-1
- Update xdm to 0.99.3 from X11R7 RC2.
* Tue Nov 01 2005 Mike A. Harris <mharris@redhat.com> 1:0.99.2-1.20051031.3
- Build with -fno-strict-aliasing to work around possible pointer aliasing
  issues
* Tue Nov 01 2005 Mike A. Harris <mharris@redhat.com> 1:0.99.2-1.20051031.2
- It is _sysconfdir not _sysconfigdir goofball!
- Add {_sysconfdir}/pam.d/xdm and {_sysconfdir}/pam.d/xserver files that were
  missing from file manifest.
* Mon Oct 31 2005 Mike A. Harris <mharris@redhat.com> 1:0.99.2-1.20051031.1
- Make sure all dirs are owned that xdm creates.
- Misc spec file cleanups
* Mon Oct 31 2005 Mike A. Harris <mharris@redhat.com> 1:0.99.2-1.20051031.0
- Update xdm to 0.99.2 from X11R7 RC1.
- Update to CVS snapshot from 20051031
- Add Epoch 1, and change package to use the xdm version number.  Later, if
  we decide to rename the package to "xdm", we can drop the Epoch tag.
- Disable Xprint support
- Use _smp_mflags
- Add xdm-0.99.2-to-20051031.patch to pick up fixes from CVS head that allow
  us to set the config dir and other dirs.
* Wed Oct 05 2005 Mike A. Harris <mharris@redhat.com> 6.99.99.0-2
- Use Fedora-Extras style BuildRoot tag
- Update BuildRequires to use new library package names
* Wed Aug 24 2005 Mike A. Harris <mharris@redhat.com> 6.99.99.0-1
- Initial build.
