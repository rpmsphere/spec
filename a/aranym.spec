Name:			aranym
Version:		1.0.2
Release:		4.1
License:		GPLv2
Summary:		32-bit Atari personal computer (Falcon030/TT030) virtual machine
URL:			http://aranym.org/
Group:			Console/Emulators
Source0:		http://prdownloads.sourceforge.net/aranym/%{name}_%{version}.orig.tar.gz
Requires:		hicolor-icon-theme
BuildRequires:		hicolor-icon-theme
BuildRequires:		desktop-file-utils
BuildRequires:		gcc-c++
BuildRequires:		SDL-devel >= 1.2.10
BuildRequires:		SDL_image-devel >= 1.2.5
BuildRequires:		zlib-devel >= 1.2.3
BuildRequires:		mpfr-devel >= 3.0.0
BuildRequires:		libusb1-devel >= 1.0.0
BuildConflicts:		SDL2-devel

%description
ARAnyM is a software only TOS clone - a virtual machine that allows you
to run TOS, EmuTOS, FreeMiNT, MagiC and Linux-m68k operating systems
and their applications.

Authors:
Ctirad Fertr, Milan Jurik, Standa Opichal, Petr Stehlik, Johan Klockars,
Didier MEQUIGNON, Patrice Mandin and others (see AUTHORS for a full list).

%prep
%setup -q

%build
# JIT only works on i586
#
%ifarch %ix86
%configure --disable-nat-debug --enable-jit-compiler --enable-nfjpeg
%{__make} depend
%{__make}
%{__mv} aranym aranym-jit
%{__make} clean
%endif

%configure --disable-nat-debug --enable-addressing=direct --enable-fullmmu --enable-lilo --enable-fixed-videoram --enable-nfjpeg
%{__make} depend
%{__make}
%{__mv} aranym aranym-mmu
%{__make} clean

%configure --disable-nat-debug --enable-addressing=direct --enable-nfjpeg
%{__make} depend
%{__make}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/aranym
make install DESTDIR=$RPM_BUILD_ROOT
install -m 755 aranym-mmu $RPM_BUILD_ROOT%{_bindir}

# should be 4755 but build fails due to SUID bit set
#
install -m 755 aratapif $RPM_BUILD_ROOT%{_bindir}

# JIT only works on i586
%ifarch %ix86
install -m 755 aranym-jit $RPM_BUILD_ROOT%{_bindir}
%endif

# add a desktop menu entry
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -m 644 contrib/icon-32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/aranym.png
install -m 644 contrib/icon-48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/aranym.png

install -m 644 contrib/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
desktop-file-install                                    \
 --delete-original                                      \
 --vendor ""                                 \
 --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
 --add-category System                                  \
 --add-category Emulator                                \
 $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
