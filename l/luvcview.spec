%undefine _debugsource_packages

Summary:	SDL-based video grabber
Name:		luvcview
Version: 	0.2.6
Release: 	11.1
Source0: 	%{name}-%{version}.tar.lzma
Source1: 	dynctrl-logitech.h
Source2: 	uvcvideo.h
Source3:	uvc_compat.h
Patch0:	 	linuxvideodev2.patch
License: 	GPLv2+
Group:		Video/Utilities
URL:		http://www.quickcamteam.net/software/linux/v4l2-software/luvcview
BuildRequires:	SDL-devel

%description
luvcview is a small video capture program ideal for webcam testing and
problem debugging.

%prep
%setup -q
cp %SOURCE1 .
cp %SOURCE2 .
cp %SOURCE3 .
%patch0 -p0

%build
make

%install
%__install -D -m 755 %{name} %{buildroot}/usr/bin/%{name}

%files
%doc README Changelog COPYING ToDo
%{_bindir}/%{name}

%changelog
* Wed Feb 18 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.6
- Rebuilt for Fedora
* Tue Sep 16 2014 umeabot <umeabot> 0.2.6-5.mga5
+ Revision: 682054
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 0.2.6-4.mga4
+ Revision: 507627
- Mageia 4 Mass Rebuild
* Sat Jan 12 2013 umeabot <umeabot> 0.2.6-3.mga3
+ Revision: 359140
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Fri Dec 07 2012 dams <dams> 0.2.6-2.mga3
+ Revision: 327852
- update %%group
* Wed Jun 08 2011 dams <dams> 0.2.6-1.mga2
+ Revision: 101784
- Fix linux/videodev2.h with a patch
- imported package luvcview
* Fri Aug 28 2009 Lev Givon <lev@mandriva.org> 0.2.6-1mdv2010.0
+ Revision: 422031
- Update to 0.2.6.
* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.4-2mdv2009.0
+ Revision: 268095
- rebuild early 2009.0 package (before pixel changes)
* Fri Jun 13 2008 Lev Givon <lev@mandriva.org> 0.2.4-1mdv2009.0
+ Revision: 218647
- import luvcview
* Wed May 28 2008 Lev Givon <lev@mandriva.org> 0.2.4-1mdv2008.1
- Package for Mandriva.
