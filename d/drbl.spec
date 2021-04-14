Summary:	DRBL (Diskless Remote Boot in Linux) package
Name:		drbl
Version:	2.32.10
Release:	1
License:	GPLv2+
Group:		Networking/Other
URL:		https://drbl.org
Source0:	http://free.nchc.org.tw/drbl-core/pool/drbl/stable/drbl/drbl_%{version}.orig.tar.xz
BuildArch:	noarch

%description
DRBL (Diskless Remote Boot in Linux).
Description:
DRBL provides a diskless or systemless environment for client machines.
It works on Debian, Ubuntu, Mageia, Red Hat, Fedora, CentOS and OpenSuSE.
DRBL uses distributed hardware resources and makes it possible for
clients to fully access local hardware.
It also includes Clonezilla, a partition and disk cloning utility similar
to Symantec Ghost(TM) or True Image(TM).

For more details, check
1. http://drbl.org or http://drbl.sourceforge.net (English)
2. http://drbl.nchc.org.tw (Traditional Chinese - Taiwan) 

%prep
%setup -q

%build
%make_build all

%install
%make_install

%files
%doc doc/*
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}/%{name}
%{_datadir}/gdm/themes/drbl-gdm

%changelog
* Mon Mar 15 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.32.10
- Rebuilt for Fedora
* Sun Dec 06 2020 luigiwalser <luigiwalser> 2.32.10-1.mga8
+ Revision: 1654010
- 2.32.10
- update source URL
* Fri Feb 14 2020 umeabot <umeabot> 2.25.10-2.mga8
+ Revision: 1521892
- Mageia 8 Mass Rebuild
* Fri Jan 04 2019 daviddavid <daviddavid> 2.25.10-1.mga7
+ Revision: 1349091
- new version: 2.25.10
* Tue Sep 18 2018 umeabot <umeabot> 2.11.15-2.mga7
+ Revision: 1261975
- Mageia 7 Mass Rebuild
* Mon Dec 28 2015 neoclust <neoclust> 2.11.15-1.mga6
+ Revision: 916186
- imported package drbl
