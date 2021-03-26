%define _default_patch_fuzz 2
%define systemdunitdir  %{_unitdir}

Summary: A high performance web server
Name: gatling
Version: 0.15
Release: 13.1
License: GPL-2.0
Group: Productivity/Networking/Web/Servers
Source: http://dl.fefe.de/%{name}-%{version}.tar.xz
Source1: rc.gatling
Source2: sysconf.gatling
Source3: gatling.socket
Source4: gatling.service
# PATCH-FIX-UPSTREAM: conrad@quisquis.de
Patch: gatling-bof.patch
# PATCH-FIX-UPSTREAM: conrad@quisquis.de
Patch1: gatling-sslseed.patch
# PATCH-FEATURE-UPSTREAM: conrad@quisquis.de
Patch2: gatling-systemd.patch
URL: http://www.fefe.de/gatling/
BuildRequires: libowfat-devel openssl-devel
BuildRequires: systemd-devel

%description
Gatling is a high performance web server featuring
- Small! (125k static Linux-x86 binary with HTTP, FTP and SMB support)
- Fast! (measure for yourself, please)
- Scalable!
- Uses platform-specific performance and scalability APIs on Linux 2.4,
  Linux 2.6, NetBSD current (2.0+), FreeBSD 4+, OpenBSD 3.4+, Solaris 9+,
  AIX 5L, IRIX 6.5+, MacOS X Panther+, HP-UX 11+
- connection keep-alive
- el-cheapo virtual domains (similar to thttpd)
- IPv6 support
- Content-Range
- transparent content negotiation (will serve foo.html.gz if foo.html was asked
  for and browser indicates it understands deflate)
