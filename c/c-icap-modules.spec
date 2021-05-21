Name: 	 c-icap-modules
Version: 0.5.3
Release: 1
Epoch:	 1
Summary: ICAP server modules
License: GPLv2
Group: 	 System/Servers
URL: 	 http://c-icap.sourceforge.net/
Provides:  c-icap-clamav = %epoch:%version-%release
Obsoletes: c-icap-clamav < %epoch:%version-%release
Source0: c_icap_modules-%version.tar.gz
BuildRequires: c-icap-devel clamav-devel clamav-data libdb-devel zlib-devel bzip2-devel

%description
Modules for Internet Content Adaptation Protocol (ICAP) server.

%prep
%setup -q -n c_icap_modules-%version
sed -i '108,650s|CLAMAV_VERSION|CLAMAV__VERSION|' services/virus_scan/clamav_mod.c

%build
autoreconf
%undefine _configure_gettext
%configure
%make_build

%install
mkdir -p %buildroot%_sysconfdir
%make_install
rm -f %buildroot%_libdir/c_icap/*.la

%files
%doc AUTHORS README NEWS SPONSORS
%_sysconfdir/*
%dir %_libdir/c_icap
%_libdir/c_icap/*.so
%dir %_datadir/c_icap
%_datadir/c_icap/templates
%_mandir/man8/c-icap*.8*
%_bindir/c-icap-mods-sguardDB

%changelog
* Thu Aug 15 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.3
- Rebuilt for Fedora
* Sun Oct 08 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.4.5-alt1
- New version
* Sat Mar 19 2016 Sergey Y. Afonin <asy@altlinux.ru> 1:0.4.2-alt3
- Updated BuildRequires (gear-buildreq output used)
- Packaged c-icap-mods-sguardDB binary
* Thu Mar 10 2016 Sergey Y. Afonin <asy@altlinux.ru> 1:0.4.2-alt2
- Removed gcc-c++ from BuildRequires
* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 1:0.4.2-alt1
- New version
