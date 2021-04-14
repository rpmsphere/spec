%define sname pgl

Name:		peerguardian
Version:	2.3.1
Release:	4.1
Summary:	A privacy oriented firewall application
Group:		Networking/Other
License:	GPLv3
URL:		http://sourceforge.net/projects/peerguardian/
Source0:	http://downloads.sourceforge.net/project/peerguardian/PeerGuardian%20Linux/%{version}/%{sname}-%{version}.tar.gz
BuildRequires:	libnetfilter_queue-devel
BuildRequires:	polkit-qt-devel
BuildRequires:	systemd-devel
BuildRequires:	dbus-devel

%description
PeerGuardian Linux (pgl) is a privacy oriented firewall application.
It blocks connections to and from hosts specified in huge blocklists 
(thousands or millions of IP ranges).
Its origin seeds in targeting aggressive IPs while using P2P.

%prep
%setup -q -n %{sname}-%{version}

%build
export LDFLAGS=-Wl,--allow-multiple-definition
export MOC=moc-qt4 UIC=uic-qt4
%configure --with-systemd=%{_unitdir}

%install
%make_install
find %{buildroot} -name "*.la" -delete

%files
%doc %{_docdir}/%{sname}/*
%{_sysconfdir}/NetworkManager/dispatcher.d/20%{sname}cmd
%{_sysconfdir}/cron.daily/%{sname}cmd
%{_sysconfdir}/dbus-1/system.d/org.netfilter.%{sname}.conf
%{_sysconfdir}/init.d/%{sname}
%{_sysconfdir}/logrotate.d/*
%{_sysconfdir}/%{sname}/*
#{_bindir}/blockcontrol2%{sname}cmd
%{_bindir}/%{sname}cmd
%{_bindir}/%{sname}gui
%{_libdir}/%{sname}/*
%{_sbindir}/%{sname}cmd.wd
%{_sbindir}/%{sname}d
%{_datadir}/applications/%{sname}gui.desktop
%{_mandir}/man1/%{sname}d.1.*
%{_datadir}/pixmaps/%{sname}gui.png
%{_unitdir}/%{sname}*.*

%changelog
* Fri Jun 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.1
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 2.2.4-3.mga5
+ Revision: 748882
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 2.2.4-2.mga5
+ Revision: 683395
- Mageia 5 Mass Rebuild
* Thu Mar 27 2014 barjac <barjac> 2.2.4-1.mga5
+ Revision: 609024
- new version 2.2.4
* Sat Dec 07 2013 barjac <barjac> 2.2.3-1.mga4
+ Revision: 555775
- imported package peerguardian
