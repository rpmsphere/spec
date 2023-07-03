Summary: Tool to set up a Yum/Apt mirror from various sources
Name: mrepo
Version: 0.8.7
Release: 4
License: GPLv2
Group: System/Packaging
URL: https://dag.wieers.com/home-made/mrepo/
Source: https://dag.wieers.com/home-made/mrepo/mrepo-%{version}.tar.bz2
Patch0: mrepo-0.8.6-lsb-init.patch
BuildArch: noarch
Requires: python2, createrepo

%description
Tool to set up a Yum/Apt mirror from various sources 
(ISO, RHN, rsync, http, ftp, ...).

mrepo builds a local Apt/Yum RPM repository from local ISO files,
downloaded updates and extra packages from RHN and 3rd party
repositories.

It can download all updates and extras automatically, creates
the repository structure and meta-data, enables HTTP access to
the repository and creates a directory-structure for remote
network installations using PXE/TFTP.

mrepo supports ftp, http, sftp, rsync, rhn and other download methods.

With mrepo, you can enable your laptop or a local server to provide
updates for the whole network and provide the proper files to
allow installations via the network.

%prep
%setup -q
%patch0 -p1
%{__perl} -pi.orig -e 's|^(VERSION)\s*=\s*.+$|$1 = "%{version}"|' mrepo

%{__cat} <<EOF >config/mrepo.cron
### Enable this if you want mrepo to daily synchronize
### your distributions and repositories at 2:30am.
#30 2 * * * root /usr/bin/mrepo -q -ug
EOF

%{__cat} <<EOF >config/mrepo.conf
### Configuration file for mrepo

### The [main] section allows to override mrepo's default settings
### The mrepo-example.conf gives an overview of all the possible settings
[main]
srcdir = /var/mrepo
wwwdir = /var/www/mrepo
confdir = /etc/mrepo.conf.d
arch = i386 x86_64

mailto = root@localhost
smtp-server = localhost

#rhnlogin = username:password

### Any other section is considered a definition for a distribution
### You can put distribution sections in /etc/mrepo.conf.d/
### Examples can be found in the documentation at:
###     %{_docdir}/%{name}-%{version}/dists/.
EOF

%install
%make_install

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/up2date_client/*.py %{buildroot}%{_datadir}/%{name}/up2date_client/*/*.py %{buildroot}%{_bindir}/*

%preun
if [ $1 -eq 0 ]; then
	/etc/init.d/mrepo stop &>/dev/null || :
	/sbin/chkconfig --del mrepo
fi

%post
/sbin/chkconfig --add mrepo

#%postun
#/sbin/service mrepo condrestart &>/dev/null || :

%files
%doc AUTHORS ChangeLog COPYING README THANKS TODO WISHLIST config/*.conf config/dists/ docs/
%config(noreplace) %{_sysconfdir}/cron.d/mrepo
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mrepo.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/mrepo
%config(noreplace) %{_sysconfdir}/mrepo.conf
%config(noreplace) %{_sysconfdir}/mrepo.conf.d/
%config %{_initrddir}/mrepo
%{_bindir}/gensystemid
%{_bindir}/rhnget
%{_bindir}/mrepo
%{_bindir}/youget
%{_datadir}/mrepo/
/var/cache/mrepo/
/var/www/mrepo/
/var/mrepo/

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.7
- Rebuilt for Fedora
* Mon Feb 08 2016 umeabot <umeabot> 0.8.7-4.mga6
+ Revision: 944063
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 0.8.7-3.mga5
+ Revision: 750879
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.8.7-2.mga5
+ Revision: 682657
- Mageia 5 Mass Rebuild
* Sat Sep 06 2014 bcornec <bcornec> 0.8.7-1.mga5
+ Revision: 672470
- update mrepo to upstream 0.8.7
* Fri Oct 18 2013 umeabot <umeabot> 0.8.6-8.mga4
+ Revision: 521417
- Mageia 4 Mass Rebuild
* Tue Jan 22 2013 fwang <fwang> 0.8.6-7.mga3
+ Revision: 390774
- update rpm group
* Sat Jan 12 2013 umeabot <umeabot> 0.8.6-6.mga3
+ Revision: 360455
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Wed Apr 18 2012 pterjan <pterjan> 0.8.6-5.mga2
+ Revision: 231282
- Add missing whitespace in LSB header
* Wed Apr 18 2012 pterjan <pterjan> 0.8.6-4.mga2
+ Revision: 231276
- Add LSB header in initscript
- Silence tarball extraction
- Drop hardcoded packager tag
- Fix License tag
* Tue Dec 13 2011 bcornec <bcornec> 0.8.6-3.mga2
+ Revision: 181092
- Upload mrepo from Mandriva
- Created package structure for mrepo.
