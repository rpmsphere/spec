Name:		ext3grep
Version:	0.10.2
Release:	9
Summary:	Investigation and recovery tool for ext3 filesystem
Group:		Security
License:	GPLv2+
URL:		https://code.google.com/p/ext3grep/
Source:		https://ext3grep.googlecode.com/files/ext3grep-%version.tar.gz
# Patch for bug 34 https://code.google.com/p/ext3grep/issues/detail?id=34
# Issue with new ext2fs lib (patch from Debian)
Patch0:		ext3grep-0.10.2-new-ext2fs.diff
# From Debian
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=894650
Patch1:		002_remove_i_dir_acl.diff
BuildRequires:	pkgconfig(ext2fs)

%description
A tool to investigate an ext3 file system for deleted content and
possibly recover it.

%prep
%setup -q
%autopatch -p1
%ifarch aarch64
cp -f /usr/lib/rpm/redhat/config.* .
%endif

%build
# https://code.google.com/p/ext3grep/issues/detail?id=14
export CXX=%{_bindir}/g++
%configure
make

%install
# Builds twice unless setting it here as well:
export CXX=%{_bindir}/g++
%make_install

%files
%doc NEWS README
%{_bindir}/ext3grep

%changelog
* Tue Jan 15 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10.2
- Rebuilt for Fedora
* Sun Sep 23 2018 umeabot <umeabot> 0.10.2-9.mga7
  (not released yet)
+ Revision: 1297647
- Mageia 7 Mass Rebuild
* Wed Jun 06 2018 wally <wally> 0.10.2-8.mga7
+ Revision: 1235002
- add patch from Debian to fix build with e2fsprogs >= 1.44.1
- fix build on aarch64
* Thu Feb 04 2016 umeabot <umeabot> 0.10.2-7.mga6
+ Revision: 935036
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 0.10.2-6.mga5
+ Revision: 740920
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.10.2-5.mga5
+ Revision: 679067
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 0.10.2-4.mga4
+ Revision: 504191
- Mageia 4 Mass Rebuild
* Fri Jan 11 2013 umeabot <umeabot> 0.10.2-3.mga3
+ Revision: 349873
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Fri Oct 26 2012 malo <malo> 0.10.2-2.mga3
+ Revision: 310541
- fix build due to new ext2fs with patch from Debian
- spec clean-up
- update RPM group
* Sat Jan 15 2011 anssi <anssi> 0.10.2-1.mga1
+ Revision: 19795
- imported package ext3grep
* Tue Aug 17 2010 Anssi Hannula <anssi@mandriva.org> 0.10.2-1mdv2011.0
+ Revision: 570722
- new version
* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.10.1-2mdv2010.0
+ Revision: 437508
- rebuild
* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 0.10.1-1mdv2009.1
+ Revision: 324630
- New upstream release
* Sat Oct 18 2008 Anssi Hannula <anssi@mandriva.org> 0.9.0-1mdv2009.1
+ Revision: 294823
- new version
- use gcc directly to avoid PCH+icecream problems (upstream bug #14)
* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-3mdv2009.0
+ Revision: 266747
- rebuild early 2009.0 package (before pixel changes)
* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.6.0-2mdv2009.0
+ Revision: 197567
- initial Mandriva release
