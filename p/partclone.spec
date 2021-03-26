Name:		partclone
Version:	0.2.91
Release:	1
Group:		Applications/System
URL:		http://partclone.sourceforge.net
License:	GPLv2
Summary:	File System Clone Utilities
Source0:	https://jaist.dl.sourceforge.net/project/partclone/testing/%{name}-%{version}.tar.gz
Patch0:		partclone-0.2.71-patch-001
BuildRequires:	e2fsprogs-devel
BuildRequires:	ntfs-3g-devel
BuildRequires:	ncurses-devel
BuildRequires:	libuuid-devel 
BuildRequires:	libvmfs-devel
BuildRequires:	libblkid-devel

%description
Partclone provides utilities to back up and restore used-blocks of a partition
and it is designed for higher compatibility of the file system by using
existing library, e.g. e2fslibs is used to read and write the ext2 partition.

Authors:
--------
    Thomas Tsai <Thomas _at_ nchc org tw>
    Jazz Wang <jazz _at_ nchc org tw>

%prep
%setup -q 
%patch0 -p1

%build
%configure \
	--enable-hfsp \
	--enable-fat \
	--enable-exfat \
	--enable-ntfs \
	--enable-vmfs \
	--enable-extfs \
	--enable-btrfs \
	--enable-minix \
	--enable-mtrace \
	--enable-fs-test
make

%install
%make_install
%find_lang %name

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md TODO
%doc %{_mandir}/man?/*
%{_sbindir}/*
%{_datadir}/%{name}/*

%changelog
* Wed Aug 16 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.91
- Update to 0.2.91

* Tue Apr 28 2015 Lawrence R. Rogers <lrr@cert.org> 0.2.71-4
* Release 0.2.71-4
	New libntfs.so for CentOS 7
	All others - recompiled to keep the revision in sync

* Fri Apr 24 2015 Lawrence R. Rogers <lrr@cert.org> 0.2.71-3
* Release 0.2.71-3
	New libntfs.so for Fedora 21
	All others - recompiled to keep the revision in sync

* Sat Nov 15 2014 Lawrence R. Rogers <lrr@cert.org> 0.2.71-2
  New libntfs.so

* Tue Oct  7 2014 Lawrence R. Rogers <lrr@cert.org> 0.2.71-1
	fix configure.ac and add libblkid-dev check
	fix xfs
	merger btrfs to 3.14 and update makefile
	try to merge btrfs 3.14.1
	fix restore-to-raw option

* Mon Oct  6 2014 Lawrence R. Rogers <lrr@cert.org> 0.2.69-2
  Removed Obsoletes as it is wrong to do here.

* Mon Mar 17 2014 Lawrence R. Rogers <lrr@cert.org> 0.2.69-1
  See included Changelog

* Mon Mar 17 2014 Lawrence R. Rogers <lrr@cert.org> 0.2.48-5
  New libntfs.so

* Fri Sep 06 2013 Lawrence R. Rogers <lrr@cert.org> 0.2.48-4
  Obsoletes ntfs-3g for CentOS

* Wed May 1 2013 Lawrence R. Rogers <lrr@cert.org> 0.2.48-3
  Now uses latest libntfs-3g so which comes from fuse-ntfs-3g instead of ntfs-3g

* Thu Feb 21 2013 Lawrence R. Rogers <lrr@cert.org> 0.2.48-2
  Now uses latest libntfs-3g so

* Fri Jun 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.2.48-1mdv2011.0
+ Revision: 801781
- update to 0.2.48

* Mon Dec 19 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.2.38-1
+ Revision: 743700
- BR ncurses-devel added
- added BR libuuid-devel, smp build re-enabled
- disable smp build
- autoconf not needed
- update to 0.2.38

  + Jerome Martin <jmartin@mandriva.org>
    - Updated to 0.1.9

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Leonardo de Amaral Vidal <leonardoav@mandriva.com>
    - Spec package fix

* Mon Jul 07 2008 Leonardo de Amaral Vidal <leonardoav@mandriva.com> 0.0.6-1mdv2009.0
+ Revision: 232459
- partclone package built
- import partclone


* Thu Feb 21 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.6-3
- Bug fixed: clone.fat was not compiled.

* Thu Feb 21 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.6-1
- New upstream 0.0.6-1.

* Sat Feb 16 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.5-16
- New upstream 0.0.5-16.

* Mon Feb 04 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.5-15
- New upstream 0.0.5-15.

* Thu Jan 24 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.5-10
- New upstream 0.0.5-10.

* Fri Jan 04 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.5-1
- New upstream 0.0.5-1.

* Thu Jan 03 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.4-4
- Sync the version number with Debian package.
- Enable static linking.

* Mon Dec 31 2007 - Steven Shiau <steven _at_ nchc org tw> 0.0.1-2
- Some doc and debian rules were added by Thomas Tsai.

* Mon Dec 10 2007 - Steven Shiau <steven _at_ nchc org tw> 0.0.1-1
- Initial release for partclone.
