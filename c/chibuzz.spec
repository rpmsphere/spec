Name: chibuzz
Summary: GTK Networking Tool
Version: 0.2.6
Release: 6.1
Group: Applications/Internet
License: GPL
URL: http://gtk-apps.org/content/show.php/ChiBuzz%3F?content=85621
Source0: http://gtk-apps.org/CONTENT/content-files/85621-%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: python-beautifulsoup, tkinter, pygtk2-libglade

%description
Chibuzz, aka Who's knocking, is a very little tool written in Python retrieves
your public IP address and display a GoogleMaps screenshot.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -a glade *.py %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
exec python2 %{name}-%{version}.py
EOF

sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%files
%doc docs/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.6
- Rebuild for Fedora
