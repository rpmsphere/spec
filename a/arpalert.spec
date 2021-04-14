Summary:	A monitor ethernet networks
Name:		arpalert
Version:	2.0.12
Release:	10.1
License:	GPLv2
Group:		Monitoring
URL:		http://www.arpalert.org/
Source0:	http://www.arpalert.org/src/%{name}-%{version}.tar.gz
Source1:	arpalert.service
Patch0:		arpalert-2.0.9-fix-str-fmt.diff
BuildRequires:	libpcap-devel

%description
This software is used for monitoring ethernet networks. It listens on a network
interface (without using 'promiscuous' mode) and catches all conversations of
MAC address to IP request. It then compares the mac addresses it detected with
a pre-configured list of authorized MAC addresses. If the MAC is not in list,
arpalert launches a pre-defined user script with the MAC address and IP address
as parameters. This software can run in daemon mode; it's very fast (low CPU
and memory consumption). It responds at signal SIGHUP (configuration reload)
and at signals SIGTERM, SIGINT, SIGQUIT and SIGABRT (arpalert stops itself).

%prep
%setup -q
%patch0 -p0

%build
export CC="gcc -Wl,--allow-multiple-definition"
%configure --localstatedir=/var
perl -pi -e "s|^lock_dir.*|lock_dir=/var/run/%{name}|g" Makefile
perl -pi -e "s|^log_dir.*|log_dir=/var/log/%{name}|g" Makefile
make

%install
%make_install

install -d %{buildroot}%{_unitdir}
install -d %{buildroot}/var/log/%{name}
install -d %{buildroot}/var/run/%{name}
install -d %{buildroot}%{_localstatedir}/lib/%{name}
install -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

sed "s:sysconfig:%{_sysconfdir}/sysconfig:" -i %{buildroot}%{_unitdir}/%{name}.service
rm -f %{buildroot}%{_includedir}/arpalert.h

%files
%doc CHANGES COPYING README
%{_unitdir}/%{name}.service
%{_sysconfdir}/arpalert
%{_sbindir}/arpalert
%{_mandir}/man8/arpalert.8*
/var/log/%{name}
/var/run/%{name}
%{_localstatedir}/lib/%{name}

%changelog
* Mon Jun 01 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.12
- Rebuilt for Fedora
* Mon Sep 22 2014 Denis Silakov <denis.silakov@rosalab.ru> 2.0.12-5
+ Revision: db37138
- Spec cleanup
