%define pkgname Sjeng-Free

Name:           sjeng
Version:        11.2
Release:        19.1
Summary:        Chess program that plays many variants
License:        GPLv2
Group:          Games/Boards
URL:            https://sjeng.org/indexold.html
Source0:        https://prdownloads.sourceforge.net/sjeng/%{pkgname}-%{version}.tar.bz2
Source1:        sjeng.6.bz2
Source2:        sjeng-README.bz2
Patch0:         sjeng-11.2-cleanup.patch
Patch1:         sjeng-11.2-fhs.patch
Patch2:         sjeng-11.2-mga-fix-build-with-automake-1.13.patch
BuildRequires:  gdbm-devel

%description
Sjeng is a chess program that plays normal chess and many variants
like crazyhouse, bughouse, suicide (aka giveaway or anti-chess) and
losers. It can also play variants which have the same rules as normal
chess, but a different starting position. It uses the XBoard/WinBoard
interface by Tim Mann, so it can be used with xboard or eboard. It
is also capable of playing on internet chess servers.

%prep
%setup -q -n %{pkgname}-%{version}
%patch 0 -p1 -b .cleanup
%patch 1 -p1 -b .fhs
%patch 2 -p0

autoreconf -fiv
bzip2 -dc %{SOURCE2} > README.debian
# (Abel) supress annoying rpmlint warning message
perl -pi -e 's/\r//g' [[:upper:]][[:upper:]]* ChangeLog

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure \
        --bindir=%{_bindir} \
        --datadir=%{_datadir}
make

%install
%makeinstall
mkdir -p %{buildroot}%{_mandir}/man6
bzip2 -dc %{SOURCE1} > %{buildroot}%{_mandir}/man6/sjeng.6

%files
%doc AUTHORS BUGS ChangeLog NEWS README README.debian
%{_bindir}/*
%{_mandir}/man6/sjeng.6*

%changelog
* Tue May 19 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 11.2
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 11.2-15.mga5
+ Revision: 745034
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 11.2-14.mga5
+ Revision: 689177
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 11.2-13.mga4
+ Revision: 518291
- Mageia 4 Mass Rebuild
* Mon Jan 14 2013 umeabot <umeabot> 11.2-12.mga3
+ Revision: 382102
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sat Jan 05 2013 kamil <kamil> 11.2-11.mga3
+ Revision: 339197
- cleaning .spec
- add P2: fix-build-with-automake-1.13.patch and don't depend on automake-1.9
* Sun Dec 02 2012 kamil <kamil> 11.2-10.mga3
+ Revision: 324773
- rebuild for Mga3 Beta1
* Tue Dec 06 2011 fwang <fwang> 11.2-9.mga2
+ Revision: 177162
- rebuild for new gdbm
* Mon Oct 03 2011 obgr_seneca <obgr_seneca> 11.2-8.mga2
+ Revision: 151340
- imported package sjeng-free
* Sat Oct  1 2011 Kamil Rytarowski <n54@gmx.com> 11.2-8
- import to Mageia
- licensed under GPLv2
- it no more provides a "chessengine"
- cleanup
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 11.2-7mdv2010.0
+ Revision: 433894
- rebuild
* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 11.2-6mdv2009.0
+ Revision: 260745
- rebuild
* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 11.2-5mdv2009.0
+ Revision: 252496
- rebuild
- fix no-buildroot-tag
* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 11.2-3mdv2008.1
+ Revision: 127301
- kill re-definition of %%buildroot on Pixel's request
* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 22:20:48 (53026)
- fix deps
* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ Import sjeng-free
* Sun Jul 03 2005 Abel Cheung <deaddog@mandriva.org> 11.2-2mdk
- Incorporate everything from Debian: manpage, patches etc.
  Thanks to Lukas Geyer!
- Also attempt to read opening book from system-wide location
* Sat Jun 11 2005 Abel Cheung <deaddog@mandriva.org> 11.2-1mdk
- First Mandriva package
