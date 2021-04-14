%undefine _debugsource_packages

Summary:	A KDE network sniffer application
Name:		ksniffer
Version:	0.3.2
Release:	8.1
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.ksniffer.org
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs3-devel
BuildRequires:	libpcap-devel

%description
KSniffer is a network statistics collector. It allows a user 
to watch all network traffic over any network interfaces 
connected to the host machine.KSniffer supports most TCP/IP 
protocols, (TCP, IP, UDP, ICMP, ARP, RARP as well as minimal IPX) 
KSniffer collects the # of packets, and # of bytes for each protocol. 
It also displays the activity in terms of kbits/sec, kbytes/sec and 
packets/sec. 
  
KSniffer also lets you watch port specific traffic for monitoring things 
like http, ftp, telnet, etc.

%prep
%setup -q

%build
%configure \
	--disable-rpath \
	--enable-nmcheck \
	--enable-pch \
	--enable-new-ldflags \
	--enable-final
make

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS README COPYING TODO VERSION
%{_datadir}/apps/ksniffer
%{_bindir}/ksniff*
%{_datadir}/applications/kde/ksniffer.desktop
%{_datadir}/icons/hicolor/*/apps/ksniffer.png

%changelog
* Sun May 05 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuilt for Fedora
* Thu Mar 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-5mdv2009.1
+ Revision: 361415
- rebuild
  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against libpcap-1.0.0
* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3.2-3mdv2009.0
+ Revision: 247897
- rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Tue Feb 26 2008 Funda Wang <fundawang@mandriva.org> 0.3.2-1mdv2008.1
+ Revision: 175396
- New version 0.3.2
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
* Tue Oct 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.1-1mdv2008.1
+ Revision: 96289
- new version
* Sun Jul 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3-1mdv2008.0
+ Revision: 54404
- update to final version
* Mon Jun 11 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3-0.alpha2.1mdv2008.0
+ Revision: 38074
- new version
* Thu Jun 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3-0.alpha1.1mdv2008.0
+ Revision: 36843
- fix file list
- new version
- drop P0
* Tue Mar 06 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-3mdv2007.0
+ Revision: 133966
- extend description a little bit
* Thu Feb 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-2mdv2007.1
+ Revision: 124353
- bump release tag
- add missing lang files
- new version
* Wed Feb 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2-0.rc1.1mdv2007.1
+ Revision: 117328
- add missing buildrequire
- Import ksniffer
