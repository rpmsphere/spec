%global debug_package %{nil}

Name: daemontools
Version: 0.76
Release: 13.1
Group: System/Base
License: Public Domain
URL: http://cr.yp.to/daemontools/
Source: http://cr.yp.to/daemontools/daemontools-0.76.tar.gz
Source1: http://smarden.org/pape/djb/manpages/daemontools-0.76-man.tar.gz
Patch: errno.patch
Patch1: fileutils.patch
Summary: A collection of tools for managing UNIX services

%description
supervise monitors a service. It starts the service and restarts the service if
it dies. Setting up a new service is easy: all supervise needs is a directory
with a run script that runs the service.

multilog saves error messages to one or more logs. It optionally timestamps
each line and, for each log, includes or excludes lines matching specified
patterns. It automatically rotates logs to limit the amount of disk space used.
If the disk fills up, it pauses and tries again, without losing any data.

svscan starts one supervise process for each subdirectory of the current
directory, up to a limit of 1000 subdirectories. svscan skips subdirectory
names starting with dots. supervise must be in svscan's path. If a subdirectory
sub is sticky, svscan starts a pair of supervise processes, one for sub, one
for sub/log, with a pipe between them.  svscan needs two free descriptors for
each pipe.

Authors:
--------
    D. J. Bernstein

%prep
%setup -q -n admin/daemontools-%{version}/ -a 1
%patch
%patch1
sed -i -e 's|-O2|%{optflags}|g' src/conf-cc
%{__cp} daemontools-man/README README.man-pages

%build
sh package/compile

%install
%{__rm} -rf $RPM_BUILD_ROOT
for i in $(< package/commands) ; do
    %{__install} -D -m 0755 command/$i $RPM_BUILD_ROOT%{_sbindir}/$i
done
for i in daemontools-man/*8 ; do
    %{__install} -D -m 0755 $i $RPM_BUILD_ROOT%{_mandir}/man8/${i##man/}
done

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_sbindir}/envdir
%{_sbindir}/envuidgid
%{_sbindir}/fghack
%{_sbindir}/multilog
%{_sbindir}/pgrphack
%{_sbindir}/readproctitle
%{_sbindir}/setlock
%{_sbindir}/setuidgid
%{_sbindir}/softlimit
%{_sbindir}/supervise
%{_sbindir}/svc
%{_sbindir}/svok
%{_sbindir}/svscan
%{_sbindir}/svscanboot
%{_sbindir}/svstat
%{_sbindir}/tai64n
%{_sbindir}/tai64nlocal
%{_mandir}/man8/daemontools-man/envdir.8*
%{_mandir}/man8/daemontools-man/envuidgid.8*
%{_mandir}/man8/daemontools-man/fghack.8*
%{_mandir}/man8/daemontools-man/multilog.8*
%{_mandir}/man8/daemontools-man/pgrphack.8*
%{_mandir}/man8/daemontools-man/readproctitle.8*
%{_mandir}/man8/daemontools-man/setlock.8*
%{_mandir}/man8/daemontools-man/setuidgid.8*
%{_mandir}/man8/daemontools-man/softlimit.8*
%{_mandir}/man8/daemontools-man/supervise.8*
%{_mandir}/man8/daemontools-man/svc.8*
%{_mandir}/man8/daemontools-man/svok.8*
%{_mandir}/man8/daemontools-man/svscan.8*
%{_mandir}/man8/daemontools-man/svscanboot.8*
%{_mandir}/man8/daemontools-man/svstat.8*
%{_mandir}/man8/daemontools-man/tai64n.8*
%{_mandir}/man8/daemontools-man/tai64nlocal.8*
%doc README.man-pages src/CHANGES src/TODO

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.76
- Rebuild for Fedora
* Sat Oct  7 2006 mrueckert@suse.de
- install into /sbin. makes more sense for something like an init
  system.
