Name:           epoptes
Version:        23.01
Release:        1
License:        GPL-2.0+
Summary:        Computer lab management tool
URL:            https://www.epoptes.org
Group:          System/X11/Utilities
Source:         https://codeload.github.com/Epoptes/epoptes/tar.gz/%{version}#/%{name}-%{version}.tar.gz
Source2:        epoptes-server.service
Source3:        epoptes-client.service
Patch0:         epoptes-support-tightvnc.patch 
BuildRequires:  intltool
BuildRequires:  openssl
#BuildRequires:  pwdutils
Requires:  python2-twisted
BuildRequires:  python2-devel
BuildRequires:  python2-distutils-extra
BuildRequires:  desktop-file-utils
BuildRequires:  systemd
Requires:       libfaketime
Requires:       librsvg2
Requires:       iperf 
Requires:       openssl
#Requires:       pwdutils
Requires:       python-twisted
Requires:       pygtk2
Requires:       python-pycha
Requires:       notify-python
Requires:       python-netifaces
# WARNING: This is much more a python-Twisted dependency than a Epoptes one.
Requires:       python-service-identity
Requires:       socat
Requires:       tightvnc
Requires:       x11vnc
Requires:       xset
Requires:       xwininfo
BuildArch:      noarch

%description
Epoptes (Επόπτης - a Greek word for overseer) is an open source computer lab
management and monitoring tool. It allows for screen broadcasting and
monitoring, remote command execution, message sending, imposing restrictions
like screen locking or sound muting the clients and much more!

%package client
Summary:        Epoptes client
Requires:       librsvg2
Requires:       iperf
Requires:       pygtk2
Requires:       socat
Requires:       tightvnc
Requires:       x11vnc
Requires:       xset
Requires:       xwininfo

%description client
This is a client part of Epoptes Computer lab management tool.

%prep
%setup -q
#patch0 -p1

for file in $(find . -type f -name "*.py" ); do
	sed -i "s|/usr/bin/env python|%{_bindir}/python3|g" $file
done

%build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}
find %{buildroot} \( -name \*.a -o -name \*.la -o -name \*.orig \) -print0 | xargs -0 rm -f
mkdir -p %{buildroot}%{_sysconfdir}/default
%__install -m 644 ./debian/epoptes.default %{buildroot}%{_sysconfdir}/default/epoptes
%__install -m 644 ./debian/epoptes-client.default %{buildroot}%{_sysconfdir}/default/epoptes-client
mkdir -p %{buildroot}%{_unitdir}
%__install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}
%__install -m 644 %{SOURCE3} %{buildroot}%{_unitdir}
%__ln_s service %{buildroot}%{_sbindir}/rcepoptes-server
%__ln_s service %{buildroot}%{_sbindir}/rcepoptes-client
%find_lang epoptes

#sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name} #%{buildroot}%{_datadir}/epoptes-client/remote-assistance
#sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name} %{buildroot}%{_datadir}/epoptes-client/*

%clean
%__rm -rf %{buildroot}

%pre
systemctl enable epoptes-server.service

%pre client
systemctl enable epoptes-client.service

%post
if ! getent group epoptes >/dev/null; then
    groupadd --system epoptes
fi

if ! [ -f /etc/epoptes/server.key ] || ! [ -f /etc/epoptes/server.crt ] || ! [ -s /etc/epoptes/server.crt ]; then
    if ! [ -d /etc/epoptes ]; then
        mkdir /etc/epoptes
    fi
    openssl req -batch -x509 -nodes -newkey rsa:1024 -days $(($(date --utc +%s) / 86400 + 3652)) -keyout /etc/epoptes/server.key -out /etc/epoptes/server.crt
    chmod 600 /etc/epoptes/server.key
fi
systemctl start epoptes-server.service

%post client
systemctl start epoptes-client.service

%preun
systemctl stop epoptes-server.service

%preun client
systemctl stop epoptes-client.service

%postun
systemctl disable epoptes-server.service

%postun client
systemctl disable epoptes-client.service

%files -f epoptes.lang
%config(noreplace) %{_sysconfdir}/default/epoptes
%{_unitdir}/epoptes-server.service
%{_sbindir}/rcepoptes-server
%{_bindir}/epoptes
%{python3_sitelib}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/ltsp/
%{_datadir}/epoptes/
%dir %{_datadir}/doc/epoptes
%{_datadir}/doc/epoptes/README.md
%{_mandir}/man1/epoptes.1.*

%files client
%config(noreplace) %{_sysconfdir}/default/epoptes-client
%{_sysconfdir}/xdg/autostart/epoptes-client.desktop
%{_unitdir}/epoptes-client.service
%{_sbindir}/rcepoptes-client
%{_sbindir}/epoptes-client
%{_datadir}/epoptes-client/
#{_datadir}/ldm/
%{_mandir}/man8/epoptes-client.8.*

%changelog
* Sun Jun 11 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 23.01
- Rebuilt for Fedora
* Wed Feb 24 2016 cyberorg@opensuse.org
- update to 0.5.9_bzr0.509
- add support for tightvncviewer as tigervnc lack needed feature
  https://github.com/TigerVNC/tigervnc/issues/227
