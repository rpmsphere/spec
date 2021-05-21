Name: 		NessusClient                 
Version: 	1.0.0.RC5                         
Release: 	1.ossii                           
Summary: 	NessusClient, a GTK GUI for the Nessus Scanner
Group:          Applications/System
License: 	GPL
URL: 		http://www.nessus.org/
Provides: 	NessusClient
Requires: 	gtk2
Packager: 	OSS Integral Institute, Co. Ltd.
Source0: 	NessusClient-1.0.0.RC5.tar.gz
Source1:	NessusClient-1.0.0.RC5.zh_TW.po
Source2:	nessus.png

%description
A GTK+ GUI for the Nessus Vulnerability Scanner

%prep
%setup -q

%build
%configure
make
cd po; make; cd ..
msgfmt %{SOURCE1} -o po/zh_TW.gmo

%install
%__rm -rf %{buildroot}
%makeinstall

#locale
%__mkdir_p %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/
%__install -m 644 po/de.gmo %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/NessusClient.mo
%__mkdir_p %{buildroot}%{_datadir}/locale/sv/LC_MESSAGES/
%__install -m 644 po/sv.gmo %{buildroot}%{_datadir}/locale/sv/LC_MESSAGES/NessusClient.mo
%__mkdir_p %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES/
%__install -m 644 po/zh_TW.gmo %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES/NessusClient.mo

# icons
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/nessus.png

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat >%{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Nessus client
Name[zh_TW]=Nessus 客戶端
Comment=System vulnerability scanner
Comment[zh_TW]=系統弱點掃描程式
Exec=%{name}
Terminal=false
Type=Application
Icon=nessus.png
Encoding=UTF-8
Categories=Application;Security;System;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS CHANGES COPYING INSTALL TODO VERSION
%{_bindir}/NessusClient
%{_bindir}/nessusclient-mkcert
%{_bindir}/nessus-mkrand
%{_mandir}/man1/NessusClient.1.gz
%{_mandir}/man1/nessusclient-mkcert.1.gz
%{_mandir}/man1/nessus-mkrand.1.gz
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/nessus.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu Sep 21 2006 Wei-Lun Chao <bluebat@member.fsf.org> 1.0.0.RC5-1.ossii
- initial package
