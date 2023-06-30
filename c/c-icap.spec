Name: 	 c-icap
Version: 0.5.10
Release: 1
Epoch:   1
Summary: ICAP server
License: LGPLv2
Group: 	 System/Servers
URL: 	 https://c-icap.sourceforge.net/
Source0: c_icap-%version.tar.gz
Source1: %name.service
Source2: %name.watch
Source3: %name.conf.tmp
Source4: %name.conf
Source5: %name.magic
Requires(pre): shadow-utils
BuildRequires: doxygen libdb-devel openldap-devel libmemcached-devel zlib-devel bzip2-devel

%description
Implementation of an Internet Content Adaptation Protocol (ICAP) server.

%package devel
Summary: ICAP development files
Group: Development/C
Requires: %name = %epoch:%version-%release

%description devel
Headers and libraries for an Internet Content Adaptation Protocol (ICAP)
server implementation.

%prep
%setup -q -n c_icap-%version

%build
autoreconf
%undefine _configure_gettext
%configure
%make_build

%install
%make_install

install -pD -m644 %SOURCE1 %buildroot%_unitdir/%name.service
mkdir -p %buildroot%_sbindir
mv %buildroot%_bindir/%name %buildroot%_sbindir/%name

mkdir -p %buildroot/var/log/%name
touch %buildroot/var/log/%name/{server,access}.log

mkdir -p %buildroot{/var/run/%name,/var/cache/%name}

rm -f %buildroot%_libdir/*.la %buildroot%_libdir/c_icap/*.la

# Install /var/run rules
install -Dm 0644 %SOURCE3 %buildroot%_sysconfdir/tmpfiles.d/%name.conf
install -Dm 0644 %SOURCE4 %buildroot%_sysconfdir/%name.conf
install -Dm 0644 %SOURCE5 %buildroot%_sysconfdir/%name.magic

%pre
/usr/sbin/groupadd -r -f _c_icap ||:
/usr/sbin/useradd -M -n _c_icap -r -d %_runtimedir/%name -s /dev/null -c "System user for %name" -g _c_icap > /dev/null 2>&1 ||:

%files
%doc AUTHORS README TODO contrib/get_file.pl
%config(noreplace) %_sysconfdir/%name.conf*
%config(noreplace) %_sysconfdir/%name.magic*
%_unitdir/%name.service
%_bindir/*
%attr (755,root,root) %_sbindir/%name
%dir %_libdir/c_icap/
%_libdir/c_icap/*.so
%_libdir/libicapapi.so.*
%attr (750,_c_icap,root) /var/log/%name/
%ghost /var/log/%name/*.log
%attr (750,_c_icap,root) /var/run/%name/
%attr (750,_c_icap,root) /var/cache/%name/
%_sysconfdir/tmpfiles.d/%name.conf
%_mandir/man8/c-icap*.8*

%files devel
%_includedir/c_icap
%_libdir/libicapapi.so

%changelog
* Sun Oct 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.10
- Rebuilt for Fedora
* Mon Oct 16 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.2-alt2
- Fix missing /var/run/c-icap after reboot
* Sun Oct 08 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.2-alt1
- New version
- Package run and cache dirs to fix daemon run
* Sat Mar 19 2016 Sergey Y. Afonin <asy@altlinux.ru> 1:0.4.2-alt3
- Updated BuildRequires (gear-buildreq output used)
* Thu Mar 10 2016 Sergey Y. Afonin <asy@altlinux.ru> 1:0.4.2-alt2
- Spec's cleanup
- Added LSB init header (fixed repocop's error)
- Removed gcc-c++ from BuildRequires
* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 1:0.4.2-alt1
- New version
- Spec's cleanup
- Built without libclamav-devel
  (modules was moved to separate c-icap-modules package)
- Renamed libdir and includedir to c_icap as in upstream
* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20080706.01-alt2.3
- Fixed build
* Mon Apr 05 2010 Anton Pischulin <letanton@altlinux.ru> 20080706.01-alt2.2
- Fixed base64.c
* Fri Feb 26 2010 Andrey Cherepanov <cas@altlinux.org> 20080706-alt0.1.M50P.1
- Backport to p5
* Wed Nov 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20080706-alt1.1
- Built for sisyphus
* Mon Sep 28 2009 Grigory Batalov <bga@altlinux.ru> 20080706-alt2.M40.1
- New upstream release (c_icap-20080706).
- Updated url_filter.
* Wed Apr 15 2009 Grigory Batalov <bga@altlinux.ru> 20060603-alt1.M40.2
- Pre-requirement of shadow-utils were added.
- Url-filter provides c-icap-skf.
* Thu Apr 09 2009 Grigory Batalov <bga@altlinux.ru> 20060603-alt1.M40.1
- Rebuilt with custom url_filter.
- Built for ALT Linux branch 4.0.
* Thu Mar 22 2007 ALT QA Team Robot <qa-robot@altlinux.org> 20060603-alt1.0
- Rebuilt with libclamav.so.2.
* Wed Jan 17 2007 Grigory Batalov <bga@altlinux.ru> 20060603-alt1
- Initial ALTLinux release.
