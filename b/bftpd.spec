Name:      bftpd
Version:   6.2
Release:   1
Summary:   A small, fast and easy-to-configure FTP server
License:   GPL
Group:     System/Servers
URL:       https://bftpd.sourceforge.net/
Source0:   https://bftpd.sourceforge.net/downloads/rpm/%{name}-%{version}.tar.gz

%description
bftpd is a easy-to-configure and small FTP server that supports chroot
without special directory preparation or configuration. Most FTP commands
are supported.

%prep
%setup -qn %name

%build
%configure
sed -i 's|-lcrypt|-Wl,--allow-multiple-definition -lcrypt|' Makefile
make

%install
sed -i 's|-g 0 \(-m ...\) -o 0|\1|' Makefile
%make_install
mv %buildroot/usr/etc %buildroot/etc
mv %buildroot/usr/var %buildroot/var
mkdir -p %buildroot/var/run/bftpd

%files
%_sysconfdir/bftpd.conf
%_sbindir/bftpd
%_mandir/man8/*
/var/run/bftpd
/var/log/bftpd.log

%changelog
* Sun Apr 07 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 6.2
- Rebuilt for Fedora
* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1-alt0.1.qa1
- NMU: rebuilt for debuginfo.
* Mon Feb 18 2008 Nick S. Grechukh <gns@altlinux.org> 2.1-alt0.1
- initial build for ALT Sisyphus
* Mon Jan 1 2007 Joe Klemmer <joe@webtrek.com>
- updated the version number.
* Mon Jan 9 2006 Joe Klemmer <joe@webtrek.com>
- added defined variables to the top of the file.
- set the config file in the %%files section so it won't
  be over written on upgrades.
- added a default attributes to the %%files section.
- redid the summery section to bring it in line with "rpm
  spec file standards" (an oxymoron if ever there was one).
- changed the depricated "Copyright" into "License".
