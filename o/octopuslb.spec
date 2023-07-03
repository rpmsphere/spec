Summary: TCP/IP Load Balancer
Name: octopuslb
Version: 1.14
Release: 2.4
License: GPLv2+
Group: System Environment/Daemons
URL: https://octopuslb.sourceforge.net/
Source: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires: net-snmp-devel >= 5.0, systemd-units

%description
Octopuslb is an extremely fast TCP load balancer with extensions 
for HTTP to allow balancing based on URI. Features include: server health 
checks and load polling, dynamic configuration, and the ability to 
carbon copy incoming requests. 

%prep
%setup -q
sed -i '1i #include <sys/resource.h>' src/init.c

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot} 
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install

mkdir -p %{buildroot}/%{_sysconfdir}/octopuslb
mv %{buildroot}/%{_sysconfdir}/octopuslb.conf %{buildroot}/%{_sysconfdir}/octopuslb/
mkdir -p %{buildroot}/%{_sysconfdir}/logrotate.d
install -m 644 %{_builddir}/%{buildsubdir}/extras/octopuslb.logrotated %{buildroot}/%{_sysconfdir}/logrotate.d/octopuslb
mkdir -p %{buildroot}/%{_localstatedir}/run/octopuslb
mkdir -p %{buildroot}/%{_localstatedir}/log/octopuslb
mkdir -p %{buildroot}/%{_unitdir}
install -m 644 %{_builddir}/%{buildsubdir}/extras/octopuslb.service %{buildroot}/%{_unitdir}/octopuslb.service
%{__sed} -i 's/\/var\/log/\/var\/log\/octopuslb/g' %{buildroot}/%{_sysconfdir}/octopuslb/octopuslb.conf

%post
/bin/systemctl daemon-reload >/dev/null

%preun
if [ $1 -eq 0 ]; then
        # On uninstall (not upgrade), disable and stop the units
        /bin/systemctl --no-reload disable octopuslb.service octopuslb.socket >/dev/null 2>&1 || :
        /bin/systemctl stop octopuslb.service >/dev/null 2>&1 || :
fi

%postun
# Reload init system configuration, to make systemd honour changed
# or deleted unit files
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%files
%doc README CHANGELOG COPYRIGHT TODO AUTHORS COPYING
%dir %{_sysconfdir}/octopuslb
%{_sbindir}/octopuslb-server
%{_sbindir}/octopuslb-admin
%{_localstatedir}/log/octopuslb
%{_localstatedir}/run/octopuslb
%config(noreplace) %{_sysconfdir}/logrotate.d/octopuslb
%config(noreplace) %{_sysconfdir}/octopuslb/octopuslb.conf
%{_mandir}/man1/*
%{_unitdir}/octopuslb.service

%changelog
* Wed Apr 29 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.14
- Rebuilt for Fedora
* Fri Sep 16 2011 Alistair Reay <alreay1@gmail.com> 1.13-1
- Ustream bump - bugfixes only
* Fri May 13 2011 Alistair Reay <alreay1@gmail.com> 1.12-1
- Ustream bump - bugfixes only
* Mon Mar 7 2011 Alistair Reay <alreay1@gmail.com> 1.11-2
- Removed buildrequires for 'net-snmp-libs'
- Changed buildroot to use %{} variables and removed literal from setup section 
* Mon Feb 28 2011 Alistair Reay <alreay1@gmail.com> 1.11-1
- After fedora community feedback - changed RPM name from 'octopus' to 'octopuslb'
- Changed binary names as well as installation directories
* Tue Nov 30 2010 Alistair Reay <alreay1@gmail.com> 1.10-1
- initial configuration for Fedora 14
