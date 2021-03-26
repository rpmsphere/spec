Name: utorrent-server
Summary: uTorrent Server
Version: 3.0
Release: 0.25053%{?dist}.bin
License: freeware
Group: Applications/Internet
Source0: utorrent-server-3.0-25053.tar.gz
Source1: utorrent-data.zip
URL: http://www.utorrent.com/

%description
Speedy, efficient, and free.
uTorrent is the world's most popular BitTorrent client for a reason.

uTorrent Server is designed for use on computers running Linux and other
UNIX-like operating systems. It provides a state-of-the-art implementation
of the BitTorrent protocol and a full-featured web-based user interface
in a small footprint.

%prep
%setup -q -n %{name}-v3_0

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}/usr/lib/%{name}
unzip %{SOURCE1} -d %{buildroot}/usr/lib/%{name}
%__cp utserver webui.zip %{buildroot}/usr/lib/%{name}
%__mkdir_p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
echo "Browsing http://admin@127.0.0.1:8080/gui"
cd /usr/lib/utorrent-server
./utserver "\$@"
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/*
%attr(755,root,root) %{_bindir}/%{name}
/usr/lib/%{name}

%changelog
* Tue Dec 28 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Inital package
