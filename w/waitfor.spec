%define __python /usr/bin/python2
Name:			waitfor
Version:		0.5
Release:		3.1
Summary:		Waits until specified Network Resource is available or Event has occured
Source:			https://www.hennessynet.com/waitfor/waitfor-%{version}.tar.gz
URL:			https://www.hennessynet.com/waitfor/
Group:			System/Monitoring
License:		GNU General Public License version 2 (GPL v2)
BuildRequires:	make xmlto lynx
BuildArch:		noarch
Requires:		python2

%description
The waitfor utility will wait until a url is available, until a port is being
listened to, until an amount of time has passed or until a shell command
succeeds. It's very useful when you want to coordinate the startup or
shutdown of services.

Authors:
--------
    Denis Hennessy <denis@hennessynet.com>

%prep
%setup -q
%__sed -i 's|^#!/usr/bin/env python$|#!%__python|' waitfor

%build
%__make waitfor.1

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -Dp -m0755 waitfor "$RPM_BUILD_ROOT%{_bindir}/waitfor"
%__install -Dp -m0644 waitfor.1 "$RPM_BUILD_ROOT%{_mandir}/man1/waitfor.1"

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc COPYING README
%{_bindir}/waitfor
%doc %{_mandir}/man1/waitfor.1*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora

* Wed Jun 24 2009 Pascal Bleser <pascal.bleser@opensuse.org> 0.4
- moved to openSUSE Build Service

* Wed Apr 11 2007 Pascal Bleser <guru@unixtech.be> 0.5-1
- new package
