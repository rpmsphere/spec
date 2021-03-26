Summary:	Opensource Clone System (ocs), clonezilla
Name:		clonezilla
Version:	3.35.2
Release:	1
License:	GPLv2+
Group:		Archiving/Backup
URL:		http://www.clonezilla.org
Source0:	http://free.nchc.org.tw/drbl-core/src/stable/%{name}-%{version}.tar.xz
Patch0:		ambiguous-python-shebang.patch
BuildArch:	noarch
Requires:	drbl >= 2.30.5
Requires:	partimage >= 0.6.7
Requires:	psmisc
Requires:	udpcast
Requires:	partclone >= 0.2.91
Requires:	ntfsprogs
Requires:	dialog

%description
Clonezilla, based on DRBL, Partition Image, ntfsclone, partclone, and udpcast,
allows you to do bare metal backup and recovery. Two types of Clonezilla
are available, Clonezilla live and Clonezilla SE (Server Edition). Clonezilla
live is suitable for single machine backup and restore. While Clonezilla SE
is for massive deployment, it can clone many (40 plus!) computers simultaneously.
For more info, check http://clonezilla.org, http://clonezilla.nchc.org.tw.

%prep
%setup -q
%patch0 -p1

%build
%make_build

%install
%make_install

%files
%doc doc/*
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/drbl/*
%{_datadir}/%{name}/
%{_sysconfdir}/drbl/*

%changelog
* Mon Mar 15 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.35.2
- Rebuild for Fedora
* Sun Dec 06 2020 luigiwalser <luigiwalser> 3.35.2-1.mga8
+ Revision: 1654011
- 3.35.2
- fix ambiguous python shebang in gen-torrent-from-ptcl
* Fri Feb 14 2020 umeabot <umeabot> 3.27.16-2.mga8
+ Revision: 1521898
- Mageia 8 Mass Rebuild
* Fri Jan 04 2019 daviddavid <daviddavid> 3.27.16-1.mga7
+ Revision: 1349098
- new version: 3.27.16
- should be a noarch pkg
- fix some owner dir
* Sat Sep 22 2018 umeabot <umeabot> 3.19.7-3.mga7
+ Revision: 1296589
- Mageia 7 Mass Rebuild
* Tue Jul 25 2017 neoclust <neoclust> 3.19.7-2.mga7
+ Revision: 1130543
- Add missing dependancy in cdialog (mga#21348)
* Mon Dec 28 2015 neoclust <neoclust> 3.19.7-1.mga6
+ Revision: 916193
- imported package clonezilla