- With optional directory index generation
- Will only serve world readable files (so you don't export files accidentally)
- Supports FTP and FTP upload as well (upload only to world writable directories
  and the files won't be downloadable unless you chmod a+r them manually)
- CGI support for HTTP, also SCGI and FastCGI (over IP sockets, not Unix Domain
  yet)
- El-cheapo .htaccess support (see README.htaccess)
- Quick-and-dirty SSL/TLS support (see README.tls)
- Can detect some common mime types itself, like file(1)
- Read-only SMB support (good enough to read a specific file from Windows or
  using smbclient from Samba)

This package contains the gatling http server plus some utilities for
handling gatling's logfiles.

%package tools
Summary: Utilities shipped with the gatling source distribution
Group: Productivity/Networking/Web/Utilities

%description tools
This package includes a few utilities from the gatling source distribution:
* cgi - simple CGI demo program, prints environment + request parameters
* dl - download http, ftp or smb URLs
* getlinks - retrieve linked URLs from html file
* ioerr - send http request to server, then shut down the connection
* rellink - make links in mirrored html files relative

%package benchmarks
Summary: Benchmark programs shipped with the gatling source distribution
Group: Productivity/Networking/Web/Utilities

%description benchmarks
This package includes some benchmark programs from the gatling source
distribution:
* bench - stress test a given URL
* bindbench - measures socket bind speed
* forkbench - measures fork() speed
* forksbench - measures fork() speed, statically linked
* httpbench - measures throughput or latency on a given URL
* manymapbench - measures mmap() speed on many files
* mktestdata - creates files for manymapbench
* mmapbench - measures mmap() speed on one file with many pages
* pthreadbench - measures pthread_create() + pipe write + terminates

%prep
%setup -q
%patch -p0
%patch1 -p1
#patch2 -p1
sed -i 's|mmap_readat(filename,\&filesize,dirfd)|mmap_read(filename,\&filesize)|' http.c
sed -i -e 's|-static||' -e 's|-lz|-lz -Wl,--allow-multiple-definition|' GNUmakefile Makefile

%build
MYCFLAGS="%{optflags} -I/usr/include/libowfat"
#MYCFLAGS="$MYCFLAGS -D_GNU_SOURCE -include stdio.h"
#MYCFLAGS="$MYCFLAGS -include unistd.h -include string.h"
#make CFLAGS="$MYCFLAGS" ZLIB= DIET= DEBUG=0 %{?_smp_mflags} forksbench
make CFLAGS="$MYCFLAGS" DIET= DEBUG=0 \
	gatling httpbench bindbench dl ioerr bench tlsgatling_nofail \
	pthreadbench cgi \
	mktestdata mmapbench manymapbench forkbench forksbench \
	acc hcat referrer hitprofile matchiprange getlinks \
	rellink \
	%{?_smp_mflags}
lic="`md5sum LICENSE | cut -d' ' -f 1`"
if [ -r "/usr/share/doc/licenses/md5/$lic" ]; then
    ln -sf /usr/share/doc/licenses/md5/"$lic" LICENSE
fi

%install
make prefix="%{buildroot}%{_prefix}" MANDIR="%{buildroot}%{_mandir}" install
mv "%{buildroot}%{_bindir}"/{tls,}gatling
install acc hcat hitprofile matchiprange referrer "%{buildroot}%{_bindir}"
install cgi ioerr rellink "%{buildroot}%{_bindir}"
install bench bindbench forkbench forksbench httpbench manymapbench \
        mktestdata mmapbench pthreadbench "%{buildroot}%{_bindir}"
install -D -m 0644 %{S:2} "%{buildroot}%{_localstatedir}/adm/fillup-templates/sysconfig.%{name}"

%if %{undefined systemdunitdir}

# SYSV-Init

%__sed -s 's=^CONFIGFILE.*=CONFIGFILE\="%{_sysconfdir}/sysconfig/%{name}"=;s=^PIDFILE.*=PIDFILE\="%{_localstatedir}/run/%{name}.pid"=' <"%{S:1}" >"%{name}".rc
%__install -D -m 755 "%{name}.rc" "%{buildroot}%{_initrddir}/%{name}"
mkdir -p "%{buildroot}%{_sbindir}"
ln -sf "%{_initrddir}"/%{name} "%{buildroot}%{_sbindir}"/rc%{name}
mkdir -p "%{buildroot}%{_libexecdir}/%{name}/log"
cat >"%{buildroot}%{_libexecdir}/%{name}/run" <<__EOS__
#!/bin/sh

CONFIGFILE="%{_sysconfdir}/sysconfig/%{name}"
[ -r "\$CONFIGFILE" ] && . "\$CONFIGFILE"

exec /usr/bin/gatling \$GATLING_OPTS 2>&1
__EOS__
cat >"%{buildroot}%{_libexecdir}/%{name}/log/run" <<__EOS__
#!/bin/sh

CONFIGFILE="%{_sysconfdir}/sysconfig/%{name}"
[ -r "\$CONFIGFILE" ] && . "\$CONFIGFILE"

exec setuidgid "\$LOGUSER" multilog t n25 s1048576 "%{_localstatedir}/log/%{name}"
__EOS__
chmod 755 "%{buildroot}%{_libexecdir}/%{name}/run" "%{buildroot}%{_libexecdir}/%{name}/log/run"
mkdir -p "%{buildroot}%{_localstatedir}/log/%{name}"

# /SYSV-Init

%endif
%if %{defined systemdunitdir}

# systemd-init

%__mkdir_p "%{buildroot}%{_sysconfdir}/%{name}"
%__mkdir_p "%{buildroot}%{systemdunitdir}"
%__install -m 0644 "%{S:3}" "%{S:4}" "%{buildroot}%{systemdunitdir}"

# /systemd-init

%endif

#%%__debug_install_post

%clean
[ "%{buildroot}" = "/" ] || rm -rf "%{buildroot}"

%pre
getent group www >/dev/null || groupadd -r www
getent passwd wwwrun >/dev/null || useradd -r -g mail -d "%{_libexecdir}/%{name}" -s /sbin/nologin -c "User for HTTP daemon" wwwrun
exit 0

%post
%if %{undefined systemdunitdir}
%fillup_and_insserv %{name}
%restart_on_update %{name}
%endif
%if %{defined systemdunitdir}
%fillup_only gatling
test -n "$FIRST_ARG" || FIRST_ARG=$1
if test "$FIRST_ARG" -ge 1 ; then
    /bin/systemctl enable gatling.socket >/dev/null 2>&1 || :
fi
%endif

%preun
%if %{undefined systemdunitdir}
%stop_on_removal %{name}
%endif
%if %{defined systemdunitdir}
test -n "$FIRST_ARG" || FIRST_ARG=$1
if test "$FIRST_ARG" -lt 1 ; then
    /bin/systemctl --no-reload disable gatling.socket >/dev/null 2>&1 || :
    /bin/systemctl stop gatling.socket >/dev/null 2>&1 || :
    /bin/systemctl stop gatling.service >/dev/null 2>&1 || :
fi
%endif

%postun
%if %{undefined systemdunitdir}
%insserv_cleanup
%restart_on_update %{name}
%endif
%if %{defined systemdunitdir}
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
test -n "$FIRST_ARG" || FIRST_ARG=$1
if test "$FIRST_ARG" -ge 1 ; then
    /bin/systemctl try-restart gatling.socket >/dev/null 2>&1 || :
fi
%endif

%files
%doc CHANGES LICENSE README README.antidos README.cgi README.ftp README.htaccess 
%doc README.http README.performance README.php README.prefetch README.proxy 
%doc README.redirect README.tls TODO
%{_localstatedir}/adm/fillup-templates/sysconfig.%{name}
%{_bindir}/acc
%{_bindir}/gatling
%{_bindir}/hcat
%{_bindir}/hitprofile
%{_bindir}/matchiprange
%{_bindir}/referrer
%{_mandir}/man1/gatling.1*
%if %{undefined systemdunitdir}
%{_libexecdir}/%{name}/
%{_initrddir}/%{name}
%{_sbindir}/rc%{name}
%attr(-,wwwrun,www) %{_localstatedir}/log/%{name}
%endif
%if %{defined systemdunitdir}
%{_sysconfdir}/%{name}/
%{systemdunitdir}/gatling.service
%{systemdunitdir}/gatling.socket
%endif

%files tools
%{_bindir}/cgi
%{_bindir}/dl
%{_bindir}/getlinks
%{_bindir}/ioerr
%{_bindir}/rellink

%files benchmarks
%doc README.bindbench README.forkbench README.httpbench README.manymapbench
%doc README.mmapbench
%{_bindir}/bench
%{_bindir}/bindbench
%{_bindir}/forkbench
%{_bindir}/forksbench
%{_bindir}/httpbench
%{_bindir}/manymapbench
%{_bindir}/mktestdata
%{_bindir}/mmapbench
%{_bindir}/pthreadbench
%{_mandir}/man1/bench.1*

%changelog
* Wed Jul 04 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.15
- Rebuild for Fedora
* Wed Dec  5 2012 conrad@quisquis.de
- Fixed -H option
* Wed Dec  5 2012 conrad@quisquis.de
- Moved ssl+chroot fix to better location... :-/
* Wed Dec  5 2012 conrad@quisquis.de
- Added fix for ssl+chroot
* Tue Dec  4 2012 conrad@quisquis.de
- Various fixes wrt systemd support
* Tue Nov  6 2012 conrad@quisquis.de
- Simplify MY_CFLAGS...
* Mon Nov  5 2012 conrad@quisquis.de
- Fixed -D in MY_CFLAGS
* Mon Nov  5 2012 conrad@quisquis.de
- Added more -includes
- Added glibc-static dep for fedora
* Mon Nov  5 2012 conrad@quisquis.de
- Added -include stdio to CFLAGS
- Attempt some macro magic to avoid pkg-config, plus better OBS guidelines compliance
* Fri Nov  2 2012 conrad@quisquis.de
- Upgrade to upstream-0.13
- Added specfile license preamble
- Make use of OBS source service
* Fri Apr 27 2012 conrad@quisquis.de
- More mods for fedora16
* Thu Apr 26 2012 conrad@quisquis.de
- Minor mods for fedora16
* Thu Dec 22 2011 conrad@quisquis.de
- Added un/defined macros for pre-10.0
* Tue Dec 20 2011 conrad@quisquis.de
- Modifications for running under systemd
* Tue Jul  5 2011 conrad@quisquis.de
- Don't default-start in runlevel 2
* Thu Jun 30 2011 conrad@quisquis.de
- Require glibc-devel-static in factory
* Mon May 30 2011 conrad@quisquis.de
- Dont require licenses in factory
* Tue Mar 22 2011 conrad@quisquis.de
- Minor fixes in spec file
* Mon Mar 21 2011 conrad@quisquis.de
- Minor fixes for init script + sysconfig template
* Thu Feb 10 2011 conrad@quisquis.de
- Added init script + sysconfig template
* Tue Feb  1 2011 conrad@quisquis.de
- Apparently -D and -include don't go well together...
* Tue Feb  1 2011 conrad@quisquis.de
- Added patch against buffer overflows in acc.c + referrer.c
- Add some #defines so unistd.h actually declares used functions
* Tue Feb  1 2011 conrad@quisquis.de
- Split into several packages
* Mon Jan 31 2011 conrad@quisquis.de
- Suppress build of rellink + referrer to avoid error messages
* Mon Jan 31 2011 conrad@quisquis.de
- Initial spec file for upstream-0.12
