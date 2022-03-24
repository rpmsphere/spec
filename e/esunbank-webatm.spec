%undefine _debugsource_packages

Name: esunbank-webatm
Summary: Service for WebATM of E.Sun Bank
Version: 1.0.0.5
Release: 1.bin
Group: Network
License: Free Software
URL: http://www.esunbank.com.tw
Source0: https://netbank.esunbank.com.tw/webatm/assets/ActiveX/EsunATM.deb
Requires: libappindicator
Requires: pcsc-lite

%description
Service for WebATM of E.Sun Bank.

%prep
%setup -T -c

%build
ar -x %{SOURCE0}

%install
mkdir -p %{buildroot}
tar xf data.tar.xz -C %{buildroot}
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/usr/local/share/esunbank %{buildroot}%{_libdir}
sed -i 's|/usr/local/share|%{_libdir}|' %{buildroot}%{_libdir}/esunbank/restart.sh %{buildroot}%{_sysconfdir}/xdg/autostart/EsunATM_Service.desktop %{buildroot}%{_datadir}/applications/esunatm.desktop
rm %{buildroot}%{_libdir}/esunbank/libcrypto.so.1.1 %{buildroot}%{_libdir}/esunbank/libssl.so.1.1

%files
%{_libdir}/esunbank
%{_sysconfdir}/xdg/autostart/EsunATM_Service.desktop
%{_datadir}/applications/esunatm.desktop

%changelog
* Sun Jan 02 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0.5
- Rebuilt for Fedora
