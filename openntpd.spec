Name:           openntpd
%define ntp_home /var/lib/ntp
Version:        6.2p3
Release:        1
License:        Other uncritical OpenSource License
Group:          Productivity/Networking/Other
BuildRequires:  openssl-devel
Conflicts:      xntp
Provides:       ntp
URL:            http://www.openntpd.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        ntpd.init
Summary:        Free and Small Network Time Protocol daemon

%description
OpenNTPD is a FREE, easy to use implementation of the Network Time
Protocol. It provides the ability to sync the local clock to remote NTP
servers and can act as NTP server itself, redistributing the local
clock.

Unlike xntp, it provides privilege separation and the ability to not
listen on remote-accessible sockets for improved security.

Authors:
--------
    Henning Brauer
    Darren Tucker <dtucker@zip.com.au>

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
autoreconf -i -f
%configure \
    --with-privsep-user=ntp \
    --with-privsep-path=%{ntp_home} \
    --disable-strip --enable-pie
%{__make} %{?jobs:-j%jobs}

%install
%{__rm} -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%{__install} -m 0755 -D %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d/ntp
%{__ln_s} /etc/init.d/ntp      $RPM_BUILD_ROOT%{_sbindir}/rcntp
%{__install} -m 0755 -d        $RPM_BUILD_ROOT%{ntp_home}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre
groupadd ntp
useradd -g ntp -s /sbin/nologin -d /var/lib/ntp -c 'OpenNTP daemon' ntp 2> /dev/null || :

%files
%{_mandir}/*/*
%doc ChangeLog AUTHORS COPYING README
%config(noreplace) %{_sysconfdir}/ntpd.conf
%{_sbindir}/ntpd
%{_sbindir}/ntpctl
%{_sbindir}/rcntp
%{_sysconfdir}/init.d/ntp
%dir %{ntp_home}

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 6.2p3
- Rebuild for Fedora
* Tue Aug  7 2007 crrodriguez@suse.de
- add missing fillup and innserv call
* Tue Sep 19 2006 dmueller@suse.de
- fix upgrade/uninstall scripts
* Wed Aug  9 2006 dmueller@suse.de
- fix stopping of daemon
* Wed May 17 2006 mrueckert@suse.de
- renamed the init script to match the xntp package
* Wed May 17 2006 mrueckert@suse.de
- removed use_pie.patch. replaced by the patches below
- added openntpd-3.9p1_asprintf_redefined_defined.patch:
  Fix the configure check so it doesnt lead to duplicated defines
  in the build checks.
- added openntpd-3.9p1_pie_configure.patch:
  added configure option to enable PIE.
* Wed May 17 2006 mrueckert@suse.de
- Update to version 3.9p1
- added %%clean
- minor cleanup
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Sep  8 2005 mrueckert@suse.de
- dont strip the binary
- minor cleanup
* Wed Sep  7 2005 dmueller@suse.de
- Initial package (3.7p1)
