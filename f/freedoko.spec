%global ename FreeDoko
%undefine _debugsource_packages

Name:		freedoko
Version:	0.7.18
Release:	1
Summary:	FreeDoko is a Doppelkopf-game
Summary(de):	FreeDoko ist ein Doppelkopfspiel
Group:		Amusements/Games/Board/Card
License:	GPL
URL:		http://free-doko.sourceforge.net/de/index.html
Source0:	https://excellmedia.dl.sourceforge.net/project/free-doko/source/%{ename}_%{version}.src.zip
BuildRequires:	cairo-devel
BuildRequires:	docbook-utils
BuildRequires:	dos2unix unix2dos
BuildRequires:	gcc-c++
BuildRequires:	glib2-devel
BuildRequires:	gnet2-devel
BuildRequires:	gtkmm30-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pango-devel
#BuildRequires:	update-desktop-files
BuildRequires:	texlive-latex
BuildRequires:  texlive-german
BuildRequires:  texlive-babel-german
BuildRequires:  texlive-ucs
BuildRequires:  texlive-metafont
BuildRequires:  texlive-mfware
BuildRequires:  texlive-gsftopk
#BuildRequires:	hpijs-standalone
BuildRequires:	w3m
BuildRequires:	asciidoc
BuildRequires:	zlib-devel
BuildRequires:  freealut-devel

%description
FreeDoko is a Doppelkopf-game, written by Borg Enders and
Diether Knof.
It is developed under and for the platforms Linux and Windows.

NOTE: you must be a member of the group games to play the game!

Authors:
FreeDoko developers <free-doko-developer@lists.sourceforge.net>
Borg Enders <ben@BorgSoft.de>
Diether Knof <dknof@gmx.de>

%description -l de
FreeDoko ist ein Doppelkopfspiel, geschrieben von Borg Enders und
Diether Knof.
Es wird unter den und für die Plattformen Linux und Windows
geschrieben.

WICHTIG: man muss als Benutzer Mitglied in der Gruppe games sein!

Autoren:
FreeDoko developers <free-doko-developer@lists.sourceforge.net>
Borg Enders <ben@BorgSoft.de>
Diether Knof <dknof@gmx.de>

%package manual
Summary:		User documetation for FreeDoko
Summary(de):		Benutzerhandbuch für FreeDoko
Group:			Documentation/Other
BuildArch:		noarch

%description manual
Usermanual for FreeDoko.

Autoren:
FreeDoko developers <free-doko-developer@lists.sourceforge.net>
Borg Enders <ben@BorgSoft.de>
Diether Knof <dknof@gmx.de>

%description -l de manual
Benutzerhandbuch für %{ename}.

Autoren:
FreeDoko developers <free-doko-developer@lists.sourceforge.net>
Borg Enders <ben@BorgSoft.de>
Diether Knof <dknof@gmx.de>

%prep
%setup -q -n %{ename}_%{version}
sed -i '67,74s|^#||' Makefile.install.directories

%build
make compile

%install
%__rm -rf %{buildroot}
make install %{?jobs:-j%{jobs}} DESTDIR=%{buildroot} OPERATING_SYSTEM=Linux

%clean
%__rm -rf %{buildroot}

