%global __arch_install_post %{nil}

Name:		freepops
Version:	0.2.9
Release:	11
Summary:	POP3 interface to webmail
License:	GPLv2+
Group:		Networking/Mail
Source: 	http://prdownloads.sourceforge.net/freepops/%{name}-%{version}.tar.gz
Source1:	freepopsd.init.d
Source2:	freepopsd.sysconfig
Source3:	manual.pdf
Patch0:		freepops-0.2.9-fix-str-fmt.patch
Patch1:		freepops-0.2.8-configure.sh.patch
Patch2:		freepops-0.2.7-Makefile.patch
Patch3:		freepops-0.2.0-config.h.patch
#Patch4:	freepops-0.2.0-updater-dialog.patch
Patch5:		freepops-0.2.7-fltk-1.1.9.patch
Patch6:		freepops-0.2.9-curl_authopt-meta.patch
Patch7:		freepops-0.2.9-getdate-use-curl.patch
URL:		http://www.freepops.org
BuildRequires:  curl-devel
BuildRequires:  openssl-devel
BuildRequires:  lua-devel
BuildRequires:	compat-lua-devel
BuildRequires:  expat-devel
BuildRequires:  readline-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  fltk-devel
Requires:	lua mktemp dialog chkconfig

%description
FreePOPs is a daemon that acts as a local pop3 server, translating
local pop3 requests to remote http requests to supported webmails.

%package updater
Summary: The new FreePOPs updater (Fltk)
Group: Networking/Mail
Requires: freepops = %{version}-%{release} fltk

%description updater
Fltk based graphical user interface for FreePOPs updating mechanism

%prep
%setup -q
%patch0 -p0
%patch1 -p0 -b .configure
%patch2 -p0 -b .makefile
%patch3 -p0 -b .config
#%patch4 -p0 -b .dialog
%patch5 -p0 -b .fltk
%patch6 -p1 -b .curl_auth
%patch7 -p1 -b .getdate
cp -p %{SOURCE3} doc
sed -i 's|PKGCONFIG lua |PKGCONFIG lua-5.1 |' configure.sh

%build
./configure.sh linux -lua -fltk-ui 
make all WHERE=%{_prefix}/ LOCALEDIR=%{_datadir}/locale \
	CC="gcc $RPM_OPT_FLAGS" \
	HCC="gcc $RPM_OPT_FLAGS"

%install
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_datadir}/freepops/lua_unofficial
mkdir -p %{buildroot}%{_datadir}/freepops/lua_updates
mkdir -p %{buildroot}%{_datadir}/freepops/lua_updates/lxp
mkdir -p %{buildroot}%{_datadir}/freepops/lua_updates/browser
mkdir -p %{buildroot}%{_datadir}/freepops/lua_updates/soap

%make_install
rm -rf %{buildroot}/usr/share/doc/freepops
chmod +x %{buildroot}%{_bindir}/freepops-updater-dialog
chmod +x %{buildroot}%{_bindir}/freepops-updater-fltk
chmod +x %{buildroot}%{_bindir}/freepops-updater-zenity

install -p -m755 %{SOURCE1} %{buildroot}%{_initrddir}/freepopsd
install -p -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/freepopsd

%ifarch x86_64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%doc  doc/MANUAL.txt doc/manual.pdf COPYING INSTALL BUILD AUTHORS ChangeLog README README.modules TODO
%{_bindir}/freepopsd
%{_bindir}/freepops-updater-dialog
%{_bindir}/freepops-updater-zenity
%{_datadir}/freepops/*
%{_mandir}/man1/*
%{_initrddir}/freepopsd
#config(noreplace) %{_sysconfdir}/freepops/config.lua
%config(noreplace) %{_sysconfdir}/sysconfig/freepopsd

%files updater
%{_bindir}/freepops-updater-fltk
%{_libdir}/freepops/updater_fltk.so
%{_datadir}/locale/*/LC_MESSAGES/updater_fltk.mo

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.9
- Rebuild for Fedora
* Sun Jan 05 2014 pterjan <pterjan> 0.2.9-11.mga4
+ Revision: 564808
- Fix build
- Build against lua 5.1

  + umeabot <umeabot>
    - Mageia 4 Mass Rebuild
    - Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sun Apr 29 2012 colin <colin> 0.2.9-8.mga2
+ Revision: 234277
- Add LSB headers to initscripts (mga#5262)

  + shlomif <shlomif>
    - Fix build against newer libcurl and rebuild for the new fltk

  + dmorgan <dmorgan>
    - Rebuild against new fltk-devel

  + fwang <fwang>
    - rebuild for new fltk

* Thu Feb 24 2011 dmorgan <dmorgan> 0.2.9-4.mga1
+ Revision: 58225
- imported package freepops


* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.9-4mdv2011.0
+ Revision: 610769
- rebuild

* Sun Jun 06 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.2.9-3mdv2010.1
+ Revision: 547155
- fix post and preun service name

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 0.2.9-2mdv2010.1
+ Revision: 537380
- rebuild

* Fri Jan 08 2010 Emmanuel Andry <eandry@mandriva.org> 0.2.9-1mdv2010.1
+ Revision: 487753
- New version 0.2.9
- drop p4 (fixed differently upstream)
- diff p0 to fix format string not literal

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Dec 13 2008 Funda Wang <fwang@mandriva.org> 0.2.8-1mdv2009.1
+ Revision: 313988
- New version 0.2.8
- rediff configure patch
- updater should link with lua too

* Sat Dec 13 2008 Funda Wang <fwang@mandriva.org> 0.2.7-2mdv2009.1
+ Revision: 313967
- there is no fltk-config any more
- fix building with newer fltk
- rediff patch2

* Wed Aug 13 2008 Emmanuel Andry <eandry@mandriva.org> 0.2.7-2mdv2009.0
+ Revision: 271477
- Move locales in the right package

* Wed Aug 13 2008 Emmanuel Andry <eandry@mandriva.org> 0.2.7-1mdv2009.0
+ Revision: 271470
- New version
- fix license
- rediff patch 1
- update file list

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2.5-5mdv2009.0
+ Revision: 245400
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.2.5-3mdv2008.1
+ Revision: 109280
- rebuild for new lzma

* Tue Oct 30 2007 Jérôme Soyer <saispo@mandriva.org> 0.2.5-2mdv2008.1
+ Revision: 103861
- fix rpm groups
- hardcoding...
- Fix Patch
- Fix BR
- New release 0.2.5

  + Pascal Terjan <pterjan@mandriva.org>
    - rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Fri Feb 23 2007 Emmanuel Andry <eandry@mandriva.org> 0.0.99-2mdv2007.0
+ Revision: 125221
- fix buildrequires
- buildrequires bison
- rebuild for libcurl
- Import freepops

* Thu Jun 22 2006 Austin Acton <austin@mandriva.org> 0.0.99-1mdk
- New release 0.0.99

* Thu Mar 23 2006 Austin Acton <austin@mandriva.org> 0.0.98-1mdk
- 0.0.98
- source URL

* Mon Mar 06 2006 Austin Acton <austin@mandriva.org> 0.0.97-1mdk
- initial package

