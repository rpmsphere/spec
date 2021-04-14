%{?!USE_GNUTLS: %define USE_GNUTLS 0}

Summary: Mascot Constructive Pilot for X
Name: macopix
Version: 3.4.0
Release: 1
License: chimari@kurumi.sakura.ne.jp
URL: http://rosegray.sakura.ne.jp/macopix
Group: Amusements/Games
Source0: http://rosegray.sakura.ne.jp/macopix/%{name}-%{version}.tar.gz
Obsoletes: age actx
BuildRequires:  libpng-devel
%define	gtk_conf_opt --program-transform-name='s/macopix/macopix/' 
BuildRequires: gtk3-devel

%if %{USE_GNUTLS}
# GNUTLS
%define	gnutls_conf_opt --with-gnutls
Requires: gnutls
BuildRequires: gnutls-devel
%else
# OPENSSL
%define	gnutls_conf_opt ""
Requires: openssl
BuildRequires: openssl-devel
%endif

%description
MaCoPiX is a desktop mascot application for UNIX / X Window system and Microsoft Windows.
 
%prep
%setup -q

%build
#export LIBS+=' -lX11'
#configure %{gtk_conf_opt} %{gnutls_conf_opt}
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_datadir}/macopix
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc README* NKR.README* AUTHORS ChangeLog* COPYING*
%{_bindir}/macopix
%{_mandir}/man1/*
%dir %{_datadir}/macopix

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.4.0
- Rebuilt for Fedora
* Sun Jun 10 2007 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- new upstream release 1.6.4
- support build with gnutls
* Wed May 30 2007 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 1.6.3c
* Sat May 19 2007 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- new upstream release 1.6.3
* Mon May 08 2007 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- new upstream release 1.6.2
- add openssl Requires tag
- add openssl-devel Buildprereq tag
- change *.jp -> *.ja in files section
* Wed May 02 2007 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- new upstream release 1.6.1
* Sun Oct 15 2006 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- new upstream release 1.4.1
- fix changelog typo
* Sat Sep 09 2006 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- new upstream release 1.4.0
* Fri Jun 03 2005 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 1.3.2
- change defalut target of configure script to Gtk+2.
- Build macopix with GTK+ 1, --define 'USE_GTK1 1'
* Fri Jun 03 2005 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 1.2.2
* Thu Oct 28 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 1.2.1
- update URL tag
* Mon Aug 09 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 1.2.0
* Thu Jul 22 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test relaase 1.2.0pre1
* Mon May 17 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 1.0.4
* Wed Apr 14 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 1.0.3
- drop patch1,2
* Fri Mar 05 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 3rd release 1.0.2
- add patch1 (change default nkf filter option with gtk2)
* Sun Feb 29 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 2nd release 1.0.2
* Tue Feb 24 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 1.0.2 for testing
- support make with gtk+2
- add patch0 (support libpng 1.2.5 configure)
* Wed Feb 11 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 2nd release 0.9.0
- Fix Requires tag typo
* Tue Feb 10 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 0.9.0
* Fri Jan 23 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 2nd release 0.9.0pre2 for testing
- add doc
- add Require libpng 
- add Buildprereq libpng-devel
- fix changelog typo
* Wed Jan 21 2004 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 0.9.0pre2 for testing
- add configure macro option
* Mon Sep 29 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 0.8.6
- add man to files list
* Sun May 25 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 2nd release 0.8.5
- remove rpm macros (distribution, vender) from build env
* Sun May 25 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 0.8.5
* Fri Apr 25 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 0.8.4
* Mon Apr 21 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 0.8.3
- change tarball format (gz -> bz2)
* Thu Apr 17 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 0.8.1
* Tue Apr 15 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 0.8.0
- add buildreq libtool >= 1.4, rpm-build
- del patch0 (included patch0 in new release source)
- change buildroot (use _tmppath)
* Wed Mar 26 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.2-20030318b-5
- fix POP3_FIX patch (undef pop3 debug flag)
* Tue Mar 25 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.2-20030318b-4
- update POP3_FIX patch (Fix POP3 Error recovery)
* Tue Mar 25 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.2-20030318b-3
- update POP3_FIX patch (included ja.po patch)
* Tue Mar 25 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.2-20030318b-2
- add POP3_FIX patch
* Wed Mar 19 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.2-20030318b-1
* Wed Mar 19 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.2-20030318-1
* Tue Mar 18 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.2-20030317b-1
- fix change log
* Tue Mar 18 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.2-20030317-1
* Mon Mar 17 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.2-20030316c-1
* Mon Mar 17 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.2-20030316-2
- del patch0 (included patch0 in new source)
* Mon Mar 17 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.0-20030312-1
- add pop3 pipe overflow patch
* Tue Mar 12 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.7.0-20030312-1
* Tue Mar 11 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.6.4-20030305-1
* Tue Mar 4 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.6.2-20030302-1
* Sun Mar 2 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.6.2-20030228-1
* Wed Feb 26 2003 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- change package name macopix
- test release 0.6.1-20030225b.tar.gz
* Fri Dec 26 2002 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.5.0-20021224-1
* Sat Dec 21 2002 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- change configure option
* Fri Dec 20 2002 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.5.0-20021216-2
- change make / make install method for gettext (thanx! sylpheed-vl.spec)
- add doc file to filelist
* Fri Dec 20 2002 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- test release 0.5.0-20021216-1
