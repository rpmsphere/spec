Name:		nodm
Version:	0.7
Release:	6.1
Summary:	Automatic Display Manager
Source0:	http://www.enricozini.org/sw/nodm/nodm-%{version}.tar.gz
Source1:	initd-nodm
Source2:	sysconfig-nodm
URL:		http://www.enricozini.org/sw/nodm/
Group:		System/X11/Displaymanagers
License:	BSD and GPLv2+
BuildRoot:	%{_tmppath}/build-%{name}-%{version}
BuildRequires:	pam-devel
BuildRequires:	help2man
BuildRequires:	gcc make glibc-devel
BuildRequires:	autoconf automake libtool pkgconfig
Requires: xorg-x11-xdm

%description
nodm is an automatic display manager which automatically starts an X session at
system boot. It is meant for devices like smartphones, but can be used on a
regular computer as well, if the security implications are acceptable.

%prep
%setup -q

%build
NOCONFIGURE=true ./autogen.sh
%configure
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall
%__install -Dm 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/%{name}
%__install -Dm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README TODO
%{_sbindir}/%{name}
%{_sysconfdir}/init.d/%{name}
%{_sysconfdir}/sysconfig/%{name}
%{_mandir}/man8/nodm.8.*

%post
ln -sf /etc/pam.d/xdm /etc/pam.d/nodm

%postun
%__rm -f /etc/pam.d/nodm

%changelog
* Sun Jul 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7
- Rebuilt for Fedora
* Tue Jun 22 2010 boris@steki.net
- Added required pam file in /etc/pam.d/ as link to xdm
  as it is always added trough xserver installation
* Tue Jun 22 2010 boris@steki.net
- Updated to new version
- Fix autotools typo
- Removed obsolete patch
- Added boot script and sysconfig template
* Mon Mar 15 2010 pascal.bleser@opensuse.org
- initial package based on the Fedora 13 spec file by Sebastian
  Dziallas (including the patch)