%ifarch %ix86
install -m 644 contrib/%{name}-jit.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}-jit.desktop
%endif
install -m 644 contrib/%{name}-mmu.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-mmu.desktop

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/aratapif.1*
%{_datadir}/%{name}
%{_docdir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/*%{name}.desktop
%{_bindir}/aratapif
%{_bindir}/aranym

# JIT only works on i586
#
%ifarch %ix86
%{_bindir}/aranym-jit
%{_mandir}/man1/%{name}-jit.1*
%{_datadir}/applications/*%{name}-jit.desktop
%else
%exclude %{_mandir}/man1/%{name}-jit.1*
%endif

%{_bindir}/aranym-mmu
%{_mandir}/man1/%{name}-mmu.1*
%{_datadir}/applications/*%{name}-mmu.desktop

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
* Fri Mar 23 2012 Petr Stehlik <pstehlik@sophics.cz> 0.9.13
New ARAnyM release.
Make use of two new desktop files.
Mandriva desktop files without the vendor prefix.
* Sat Mar 17 2012 Petr Stehlik <pstehlik@sophics.cz> 0.9.12
New ARAnyM release.
New FPU emulation for MMU mode (using MPFR)
New Native Features enabled (PCI, USB)
New dependencies (zlib, mpfr, libusb)
* Wed May 26 2010 Petr Stehlik <pstehlik@sophics.cz> 0.9.10
New ARAnyM release.
Icons moved to icons dir.
Source archive filename follows Debian convention.
* Sat Sep 05 2009 Petr Stehlik <pstehlik@sophics.cz> 0.9.9
New ARAnyM release.
* Sat Apr 25 2009 Petr Stehlik <pstehlik@sophics.cz>
New ARAnyM release.
* Sat Nov 08 2008 Petr Stehlik <pstehlik@sophics.cz>
New ARAnyM release.
* Wed Jan 30 2008 Petr Stehlik <pstehlik@sophics.cz>
Added SDL_image to Requires:
Bumped the minimal SDL version to 1.2.10
Enabled the Requires: for mandriva (still untested)
* Tue Jan 29 2008 Petr Stehlik <pstehlik@sophics.cz>
Desktop file corrected and renamed to lowercase.
_icondir defined for Fedora. For other changes see ChangeLog.
* Mon Jan 28 2008 Petr Stehlik <pstehlik@sophics.cz>
The right icon added. Desktop file updated. Build system root changed.
New release. Version increased. Other changes in NEWS file.
* Mon Jul 09 2007 Petr Stehlik <pstehlik@sophics.cz>
New release. Version increased. Other changes in NEWS file.
* Tue Oct 11 2006 David Bolt <davjam@davjam.org>	0.9.4beta
Added an aranym.desktop file for inclusion in desktop menus.
Temporarily uses emulator.png as the menu icon.
Added bits to spec file to try and build packages for (open)SUSE, Mandriva
and Fedora Core distributions without any changes.
* Fri Sep 22 2006 Petr Stehlik <pstehlik@sophics.cz>
New release. Version increased. Other changes in NEWS file.
Thanks to David Bolt this spec file is nicely updated - does not fail
on 64bit anymore. Thanks, David!
* Mon Feb 20 2006 Petr Stehlik <pstehlik@sophics.cz>
URL changed to aranym.org. Version increased. Other changes in NEWS file.
* Sun Apr 17 2005 Petr Stehlik <pstehlik@sophics.cz>
Files list fixed.
* Thu Apr 14 2005 Petr Stehlik <pstehlik@sophics.cz>
Version increased. NFJPEG enabled.
* Tue Feb 22 2005 Petr Stehlik <pstehlik@sophics.cz>
Version increased. aranymrc.example removed.
* Sun Feb 20 2005 Petr Stehlik <pstehlik@sophics.cz>
Version increased. LILO enabled in the MMU version.
* Sun Nov 07 2004 Petr Stehlik <pstehlik@sophics.cz>
Version increased.
* Tue Jul 06 2004 Petr Stehlik <pstehlik@sophics.cz>
Version increased.
* Mon Jul 05 2004 Petr Stehlik <pstehlik@sophics.cz>
Version increased. tools/createdisk/ removed. tools/arabridge added.
For other changes see the NEWS file.
* Sun Feb 15 2004 Petr Stehlik <pstehlik@sophics.cz>
Version increased. For other changes see the NEWS file.
* Sun Feb 08 2004 Petr Stehlik <pstehlik@sophics.cz>
Version increased. For other changes see the NEWS file.
* Wed Jan 07 2004 Petr Stehlik <pstehlik@sophics.cz>
Version increased. For other changes see the NEWS file.
* Sat Jan 03 2004 Petr Stehlik <pstehlik@sophics.cz>
font8.bmp removed.
* Sat Oct 04 2003 Petr Stehlik <pstehlik@sophics.cz>
Version increased. NFCDROM.BOS added.
* Fri Apr 11 2003 Petr Stehlik <pstehlik@sophics.cz>
Man dir fixed. Debug info disabled.
* Mon Apr 08 2003 Petr Stehlik <pstehlik@sophics.cz>
Various fixes for the 0.8.0. And full 68040 PMMU build added as aranym-mmu.
Also manual page added.
* Mon Mar 24 2003 Petr Stehlik <pstehlik@sophics.cz>
HostFS and network drivers added. ARATAPIF installed setuid root.
Ethernet enabled.
* Sun Mar 23 2003 Petr Stehlik <pstehlik@sophics.cz>
Version increased for the new release. See the NEWS file for details.
* Fri Mar 07 2003 Petr Stehlik <pstehlik@sophics.cz>
Fixed paths to share/aranym folder.
* Wed Jan 29 2003 Petr Stehlik <pstehlik@sophics.cz>
New release. Updated list of provided files.
* Tue Oct 22 2002 Petr Stehlik <pstehlik@sophics.cz>
aranym-jit (JIT compiler for m68k CPU) generated.
* Sun Oct 20 2002 Petr Stehlik <pstehlik@sophics.cz>
EmuTOS image file renamed back.
* Sat Oct 12 2002 Petr Stehlik <pstehlik@sophics.cz>
EmuTOS image file renamed. Updated for new release.
* Sun Jul 21 2002 Petr Stehlik <pstehlik@sophics.cz>
SDL GUI font and EmuTOS image files added.
* Sat Jul 20 2002 Petr Stehlik <pstehlik@sophics.cz>
Version increased.
* Thu Jun 06 2002 Petr Stehlik <pstehlik@sophics.cz>
Install path changed from /usr/local to /usr
* Mon Apr 22 2002 Petr Stehlik <pstehlik@sophics.cz>
Sound driver added
* Sun Apr 14 2002 Petr Stehlik <pstehlik@sophics.cz>
First working version
