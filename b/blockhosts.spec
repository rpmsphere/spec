%global _name BlockHosts

Name:			blockhosts
Version:		2.7.0
Summary:		Block IP Addresses based on system logs showing undesirable access patterns
License:		https://creativecommons.org/licenses/publicdomain/
URL:			https://www.aczoom.com/cms/blockhosts/
Source0:		%{_name}-%{version}.tar.gz
Group:			Applications/System
Release:		1
Patch0:			blockhosts.cfg.2.4.0.diff
BuildArch:		noarch

%description
Block IP Addresses based on login or access failure
information in system logs.

Updates a hosts blockfile (such as hosts.allow) automatically,
to block IP addresses. Will also expire previously blocked addresses
based on age of last failed login attempt, this keeps the blockfile
size manageable.
In addition to TCP_WRAPPERS, can also execute iptables or ip route commands
to block all TCP/IP network input from an IP address, so all services, even
those that do not run under libwrap TCP_WRAPPERS, can be protected.

Facilities for whitelists and blacklists, and email notification on major
events are also available.

%prep
%setup -q -n %{_name}-%{version}
%patch0

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logwatch/conf/services
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logwatch/scripts/services

install -m 644 blockhosts.cfg $RPM_BUILD_ROOT%{_sysconfdir}/blockhosts.cfg
install -m 644 logwatch/blockhosts.conf $RPM_BUILD_ROOT%{_sysconfdir}/logwatch/conf/services/blockhosts.conf
install -m 644 logwatch/blockhosts $RPM_BUILD_ROOT%{_sysconfdir}/logwatch/scripts/services/blockhosts
install -m 644 logrotate.d/blockhosts $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/blockhosts
install -m 755 blockhosts.py $RPM_BUILD_ROOT%{_bindir}/blockhosts.py
#install -m 755 bhrss.py $RPM_BUILD_ROOT%{_bindir}/bhrss.py

sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%post
if [ "$1" = 1 ]
then
cat <<_END_ >>/etc/hosts.allow
#---- BlockHosts Additions
#---- BlockHosts Additions
sshd : ALL: spawn %{_bindir}/blockhosts.py & : allow
_END_
fi

%postun
if [ "$1" = 0 ]
then
tempfil=$(mktemp)
sed '/^#---- BlockHosts Additions$/,/^#---- BlockHosts Additions$/d' < /etc/hosts.allow | \
egrep -v -e '^sshd : ALL: spawn %{_bindir}/blockhosts.py & : allow$' >$tempfil
[ "$?" -eq 0 ] && cp $tempfil /etc/hosts.allow
rm $tempfil
fi

%files
%dir %{_sysconfdir}/logwatch
%dir %{_sysconfdir}/logwatch/conf
%dir %{_sysconfdir}/logwatch/scripts
%dir %{_sysconfdir}/logwatch/conf/services
%dir %{_sysconfdir}/logwatch/scripts/services
%config %{_sysconfdir}/blockhosts.cfg
%config %{_sysconfdir}/logrotate.d/blockhosts
%config %{_sysconfdir}/logwatch/conf/services/blockhosts.conf
%config %{_sysconfdir}/logwatch/scripts/services/blockhosts
%{_bindir}/blockhosts.py
#{_bindir}/bhrss.py
%doc CHANGES INSTALL LICENSE README blockhosts.html

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.0
- Rebuilt for Fedora
* Sat Apr 17 2010 David Bolt <davjam@davjam.org> 2.4.0
- first package for openSUSE
