%undefine _debugsource_packages

Name:         crafty
BuildRequires: gcc-c++ unzip
License:      Contact author, Other License(s), see package
Group:        Amusements/Games/Board/Chess
Summary:      A Chess Program
Version:      25.2
Release:      1
URL:          https://www.craftychess.com/
Source:       ftp://ftp.cis.uab.edu/pub/hyatt/source/%{name}-%{version}.zip
Source1:      crafty-misc.tar.bz2
Source2:      bitmaps.tar.gz
Patch0:       %{name}-23.4.diff
Requires:     xboard

%description
A strong playing chess program. It uses opening books and endgame
databases. The graphical interface (xcrafty) requires the xboard
package.

Authors:
--------
    Bob Hyatt <hyatt@cis.uab.edu>

%prep
#setup -qc -D -a 1 -a 2
%setup -q -c -a 1 -a 2
mkdir .crafty
touch .craftyrc .crafty/book.bin .crafty/books.bin
chmod 755 bitmaps
chmod 644 bitmaps/*
rm bitmaps/gifs.tar
#%patch 0 -p1
%ifarch %ix86
sed -i 's|INLINE64|INLINE32|' Makefile
%else
sed -i 's|-mpopcnt||' Makefile
%endif
sed -i 's|-Wall|-Wall -fPIE|' Makefile

%build
make unix-gcc
sh make_books
# use large opening book
mv large_book.bin book.bin

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/usr/bin
install -m 755 crafty $RPM_BUILD_ROOT/usr/bin
install -m 755 xcrafty $RPM_BUILD_ROOT/usr/bin
install -m 755 speak $RPM_BUILD_ROOT/usr/bin/crafty-speak
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man6
install -m 644 crafty.6 $RPM_BUILD_ROOT%{_mandir}/man6
ln -s crafty.6.gz $RPM_BUILD_ROOT%{_mandir}/man6/xcrafty.6.gz
install -d -m 755 $RPM_BUILD_ROOT/usr/share/crafty/tb
install -d -m 755 $RPM_BUILD_ROOT/usr/share/crafty/bitmaps
install -d -m 755 $RPM_BUILD_ROOT/usr/share/crafty/sound
install -m 644 book.bin books.bin crafty.hlp $RPM_BUILD_ROOT/usr/share/crafty
install -m 644 tb/k[bnpqr]k.nb[bw].emd $RPM_BUILD_ROOT/usr/share/crafty/tb
install -m 644 bitmaps/* $RPM_BUILD_ROOT/usr/share/crafty/bitmaps

%files
%doc doc/crafty.doc
%doc doc/crafty.faq
%doc doc/read.me
%doc doc/tournament.howto
%doc README.SuSE
/usr/bin/crafty
/usr/bin/xcrafty
/usr/bin/crafty-speak
%{_mandir}/man6/crafty.6.gz
%{_mandir}/man6/xcrafty.6.gz
/usr/share/crafty

%changelog
* Sun Mar 19 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 25.2
- Rebuilt for Fedora
* Wed Sep 23 2009 snwint@suse.de
- update to version 23.0
* Fri Nov 16 2007 snwint@suse.de
- update to version 21.6
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Jan 13 2006 snwint@suse.de
- update to 20.1
- use larger opening book
* Thu Sep  8 2005 snwint@suse.de
- man page file permission fix (#114849)
* Fri Jul 15 2005 snwint@suse.de
- update to version 19.19
* Mon Sep 20 2004 snwint@suse.de
- fixed annotate bitmap path (found by Matthew Gatto)
- install crafty.hlp
- fixed some compile warnings
* Fri Sep  3 2004 snwint@suse.de
- new version
* Tue Apr 27 2004 ro@suse.de
- use RPM_OPT_FLAGS
- added -fno-strict-aliasing
* Thu Apr  1 2004 snwint@suse.de
- removed some strcpy()'s to avoid some security risk (#36274)
* Mon Mar  8 2004 snwint@suse.de
- new version
* Wed Jul 23 2003 coolo@suse.de
- use BuildRoot
* Sat Feb 15 2003 snwint@suse.de
- new version
* Tue Feb  4 2003 sbrabec@suse.cz
- Provide chess_backend.
* Wed Sep 11 2002 snwint@suse.de
- compile on ppc64
* Mon Aug 12 2002 snwint@suse.de
- upgraded to new version
* Fri Jul 12 2002 snwint@suse.de
- make it build on ppc64
* Tue May 28 2002 snwint@suse.de
- make it build on more archs
* Thu Mar 14 2002 snwint@suse.de
- fixed typo to make it build on non-ia32 archs
* Mon Feb 11 2002 snwint@suse.de
- updated to v18.13
- build without SMP support, the EGTB code doesn't like it
* Wed Jul 18 2001 snwint@suse.de
- use SMP on all architectures
* Tue Jul 17 2001 snwint@suse.de
- link with g++
- work around stdarg problem on ppc & s390
* Mon Jul 16 2001 snwint@suse.de
- upgraded to new version
* Mon Jun  4 2001 kukuk@suse.de
- Fix to compile on more non-x86 architectures
* Sat Dec  9 2000 nashif@suse.de
- sorted
* Wed Jun 21 2000 schwab@suse.de
- Fix makefile for ia64.
* Tue Mar 21 2000 ro@suse.de
- fixed to compile on alpha
* Sun Mar  5 2000 snwint@suse.de
- updated intel version; axp, ppc etc will need Makefile fixes
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Wed Aug 25 1999 uli@suse.de
- fixed for PPC
* Tue Jun 22 1999 uli@suse.de
- fixed for AXP
* Thu Jun 10 1999 snwint@suse.de
- wrote a man page
* Wed Jun  9 1999 snwint@suse.de
- created the package
- moved crafty's config/log/rc files to ~/.crafty/ and ~/.craftyrc
- tablebases are active by default
