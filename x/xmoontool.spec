Name:           xmoontool
Version:        3.0.1
Release:        7.1
Summary:        The Moon in focus
License:        SUSE-Public-Domain
Group:          Productivity/Scientific/Astronomy
URL:            http://www.fourmilab.ch/earthview/vplanet.html
Source0:        xmoontool-22sep94.tar.gz
Source1:        xmoontool.desktop
Patch0:         xmoontool-22sep94.patch
Patch1:         xmoontool-22sep94-y2kfix.patch
Patch2:         xmoontool-22sep94-filepermissions.patch
Patch3:         xmoontool-22sep94-xorg7.patch
BuildRequires:  motif-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:  ImageMagick
Provides:       moontool

%description
One of the most important programs existing :-) Using this program, you
can display all important information about the moon constantly. At
last...

Hint: The option -c makes it also work with color ;-)

%prep
%setup -q -n xmoontool-22sep94
%patch0
%patch1
%patch2
%patch3

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -I%{_prefix}/include" XLIBDIR=%{_libdir}
convert moon_icon %{name}.png

%install
make "DESTDIR=%{buildroot}" install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%changelog
* Tue Jan 16 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.1
- Rebuilt for Fedora
* Mon Mar  2 2015 sfalken@opensuse.org
- Added Categories and GenericName to .desktop to clear
  brp-check-suse errors
* Sat Nov  1 2014 crrodriguez@opensuse.org
- Run spec cleaner
- Switch to individual pkgconfig() build requires
  instead of using metapackage xorg-x11-devel
- moontool-22sep94-xorg7.patch extend to avoid overlinking
  multiple unneeded libraries and fix implicit declarations.
* Mon Nov  8 2010 coolo@novell.com
- remove support for pre-9.1
* Fri Aug 11 2006 lmichnovic@suse.cz
- adjusting paths to omit X11R6 when X.org is 7.x (*xorg7.patch)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Sat Jan 21 2006 schwab@suse.de
- Don't strip binaries.
* Fri May  7 2004 hmacht@suse.de
- added # norootforbuild in specfile
- added patch2 to correct filepermissions
* Fri Aug 15 2003 adrian@suse.de
- add desktop file
* Fri Jan 11 2002 cihlar@suse.cz
- use %%{_lib}
* Sat Nov  3 2001 sndirsch@suse.de
- fixed the "Fatal Error!  No visuals that we can use" problem. It
  is no longer necessary to execute "xmoontool -c" on non-8bit
  visuals
* Thu Nov  9 2000 cihlar@suse.cz
- renamed moontool -> xmoontool
- uses openmotif now
- fixed copyright
* Fri Jul 28 2000 bjacke@suse.de
- fixed y2k bug
* Wed May 17 2000 cihlar@suse.cz
- Group sorted
* Wed Mar 22 2000 cihlar@suse.cz
- added BuildRoot
* Fri Mar  3 2000 fehr@suse.de
- move man pages to /usr/share/man
* Thu Dec  9 1999 kukuk@suse.de
- Use RPM_OPT_FLAGS
* Thu Sep 23 1999 uli@suse.de
- fixed Makefile for PPC
* Mon Sep 20 1999 uli@suse.de
- no builds with lesstif
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Tue Feb  2 1999 ro@suse.de
- no m486 on alpha
* Thu May  7 1998 fehr@suse.de
- add library -lXp for Motif 2.1
* Tue Dec  9 1997 ro@suse.de
- build static and dynamic version
* Wed Oct  8 1997 fehr@suse.de
- prepare for automatic build of package
