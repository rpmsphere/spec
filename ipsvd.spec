%global debug_package %{nil}

Name:           ipsvd
Version:        0.13.0
Release:        3.1
Group:          System/Base
License:        BSD
#define _sbindir /sbin
URL:            http://smarden.org/ipsvd/
Source:         http://smarden.org/ipsvd/ipsvd-%{version}.tar.gz
Summary:        Internet protocol service daemons

%description
ipsvd is a set of internet protocol service daemons for Unix. It currently
includes a TCP/IP service daemon, an SSLv3 TCP/IP service daemon (Linux and
MacOSX), and an UDP/IP service daemon. 

An internet protocol service (ipsv) daemon waits for incoming connections on a
local socket; for new connections, it conditionally runs an arbitrary program
with standard input reading from the socket, and standard output writing to the
socket (if connected), to handle the connection. Standard error is used for
logging. 

ipsv daemons can be told to read and follow pre-defined instructions on how to
handle incoming connections; based on the client's IP address or hostname, they
can run different programs, set a different environment, deny a connection, or
set a per host concurrency limit. 

Normally the ipsv daemons are run by a supervisor process, such as runsv from
the runit package, or supervise from the daemontools package. 

ipsvd can be used to run services normally run by inetd, xinetd, or tcpserver.

Authors:
---------
    Gerrit Pape <pape@smarden.org>


%prep
%setup -q -n net/%{name}-%{version}
sed -i -e 's|-O2|%{optflags}|g' src/conf-cc

%build
sh package/compile

%install
for i in $(< package/commands) ; do
    %{__install} -D -m 0755 command/$i $RPM_BUILD_ROOT%{_sbindir}/$i
done
for i in man/*8 ; do
    %{__install} -D -m 0755 $i $RPM_BUILD_ROOT%{_mandir}/man8/${i##man/}
done

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc package/CHANGES package/COPYING package/README
%doc doc/*
%{_sbindir}/ipsvd-cdb
%{_sbindir}/tcpsvd
%{_sbindir}/udpsvd
%{_mandir}/man8/ipsvd-cdb.8*
%{_mandir}/man8/sslio.8*
%{_mandir}/man8/sslsvd.8*
%{_mandir}/man8/tcpsvd.8*
%{_mandir}/man8/udpsvd.8*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.13.0
- Rebuild for Fedora
* Thu Sep  6 2007 mrueckert@suse.de
- update to 0.13.0
* Sun Sep  3 2006 mrueckert@suse.de
- move binaries into /sbin
- dont depend on runit.
