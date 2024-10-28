%undefine _debugsource_packages

Name:           xman
Version:        1.1.5
Release:        1
Summary:        Manual page display program for the X Window System
Group:          Development/X11
License:        MIT
URL:            https://xorg.freedesktop.org
Source:         https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.gz
BuildRequires:  libXaw-devel
#BuildRequires: libXprintUtil-devel
BuildRequires:  libXp-devel
BuildRequires:  xorg-x11-util-macros

%description
Xman is a manual page display program for the X Window System.

%prep
%setup -q

%build
%configure --disable-xprint
make

%install
%make_install

%files
%{_bindir}/xman
%{_datadir}/X11/xman.help
%{_datadir}/X11/app-defaults/Xman
%{_mandir}/man1/xman.*

%changelog
* Sun Nov 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.5
- Rebuilt for Fedora
* Sat Oct 19 2013 umeabot <umeabot> 1.1.3-2.mga4
+ Revision: 534216
- Mageia 4 Mass Rebuild
* Mon Sep 09 2013 sander85 <sander85> 1.1.3-1.mga4
+ Revision: 476617
- New version: 1.1.3
* Mon Jan 14 2013 umeabot <umeabot> 1.1.2-2.mga3
+ Revision: 387114
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Jun 30 2011 tv <tv> 1.1.2-1.mga2
+ Revision: 116970
- new release
* Fri Jan 21 2011 ennael <ennael> 1.1.1-1.mga1
+ Revision: 27864
- imported package xman
* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 592500
- new release
* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 464744
- New version: 1.1.0
  Lzma and bzip2 patches integrated upstream
* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.3-7mdv2009.1
+ Revision: 366706
- no more autoconf needed
  + Antoine Ginies <aginies@mandriva.com>
    - rebuild
* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-6mdv2009.0
+ Revision: 226062
- rebuild
* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-5mdv2008.1
+ Revision: 166687
- Revert to use upstream tarball, build requires and remove non mandatory local patches.
* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-4mdv2008.1
+ Revision: 154425
- Updated BuildRequires and resubmit package.
  Switched to store patches in git repository (in branch mandriva+custom),
  and extract tarball with git-archive.
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 1.0.3-3mdv2008.1
+ Revision: 106450
- rebuild for new lzma
* Mon Oct 29 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 103565
- Add lzma support and defaults to no xprint support.
* Fri Aug 10 2007 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2008.0
+ Revision: 61656
- fix man extension
- new release
* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 21:09:36 (59517)
- rebuild to fix libXaw.so.8 dependency
* Tue Jun 06 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-06-06 19:37:48 (36717)
- added patch: support man pages compressed using bzip2
* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading
* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway
* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1
* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:34:52 (31402)
- fill in more missing descriptions
* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release
* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
