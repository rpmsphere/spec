Name:           downtimed
Version:        0.4
Release:        4.1
Summary:        Downtime Monitoring Daemon
# http://dist.epipe.com/downtimed/downtimed-%{version}.tar.gz
Source:         downtimed-%{version}.tar.bz2
Source1:        downtimed.init
Source2:        downtimed.sysconfig
URL:            http://dist.epipe.com/downtimed/
Group:          System/Monitoring
License:        BSD3c
BuildRoot:      %{_tmppath}/build-%{name}-%{version}
BuildRequires:  gcc make glibc-devel
BuildRequires:  autoconf automake libtool

%description
downtimed is a program that monitors operating system downtime, uptime,
shutdowns, and crashes and records any findings either to the system log or to
a separately specified log file. At OS startup it logs information about
previous downtime. It then periodically updates a time stamp file on the disk,
which is used to determine the approximate time when the system was last up and
running. During a graceful system shutdown, it records a time stamp in another
file.

%prep
%setup -q

%build
%configure
%__make %{?jobs:-j%{jobs}}

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install

%__install -d "$RPM_BUILD_ROOT%{_localstatedir}/lib/downtimed"

%__install -D -m0755 "%{SOURCE1}" "$RPM_BUILD_ROOT/etc/init.d/%{name}"
%__install -d "$RPM_BUILD_ROOT%{_sbindir}"
%__ln_s "../../etc/init.d/%{name}" "$RPM_BUILD_ROOT%{_sbindir}/rc%{name}"

%__install -D -m0644 "%{SOURCE2}" "$RPM_BUILD_ROOT/var/adm/fillup-templates/sysconfig.%{name}"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc LICENSE NEWS README
%{_bindir}/downtimes
%{_sbindir}/downtimed
%doc %{_mandir}/man1/downtimes.1.*
%doc %{_mandir}/man8/downtimed.8.*
%dir %{_localstatedir}/lib/downtimed
/etc/init.d/%{name}
/usr/sbin/rc%{name}
/var/adm/fillup-templates/sysconfig.%{name}

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora

* Sat Dec 25 2010 pascal.bleser@opensuse.org
- update to 0.4:
  * change backwards lseek(2) to forward lseek(2) as the backwards seek fails on some platforms
  * other minor fixes
- changes from 0.3: no user-visible changes
- changes from 0.2:
  * implemented downtimes(1) command for displaying the contents of the downtime database in human readable format
  * implemented downtime database in the downtimed(8) daemon
  * moved the location of data files from /var/lib/misc/downtimed/ to /var/lib/downtimed/ on Linux
  * the default sleep time between time stamp updates is now 15 seconds instead of 5 as previously
  * minor documentation improvements

* Sat May 22 2010 pascal.bleser@opensuse.org
- initial package (0.1)
