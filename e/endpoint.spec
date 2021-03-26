%define __arch_install_post %{nil}

Summary: 	Ixia Performance Endpoint
Name: 		endpoint
Version: 	8.1
Release: 	1%{?dist}.bin
License: 	Commercial, freeware
Group:		Applications/Communications
Source0:	http://downloads.ixiacom.com/products/ixchariot/endpoint_library/8.10/8.1.49.17/linux_amd64/pelinux_amd64_81.tar.gz
Source1:	http://downloads.ixiacom.com/products/ixchariot/endpoint_library/8.10/8.1.49.17/linux/pelnx_81.tar.gz
URL:		http://legacy-www.ixiacom.com/support/endpoint_library/index.php

%description
This software only runs in conjunction with IxChariot.
A Performance Endpoint is a "skinny" network application that
understands how to execute many different test scripts over
different protocols.

When a Performance Endpoint runs a script, it looks just like an
application to the network.  It collects performance statistics
and sends them to the console, which produces reports or alerts
reflecting the response time, connectivity, and throughput in
your network.

%prep
%ifarch x86_64
%setup -q -c
%else
%setup -q -T -b 1 -c
%endif

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a temp/* %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#! /bin/bash
cd /usr/libexec/%{name}
exec ./endpoint
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_libexecdir}/%{name}

%changelog
* Thu Nov 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> 8.1
- initial package
