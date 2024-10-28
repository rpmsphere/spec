Summary:        Supported fork of the thttpd web server
Name:           sthttpd
Version:        2.27.0
Release:        18.1
License:        BSD
Group:          System/Servers
URL:            https://opensource.dyc.edu/sthttpd
Source0:        ftp://opensource.dyc.edu/pub/sthttpd/sthttpd-%{version}.tar.gz
Source1:        ftp://opensource.dyc.edu/pub/sthttpd/sthttpd-%{version}.tar.gz.asc
Source2:        thttpd.service
Source3:        thttpd.conf
Source4:        thttpd.logrotate
Source5:        thttpd.sysconfig
Source6:        thttpd-index.html
# https://jonas.fearmuffs.net/software/thttpd/thttpd-2.25b+impan-pl5.diff.gz
Patch0:         sthttpd-2.26.4+impan-pl5.diff
# https://www.ogris.de/thttpd/thttpd-2.25b.access.patch.diff
Patch1:         sthttpd-2.26.4-htaccess.diff
# https://rekl.yi.org/thttpd/pub/patch-thttpd-2.25b-re1
Patch2:         sthttpd-2.26.4-re1.diff
Patch3:         sthttpd-2.27.0-no_funky_crap.diff
Provides:       webserver
BuildRequires:  zlib-devel

%description
This is a fork of Jef Poskanzer's popular thttpd server, which you can read
about on his acme.com page. When the gentoo ebuild was abandoned in March 2012,
I decided to take a look at this package. Since upstream considered this
project "done" and was not accepting any new patches, and since the Gentoo tree
had a backlog of patches going back to 2006, I decided let it get tree cleaned.
However, the masses revolted! So, I decided the only sensible thing was to fork
the code and create an avenue for people who wanted to continue patching the
code. My major contribution to the fork was to revamp the build system and
modernize it. That was an almost total rewrite. However, the codebase remains
essentially the same, plus the dozen or so Gentoo patches that we'd collected
along the way.

%prep
%setup -q
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1

# tag the default index.html page
cp %{SOURCE6} index.html
perl -pi -e "s|_NAME_-_VERSION_|%{name}-%{version}|g" index.html

echo "# put some css in here for directory listings" > dirlist.css 
echo "# put some css in here for custom error messages" > error.css
echo "<b>This directory contains 'el cheapo' style web links.</b>" > .description

# Convert man pages to UTF8
for man in docs/*.8 docs/*.1; do
    iconv -f iso8859-1 -t utf-8 -o tmp ${man}
    mv -f tmp ${man}
done

%build
# due to P2
export LIBS="-lz"

%configure

%make_build \
    prefix=%{_prefix} \
    BINDIR=%{_sbindir} \
    MANDIR=%{_mandir} \
    WEBDIR=/var/lib/thttpd \
    WEBGROUP=thttpd \
    CGIBINDIR=/var/lib/thttpd/cgi-bin

%install
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}%{_sysconfdir}/{sysconfig,logrotate.d}
install -d %{buildroot}/var/lib/thttpd/{cgi-bin,errors,styles,links}
install -d %{buildroot}/var/log/thttpd
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man{1,8}

%make_install WEBDIR=/var/lib/thttpd

install -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/
install -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/thttpd.conf
install -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/thttpd
install -m0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/thttpd

install -m0644 index.html %{buildroot}/var/lib/thttpd/
install -m0644 dirlist.css %{buildroot}/var/lib/thttpd/styles/
install -m0644 error.css %{buildroot}/var/lib/thttpd/styles/
install -m0644 .description %{buildroot}/var/lib/thttpd/links/

# el-cheapo softlinks
pushd %{buildroot}/var/lib/thttpd/links
    ln -snf "https://opensource.dyc.edu/pub/sthttpd/sthttpd-%{version}.tar.gz" sthttpd-%{version}.tar.gz
popd

# don't ship this one
rm -f %{buildroot}/var/lib/thttpd/cgi-bin/printenv

# rename this one
mv %{buildroot}%{_sbindir}/htpasswd %{buildroot}%{_sbindir}/th_htpasswd

%pre
useradd thttpd -d /var/lib/thttpd -s /bin/nologin

%postun
userdel thttpd

%files
%doc README TODO
%{_unitdir}/thttpd.service
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/thttpd.conf
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/logrotate.d/thttpd
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/sysconfig/thttpd
%config(noreplace) %attr(0644,root,root) /var/lib/thttpd/styles/*.css
%config(noreplace) %attr(0644,root,root) /var/lib/thttpd/index.html
%attr(2755,thttpd,thttpd) %{_sbindir}/makeweb
%attr(0755,root,root) %{_sbindir}/th_htpasswd
%attr(0755,root,root) %{_sbindir}/syslogtocern
%attr(0755,root,root) %{_sbindir}/thttpd
%attr(0755,thttpd,thttpd) %dir /var/lib/thttpd
%attr(0755,thttpd,thttpd) %dir /var/lib/thttpd/cgi-bin
%attr(0755,thttpd,thttpd) %dir /var/log/thttpd
%attr(0755,root,root) /var/lib/thttpd/cgi-bin/phf
%attr(0755,root,root) /var/lib/thttpd/cgi-bin/redirect
%attr(0755,root,root) /var/lib/thttpd/cgi-bin/ssi
%attr(0644,root,root) %{_mandir}/man*/*
%attr(0644,thttpd,thttpd) /var/lib/thttpd/links/.description
%attr(0644,thttpd,thttpd) /var/lib/thttpd/links/*

%changelog
* Wed Jul 04 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.27.0
- Rebuilt for Fedora
* Fri Jan 22 2016 daviddavid <daviddavid> 2.27.0-2.mga6
+ Revision: 926450
- switch to %%configure2_5x to fix build
* Tue Nov 17 2015 oden <oden> 2.27.0-1.mga6
+ Revision: 903763
- 2.27.0
* Wed Oct 15 2014 umeabot <umeabot> 2.26.4-4.mga5
+ Revision: 739916
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 2.26.4-3.mga5
+ Revision: 689545
- Mageia 5 Mass Rebuild
* Sat Oct 19 2013 umeabot <umeabot> 2.26.4-2.mga4
+ Revision: 523902
- Mageia 4 Mass Rebuild
* Sun May 26 2013 oden <oden> 2.26.4-1.mga4
+ Revision: 427938
- imported package sthttpd
* Wed May 22 2013 Oden Eriksson <oeriksson@mandriva.com> 2.26.4-1
- based on my thttpd package from Mandriva