- add _service thanks lbsousajr@gmail.com
* Thu Oct  1 2015 cyberorg@opensuse.org
- Regenerate certificates if it is still old style
- Add python-netifaces dep
* Wed Sep 30 2015 cyberorg@opensuse.org
- Update to bzr revision 436
- Add openssl.cnf to add CommonName, new socat requires it
* Thu Sep 24 2015 cyberorg@opensuse.org
- use tightvncviewer as other vncviewers are brokenn bnc #939259
* Mon Mar  2 2015 lbsousajr@gmail.com
- Fix VNC viewer related requirements from official repositories.
  Old requirement tightvncviewer is broken since openSUSE 13.2.
  + For openSUSE 13.2 and newer, now requires package tigervnc.
  + For openSUSE 13.1, now requires package tightvnc.
* Mon Dec 15 2014 lbsousajr@gmail.com
- Add new patch to fix epoptes-client's script get-display in
  openSUSE new contexts:
  + systemd-logind has replaced ConsoleKit.
  + XAUTHORITY file may not be found at ~/.Xauthority. GDM/GNOME
    and KDE store this file in different paths.
* Thu Dec 11 2014 lbsousajr@gmail.com
- Small changes in file epoptes-client.service:
  + Don't fail if file /etc/default/epoptes-client can't be read.
  + Run command "epoptes-client -c" also if certificate file
    exists, but is empty.
* Thu Dec 11 2014 lbsousajr@gmail.com
- More improvements on file epoptes-client-enable-wol@.service:
  + Simplify dependencies.
  + Don't fail if file /etc/default/epoptes-client can't be read.
  + Replace /bin/sh invocation with systemd directives.
* Wed Dec 10 2014 lbsousajr@gmail.com
- Drop epoptes-client if-up.d/if-down.d scripts for openSUSE 13.2+,
  since its new Wicked network management tool doesn't support
  starting these scripts. Fortunately, now both Wicked and
  NetworkManager services trigger network-online.target,
  so we can just add it as a dependency for
  epoptes-client.service. This one now must be enabled explicitly
  (systemctl enable epoptes-client).
- For the same reason, we don't build package
  epoptes-client-nm-dispatcher for openSUSE 13.2+.
- epoptes-client-fetch-certificate.service was merged into
  epoptes-client.service at ExecStartPre level.
- epoptes-client-ethtool@.service was enhanced and renamed to
  epoptes-client-enable-wol@.service. It must be enabled
  explicitly for openSUSE 13.2+.
* Mon Dec  8 2014 lbsousajr@gmail.com
- Drop non-systemd init scripts, and fix latest rpmlint warnings.
* Mon Jun  9 2014 cyberorg@opensuse.org
- update to bzr snapshot, new feature: network benchmark
* Thu Dec 19 2013 lbsousajr@gmail.com
- Add workaround patch to fix broadcasting problems
  in multiseat context (LP #978050).
  + Needed until epoptes-client system daemon can handle
    properly multiple seats/displays.
* Thu Dec 19 2013 lbsousajr@gmail.com
- Add patch to keep standalone clients reconnecting to server
  when connection is lost. LTSP clients are not affected.
* Wed Dec 18 2013 lbsousajr@gmail.com
- Include ifup scripts by default in package epoptes-client,
  since it's openSUSE's default network configuration method.
- New package epoptes-client-nm-dispatcher includes the other
  dispatcher scripts for NetworkManager.
* Sun Dec 15 2013 lars@linux-schulserver.de
- add SuSEfirewall2 file to allow epoptes' port to be opened via
  YaST SuSEfirewall module
* Thu Dec 12 2013 lbsousajr@gmail.com
- Add patch to enable shutdown/reboot dbus calls for systemd-logind
* Thu Dec 12 2013 lbsousajr@gmail.com
- Big cleanup in epoptes.spec
  + Drop support for Fedora and older versions of [open]SUSE
* Thu Dec 12 2013 cyberorg@opensuse.org
- add rcepoptes-server for old-school control
- add epoptes-debian-only-functions.patch
* Tue Dec 10 2013 lbsousajr@gmail.com
- Introduce ifup/NetworkManager dispatcher scripts to start
  epoptes-client*.service when network is online
  Needed until we get a stable way to enable epoptes-client*.service
  at boot. It currently fails to wait for network to be online.
* Mon Dec  9 2013 lbsousajr@gmail.com
- Restore package architecture for SLE_11_SP3
  (see also: https://comments.gmane.org/gmane.linux.suse.opensuse.buildservice/9427)
- Add "BuildRequires: systemd" when needed
* Mon Dec  9 2013 lbsousajr@gmail.com
- Package cleanup:
  + Change package architecture to noarch
  + Remove uneeded explicit library dependencies
  + Filter desktopfile-without-binary rpmlint warnings
    (see also: https://bugzilla.redhat.com/show_bug.cgi?id=991278)
* Wed Dec  4 2013 lbsousajr@gmail.com
- New upstream version: 0.5.7
* Fri Jul 19 2013 lars@linux-schulserver.de
- specfile cleanup
- added rpmlintrc
* Thu Dec 13 2012 cyberorg@opensuse.org
- fix fedora reqs
* Sat Aug 25 2012 cyberorg@opensuse.org
- Test fedora package
* Sat Aug 25 2012 cyberorg@opensuse.org
- Initial package for openSUSE
