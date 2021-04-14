Name:		irker
Version:	2.13
Release:	2.1
Summary:	IRC Message Relay
License:	BSD
Group:		Networking/IRC
URL: 		http://www.catb.org/esr/irker/
Source0:	http://www.catb.org/~esr/irker/%{name}-%{version}.tar.gz
Patch0: irker-1.9-systemd-unit-user.patch
BuildArch: noarch
Requires: python-irc
Requires: python-simplejson
BuildRequires: xmlto
BuildRequires: docbook-style-xsl
BuildRequires: systemd-devel

%description
An IRC client that runs as a daemon accepting notification requestsas JSON 
objects presented to a listening socket. It is meant to be used by hook scripts
in version-control repositories, allowing them to send commit notifications to
project IRC channels.

A hook script that works with git, hg, and svn is included in the distribution.

%prep
%setup -q
#patch0 -p1
sed -i 's/-o 0 -g 0 //' Makefile

%build
make

%install
%make_install
install -Dm755 irkerhook.py %{buildroot}%{_prefix}/lib/%{name}/irkerhook.py

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}/usr/lib/irker/irkerhook.py %{buildroot}/usr/bin/irkerd

%files
%doc README
%{_bindir}/%{name}*
%{_unitdir}/%{name}*.service
%{_mandir}/man*/irk*
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/irkerhook.py*

%changelog
* Tue May 17 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.13
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 2.11-3.mga5
+ Revision: 745364
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 2.11-2.mga5
+ Revision: 680565
- Mageia 5 Mass Rebuild
* Sat Aug 30 2014 colin <colin> 2.11-1.mga5
+ Revision: 669560
- New version: 2.11
* Tue Oct 22 2013 umeabot <umeabot> 1.15-4.mga4
+ Revision: 545880
- Mageia 4 Mass Rebuild
* Thu Oct 17 2013 luigiwalser <luigiwalser> 1.15-3.mga4
+ Revision: 501939
- include pyc and pyo files in files list
* Sat Jan 12 2013 umeabot <umeabot> 1.15-2.mga3
+ Revision: 354495
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Fri Dec 28 2012 boklm <boklm> 1.15-1.mga3
+ Revision: 335826
- Version 1.15
- Install irkerhook.py in /usr/lib/irker
* Tue Oct 09 2012 colin <colin> 1.9-1.mga3
+ Revision: 303709
- Add systemd-devel BR for .service file
- Add some requires and buildrequires
- imported package irker
