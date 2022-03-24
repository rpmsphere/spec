%undefine _debugsource_packages

Name: openfortigui
Summary: GUI for openfortivpn
Version: 0.9.5
Release: 1
Group: admin
License: Free Software
URL: https://github.com/theinvisible/openfortigui
Source0: %{name}-%{version}.tar.gz
BuildRequires: desktop-file-utils
BuildRequires: qtkeychain-qt5-devel
#Requires: libqt5core5a
#Requires: libqt5gui5
#Requires: libqt5keychain1
#Requires: libqt5network5
#Requires: libqt5widgets5
#Requires: libssl1.1
#Requires: sudo,
#Requires: qttranslations5-l10n,
#Requires: ppp,
#Requires: lsb-release

%description
VPN-GUI to connect to Fortigate-Hardware, based on openfortivpn.

%prep
%setup -q
sed -i -e 's|strlcpy|strncpy|' -e 's|ifr.ifr_addr.sa_len|sizeof(ifr.ifr_addr)|' openfortigui/openfortivpn/src/tunnel.c

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
#qmake-qt5
make %{?_smp_mflags}

%install
#make install DESTDIR=%{buildroot}
install -Dm644 %{name}/sudo/%{name} %{buildroot}%{_sysconfdir}/sudoers.d/%{name}
install -Dm755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}/app-entry/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{name}/app-entry/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc LICENSE* README.md
%{_sysconfdir}/sudoers.d/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.5
- Rebuilt for Fedora
