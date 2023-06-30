Summary: 	Panel for the Matchbox Desktop
Name: 		matchbox-panel
Version: 	2.11
Release: 	20.1
URL: 		https://matchbox-project.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0:	https://git.yoctoproject.org/cgit.cgi/matchbox-panel-2/snapshot/matchbox-panel-2-%{version}.tar.gz
Patch0:     0001-applets-systray-Allow-icons-to-be-smaller.patch
BuildRequires:	libjpeg-devel desktop-file-utils
BuildRequires:	startup-notification-devel
BuildRequires:	glib2-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk3-devel
BuildRequires:	dbus-glib-devel

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the panel from Matchbox.

%package devel
Summary: Development files for %{name}
Requires: %{name}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q -n matchbox-panel-2-%{version}
%patch0 -p 1

%build
autoreconf -ifv
glib-gettextize --force --copy
export CFLAGS="%{optflags} -Wno-format-overflow"
%configure
make

%install
%makeinstall

%files
%doc AUTHORS README ChangeLog COPYING
%{_bindir}/%{name}
%{_libdir}/%{name}/*.so
%exclude %{_libdir}/%{name}/*.la
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/%{name}

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Aug 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.11
- Rebuilt for Fedora
* Fri Oct 18 2013 umeabot <umeabot> 0.9.3-8.mga4
+ Revision: 507722
- Mageia 4 Mass Rebuild
* Sat Jan 12 2013 umeabot <umeabot> 0.9.3-7.mga3
+ Revision: 359426
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Fri Jan 11 2013 fwang <fwang> 0.9.3-6.mga3
+ Revision: 345494
- fix build with latest automake 1.13
- rebuild for new iw
* Fri Dec 28 2012 wally <wally> 0.9.3-5.mga3
+ Revision: 335896
- fix desktop files
- add patch to fix linking
- clean .spec a bit
* Sun Apr 10 2011 dmorgan <dmorgan> 0.9.3-4.mga1
+ Revision: 82928
- imported package matchbox-panel
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.9.3-4mdv2010.0
+ Revision: 429962
- rebuild
* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.3-3mdv2009.0
+ Revision: 252013
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request
* Mon Nov 05 2007 Funda Wang <fundawang@mandriva.org> 0.9.3-1mdv2008.1
+ Revision: 106046
- New version 0.9.3
- import matchbox-panel
* Fri Nov 25 2005 Austin Acton <austin@mandriva.org> 0.9.2-3mdk
- Rebuild
* Fri Jul 29 2005 Olivier Blin <oblin@mandriva.com> 0.9.2-2mdk
- rebuild for new libiw
* Thu May 12 2005 Austin Acton <austin@mandriva.org> 0.9.2-1mdk
- 0.9.2
* Mon Jan 24 2005 Austin Acton <austin@mandrake.org> 0.9.1-1mdk
- 0.9.1
* Mon Jan 10 2005 Austin Acton <austin@mandrake.org> 0.9-1mdk
- 0.9
* Mon Aug 30 2004 Austin Acton <austin@mandrake.org> 0.8.3-1mdk
- 0.8.3
* Tue Jul 27 2004 Austin Acton <austin@mandrake.org> 0.8.2-1mdk
- 0.8.2
* Mon Jul 20 2004 Austin Acton <austin@mandrake.org> 0.8.1-1mdk
- 0.8.1
