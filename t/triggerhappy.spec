%undefine _debugsource_packages

Name:           triggerhappy
Version:        0.5.0
Release:        5.1
Summary:        Lightweight hotkey daemon
License:        GPL-3.0+
Group:          System/Base
URL:            https://github.com/wertarbyte/triggerhappy
Source:         https://github.com/wertarbyte/triggerhappy/archive/release/0.5.0.tar.gz#/%{name}-release-%{version}.tar.gz
Patch:          0001-Fix-systemd-service.patch

%description
Triggerhappy is a hotkey daemon developed with small and embedded systems in
mind, e.g. linux based routers. It attaches to the input device files and
interprets the event data received and executes scripts configured in its
configuration.

%prep
%setup -q -n %{name}-release-%{version}
%patch -p1

%build
make %{?_smp_mflags}

%install
%make_install
install -D -m 644 -t %{buildroot}/usr/lib/systemd/system systemd/%{name}.service systemd/%{name}.socket
install -D -m 644 udev/triggerhappy-udev.rules %{buildroot}/usr/lib/udev/rules.d/98-triggerhappy.rules
mkdir -p %{buildroot}/etc/triggerhappy/triggers.d/

%pre
systemctl stop %{name}.service %{name}.socket

%post
systemctl start %{name}.service %{name}.socket

%postun
systemctl disable %{name}.service %{name}.socket

%preun
systemctl stop %{name}.service %{name}.socket

%files
%doc AUTHORS README COPYING triggerhappy.conf.examples
%{_sbindir}/th*
%{_mandir}/man1/th*
%dir %{_udevrulesdir}
/usr/lib/udev/rules.d/??-%{name}.rules
/usr/lib/systemd/system/%{name}.*
%dir /etc/triggerhappy/triggers.d/
%dir /etc/triggerhappy

%changelog
* Mon Aug 07 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuilt for Fedora
* Wed Jun 14 2017 msuchanek@suse.com
- Fix build failure due to unowned udev directories.
* Fri Mar 10 2017 msuchanek@suse.com
- package triggerhappy
    + fix provided systemd service to not timeout
