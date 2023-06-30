Summary: A single-tasking high performance http server
Name: boa
Version: 0.94.14rc21
Release: 1
URL: https://www.boa.org/
Group: System Environment/Daemons
Source: https://www.boa.org/boa-%{version}.tar.gz
License: GNU general public license
Provides: webserver

%description
Boa is a single-tasking HTTP server. That means that
unlike traditional web servers, it does not fork for each
incoming connection, nor does it fork many copies of
itself to handle multiple connections. It internally mul-
tiplexes all of the ongoing HTTP connections, and forks
only for CGI programs (which must be separate processes.)
Preliminary tests show Boa is more than twice as fast as
Apache.

Boa was created in 1991 by Paul Phillips <psp@well.com>.
It is now being maintained and enhanced by Larry Doolittle
<ldoolitt@boa.org> and Jon Nelson <jnelson@boa.org>.

%prep
%setup -q

%build
%configure
make
(cd docs && gzip -c boa.8 > boa.8.gz)
(cd docs && make boa.html)

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/home/httpd/{html,cgi-bin}
mkdir -p $RPM_BUILD_ROOT/var/log/boa
mkdir -p $RPM_BUILD_ROOT/usr/lib/boa
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/etc/boa

install -m755 src/boa $RPM_BUILD_ROOT/usr/sbin/
install -m755 src/boa_indexer $RPM_BUILD_ROOT/usr/lib/boa/
install -m644 contrib/rpm/boa.conf $RPM_BUILD_ROOT/etc/boa/

install -m755 contrib/rpm/boa.init-redhat $RPM_BUILD_ROOT/etc/init.d/boa
mkdir -p $RPM_BUILD_ROOT/etc/{boa,logrotate.d}
install -m644 contrib/rpm/boa.logrotate $RPM_BUILD_ROOT/etc/logrotate.d/boa

mv docs/boa.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8/

touch $RPM_BUILD_ROOT/var/log/boa/{error,access}_log

%files
%dir /home/httpd/html
%dir /home/httpd/cgi-bin
%dir /var/log/boa
%doc COPYING CREDITS CHANGES README docs/boa.html docs/boa_banner.png docs/boa.texi
%doc /%{_mandir}/man8/*
%dir /etc/boa
%config /etc/boa/boa.conf
%config /etc/init.d/boa
%config /etc/logrotate.d/boa
%ghost %attr(600,nobody,nobody)/var/log/boa/error_log
%ghost %attr(600,nobody,nobody)/var/log/boa/access_log
/usr/sbin/boa
/usr/lib/boa/boa_indexer

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.94.14rc21
- Rebuilt for Fedora
* Sun Aug 6 2000 Jonathon D Nelson <jnelson@boa.org>
- revamp packaging based upon examples provided by 
  Jules Stuifbergen <jules@zjuul.net> and others
