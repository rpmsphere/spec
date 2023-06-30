%define webappsdir %{_sysconfdir}/httpd/conf.d

Summary:	GForge Collaborative Development Environment
Name:		gforge
Version:	4.5.19
Release:	1
License:	GPL
Group:		System/Servers
URL:		https://www.gforge.org/
Source0:	https://gforge.org/frs/download.php/103/%{name}-%{version}.tar.bz2
Source1:	gforge-lib-jpgraph-1.5.2.tar.bz2
Source2:	html_docs.tar.bz2
Source10:	sample-apache.vhost.in.bz2
Source11:	local.pl.in.bz2
Source20:	gforge.cron.bz2
Source21:	gforge-plugin-cvstracker.cron.bz2
Source22:	gforge-plugin-scmcvs.cron.bz2
Source23:	gforge-plugin-scmsvn.cron.bz2
Patch0:		gforge-4.5.6-mdv_conf.diff
Patch1:		gforge-4.5.6-autofoo.diff
Patch100:	gforge-lib-jpgraph-1.5.2-fake.patch
Patch101:	gforge-lib-jpgraph-1.5.2-rh9.patch
Requires:	rcs cvs mailman postgresql postgresql-server postgresql-pl
Requires:	perl-DBD-Pg perl-DBI perl-HTML-Parser perl-IPC-Run perl-URI
Requires:	php-cli php-gd php-ldap php-mbstring php-pgsql mod_php
Requires:	mod_auth_gforge
#Requires:	jpgraph viewvc
BuildRequires:	autoconf
BuildArch:	noarch
#BuildRequires:	libxslt-proc docbook-style-xsl docbook-style-xsl libxml2-utils

%define py_ver %(python -c "import sys; v=sys.version_info[:2]; print '%%d.%%d'%%v" 2>/dev/null || echo PYTHON-NOT-FOUND)
%define py_prefix  %(python -c "import sys; print sys.prefix" 2>/dev/null || echo PYTHON-NOT-FOUND)
%define py_libdir  %{py_prefix}/%{_lib}/python%{py_ver}
%define py_sitedir %{py_libdir}/site-packages

%description
GForge is a web-based Collaborative Development Environment
offering easy access to CVS, mailing lists, bug tracking, message
boards/forums, task management, permanent file archival, and total
web-based administration.

%package	plugin-scmcvs
Summary:	CVS Plugin for GForge CDE
Group:		System/Servers
Requires:	cvs viewvc
Requires(post): %{name} >= %{version}
Requires(preun): %{name} >= %{version}
Requires:	%{name} >= %{version}

%description	plugin-scmcvs
This plug-in contains the CVS subsystem of Gforge. It allows each
Gforge project to have its own CVS repository, and gives some control
over it to the project's administrator.

%package	plugin-scmsvn
Summary:	SVN (Subversion) Plugin for GForge CDE
Group:		System/Servers
Requires:	subversion viewvc
Requires(post): %{name} >= %{version}
Requires(preun): %{name} >= %{version}
Requires:	%{name} >= %{version}

%description	plugin-scmsvn
This plug-in contains the Subversion subsystem of Gforge. It
allows each Gforge project to have its own Subversion repository,
and gives some control over it to the project's administrator.

%package	plugin-cvstracker
Summary:	CVS Tracker Plugin for GForge CDE
Group:		System/Servers
Requires(post): %{name} >= %{version}
Requires(preun): %{name} >= %{version}
Requires:	%{name} >= %{version}
Requires:	gforge-plugin-scmcvs

%description	plugin-cvstracker
This RPM installs CVS tracker plugin for GForge CDE which allows to link
cvs logs to trackers and tasks in GForge.

%prep

