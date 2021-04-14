%undefine _debugsource_packages

Summary:	An X Window System based CPU state monitor
Name:		xcpustate
Version:	2.9
Release:	22.1
License:	MIT-style
Group:		Monitoring
BuildRequires:	libX11-devel
BuildRequires:	elfutils-libelf-devel
BuildRequires:	imake
BuildRequires:	libXt-devel
BuildRequires:	libXaw-devel
BuildRequires:	libXmu-devel
BuildRequires:	libtirpc-devel
URL:		ftp://ftp.cs.toronto.edu/pub/jdd/xcpustate/
Source0:	ftp://ftp.cs.toronto.edu/pub/jdd/xcpustate/%{name}-%{version}.tar.lzma
Source11:	%{name}16.png
Source12:	%{name}32.png
Source13:	%{name}48.png
Patch1:		xcpustate-2.5-alpha.patch
Patch2:		xcpustate-2.5-6.0.patch
Patch3:		xcpustate-2.9-missingheaders.patch

%description
The xcpustate utility is an X Window System based monitor which shows
the amount of time that the CPU is spending in different states.  On a
Linux system, xcpustate displays a bar that indicates the amounts of idle,
user, nice and system time (from left to right) used by the CPU.

Install the xcpustate package if you'd like to use a horizontal bar style
CPU state monitor.

%prep
%setup -q
%patch2 -p1 -b .glibc
%patch3 -p1 -b .headers
%ifarch alpha
%patch1 -p1 -b .alpha
%endif

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS -I/usr/include/tirpc -ltirpc" MANPATH=%_mandir

%install
%make_install install.man MANPATH=%_mandir

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=XCpuState
Comment=CPU load indicator
Exec=%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=System;Monitor;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files
%doc README
%attr(0755,root,root) %_bindir/xcpustate
%attr(0644,root,root) %_mandir/man1/xcpustate.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
* Thu May 28 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.9
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 2.9-9.mga5
+ Revision: 746600
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 2.9-8.mga5
+ Revision: 690573
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 2.9-7.mga4
+ Revision: 520496
- Mageia 4 Mass Rebuild
* Mon Jan 14 2013 umeabot <umeabot> 2.9-6.mga3
+ Revision: 386705
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Mar 22 2011 steletch <steletch> 2.9-5.mga1
+ Revision: 75608
- Clean spec file
- imported package xcpustate
* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 2.9-5mdv2011.0
+ Revision: 608196
- rebuild
* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.9-4mdv2010.1
+ Revision: 524397
- rebuilt for 2010.1
* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.9-3mdv2009.1
+ Revision: 351217
- rebuild
* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 2.9-2mdv2009.0
+ Revision: 218427
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.9-2mdv2008.1
+ Revision: 179533
- rebuild
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 2.9-1mdv2008.0
+ Revision: 76433
- rebuild for 2008
- fd.o icons
- correct xdg menu categories
- drop old menu and icons
- add new patch3 (we don't have system-wide copies of these headers as they vary depending on what kernel is installed, so let's just stop them from being read)
- rediff patch2
- drop patch0 and patch3 (patch3 reverted patch0...)
- minor spec clean
- new release 2.9
  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character
    - fix man pages extension
* Fri Aug 18 2006 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2006-08-18 09:04:40 (56726)
- add BuildRequires: libxt-devel libxaw-devel libxmu-devel
* Wed Aug 16 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-16 03:29:03 (56265)
- fix path according new x11
- xdg menu
* Wed Aug 16 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-16 03:18:00 (56264)
Import xcpustate
* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.5-21mdk
- Rebuild
* Thu Dec 23 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.5-20mdk
- fix buildrequires
- cleanups
* Wed Sep 01 2004 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 2.5-19mdk
- rebuild for rpm 4.2