%files
#doc AUTHORS ChangeLog COPYING README Release.txt
%{_bindir}/FreeDoko
%{_bindir}/freedoko
%{_datadir}/%{ename}
%{_mandir}/man6/*
%{_datadir}/pixmaps/%{ename}.png
%{_datadir}/applications/%{ename}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{ename}.mo

%files manual
%{_docdir}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.18
- Rebuilt for Fedora
* Fri Jan 09 2009 Feather Mountain <john@ossii.com.tw> 0.7.5-567.ossii
- Rebuild for M6(OSSII)
* Fri Jun 06 2008 Toni Graffy <toni@links2linux.de> 0.7.5-567.pm.svn20080529
- update to 0.7.5 (svn 29.05.2008)
* Mon Apr 21 2008 Toni Graffy <toni@links2linux.de> 0.7.5-556.pm.svn20080420
- update to 0.7.5 (svn 20.04.2008)
* Sun Jan 06 2008 Toni Graffy <toni@links2linux.de> 0.7.5-536.pm.svn20080106
- update to 0.7.5 (svn 06.01.2008)
* Thu Dec 20 2007 Toni Graffy <toni@links2linux.de> 0.7.5-536.pm.svn20071216
- update to 0.7.5 (svn 16.12.2007)
* Mon Dec 03 2007 Toni Graffy <toni@links2linux.de> 0.7.5-529.pm.svn20071203
- update to 0.7.5 (svn 03.12.2007)
* Wed Sep 26 2007 Toni Graffy <toni@links2linux.de> 0.7.5-526.pm.svn20070924
- update to 0.7.5 (svn 24.09.2007)
* Sat Sep 08 2007 Toni Graffy <toni@links2linux.de> 0.7.5-517.pm.svn20070902
- update to 0.7.5 (svn 02.09.2007)
* Sun Aug 26 2007 Toni Graffy <toni@links2linux.de> 0.7.5-0.pm.svn20070825
- update to 0.7.5 (svn 25.08.2007)
* Fri Jul 20 2007 Toni Graffy <toni@links2linux.de> 0.7.5-0.pm.svn20070718
- update to 0.7.5 (svn 18.07.2007)
* Sat Jun 23 2007 Toni Graffy <toni@links2linux.de> 0.7.5-0.pm.svn20070622
- update to 0.7.5 (svn 22.06.2007)
* Sun May 13 2007 Toni Graffy <toni@links2linux.de> 0.7.5-0.pm.svn20070513
- update to 0.7.5 (svn 13.05.2007)
* Mon Mar 19 2007 Toni Graffy <toni@links2linux.de> 0.7.5-0.pm.svn20070319
- update to 0.7.5 (svn 19.03.2007)
* Sat Jan 27 2007 Toni Graffy <toni@links2linux.de> 0.7.4-1.pm.1
- update to 0.7.4 final
* Wed Jan 10 2007 Toni Graffy <toni@links2linux.de> 0.7.4-0.pm.svn20070110
- update to 0.7.4 (svn 10.01.2007)
* Tue Dec 05 2006 Toni Graffy <toni@links2linux.de> 0.7.4-0.pm.svn20061205
- update to 0.7.4 (svn 05.12.2006)
* Thu Nov 16 2006 Toni Graffy <toni@links2linux.de> 0.7.4-0.pm.svn20061116
- update to 0.7.4 (svn 16.11.2006)
 - using external Altenburg-cardset instead of xskat-cardset
* Tue Oct 31 2006 Toni Graffy <toni@links2linux.de> 0.7.4-0.pm.svn20061031
- update to 0.7.4 (svn 31.10.2006)
* Mon Oct 23 2006 Toni Graffy <toni@links2linux.de> 0.7.4-0.pm.svn20061022
- update to 0.7.4 (svn 22.10.2006)
* Tue Oct 17 2006 Toni Graffy <toni@links2linux.de> 0.7.4-0.pm.svn20061017
- update to 0.7.4 (svn 17.10.2006)
* Wed Oct 11 2006 Toni Graffy <toni@links2linux.de> 0.7.4-0.pm.svn20061011
- update to 0.7.4 (svn 11.10.2006)
* Sat Sep 30 2006 Toni Graffy <toni@links2linux.de> 0.7.4-0.pm.svn20061001
- update to 0.7.4 (svn 01.10.2006)
- corrected BuildRequires: gcc-c++, dos2unix
* Sun Sep 24 2006 Toni Graffy <toni@links2linux.de> 0.7.4-0.pm.svn20060924
- update to 0.7.4 (svn 24.09.2006)
* Sat Sep 16 2006 Toni Graffy <toni@links2linux.de> 0.7.4-0.pm.svn20060914
- update to 0.7.4 (svn 14.09.2006)
- initial build for packman
* Sun Sep 10 2006 oc2pus <oc2pus@arcor.de> 0.7.4-0.oc2pus.svn20060910
- update to 0.7.4 (svn 10.09.2006)
* Tue Sep 05 2006 oc2pus <oc2pus@arcor.de> 0.7.4-0.oc2pus.svn20060905
- update to 0.7.4 (svn 05.09.2006)
* Thu Aug 10 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.1
- update to 0.7.3
- clean up spec-file, removed html-manual
- removed patch, is in upstream
* Wed Aug 09 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060809
- update to 0.7.3 (svn 09.08.2006)
* Sat Aug 05 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060805
- update to 0.7.3 (svn 05.08.2006)
* Tue Aug 01 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060801
- update to 0.7.3 (svn 01.08.2006)
* Mon Jul 31 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060731
- update to 0.7.3 (svn 31.07.2006)
- removed html-manual (is online on website)
* Sun Jul 23 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060723
- update to 0.7.3 (svn 23.07.2006)
* Wed Jul 19 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060719
- update to 0.7.3 (svn 19.07.2006)
* Mon Jul 17 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060717
- update to 0.7.3 (svn 17.07.2006)
- removed neededforbuild
* Tue Jul 11 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060711
- update to 0.7.3 (svn 11.07.2006)
* Wed Jul 05 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060705
- update to 0.7.3 (svn 05.07.2006)
* Sat Jul 01 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060701
- update to 0.7.3 (svn 01.07.2006)
* Thu Jun 29 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060629
- update to 0.7.3 (svn 29.06.2006)
* Tue Jun 27 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060627
- update to 0.7.3 (svn 27.06.2006)
* Sat Jun 10 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060610
- update to 0.7.3 (svn 10.06.2006)
* Thu Jun 01 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060601
- update to 0.7.3 (svn 01.06.2006)
- removed patch "extra qualification"-error
* Tue May 23 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060523
- update to 0.7.3 (svn 23.05.2006)
* Sat May 20 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060520
- update to 0.7.3 (svn 20.05.2006)
* Thu May 11 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060511
- update to 0.7.3 (svn 11.05.2006)
* Mon May 08 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060508
- update to 0.7.3 (svn 08.05.2006)
* Wed May 03 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060503
- update to 0.7.3 (svn 03.05.2006)
* Fri Apr 28 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.svn20060428
- update to 0.7.3 (svn 28.04.2006)
- changed release-prefix to 0.oc2pus.svnYYYYMMDD
* Mon Apr 24 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.cvs20060424
- update to 0.7.3 (cvs 24.04.2006)
* Sun Apr 16 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.cvs20060416
- update to 0.7.3 (cvs 16.04.2006)
* Mon Apr 10 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.cvs20060410
- update to 0.7.3 (cvs 10.04.2006)
- added -n option to suse_update_desktop_files-call
* Wed Apr 05 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.cvs20060405
- update to 0.7.3 (cvs 05.04.2006)
* Thu Mar 30 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.cvs20060330
- update to 0.7.3 (cvs 30.03.2006)
* Thu Mar 23 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.cvs20060323
- update to 0.7.3 (cvs 23.03.2006)
- removed startscript
- moved all pdf-files to manual-package
* Thu Mar 16 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.cvs20060316
- update to 0.7.3 (cvs 16.03.2006)
* Fri Mar 10 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.cvs20060310
- update to 0.7.3 (cvs 10.03.2006)
* Sat Mar 04 2006 oc2pus <oc2pus@arcor.de> 0.7.3-0.oc2pus.cvs20060304
- update to 0.7.3 (cvs 04.03.2006)
* Sat Feb 26 2006 oc2pus <oc2pus@arcor.de> 0.7.2b-0.oc2pus.1
- update to 0.7.2b
- added Makefile.local
- repacked as tar.bz2
* Thu Aug 18 2005 oc2pus <oc2pus@arcor.de> 0.6.9-0.oc2pus.1
- Initial rpm build 0.6.9
