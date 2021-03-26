%define mod_name mod_auth_gforge
%define mod_conf A56_%{mod_name}.conf
%define mod_so %{mod_name}.so

Summary:	Apache module for Gforge PostgreSQL auth
Name:		%{mod_name}
Version:	0.5.9.3
Release:	8
Group:		System/Servers
License:	Apache License
URL:		http://gforge.org/
Source0: 	libapache2-mod-auth-gforge-%{version}.tar.bz2
Source1:	%{mod_conf}.bz2
Patch0:		libapache2-mod-auth-gforge-0.5.9.3-pgsql.diff
Patch1:		libapache2-mod-auth-gforge-0.5.9.3-apr1x.diff
Requires:	httpd >= 2.0.54
BuildRequires:	httpd
BuildRequires:	php-cli
Requires:	mod_dav_svn
BuildRequires:	httpd-devel >= 2.0.54
BuildRequires:	postgresql-devel
BuildRequires:	subversion-devel
Requires:	subversion
BuildRequires:	file

%description
An apache module for authenticating and authorizing users against information
stored in the Gforge PostgreSQL database.

%prep

%setup -q -n libapache2-mod-auth-gforge-%{version}
%patch0 -p1
%patch1 -p0

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

sed -i 's|pgsql/||' src/database.h src/mod_auth_gforge.c src/database.c src/utils.c

%build

%configure \
    --with-apxs=%{_sbindir}/apxs \
    --with-aprconfig=`if [ -x %{_bindir}/apr-config ]; then echo %{_bindir}/apr-config; else echo %{_bindir}/apr-1-config; fi` \
    --with-pgconfig=%{_bindir}/pg_config \
    --with-apache-modules=%{_libdir}/httpd/modules \
    --with-php-binary=%{_bindir}/php \
    --with-apache-user=apache \
    --with-package-version=%{version}

%__make

%install
rm -rf %{buildroot}

%makeinstall APACHEUSER=`id -ng` DESTDIR=%{buildroot}

install -d %{buildroot}%{_sysconfdir}/httpd/modules.d

bzcat %{SOURCE1} > %{buildroot}%{_sysconfdir}/httpd/modules.d/%{mod_conf}

install -d %{buildroot}%{_datadir}/gforge
mv %{buildroot}/usr/lib/gforge/bin %{buildroot}%{_datadir}/gforge/

# cleanup
rm -f %{buildroot}%{_sysconfdir}/httpd/conf.d/zmod_auth_gforge.conf

%post
if [ -f %{_var}/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f %{_var}/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart 1>&2
    fi
fi

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog NEWS README TESTS TODO
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/gforge/httpd.d/17webdav
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/%{mod_conf}
%attr(0755,root,root) %{_libdir}/httpd/modules/%{mod_so}
%attr(0755,root,root) %{_datadir}/gforge/bin/committree.sh
%attr(0755,root,root) %{_datadir}/gforge/bin/create_groups.php
%attr(0755,root,root) %{_datadir}/gforge/bin/create_groups_svn.php
%attr(0755,root,root) %{_datadir}/gforge/bin/create_users.php


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue May 6 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.5.9.3-8.ossii
- rebuild for M6(CentOS5)

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.5.9.3-8mdv2008.1
+ Revision: 135820
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 08 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.9.3-8mdv2008.0
+ Revision: 82515
- rebuild

* Sat Aug 18 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.9.3-7mdv2008.0
+ Revision: 65618
- rebuild


* Sat Mar 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.9.3-6mdv2007.1
+ Revision: 140606
- rebuild

* Fri Mar 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.9.3-5mdv2007.1
+ Revision: 131430
- rebuild

* Tue Dec 19 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.9.3-4mdv2007.1
+ Revision: 100336
- make it build
- Import apache-mod_auth_gforge

* Mon Aug 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.9.3-4mdv2007.0
- rebuild

* Tue May 09 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.9.3-3mdk
- fix deprecated apr calls (Lutz Güttler)

* Sat Apr 29 2006 Emmanuel Blindauer <blindauer@mandriva.org> 0.5.9.3-2mdk
- Fix the apr-config detection

* Fri Mar 24 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.9.3-1mdk
- initial Mandriva package

