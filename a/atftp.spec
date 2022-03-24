Name: atftp
Summary: Advanced Trivial File Transfer Protocol (ATFTP) - TFTP server
Group: System Environment/Daemons
Version: 0.7.4
Release: 1
License: GPL
Source: /usr/src/redhat/SOURCES/atftp-%{version}.tar.gz

%description
Multithreaded TFTP server implementing all options (option extension and
multicast) as specified in RFC1350, RFC2090, RFC2347, RFC2348 and RFC2349.
Atftpd also support multicast protocol knowed as mtftp, defined in the PXE
specification. The server supports being started from inetd(8) as well as
a deamon using init scripts.

%package client
Summary: Advanced Trivial File Transfer Protocol (ATFTP) - TFTP client
Group: Applications/Internet

%description client
Advanced Trivial File Transfer Protocol client program for requesting
files using the TFTP protocol.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%files
%{_mandir}/man8/atftpd.8.gz
%{_sbindir}/atftpd
%{_mandir}/man8/in.tftpd.8.gz
%{_sbindir}/in.tftpd

%files client
%{_mandir}/man1/atftp.1.gz
%{_bindir}/atftp

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.4
- Rebuilt for Fedora
* Tue Jan 07 2003 Thayne Harbaugh <thayne@plug.org>
- put client in sub-rpm
