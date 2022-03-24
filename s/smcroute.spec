Summary: Static Multicast Routing Daemon
Name: smcroute
Version: 2.5.5
Release: 1
License: GPL
Group: System/Servers
Source: https://github.com/troglobit/smcroute/releases/download/%version/%name-%version.tar.gz
URL: http://troglobit.com/project/smcroute/

%description
SMCRoute is a daemon and command line tool to manipulate the multicast routes
of the Linux kernel. It can be used as an alternative to dynamic multicast
routers like 'mrouted' in situations where (only) static multicast routes
should be maintained and/or no proper IGMP signaling exists.

%prep
%setup -q

%build
./autogen.sh
%configure
%make_build all

%install
%make_install

%files
/usr/lib/systemd/system/smcroute.service
%_docdir/smcroute
%_sbindir/*
%_mandir/man?/*

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.5
- Rebuilt for Fedora
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.94.1-alt2.qa1
- NMU: rebuilt for debuginfo.
* Mon Mar 01 2010 Afanasov Dmitry <ender@altlinux.org> 0.94.1-alt2
- build with ipv6 support but disable it by default
* Sat Feb 27 2010 Afanasov Dmitry <ender@altlinux.org> 0.94.1-alt1
- 0.94.1 release
- change Url
- add pidfile support
- add init script
* Tue Sep 02 2008 Afanasov Dmitry <ender@altlinux.org> 0.93d-alt1
- first build
