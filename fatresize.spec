Name: fatresize
Version: 1.0.3
Release: 8.1
License: GPLv2+
Group: File tools
Summary: FAT16/FAT32 resizer
URL: http://sourceforge.net/projects/%name/
# git://fatresize.git.sourceforge.net/gitroot/fatresize/fatresize
Source: %name-%version.tar.gz
BuildRequires: parted-devel
BuildRequires: e2fsprogs-devel
BuildRequires: docbook-utils
BuildRequires: w3m

%description
The FAT16/FAT32 non-destructive resizer.

%prep
%setup -q
sed -i -e 's|, return 0||' -e 's|, return||' -e 's|start <= end,|start <= end);|' -e '386d' fatresize.c

%build
autoreconf -if
%configure
sed -i -e 's|-lparted|-lparted -lparted-fs-resize|' -e 's|docbook-to-man|docbook2man|' Makefile
make

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%_sbindir/*
%_mandir/man1/*

%changelog
* Wed Feb 25 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuild for Fedora
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.3-alt11.git20090730.qa1
- NMU: rebuilt for debuginfo.
* Thu Apr 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt11.git20090730
- Version 1.0.3
* Sun Aug 10 2008 Led <led@altlinux.ru> 1.0.2-alt11
- fixed spec
- added %name-1.0.2-alt.patch
* Wed Aug 15 2007 Led <led@altlinux.ru> 1.0.2-alt10
- rebuild with libparted-1.8.so.8
- fixed License
* Mon May 14 2007 Led <led@altlinux.ru> 1.0.2-alt9
- rebuild with libparted-1.8.so.7
* Sun Mar 25 2007 Led <led@altlinux.ru> 1.0.2-alt8
- rebuild with libparted-1.8.so.6
* Mon Mar 19 2007 Led <led@altlinux.ru> 1.0.2-alt7
- rebuild with libparted-1.8.so.4
- added %name-1.0.2+libparted-1.8.3.patch
* Tue Jan 16 2007 Led <led@altlinux.ru> 1.0.2-alt6
- rebuild with libparted-1.8.so.2
* Mon Nov 27 2006 Led <led@altlinux.ru> 1.0.2-alt5
- rebuild with libparted-1.8.so.0
- added docs
* Wed Jul 05 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.2-alt4.1
- NMU: rebuild with libparted-1.7.so.1
* Tue Sep 20 2005 Kachalov Anton <mouse@altlinux.ru> 1.0.2-alt4
- LFS support
* Mon Sep 19 2005 Kachalov Anton <mouse@altlinux.ru> 1.0.2-alt3
- restore original partition geometry while resizing EVMS partition
* Thu Sep 15 2005 Kachalov Anton <mouse@altlinux.ru> 1.0.2-alt2
- added default name translation of EVMS partitions
- synced resize code with new cmd-line parted utility 1.6.24
* Wed Sep 07 2005 Kachalov Anton <mouse@altlinux.ru> 1.0.2-alt1
- tell k|M|G and ki|Mi|Gi suffixes
- proper filesystem information
- resize partition only for non-EVMS partitions
* Wed Apr 13 2005 Kachalov Anton <mouse@altlinux.ru> 1.0.1-alt1
- removed translation option: fix new geometry boundary
* Mon Apr 11 2005 Anton D. Kachalov <mouse@altlinux.org> 1.0-alt2
- added translating option
* Fri Apr 08 2005 Anton D. Kachalov <mouse@altlinux.org> 1.0-alt1
- first build
