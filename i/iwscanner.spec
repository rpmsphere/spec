Name:		iwscanner
Version:	0.2.4
Release:	4.1
Summary:	Wireless scanner based on iwtools
URL:		http://kuthulu.com/iwscanner/index.php
License:	LGPLv2+
Group:		Networking/Other
Source0:	http://kuthulu.com/iwscanner/%{name}-%{version}.tgz
Source1:	kuthulu-%{name}.desktop
BuildArch:	noarch
Requires:	pygtk2
Requires:	wireless-tools

%description
A simple NetStumbler like wireless scanner based on iwtools.

%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}

# wrapper script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
exec /usr/share/iwscanner/iwscanner.py
EOF
%__chmod 755 %{buildroot}%{_bindir}/%{name}
%__mkdir_p %{buildroot}%{_datadir}/applications
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

# datafiles
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp * %{buildroot}%{_datadir}/%{name}/

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/%{name}.py

%clean
%__rm -rf %{buildroot}

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Dec 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4
- Rebuild for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.2.4-2
+ Revision: 27950e0
- MassBuild#464: Increase release tag
