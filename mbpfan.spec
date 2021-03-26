Name:           mbpfan
URL:            https://github.com/dgraziotin/mbpfan
License:        GNU General Public License (GPL)
Group:          System/Utility
Version:        2.1.1
Release:        1
Summary:        Automatically adjust the fan on a MacBook Pro
Source:         https://github.com/dgraziotin/mbpfan/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Mbpfan is a daemon that controls the fans of Macbook/Macbook Pro
laptops when they run GNU/Linux. It is a lightweight replacement
of macfanctld, although it does not implement all of its features.
It has got a different algorithm to control the fans. In a couple
of words, it keeps Macbook fans a lot more silent.

This project is an enhanced version of Allan McRae mbpfan.

The mbpfan project is a daemon that uses input from coretemp
module and sets the fan speed using the applesmc module. This
enhanced version assumes any number of processors and fans
(max. 10).

%prep
%setup -q

%build
make

%install
%make_install
#install -D -m755 bin/mbpfan $RPM_BUILD_ROOT/usr/sbin/mbpfan
#install -D -m644 mbpfan.conf $RPM_BUILD_ROOT/etc/mbpfan.conf
install -D -m644 mbpfan.service $RPM_BUILD_ROOT/usr/lib/systemd/system/mbpfan.service

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_post mbpfan.service

%preun
%systemd_preun mbpfan.service

%postun
%systemd_postun_with_restart mbpfan.service 

%files
%doc AUTHORS README.md COPYING
%{_sbindir}/mbpfan
%{_sysconfdir}/mbpfan.conf
%{_mandir}/man8/mbpfan.8.*
%{_unitdir}/mbpfan.service

%changelog
* Wed Sep 04 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.1
- Rebuild for Fedora
* Thu Nov 27 2008 - uli@suse.de
- update -> 1.9
  New open source, hardware accelerated OpenGL plugin included! dfOpenGL
  is still in a very basic state and does not include many game fixes at
  this time, but feel free to play with it.
  You should remove your old ~/.pcsx directory before using PCSX-df, to
  avoid any possible compatibility issues, such as missing folders. Remember
  that memcards and savestates are kept there, so be sure to copy them out
  first!
- fixed several problems found by rpmlint
- use RPM_OPT_FLAGS
* Wed Jun 18 2008 - uli@suse.de
- update -> 1.818
  GUI version info display
  HLE bios updates (cvs)
  dfiso - new glade interface (Andrew cvs)
  dfsound oss pthread build fix
  dfxvideo ppc: use YUYV mode on ppc. (Marcus Comstedt)
  updated pixmaps from Ryan
- fixed sprintf() usage in cd/iso plugins (configuration should work again)
- fixed to build on AMD64
* Mon Jan 21 2008 - uli@suse.de
- switched to pcsx-df (version 1.817)
* Thu Jun 21 2007 - uli@suse.de
- move plugins out of /usr/share
* Tue Feb 27 2007 - dmueller@suse.de
- reduce BuildRequires
* Wed Feb 22 2006 - uli@suse.de
- update -> 1.5 (fixes bug #152061)
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Sun Jan 15 2006 - schwab@suse.de
- Don't strip binaries.
* Wed Oct 12 2005 - mmj@suse.de
- add -fno-strict-aliasing
* Tue Apr 26 2005 - yxu@suse.de
- eliminate superflous data type definitions
* Tue Jun 29 2004 - ro@suse.de
- added libjpeg to neededforbuild
* Tue Jun 29 2004 - ro@suse.de
- added libtiff to neededforbuild
* Sat Jan 10 2004 - adrian@suse.de
- build as user
* Fri Aug 15 2003 - adrian@suse.de
- add desktop file
* Mon Jul 28 2003 - ro@suse.de
- added libexif to neededforbuild
* Thu Jun 05 2003 - ro@suse.de
- added psx-plugins to neededforbuild
* Wed May 28 2003 - coolo@suse.de
- use BuildRoot
* Wed Jan 29 2003 - ro@suse.de
- fix build with gcc-3.3 (preprocessor token pasting)
* Fri Jul 12 2002 - uli@suse.de
- update -> 1.3 (HLE BIOS rewritten, lots of fixes, SPUasync
  support, gme support)
* Fri Jul 05 2002 - kukuk@suse.de
- Use %%ix86 macro
* Thu May 23 2002 - uli@suse.de
- made wrapper script deal with changes in cfg dir
* Mon May 06 2002 - uli@suse.de
- update -> 1.2 (sound works, speedups, mouse and analog emulation
  fixed & more)
* Wed Feb 06 2002 - uli@suse.de
- moved plugins to separate package psx-plugins
* Thu Jan 17 2002 - uli@suse.de
- use MesaGL plugin that does not depend on libXxf86vm.so.1
* Mon Jan 14 2002 - uli@suse.de
- updated PeopsSoftGpu -> 1.4 (bugfixes, fullscreen support)
* Fri Jan 11 2002 - uli@suse.de
- added bugfix patch from homepage
- added missing "About" pixmap
- disabled CD debug output
* Mon Jan 07 2002 - uli@suse.de
- initial package
- builds on all archs, but only works on x86 and ARM :)
- aborted attempts to do endianness/64 bit fixes, too
  time-intensive
