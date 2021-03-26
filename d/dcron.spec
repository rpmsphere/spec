Name:               dcron
Version:            4.5
Release:            7.1
Summary:            Lightweight Cron Daemon
Source:             http://www.jimpryor.net/linux/releases/dcron-%{version}.tar.gz
Source1:            dcron.init
Patch1:             dcron-fix_makefile.patch
URL:                http://www.jimpryor.net/linux/dcron.html
Group:              System/Daemons
License:            GNU General Public License version 2 or later (GPL v2 or later)
BuildRequires:      gcc make glibc-devel pkgconfig

%description
crond is a background daemon that parses individual crontab files and executes
commands on behalf of the users in question.

This lightweight cron daemon aims to be simple and secure, with just enough
features to stay useful. It was written from scratch by Matt Dillon in 1994.
It's now developed and maintained by Jim Pryor.

In the author's opinion, having to combine a cron daemon with another daemon
like anacron makes for too much complexity. So the goal is a simple cron daemon
that can also take over the central functions of anacron.

Unlike other fatter cron daemons, though, this cron doesn't even try to manage
environment variables or act as a shell. All jobs are run with `/bin/sh` for
conformity and portability. We don't try to use the user's preferred shell:
that breaks down for special users and even makes some of us normal users
unhappy (for example, /bin/csh does not use a true O_APPEND mode and has
difficulty redirecting stdout and stderr both to different places!). You can,
of course, run shell scripts in whatever language you like by making them
executable with #!/bin/csh or whatever as the first line. If you don't like the
extra processes, just `exec` them.

%prep
%setup -q
%patch1

%build
%__make %{?_smp_flags} \
    OPTFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    SCRONTABS="%{_sysconfdir}/%{name}.d" \
    CRONTABS="%{_var}/spool/%{name}/crontabs" \
    CRONSTAMPS="%{_var}/spool/%{name}/cronstamps" \
    LOG_IDENT="%{name}" \
    SBINDIR="%{_sbindir}" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}" \
    INSTALL="%__install"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__make %{?_smp_flags} \
    OPTFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    SCRONTABS="%{_sysconfdir}/%{name}.d" \
    CRONTABS="%{_var}/spool/%{name}/crontabs" \
    CRONSTAMPS="%{_var}/spool/%{name}/cronstamps" \
    LOG_IDENT="%{name}" \
    SBINDIR="%{_sbindir}" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}" \
    INSTALL="%__install" \
    DESTDIR="$RPM_BUILD_ROOT" \
    install

%__mv -v "$RPM_BUILD_ROOT%{_bindir}"/{crontab,dcrontab}
%__mv -v "$RPM_BUILD_ROOT%{_sbindir}"/{crond,dcrond}
%__mv -v "$RPM_BUILD_ROOT%{_mandir}/man1"/{crontab,dcrontab}.1
%__mv -v "$RPM_BUILD_ROOT%{_mandir}/man8"/{crond,dcrond}.8

%__install -D -v -m0744 "%{SOURCE1}" "$RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name}"
%__install -d "$RPM_BUILD_ROOT/usr/sbin"
%__ln_s -f "../../etc/init.d/%{name}" "$RPM_BUILD_ROOT/usr/sbin/rc%{name}"

%__install -m0755 -d "$RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d"
for d in crontabs cronstamps; do
    %__install -m0700 -d "$RPM_BUILD_ROOT%{_var}/spool/%{name}/$d"
done

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc CHANGELOG README
%{_sysconfdir}/%{name}.d
%attr(755,root,root)%{_bindir}/dcrontab
%{_sbindir}/dcrond
/etc/init.d/%{name}
/usr/sbin/rc%{name}
%doc %{_mandir}/man1/dcrontab.1.*
%doc %{_mandir}/man8/dcrond.8.*
%dir %attr(700,root,root) %{_var}/spool/%{name}
%dir %attr(700,root,root) %{_var}/spool/%{name}/crontabs
%dir %attr(700,root,root) %{_var}/spool/%{name}/cronstamps

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 4.5
- Rebuild for Fedora
* Wed May 11 2011 pascal.bleser@opensuse.org
- initial version (4.5)
