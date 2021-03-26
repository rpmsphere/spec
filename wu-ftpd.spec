%define ccver CC4
Summary:	An FTP daemon originally developed by Washington University
Name:		wu-ftpd
Version:	2.8.0
Release:	2
License:	BSD
Group:		System/Servers
Source0:	http://www.wfms.org/wu-ftpd/wu-ftpd-%version-%ccver.tar.gz
URL:		http://www.wfms.org/wu-ftpd

Source1:	ftpd.log
Source2:	ftp.pamd
Source3:	wu-ftpd-xinetd
# safe glob.c
Source4:	wu-ftpd-2.6.1-safer-glob.c
Source5:	wu-ftpd.service.bz2
Patch0:		wu-ftpd-2.6.0-redhat-ported.patch
Patch1:		wu-ftpd-2.6.0-owners.patch
Patch11:	wu-ftpd-2.8.0-pasv-port-allow-correction.patch
Patch100:	wu-ftpd-2.6.0-nonrootfix.patch
Provides:	ftpserver, BeroFTPD = 1.4.0
Requires(pre):		rpm-helper
Requires(post):     rpm-helper
Requires(postun):   rpm-helper
Requires(preun):    rpm-helper
Requires(post): xinetd
Requires(postun): xinetd
Requires: xinetd
Obsoletes:	BeroFTPD < 1.4.0
BuildRequires:	byacc
BuildRequires:	openssl-static-devel

%description
The wu-ftpd package contains the wu-ftpd FTP (File Transfer Protocol)
server daemon.  The FTP protocol is a method of transferring files
between machines on a network and/or over the Internet.  Wu-ftpd's
features include logging of transfers, logging of commands, on the fly
compression and archiving, classification of users' type and location,
per class limits, per directory upload permissions, restricted guest
accounts, system wide and per directory messages, directory alias,
cdpath, filename filter and virtual host support.

Install the wu-ftpd package if you need to provide FTP service to remote
users.

%prep
%setup -q -n %name-%version-%ccver
mkdir rhsconfig
%patch0 -p1 -b .rh~
%patch1 -p1 -b .owners~
%patch11 -p1 -b .portcorr~
%patch100 -p1 -b .nonroot~
cp %{SOURCE4} src/glob.c

%build
%configure --enable-pam --disable-rfc931 --enable-ratios \
	--enable-passwd --enable-ls --disable-dnsretry --enable-ls --enable-ipv6 \
        --enable-tls

perl -pi -e "s,/\* #undef SHADOW_PASSWORD \*/,#define SHADOW_PASSWORD 1,g" src/config.h

make all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir}}
%makeinstall_std
install -c -m755 util/xferstats $RPM_BUILD_ROOT%{_sbindir}
cd rhsconfig
install -c -m 600 ftpaccess ftpusers  ftphosts ftpgroups ftpconversions $RPM_BUILD_ROOT%{_sysconfdir}
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/ftp
ln -sf in.ftpd $RPM_BUILD_ROOT%{_sbindir}/wu.ftpd
ln -sf in.ftpd $RPM_BUILD_ROOT%{_sbindir}/in.wuftpd

install -D -m644 %{SOURCE3} %buildroot%{_sysconfdir}/xinetd.d/wu-ftpd

mkdir -p %buildroot%{_sysconfdir}/avahi/services/
bzcat %{SOURCE5} > %buildroot%{_sysconfdir}/avahi/services/wu-ftpd.service

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%_pre_useradd ftp /var/ftp /bin/false

%post
if [ ! -f /var/log/xferlog ]; then
    touch /var/log/xferlog
    chmod 600 /var/log/xferlog
fi
/sbin/service xinetd reload > /dev/null 2>&1 || :

%postun
/sbin/service xinetd reload > /dev/null 2>&1 || :
%_postun_userdel ftp

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/xinetd.d/wu-ftpd
%doc README ERRATA CHANGES CONTRIBUTORS
%doc doc/HOWTO doc/TODO doc/examples
%{_mandir}/*/*.*
%config(noreplace) %{_sysconfdir}/ftp*
%config(noreplace) %{_sysconfdir}/pam.d/ftp
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/avahi/services/wu-ftpd.service

%defattr(0755,bin,bin)
%{_sbindir}/*
%{_bindir}/*



%changelog

* Tue Apr 14 2015 abfonly <abfonly@gmail.com> 2.8.0-2
- (6e1bdf2) Updated wu-ftpd.spec


