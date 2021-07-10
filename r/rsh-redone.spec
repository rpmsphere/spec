%undefine _debugsource_packages

Name:           rsh-redone
Version:        83
Release:        8.1
License:        GPL
BuildRequires:  cmake
BuildRequires:  pam-devel
BuildRequires:  uif2iso
Group:          Productivity/Networking/Other
Summary:        Reimplementation of rsh and rlogin
Patch:		rsh-redone_83-1.diff.bz2
Source0:	%{name}-%{version}.tar.bz2

%description
Rsh-redone is a reimplementation of the remote shell clients and servers.
It is written from the ground up to avoid the bugs found in the standard
clients and servers. It also fully supports IPv6.

%package client
Group:          Productivity/Networking/Other
Summary:        Reimplementation of rsh and rlogin
Conflicts:		rsh

%description client
rsh-redone is a reimplementation of the remote shell clients and servers.
It is written from the ground up to avoid the bugs found in the standard
clients and servers. It also fully supports IPv6.

This package provides rsh and rlogin. 

%package server
Group:          Productivity/Networking/Other
Summary:        Reimplementation of rshd and rlogind
Conflicts:       rsh

%description server
rsh-redone is a reimplementation of the remote shell clients and servers.
It is written from the ground up to avoid the bugs found in the standard
clients and servers. It also fully supports IPv6.

This package provides rshd and rlogind

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf "$RPM_BUILD_ROOT"
%make_install
mv %{buildroot}/usr/etc %{buildroot}/etc

%clean
rm -rf "$RPM_BUILD_ROOT"

%files client
%{_bindir}/rlogin
%{_bindir}/rsh
%{_mandir}/man1/rlogin.1.gz
%{_mandir}/man1/rsh.1.gz
%{_mandir}/man5/rhosts.5.gz

%files server
%config /etc/pam.d/rlogin
%config /etc/pam.d/rsh
%{_sbindir}/in.rlogind
%{_sbindir}/in.rshd
%{_mandir}/man8/rlogind.8.gz
%{_mandir}/man8/rshd.8.gz

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 83
- Rebuilt for Fedora
* Fri Apr 11 2008 crrodriguez@suse.de
- initial version for openSUSE buildservice
