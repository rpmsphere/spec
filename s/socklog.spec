%undefine _debugsource_packages

Name:           socklog
Version:        2.1.0
Release:        18.1
Group:          System/Base
License:        BSD
Requires:       runit
URL:            https://smarden.org/socklog/
Source:         https://smarden.org/socklog/socklog-%{version}.tar.gz
Patch:          socklog-2.1.0_compile_warnings.patch
Patch1:         socklog_2.1.0-4.diff.gz
Summary:        System and kernel logging services

%description
socklog, in cooperation with the runit package, is a small and secure
replacement for syslogd. There are three main features syslogd provides:
receiving syslog messages from an unix domain socket ("/dev/log") and writing
them to various files on disk depending on facility and priority.  receiving
syslog messages from an udp socket ("0.0.0.0:514") and writing them to various
files on disk depending on facility and priority.  writing received syslog
messages to an udp socket ("a.b.c.d:514") 

socklog provides these features with the help of runit's runsvdir, runsv, and
svlogd, provides a different network logging concept, and additionally does log
event notification. 

svlogd has a built in log file rotation based on file size, so there is no need
for any cron jobs or similar to rotate the logs. Log partitions can be
calculated properly.

Authors:
---------
    Gerrit Pape <pape@smarden.org>

%package run
Group:          System/Base
Requires:       %{name} = %{version}
Requires:       runit
Provides:       syslog
Summary:        system and kernel logging services

%description run
socklog cooperates with the runit package to create a small and secure
replacement for syslogd. socklog supports system logging through Unix domain
sockets (/dev/log), UDP sockets (0.0.0.0:514), as well as TCP socket, with the
help of runit's runsvdir, runsv, and svlogd. socklog provides a different
network logging concept, and also does log event notification. svlogd has built
in log file rotation based on file size, so there is no need for any cron jobs
to rotate the logs. socklog is small, secure, and reliable. 

See https://smarden.org/socklog/ for more information. 

This package sets up the socklog-unix and socklog-klog services to provide a
system log service and kernel log service respectively.

Authors:
---------
    Gerrit Pape <pape@smarden.org>

%prep
%setup -q -n admin/%{name}-%{version}
%patch
%patch1 -p1
sed -i -e 's|-O2|%{optflags}|g' src/conf-cc

%build
sh package/compile

%install
%{__rm} -rf $RPM_BUILD_ROOT
for i in $(< package/commands) ; do
    %{__install} -D -m 0755 command/$i $RPM_BUILD_ROOT%{_sbindir}/$i