%setup -q -a1 -a2
# tuck away these first
cp etc/local.inc.example etc/local.inc.example.bak
cp plugins/scmcvs/etc/plugins/scmcvs/config.php plugins/scmcvs/etc/plugins/scmcvs/config.php.bak
cp plugins/cvstracker/etc/plugins/cvstracker/config.php plugins/cvstracker/etc/plugins/cvstracker/config.php.bak
%patch0 -p1

cp etc/local.inc.example contrib/autoconf/local.inc.in
cp plugins/scmcvs/etc/plugins/scmcvs/config.php contrib/autoconf/scmcvs-config.php.in
cp plugins/cvstracker/etc/plugins/cvstracker/config.php contrib/autoconf/cvstracker-config.php.in
bzcat %{SOURCE10} > contrib/autoconf/sample-apache.vhost.in
bzcat %{SOURCE11} > contrib/autoconf/local.pl.in

cp etc/local.inc.example.bak etc/local.inc.example
cp plugins/scmcvs/etc/plugins/scmcvs/config.php.bak plugins/scmcvs/etc/plugins/scmcvs/config.php
cp plugins/cvstracker/etc/plugins/cvstracker/config.php.bak plugins/cvstracker/etc/plugins/cvstracker/config.php

%patch1 -p0

pushd contrib/autoconf
    rm -f configure; autoconf
popd

bzcat %{SOURCE20} > gforge.cron
bzcat %{SOURCE21} > gforge-plugin-cvstracker.cron
bzcat %{SOURCE22} > gforge-plugin-scmcvs.cron
bzcat %{SOURCE23} > gforge-plugin-scmsvn.cron

#find . -type d -perm 0700 -exec chmod 755 {} \;
#find . -type f -perm 0555 -exec chmod 755 {} \;
#find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# corrections
find -type f -print0|xargs -0 perl -p -i -e "s|^#\! /usr/bin/php4|#\!/usr/bin/php|g; \
    s|/opt/gforge/gforge/plugins|/var/www/gforge/plugins|g; \
    s|/usr/share/gforge|/var/www/gforge|g; \
    s|/usr/lib/gforge|/var/www/gforge|g; \
    s|/usr/lib/mailman|%{_libdir}/mailman|g"

# cosmetics + rpmlint antidote
find -type f -print0|xargs -0 perl -p -i -e "s|^# \!/usr/bin|#\!/usr/bin|g; \
    s|^# \!/bin|#\!/bin|g"

# fix python libdir path
find -type f -print0|xargs -0 perl -p -i -e "s|/usr/lib/python2\.3/|%{py_libdir}/|g"

# strip away annoying ^M
find -type f -print0|xargs -0 file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

# fix gforge-lib-jpgraph-1.5.2
pushd gforge-lib-jpgraph-1.5.2
%patch100 -p1
%patch101 -p1
popd

%build

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{webappsdir}

install -d %{buildroot}/bin
install -d %{buildroot}%{_sysconfdir}/cron.d

install -d %{buildroot}%{_sysconfdir}/gforge/autoconf
install -d %{buildroot}%{_sysconfdir}/gforge/httpd.d
install -d %{buildroot}%{_sysconfdir}/gforge/plugins

install -d %{buildroot}/var/cache/gforge

install -d %{buildroot}/var/www/gforge/bin
install -d %{buildroot}/var/www/gforge/lib
install -d %{buildroot}/var/www/gforge/plugins

install -d %{buildroot}%{_localstatedir}/gforge/uploads
install -d %{buildroot}%{_localstatedir}/gforge/download
install -d %{buildroot}%{_localstatedir}/gforge/scmtarballs
install -d %{buildroot}%{_localstatedir}/gforge/scmsnapshots
install -d %{buildroot}%{_localstatedir}/gforge/localizationcache

install -d %{buildroot}%{_localstatedir}/gforge/chroot
install -d %{buildroot}%{_localstatedir}/gforge/chroot/home
install -d %{buildroot}%{_localstatedir}/gforge/chroot/home/users
install -d %{buildroot}%{_localstatedir}/gforge/chroot/home/groups

