Name:           efax-gtk
Summary:        GTK2 front-end for efax
Version:        3.2.15
Release:        1
Group:          Communications/Fax
URL:            http://efax-gtk.sourceforge.net
License:        GPLv2
Source0:        http://downloads.sourceforge.net/efax-gtk/%{name}-%{version}.src.tgz
BuildRequires:  pkgconfig
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libtiff-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  c++-gtk-utils-gtk2-devel
Requires:       ghostscript
Requires:       cups
Requires:       gv
Requires:       efax

%description
A GUI front-end for the efax fax program. 
It interfaces with efax directly, replacing the scripts supplied
with efax. It can be used for receiving and sending faxes, and for
viewing, printing, and managing faxes which have been received and sent.

%prep
%setup -q
#sed -i -e 's|PS_VIEWER: gv|PS_VIEWER: evince|' -e 's|SOCK_SERVER: Yes|SOCK_SERVER: No|' efax-gtkrc
sed -i -e 's|/var/lock|/tmp|' -e 's|ttyS1|ttyS0|' -e 's|#WORK_SUBDIR:|WORK_SUBDIR: .config/efax-gtk|' efax-gtkrc

%build
%configure
sed -i 's|-Werror=format-security|-Wl,--allow-multiple-definition|g' Makefile */Makefile */*/Makefile
sed -i 's|install-data-hook||g' Makefile efax-gtk-faxfilter/Makefile
sed -i 's|usr/local|usr|g' Makefile
sed -i 's|efax-gtk.png|efax-gtk|g' efax-gtk.desktop
make

%install
%make_install

#menu
desktop-file-install --vendor="" \
  --remove-key="Encoding" \
  --remove-category="Application" \
  --remove-category="GTK" \
  --add-category="Telephony;" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

mv %{buildroot}%{_mandir}/man1/efax.1 %{buildroot}%{_mandir}/man1/efax-gtk.1
mv %{buildroot}%{_mandir}/man1/efix.1 %{buildroot}%{_mandir}/man1/efix-gtk.1
rm %{buildroot}%{_bindir}/efax-0.9a %{buildroot}%{_bindir}/efix-0.9a
ln -s efax %{buildroot}%{_bindir}/efax-0.9a
ln -s efix %{buildroot}%{_bindir}/efix-0.9a

%find_lang %{name}

%post
touch /tmp/faxfile.ps
chmod a+rw /tmp/faxfile.ps

%files -f %{name}.lang
%doc AUTHORS README BUGS COPYING
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_datadir}/pixmaps/%{name}.png
%{_localstatedir}/spool/fax/*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.15
- Rebuilt for Fedora
* Mon Sep 21 2015 barjac <barjac> 3.2.13-1.mga6
+ Revision: 882061
- new version 3.2.13
* Mon Aug 31 2015 cjw <cjw> 3.2.12-5.mga6
+ Revision: 871546
- rebuild with gcc 5
* Wed Oct 15 2014 umeabot <umeabot> 3.2.12-4.mga5
+ Revision: 743069
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 3.2.12-3.mga5
+ Revision: 678966
- Mageia 5 Mass Rebuild
* Sat Oct 19 2013 umeabot <umeabot> 3.2.12-2.mga4
+ Revision: 531769
- Mageia 4 Mass Rebuild
  + wally <wally>
    - fix source URL
* Sat Aug 10 2013 barjac <barjac> 3.2.12-1.mga4
+ Revision: 465049
- new version
- changed build require
- removed un-needed require
* Fri Jan 11 2013 umeabot <umeabot> 3.2.11-2.mga3
+ Revision: 349535
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Mon Jan 07 2013 barjac <barjac> 3.2.11-1.mga3
+ Revision: 341270
- new version 3.2.11
* Fri Sep 28 2012 barjac <barjac> 3.2.9-2.mga3
+ Revision: 299044
- Changed group to new policy
* Tue Feb 14 2012 barjac <barjac> 3.2.9-1.mga2
+ Revision: 208964
- new version
- changed BuildRequires, Added Requires
* Fri Dec 23 2011 fwang <fwang> 3.2.8-2.mga2
+ Revision: 186505
- rebuild for new libtiff
* Sat Dec 03 2011 shlomif <shlomif> 3.2.8-1.mga2
+ Revision: 175558
- New version 3.2.8.
* Sat Nov 19 2011 barjac <barjac> 3.2.5-1.mga2
+ Revision: 169028
- Added BR dbus-glib-devel, corrected menu category
- imported package efax-gtk
* Tue Nov 15 2011 Barry Jackson <zen25000[at]zen.co.uk> 3.2.5-1.mga2 
- Import efax-gtk. Removed BR libdbus-glib-1-devel.
* Tue Oct 19 2010 Ahmad Samir <ahmadsamir@mandriva.org> 3.2.5-1mdv2011.0
+ Revision: 586705
- update to 3.2.5
* Sun Sep 26 2010 Ahmad Samir <ahmadsamir@mandriva.org> 3.2.4-1mdv2011.0
+ Revision: 581044
- add BR, libdbus-glib-1-devel
- update to 3.2.4
- update license tag
- update file list
- clean spec and remove the "mdkversion < 200900" bits, too old now
* Fri Aug 21 2009 Frederik Himpe <fhimpe@mandriva.org> 3.0.20-1mdv2010.0
+ Revision: 419089
- update to new version 3.0.20
* Tue Jul 28 2009 Frederik Himpe <fhimpe@mandriva.org> 3.0.19-1mdv2010.0
+ Revision: 402570
- BuildRequires: libtiff-devel
- Update to new version 3.0.19
  + JM-CM-)rM-CM-4me Soyer <saispo@mandriva.org>
    - New upstream release
    - New upstream release
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Sat Nov 17 2007 JM-CM-)rM-CM-4me Soyer <saispo@mandriva.org> 3.0.16-1mdv2008.1
+ Revision: 109349
- New release
* Tue Jul 31 2007 JM-CM-)rM-CM-4me Soyer <saispo@mandriva.org> 3.0.15-1mdv2008.0
+ Revision: 56953
- New release 3.0.15
* Sun Apr 01 2007 JM-CM-)rM-CM-4me Soyer <saispo@mandriva.org> 3.0.14-1mdv2007.1
+ Revision: 150142
- New release
* Tue Mar 13 2007 JM-CM-)rM-CM-4me Soyer <saispo@mandriva.org> 3.0.13-1mdv2007.1
+ Revision: 142195
- New release 3.0.13
* Wed Jan 03 2007 JM-CM-)rM-CM-4me Soyer <saispo@mandriva.org> 3.0.12-1mdv2007.1
+ Revision: 103725
- Add BuildRequires
  + Lenny Cartier <lenny@mandriva.com>
    - Update to 3.0.12
    - Import efax-gtk
* Fri Aug 25 2006 Lenny Cartier <lenny@mandriva.com> 3.0.11-1mdv2007.0
- 3.0.11
- xdg
* Tue Jun 13 2006 Lenny Cartier <lenny@mandriva.com> 3.0.10-1mdv2007.0
- 3.0.10
* Mon Mar 13 2006 Austin Acton <austin@mandriva.org> 3.0.9-1mdk
- New release 3.0.9
* Mon Jan 16 2006 Lenny Cartier <lenny@mandriva.com> 3.0.8-1mdk
- 3.0.8
* Sun Dec 04 2005 Austin Acton <austin@mandriva.org> 3.0.7-1mdk
- New release 3.0.7
* Wed Nov 02 2005 Nicolas LM-icureuil <neoclust@mandriva.org> 3.0.6-2mdk
- Fix BuildRequires
* Tue Oct 18 2005 Lenny Cartier <lenny@mandriva.com> 3.0.6-1mdk
- 3.0.6
* Fri Oct 07 2005 Austin Acton <austin@mandriva.org> 3.0.5-1mdk
- New release 3.0.5
* Wed Aug 17 2005 Austin Acton <austin@mandriva.org> 3.0.4-1mdk
- New release 3.0.4
* Mon Jul 18 2005 Austin Acton <austin@mandriva.org> 3.0.3-1mdk
- New release 3.0.3
* Mon Jun 06 2005 Austin Acton <austin@mandriva.org> 3.0.2-1mdk
- New release 3.0.2
* Fri May 13 2005 Austin Acton <austin@mandriva.org> 3.0.1-1mdk
- New release 3.0.1
- source URL
* Tue May 10 2005 Austin Acton <austin@mandrake.org> 3.0.0-1mdk
- 3.0.0
- new buildrequires
* Sun Feb 27 2005 Austin Acton <austin@mandrake.org> 2.2.15-1mdk
- 2.2.15
* Mon Dec 27 2004 Austin Acton <austin@mandrake.org> 2.2.14-1mdk
- 2.2.14
* Sat Dec 25 2004 Austin Acton <austin@mandrake.org> 2.2.13-2mdk
- don't use /var/lock (bug #12684)
- use /dev/modem as default (bug #12684)
- thanks Richard Neill
* Sat Nov 20 2004 Austin Acton <austin@mandrake.org> 2.2.13-1mdk
- 2.2.13
* Mon Oct 25 2004 Austin Acton <austin@mandrake.org> 2.2.12-1mdk
- 2.2.12
* Sun Sep 26 2004 Austin Acton <austin@mandrake.org> 2.2.11-1mdk
- 2.2.11
- configure 2.5
* Mon Jul 26 2004 Austin Acton <austin@mandrake.org> 2.2.9-1mdk
- 2.2.9
* Sun Jun 20 2004 Austin Acton <austin@mandrake.org> 2.2.8-1mdk
- 2.2.8
* Thu Jun 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.2.7a-1mdk
- 2.2.7a
* Thu May 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.2.7-1mdk
- 2.2.7