done
for i in man/*8 ; do
    %{__install} -D -m 0755 $i $RPM_BUILD_ROOT%{_mandir}/man8/${i##man/}
done
%define sv_run_path /var/run
%{__install} -d $RPM_BUILD_ROOT/var/{service,run,log/socklog}
for i in unix klog inet ucspi-tcp; do \
  install -D -m 0755 debian/etc/$i/run \
    $RPM_BUILD_ROOT/etc/sv/socklog-$i/run
  install -D -m 0755 debian/etc/$i/log/run \
    $RPM_BUILD_ROOT/etc/sv/socklog-$i/log/run
done
install -m 0755 debian/etc/unix/check \
  $RPM_BUILD_ROOT/etc/sv/socklog-unix/check
install -D -m0755 debian/etc/notify/run \
  $RPM_BUILD_ROOT/etc/sv/socklog-notify/run
# links
for i in unix klog inet ucspi-tcp; do \
  ln -s %{sv_run_path}/sv.socklog-$i \
    $RPM_BUILD_ROOT/etc/sv/socklog-$i/supervise
  ln -s %{sv_run_path}/sv.socklog-$i.log \
    $RPM_BUILD_ROOT/etc/sv/socklog-$i/log/supervise
  %{__install} -d $RPM_BUILD_ROOT%{sv_run_path}/sv.socklog-$i \
                  $RPM_BUILD_ROOT%{sv_run_path}/sv.socklog-$i.log
done
ln -s %{sv_run_path}/sv.socklog-notify \
  $RPM_BUILD_ROOT/etc/sv/socklog-notify/supervise
%{__install} -d $RPM_BUILD_ROOT%{sv_run_path}/sv.socklog-notify
for i in klog inet ucspi-tcp; do \
  ln -s /var/log/socklog-$i $RPM_BUILD_ROOT/etc/sv/socklog-$i/log/main
  %{__install} -d $RPM_BUILD_ROOT/var/log/socklog-$i
done
ln -s /var/log/socklog $RPM_BUILD_ROOT/etc/sv/socklog-unix/log/main
touch $RPM_BUILD_ROOT/var/service/socklog-unix
touch $RPM_BUILD_ROOT/var/service/socklog-klog

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -r log &>/dev/null || :
/usr/sbin/useradd -o -g log -s /bin/false -r -c "socklog log user" -d /var/log/socklog log &>/dev/null || :

%post run
# create log directories that don't exist
TEMP=`mktemp -d`
trap '! test -e "$TEMP" || rm -rf "$TEMP"' EXIT
if ! test -d /var/log/socklog; then
  socklog-conf unix nobody log "$TEMP" && \
  chown -R log:log /var/log/socklog || exit 1
fi
for i in klog inet ucspi-tcp; do
  if ! test -d /var/log/socklog-$i; then
    socklog-conf $i nobody log "$TEMP" && \
    chown -R log:log /var/log/socklog-$i || exit 1
  fi
done
# enable system- and kernel-log-service
for i in unix klog; do
  test -e /var/service/socklog-$i || test -h /var/service/socklog-$i || \
    ln -s /etc/sv/socklog-$i /var/service/ || exit 1
done
for i in unix klog inet ucspi-tcp notify; do
  test -h /var/service/socklog-$i || continue
  test "`readlink /var/service/socklog-$i`" = "/etc/socklog/$i" || continue
  rm -f /var/service/socklog-$i &&
    ln -s /etc/sv/socklog-$i /var/service/ || exit 1
done

%preun run
if [ "$1" = 0 ] ; then
    sv -w14 force-stop socklog-unix socklog-klog || :
    for i in unix klog inet notify ucspi-tcp; do
      test ! -h /var/service/socklog-$i || rm -f /var/service/socklog-$i
    done
fi

%files run
%ghost /var/service/socklog-unix
%ghost /var/service/socklog-klog
#
%dir /etc/sv/socklog-unix
%dir /etc/sv/socklog-unix/log
%dir /var/run/sv.socklog-unix
%dir /var/run/sv.socklog-unix.log
%ghost %dir %attr(-,log,log) /var/log/socklog
%config(noreplace) /etc/sv/socklog-unix/run
%config(noreplace) /etc/sv/socklog-unix/check
%config(noreplace) /etc/sv/socklog-unix/log/run
/etc/sv/socklog-unix/supervise
/etc/sv/socklog-unix/log/main
/etc/sv/socklog-unix/log/supervise
#
%dir /etc/sv/socklog-klog
%dir /etc/sv/socklog-klog/log
%dir /var/run/sv.socklog-klog
%dir /var/run/sv.socklog-klog.log
%ghost %dir %attr(-,log,log) /var/log/socklog-klog
%config(noreplace) /etc/sv/socklog-klog/run
%config(noreplace) /etc/sv/socklog-klog/log/run
/etc/sv/socklog-klog/log/main
/etc/sv/socklog-klog/log/supervise
/etc/sv/socklog-klog/supervise
#
%dir /etc/sv/socklog-inet
%dir /etc/sv/socklog-inet/log
%dir /var/run/sv.socklog-inet
%dir /var/run/sv.socklog-inet.log
%ghost %dir %attr(-,log,log) /var/log/socklog-inet
%config(noreplace) /etc/sv/socklog-inet/run
%config(noreplace) /etc/sv/socklog-inet/log/run
/etc/sv/socklog-inet/log/main
/etc/sv/socklog-inet/log/supervise
/etc/sv/socklog-inet/supervise
#
%dir /etc/sv/socklog-ucspi-tcp
%dir /etc/sv/socklog-ucspi-tcp/log
%dir /var/run/sv.socklog-ucspi-tcp
%dir /var/run/sv.socklog-ucspi-tcp.log
%ghost %dir %attr(-,log,log) /var/log/socklog-ucspi-tcp
%config(noreplace) /etc/sv/socklog-ucspi-tcp/run
%config(noreplace) /etc/sv/socklog-ucspi-tcp/log/run
/etc/sv/socklog-ucspi-tcp/log/main
/etc/sv/socklog-ucspi-tcp/log/supervise
/etc/sv/socklog-ucspi-tcp/supervise
#
%dir /etc/sv/socklog-notify
%dir /var/run/sv.socklog-notify
%config(noreplace) /etc/sv/socklog-notify/run
/etc/sv/socklog-notify/supervise

%files
%{_sbindir}/socklog
%{_sbindir}/socklog-check
%{_sbindir}/socklog-conf
%{_sbindir}/tryto
%{_sbindir}/uncat
%{_mandir}/man8/socklog-check.8*
%{_mandir}/man8/socklog-conf.8*
%{_mandir}/man8/socklog.8*
%doc package/CHANGES package/COPYING package/README
%doc doc/*

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuilt for Fedora
* Sun Sep  3 2006 mrueckert@suse.de
- move binaries to /sbin
* Sun Sep  3 2006 mrueckert@suse.de
- added socklog-run package
