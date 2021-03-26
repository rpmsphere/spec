Name:           web-obex
Version:        20100328
Release:        1
Summary:        Web-based UI of obexftp
Group:          Applications/Internet
License:        GPL
URL:            https://github.com/penk/web-obex
Source0:        %{name}.tar.gz
Requires:       httpd, obexftp, bluez, mplayer, firefox
BuildArch:	noarch

%description
Web-obex is a web-based UI of obexftp to download and play music from mobile phone.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_var}/www/html
cp -a * $RPM_BUILD_ROOT%{_var}/www/html

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/bash
service httpd condrestart
hciconfig hci0 up
firefox http://localhost/index.html
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,apache,apache)
%attr(755,root,root) %{_bindir}/%{name}
%{_var}/www/html/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Apr 19 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Initial package
