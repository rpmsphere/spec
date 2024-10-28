%undefine _debugsource_packages

Summary: Program to snoop on a TTY through another
Name: ttysnoop
Version: 0.12c
Release: 4.1
License: distributable
Group: System Environment/Base
URL: https://sunsite.unc.edu/pub/Linux/utils/terminal/
Source: https://sunsite.unc.edu/pub/Linux/utils/terminal/ttysnoop-%{version}.tar.gz
Patch0: ttysnoop-0.12c-glibc.patch

%description
The package allows you to snoop on login tty's through another tty-device
or pseudo-tty. The snoop-tty becomes a 'clone' of the original tty,
redirecting both input and output from/to it.

%prep
%setup -q
%patch 0 -p1

%build
%{__make} %{?_smp_mflags} RPM_OPTS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 ttysnoop %{buildroot}%{_sbindir}/ttysnoop
%{__install} -Dp -m0755 ttysnoops %{buildroot}%{_sbindir}/ttysnoops
%{__install} -Dp -m0644 ttysnoop.8 %{buildroot}%{_mandir}/man8/ttysnoop.8
%{__install} -Dp -m0644 snooptab.dist %{buildroot}%{_sysconfdir}/snooptab

%files
%doc README
%{_mandir}/man8/ttysnoop.8*
%config %{_sysconfdir}/snooptab
%{_sbindir}/ttysnoop
%{_sbindir}/ttysnoops

%changelog
* Wed Jul 08 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.12c
- Rebuilt for Fedora
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.12c-1.2 - 7981+/dag
- Rebuilt for Fedora Core 5.
* Mon Aug 22 2005 Dag Wieers <dag@wieers.com> - 0.12c-1
- Initial package. (using DAR)
