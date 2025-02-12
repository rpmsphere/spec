%define         privuser  schat
%define         privgroup schat
%define         privpath  /var/empty

Name:           schat
Version:        0.8.6.3549
Release:        7.1
Summary:        IMPOMEZIA Simple Chat
URL:            https://impomezia.com/project/schat
License:        GPLv3+
Group:          Networking/Chat
Source0:        %name-%version.tar.bz2
Source1:        schatd-logrotate
Source2:        %name.desktop
Source3:        %{name}d
Source4:        %name.conf
Source5:        %{name}d.sh
BuildRequires:  qtwebkit-devel

%description
IMPOMEZIA Simple Chat is a simple cross-platform client-server
chat for local networks and the Internet with the possibility
of individual settings for a specific network, with open source
code, written in Qt/C++.

%package server
Summary: Server for IMPOMEZIA Simple Chat (%name)
Group: System/Servers

%description server
Server for IMPOMEZIA Simple Chat (%name)

%prep
%setup -q

%build
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %{name}.pro
make

%install
install -Dp -m 0755 out/release/%name %buildroot/%_bindir/%name
install -Dp -m 0755 out/release/%{name}d %buildroot/%_sbindir/%{name}d
install -Dp -m 0755 %SOURCE3 %buildroot/etc/init.d/%{name}d
install -Dp -m 0644 %SOURCE4 %buildroot%_sysconfdir/%name/%name.conf
install -Dp -m 0755 %SOURCE5 %buildroot/%_sbindir/%{name}d.sh
install -Dp -m 0644 %SOURCE1 %buildroot/%_sysconfdir/logrotate.d/%name
install -Dp -m 0644 %SOURCE2 %buildroot/%_datadir/applications/%name.desktop

cp -a data/{motd.html,normalize.xml} %buildroot%_sysconfdir/%name/

# Data install
mkdir -p %buildroot/{%_datadir/%name,%_docdir/%name/html,%_datadir/%name/translations}
cp -a data/doc/members.html data/emoticons data/networks data/sounds %buildroot/%_datadir/%name/
cp -a data/doc/ChangeLog.html %buildroot/%_docdir/%name/html/
cp -a data/translations/*uk* %buildroot%_datadir/%name/translations/

# Icons
install -Dm644 data/images/%name.png %buildroot/%_datadir/pixmaps/%name.png

mkdir -p %buildroot/{%_sysconfdir/%name,/var/log/%name,/var/run/%name,%_localstatedir/%name}

%pre server
/usr/sbin/groupadd -r -f %privgroup
/usr/sbin/useradd -r -s /dev/null -g %privgroup -d %privpath >/dev/null -c 'schat daemon' %privuser >/dev/null 2>&1 ||:

%post server
%post_service %{name}d
service %{name}d condrestart

%preun server
service %{name}d condstop
# #/usr/sbin/userdel %privuser

%files
%_docdir/%name
%_bindir/%name
%_datadir/%name
%exclude %_datadir/%name/networks/SimpleNet.xml
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png

%files server
%_sbindir/*
/etc/init.d/%{name}d
%_sysconfdir/logrotate.d/%name
%attr(770,root,%privgroup) %_sysconfdir/%name
%attr(2660,root,%privgroup) %config(noreplace) %_sysconfdir/%name/%name.conf
%attr(2660,root,%privgroup) %config(noreplace) %_sysconfdir/%name/motd.html
%attr(2660,root,%privgroup) %config(noreplace) %_sysconfdir/%name/normalize.xml
%dir %attr(2770,root,%privgroup) /var/log/%name
%dir %attr(2770,root,%privgroup) /var/run/%name
%dir %attr(2770,root,%privgroup) %_localstatedir/%name

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.6.3549
- Rebuilt for Fedora

* Sun Mar 03 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.6-alt1.svn3549
- 0.8.6.3549

* Fri Mar 01 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.6-alt1.svn3539
- 0.8.6.3539

* Wed Feb 27 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.6-alt1.svn3531
- 0.8.6.3531

* Wed Nov 07 2012 Motsyo Gennadi <drool@altlinux.ru> 0.8.5-alt1.svn3271
- 0.8.5.3271

* Fri Feb 17 2012 Motsyo Gennadi <drool@altlinux.ru> 0.8.4-alt1.svn2311
- 0.8.4.2311

* Mon Feb 13 2012 Motsyo Gennadi <drool@altlinux.ru> 0.8.4-alt1.svn2297
- 0.8.4.2297

* Sat Aug 27 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.3-alt1.svn1675
- 0.8.3.1675

* Thu Aug 25 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.3-alt1.svn1668
- 0.8.3.1668 (add Ukrainian translation)

* Mon Aug 15 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.2-alt1.svn1637
- 0.8.2.1637 released (fixed build with Qt-4.4)

* Sat Aug 13 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.2-alt1.svn1629
- 0.8.2.1629 released

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.1-alt1.svn1452.qa1
- NMU (by repocop). See https://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for schat
  * postclean-03-private-rpm-macros for the spec file

* Wed Apr 20 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.1-alt1.svn1452
- 0.8.1.1452 released

* Sun Feb 13 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn1438
- 0.8.0.1438 released

* Fri Feb 04 2011 Motsyo Gennadi <drool@altlinux.ru> 0.7.5-alt0.1.svn1428
- svn 1428

* Tue Nov 23 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.4-alt1.svn1350
- release 0.7.4

* Fri Nov 12 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt2.svn1347
- svn 1347

* Fri Aug 27 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt2.svn1339
- svn 1339
- change license tag from GPLv3 to GPLv3+
- moved ChangeLog.html for search path

* Thu Aug 26 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt2.svn1333
- svn 1333

* Wed Aug 25 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt2.svn1329
- svn 1329

* Tue Aug 24 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt2.svn1325
- svn 1325
- release 0.7.3

* Thu Jul 22 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt0.1.svn1320.1
- fix repocop wanings (remove svn subdir, add condstop to init-script)

* Fri Jul 09 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt0.1.svn1320
- svn 1320

* Tue Jul 06 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt0.1.svn1317
- svn 1317
- create subpackage for schat-server

* Sun Jul 04 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt0.1.svn1313
- svn 1313

* Mon Jun 21 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt0.1.svn1296
- initial build for ALT Linux
