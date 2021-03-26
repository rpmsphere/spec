Summary: 	Desktop for the Matchbox
Name: 		matchbox-desktop
Version: 	2.2
Release: 	10.1
URL: 		http://matchbox-project.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0: 	http://git.yoctoproject.org/cgit/cgit.cgi/matchbox-desktop-2/snapshot/matchbox-desktop-2-%{version}.tar.gz
BuildRequires:	pkgconfig
BuildRequires:	libmatchbox-devel
BuildRequires:	startup-notification-devel
BuildRequires:	gtk3-devel
Requires:	matchbox-panel
Requires:	matchbox-window-manager
Requires:	matchbox-common
Obsoletes:	matchbox-desktop-devel < %{version}-%{release}

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the main desktop from Matchbox.

%prep
%setup -q -n matchbox-desktop-2-2.2

%build
export LDFLAGS=-lX11
autoreconf -ifv
%configure --enable-startup-notification
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS README ChangeLog
%_bindir/%name

%changelog
* Thu Aug 16 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuild for Fedora
* Fri Oct 18 2013 umeabot <umeabot> 2.0-8.mga4
+ Revision: 507720
- Mageia 4 Mass Rebuild
* Sat Jan 12 2013 umeabot <umeabot> 2.0-7.mga3
+ Revision: 359423
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sat Dec 15 2012 pterjan <pterjan> 2.0-6.mga3
+ Revision: 331323
- Drop scriptlets, make_session seem empty nowadays
- Drop obsolete configure option
- Linx against libX11 (fixes build)
* Sun Apr 10 2011 dmorgan <dmorgan> 2.0-5.mga1
+ Revision: 82846
- Remove mdv macros
- imported package matchbox-desktop
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.0-5mdv2010.0
+ Revision: 429959
- rebuild
* Sat Sep 06 2008 Adam Williamson <awilliamson@mandriva.org> 2.0-4mdv2009.0
+ Revision: 281764
- obsoletes matchbox-desktop-devel (used to be part of this package up till
  2.0, now orphaned)
- one require per line
* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0-3mdv2009.0
+ Revision: 251955
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request
  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
* Tue Nov 06 2007 Funda Wang <fundawang@mandriva.org> 2.0-1mdv2008.1
+ Revision: 106243
- BR gtk+2
- New version 2.0
- import matchbox-desktop
* Mon Jan 24 2005 Austin Acton <austin@mandrake.org> 0.9.1-1mdk
- 0.9.1
* Tue Jan 5 2005 Austin Acton <austin@mandrake.org> 0.9-1mdk
- 0.9
* Tue Jul 27 2004 Austin Acton <austin@mandrake.org> 0.8.1-2mdk
- devel headers do not require main
- enable startup notification
* Tue Jul 27 2004 Austin Acton <austin@mandrake.org> 0.8.1-1mdk
- modules in /usr/lib (thanks to author)
* Wed Jul 21 2004 Austin Acton <austin@mandrake.org> 0.8-3mdk
- allow modules in /usr/share (not good)
* Wed Jul 21 2004 Austin Acton <austin@mandrake.org> 0.8-2mdk
- require common, panel, and window manager
- add wmsession config
* Mon Jul 20 2004 Austin Acton <austin@mandrake.org> 0.8-1mdk
- 0.8