install -d %{buildroot}%{_localstatedir}/jpgraph

# project vhost space
install -d %{buildroot}%{_localstatedir}/gforge/homedirs
install -d %{buildroot}/home/groups
ln -s /home/groups %{buildroot}%{_localstatedir}/gforge/homedirs/groups

# Create default location for SVN repositories
install -d %{buildroot}%{_localstatedir}/gforge/svnroot
ln -s %{_localstatedir}/gforge/svnroot %{buildroot}/svnroot

# Create default location for CVS repositories
install -d %{buildroot}%{_localstatedir}/gforge/cvsroot
ln -s %{_localstatedir}/gforge/cvsroot %{buildroot}/cvsroot

# sets up pretty xslt pages for svn when browsing with a web browser
install -m0644 cronjobs/dav-svn/www/svnindex* %{buildroot}/var/www/gforge/bin/

# restricted shell for cvs accounts
install -m0755 cronjobs/cvs-cron/cvssh.pl %{buildroot}/bin/

# Create default location for gforge config files
install -m0644 etc/local.inc.example %{buildroot}%{_sysconfdir}/gforge/local.inc.example
install -m0644 etc/gforge-httpd.conf.example %{buildroot}%{_sysconfdir}/gforge/httpd.conf.example

# copy viewvc and make sure it's in the local.inc sys_scmweb path
ln -s /var/www/cgi-bin/viewcvs.cgi %{buildroot}%{_sysconfdir}/gforge/viewcvs.cgi

# install the main stuff
for i in common cronjobs db utils www ; do
    cp -a $i %{buildroot}/var/www/gforge/
done

