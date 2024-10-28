%undefine _debugsource_packages

Summary:        A keyboard shortcut daemon
Name:           actkbd
Version:        0.2.8
Release:        4.1
URL:            https://users.softlab.ece.ntua.gr/~thkala/projects/actkbd/
License:        GPL v2+
Group:          System/Configuration/Other
Source:         %name-%version.tar
Patch0:         actkbd-0.2.7-amd64.patch

%description
actkbd is a daemon that reacts to user defined keys and launches
specific commands. It can be used to utilize multimedia keys on
simple setups, or assigned custom actions to rarely used keys.

%prep
%setup -q
%patch 0 -p1
sed -i 's|-Wall|-fPIE|' Makefile

%build
%make_build

%install
install -D -m 755 %name %buildroot%_sbindir/%name
install -D -m 644 %name.conf %buildroot%_sysconfdir/%name.conf
install -pD -m 755 %name.init  %buildroot%_initrddir/%name
install -pD -m 644 %name.service %buildroot%_unitdir/%name.service

%files
%doc AUTHORS ChangeLog COPYING FAQ NEWS README TODO samples/*
%config %_sysconfdir/%name.conf
%_sbindir/%name
%_initrddir/%name
%_unitdir/%name.service

%changelog
* Thu Dec 21 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.8
- Rebuilt for Fedora
* Sun Jul 06 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.2.8-alt2
- Fix lsb header in init script
* Fri Jul 04 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.2.8-alt1
- Initial build
