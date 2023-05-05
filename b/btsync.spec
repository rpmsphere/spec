%global __filter_GLIBC_PRIVATE 1
%undefine _debugsource_packages

Name:           btsync
Version:        1.4.111
Release:        1.bin
Summary:        BitTorrent Sync
License:        Proprietary
URL:            http://labs.bittorrent.com/experiments/sync.html
Source0:        https://github.com/FreemanZY/BTSync-DHT-Docker/raw/master/btsync_x64-%{version}.tar.gz
Source1:        btsync.service
Source2:        btsync-pre
ExclusiveArch: x86_64

%description
BitTorrent Sync.

%prep
%setup -c

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 btsync %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_userunitdir}
install -p -m 0644 %{S:1} %{buildroot}%{_userunitdir}
mkdir -p %{buildroot}%{_libexecdir}
install -p -m 0755 %{S:2} %{buildroot}%{_libexecdir}

%files
%doc LICENSE.TXT README
%{_bindir}/btsync
%{_userunitdir}/btsync.service
%{_libexecdir}/btsync-pre

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.111
- Rebuilt for Fedora
* Thu May 29 2014 Jeffrey Ollie <jeff@ocjtech.us> - 1.3.105-1
- 1.3.105
- switch system unit file to a user unit file
* Sat Mar 15 2014 Jeffrey Ollie <jeff@ocjtech.us> - 1.2.92-2
- Update btsync-pre to open firewall ports
* Sat Mar 15 2014 Jeffrey Ollie <jeff@ocjtech.us> - 1.2.92-1
- Update to 1.2.92
* Mon Dec  2 2013 Jeffrey Ollie <jeff@ocjtech.us> - 1.2.82-1
- Update to 1.2.82
* Fri Nov  8 2013 Jeffrey Ollie <jeff@ocjtech.us> - 1.2.68-1
- Update to 1.2.68
* Fri Sep 27 2013 Jeffrey Ollie <jeff@ocjtech.us> - 1.1.82-3
- Fix logging in btsync-pre
* Fri Sep 27 2013 Jeffrey Ollie <jeff@ocjtech.us> - 1.1.82-2
- Filter out GLIBC_PRIVATE requirements
- Add some comments on how to obtain latest version
* Fri Sep 27 2013 Jeffrey Ollie <jeff@ocjtech.us> - 1.1.82-1
- First version