# install autocond stuff
install -m0644 contrib/autoconf/*.in %{buildroot}%{_sysconfdir}/gforge/autoconf/
install -m0644 contrib/autoconf/*.ac %{buildroot}%{_sysconfdir}/gforge/autoconf/
install -m0644 contrib/autoconf/README* %{buildroot}%{_sysconfdir}/gforge/autoconf/
install -m0755 contrib/autoconf/configure %{buildroot}%{_sysconfdir}/gforge/autoconf/
touch %{buildroot}%{webappsdir}/gforge.conf
touch %{buildroot}%{_sysconfdir}/gforge/local.pl

install -m0755 utils/include.pl %{buildroot}/var/www/gforge/lib/

# cron
install -m0664 gforge.cron %{buildroot}%{_sysconfdir}/cron.d/gforge

################################################################################
# CVS Plugin for GForge CDE
install -d %{buildroot}%{_sysconfdir}/gforge/plugins/scmcvs/languages
install -d %{buildroot}/var/www/gforge/plugins/scmcvs/cgi-bin

install -m0644 gforge-plugin-scmcvs.cron %{buildroot}%{_sysconfdir}/cron.d/gforge-plugin-scmcvs

for dir in bin include lib www; do
    cp -a plugins/scmcvs/$dir %{buildroot}/var/www/gforge/plugins/scmcvs/
done

install -m0755 plugins/scmcvs/cgi-bin/cvsweb %{buildroot}/var/www/gforge/bin/
install -m0755 plugins/scmcvs/cgi-bin/cvsweb %{buildroot}/var/www/gforge/plugins/scmcvs/cgi-bin/

cp -a plugins/scmcvs/etc/* %{buildroot}%{_sysconfdir}/gforge/

install -m0644 plugins/scmcvs/etc/plugins/scmcvs/config.php.bak %{buildroot}%{_sysconfdir}/gforge/plugins/scmcvs/config.php
install -m0644 plugins/scmcvs/etc/plugins/scmcvs/cvsweb.conf %{buildroot}%{_sysconfdir}/gforge/plugins/scmcvs/

################################################################################
# SVN Plugin for GForge CDE
install -d %{buildroot}%{_sysconfdir}/gforge/plugins/scmsvn/languages
install -d %{buildroot}/var/www/gforge/plugins/scmsvn/cgi-bin

install -m0644 gforge-plugin-scmsvn.cron %{buildroot}%{_sysconfdir}/cron.d/gforge-plugin-scmsvn

for dir in bin cronjobs include lib www; do
    cp -a plugins/scmsvn/$dir %{buildroot}/var/www/gforge/plugins/scmsvn/
done

install -m0755 plugins/scmsvn/cgi-bin/viewcvs.cgi %{buildroot}/var/www/gforge/bin/
install -m0755 plugins/scmsvn/cgi-bin/viewcvs.cgi %{buildroot}/var/www/gforge/plugins/scmsvn/cgi-bin/

cp -a plugins/scmsvn/etc/* %{buildroot}%{_sysconfdir}/gforge/
install -m0644 plugins/scmsvn/etc/plugins/scmsvn/config.php %{buildroot}%{_sysconfdir}/gforge/plugins/scmsvn/

################################################################################
# CVS Tracker Plugin for GForge CDE
install -d %{buildroot}/var/www/gforge/plugins/cvstracker
install -d %{buildroot}%{_sysconfdir}/gforge/plugins/cvstracker

install -m0644 gforge-plugin-cvstracker.cron %{buildroot}/%{_sysconfdir}/cron.d/gforge-plugin-cvstracker

for dir in bin include lib www; do
    cp -a plugins/cvstracker/$dir %{buildroot}/var/www/gforge/plugins/cvstracker/
done;

install -m0644 plugins/cvstracker/etc/plugins/cvstracker/config.php.bak %{buildroot}%{_sysconfdir}/gforge/plugins/cvstracker/config.php

################################################################################
# gforge-lib-jpgraph-1.5.2
install -d %{buildroot}/var/www/gforge/jpgraph
install -m0644 gforge-lib-jpgraph-1.5.2/src/*.php %{buildroot}/var/www/gforge/jpgraph/
cp gforge-lib-jpgraph-1.5.2/COPYING COPYING.jpgraph
cp gforge-lib-jpgraph-1.5.2/README README.jpgraph
cp gforge-lib-jpgraph-1.5.2/src/Changelog Changelog.jpgraph

# fix attribs
find %{buildroot}/var/www/gforge -type d -print0 -exec chmod 755 {} \;
find %{buildroot}/var/www/gforge -type f -name "*.php" -print0 -exec chmod 644 {} \;
find %{buildroot}/var/www/gforge -type f -name "*.sql" -print0 -exec chmod 644 {} \;
find %{buildroot}/var/www/gforge -type f -name "*.sh" -print0 -exec chmod 755 {} \;
find %{buildroot}/var/www/gforge -type f -name "*.pl" -print0 -exec chmod 755 {} \;

# cleanup not wanted stuff
rm -rf docs/docbook

# fix directory lists
find %{buildroot}%{_sysconfdir}/gforge -type d | sed -e "s|%{buildroot}||" | grep -v "/gforge/plugins" | sed -e 's/^/%attr(0755,root,apache) %dir /' > %{name}.filelist
find %{buildroot}/var/www/gforge -type d | sed -e "s|%{buildroot}||" | grep -v "/var/www/gforge/plugins" | sed -e 's/^/%attr(0755,root,apache) %dir /' >> %{name}.filelist
find %{buildroot}/var/www/gforge/plugins/scmcvs -type d | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(0755,root,apache) %dir /' > %{name}-plugin-scmcvs.filelist
find %{buildroot}/var/www/gforge/plugins/scmsvn -type d | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(0755,root,apache) %dir /' > %{name}-plugin-scmsvn.filelist
find %{buildroot}/var/www/gforge/plugins/cvstracker -type d | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(0755,root,apache) %dir /' > %{name}-plugin-cvstracker.filelist

# fix file lists
find %{buildroot}/var/www/gforge -type f | sed -e "s|%{buildroot}||" | grep -v "/var/www/gforge/plugins" | sed -e 's/^/%attr(-,root,apache) /' >> %{name}.filelist
find %{buildroot}/var/www/gforge/plugins/scmcvs -type f | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(-,root,apache) /' >> %{name}-plugin-scmcvs.filelist
find %{buildroot}/var/www/gforge/plugins/scmsvn -type f | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(-,root,apache) /' >> %{name}-plugin-scmsvn.filelist
find %{buildroot}/var/www/gforge/plugins/cvstracker -type f | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(-,root,apache) /' >> %{name}-plugin-cvstracker.filelist

# add a simple README
cat > README.Mandriva << EOF

simple installation draft

T H E   G F O R G E   Q U I C K   H O W T O
-------------------------------------------

Change directory to %{_sysconfdir}/gforge/autoconf/ and issue

./configure --help

Run configure with the appropriate switches to generate the gforge
config files. Copy the files to where they are supposed to live:

cp cvstracker-config.php %{_sysconfdir}/gforge/plugins/cvstracker/config.php
cp scmcvs-config.php %{_sysconfdir}/gforge/plugins/scmcvs/config.php
cp local.inc %{_sysconfdir}/gforge/
cp local.pl%{_sysconfdir}/gforge/
cp sample-apache.vhost %{webappsdir}/gforge.conf

Later this step will be taken care of using a Makefile for example.

Read how to populate the postgresql database in the provided documentation.

EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}/var/www/gforge/cronjobs/cvs-cron/syncmail %{buildroot}/var/www/gforge/plugins/scm*/*bin/* %{buildroot}/var/www/gforge/bin/viewcvs.cgi

%pre
/usr/sbin/useradd -d /var/www/gforge -s /bin/sh gforge

%postun
/usr/sbin/userdel gforge

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files -f %{name}.filelist
%doc AUTHORS* Change* COPYING* INSTALL README* docs/* html_docs contrib
%attr(0640,root,apache) %config(noreplace) %{webappsdir}/gforge.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/gforge

%attr(0644,root,root) %{_sysconfdir}/gforge/httpd.d/*
%attr(0644,root,root) %{_sysconfdir}/gforge/*.example
%attr(0640,apache,gforge) %config(noreplace) %{_sysconfdir}/gforge/local.pl

%{_sysconfdir}/gforge/viewcvs.cgi

%attr(0644,root,root) %{_sysconfdir}/gforge/autoconf/*.in
%attr(0644,root,root) %{_sysconfdir}/gforge/autoconf/README*
%attr(0644,root,root) %{_sysconfdir}/gforge/autoconf/configure.ac
%attr(0755,root,root) %{_sysconfdir}/gforge/autoconf/configure

%attr(0755,root,root) /bin/cvssh.pl
#attr(0755,root,root) %dir /cvsroot
#attr(0755,root,root) %dir /svnroot

#%attr(0755,root,root) /var/www/gforge/bin/cvsweb
#%attr(0755,root,root) /var/www/gforge/bin/viewcvs.cgi
#attr(0755,root,root) /var/www/gforge/cronjobs/mail/privatize_list.py?

%attr(0775,apache,apache) %dir %{_localstatedir}/gforge/uploads
%attr(0775,apache,apache) %dir %{_localstatedir}/gforge/download
%attr(0775,apache,apache) %dir %{_localstatedir}/gforge/scmsnapshots
%attr(0775,apache,apache) %dir %{_localstatedir}/gforge/scmtarballs
#attr(0775,apache,apache) %dir %{_localstatedir}/gforge/homedirs/groups

%attr(0775,apache,apache) %dir /var/cache/gforge
%attr(0775,apache,apache) %dir %{_localstatedir}/jpgraph

%attr(0755,root,root) %dir %{_localstatedir}/gforge/chroot
%attr(0755,root,root) %dir %{_localstatedir}/gforge/chroot/home
%attr(0755,root,root) %dir %{_localstatedir}/gforge/chroot/home/users
%attr(0755,root,root) %dir %{_localstatedir}/gforge/chroot/home/groups
/cvsroot
/svnroot
/var/gforge/homedirs/groups
/var/www/gforge/cronjobs/mail/privatize_list.py*

%files plugin-scmcvs -f %{name}-plugin-scmcvs.filelist
%doc plugins/scmcvs/AUTHORS plugins/scmcvs/README plugins/scmcvs/TODO
%dir %{_sysconfdir}/gforge/plugins/scmcvs
%dir %{_sysconfdir}/gforge/plugins/scmcvs/languages
%attr(0664,apache,gforge) %config(noreplace) %{_sysconfdir}/gforge/plugins/scmcvs/config.php
%exclude %{_sysconfdir}/gforge/plugins/scmcvs/config.php.bak 
%exclude %{_sysconfdir}/gforge/plugins/scmcvs/config.php.orig
%attr(0664,apache,gforge) %config(noreplace) %{_sysconfdir}/gforge/plugins/scmcvs/cvsweb.conf
%attr(0664,root,root) %config(noreplace) %{_sysconfdir}/cron.d/gforge-plugin-scmcvs
%{_sysconfdir}/gforge/httpd.d/*cvs*
%attr(0755,root,root) /var/www/gforge/bin/cvsweb
#/var/www/gforge/plugins/scmcvs

%files plugin-scmsvn -f %{name}-plugin-scmsvn.filelist
%doc plugins/scmsvn/README
%dir %{_sysconfdir}/gforge/plugins/scmsvn
%dir %{_sysconfdir}/gforge/plugins/scmsvn/languages
%attr(0664,apache,gforge) %config(noreplace) %{_sysconfdir}/gforge/plugins/scmsvn/config.php
%attr(0664,root,root) %config(noreplace) %{_sysconfdir}/cron.d/gforge-plugin-scmsvn
%attr(0755,root,root) /var/www/gforge/bin/viewcvs.cgi
#/var/www/gforge/plugins/scmsvn

%files plugin-cvstracker -f %{name}-plugin-cvstracker.filelist
%doc plugins/cvstracker/AUTHORS plugins/cvstracker/README
%attr(0664,apache,gforge) %config(noreplace) %{_sysconfdir}/gforge/plugins/cvstracker/config.php
#%attr(0664,apache,gforge) %config(noreplace) %{_sysconfdir}/gforge/plugins/cvstracker/cvstracker.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/gforge-plugin-cvstracker
#/var/www/gforge/plugins/cvstracker

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 4.5.19
- Rebuilt for Fedora
* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 4.5.11-1mdv2008.1
+ Revision: 140737
- restore BuildRoot
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
* Fri Jul 06 2007 Funda Wang <fundawang@mandriva.org> 4.5.11-1mdv2008.0
+ Revision: 49138
- Import gforge
* Tue May 09 2006 Oden Eriksson <oeriksson@mandriva.com> 4.5.11-1mdk
- 4.5.11
- fix deps
- make the html generation conditional. it refuses build on cs30, so
  just generate it on cooker and repackage...
* Fri Mar 24 2006 Oden Eriksson <oeriksson@mandriva.com> 4.5.6-1mdk
- 4.5.6, first official upload...
- dropped all the undocumented stuff
- added _a lot of fixes_
* Fri Oct 21 2005 Oden Eriksson <oeriksson@mandriva.com> 4.5.0.1-3mdk
- added P2
- rediffed P1
- make the html docs
* Wed Oct 19 2005 Oden Eriksson <oeriksson@mandriva.com> 4.5.0.1-2mdk
- added patches and spec file magic
- make it work on LE too
* Mon Oct 10 2005 Oden Eriksson <oeriksson@mandriva.com> 4.5.0.1-1mdk
- initial Mandriva package
- used parts of the provided spec files
