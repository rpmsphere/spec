%global __os_install_post %{nil}

Summary: Programs and libs needed for manipulating reiserfs partitions
Name: progsreiserfs
Version: 0.3.0.4
Release: 4.1
License: GPL
Group: Applications/System
URL: http://www.namesys.com
Source: ftp://ftp.namesys.com/pub/libreiserfs/progsreiserfs-0.3.0.4.tar.gz

%description
This is a library for reiserfs filesystem access and manipulation.
The primary goal is to develop the nice, full functionality library
wich might be linked against any projects which needed reiserfs filesystem
access. There are GNU Parted, GNU GRUB, Yaboot, Partimage, EVMS, etc.

%prep
%setup -q

%build
export LDFLAGS=-L`pwd`/libdal/.libs
%configure --enable-static=yes --enable-shared=yes
sed -i 's|-Werror=format-security||' `find . -name Makefile`
%{__make} %{?_smp_mflags}

%install
%make_install

%package devel
Summary: Progsreiserfs development files
Group: Development/Libraries
Requires: progsreiserfs = %{version}-%{release}

%description devel
Development files of progsreiserfs.

%package conflict
Summary: The files conflicting with the package reiserfs-utils
Group: Applications/System
Requires: progsreiserfs = %{version}-%{release}

%description conflict
This subpackage contains the files which are conflicting with the files of
the package reiserfs-utils.

%files
%{_libdir}/libdal-0.3.so.0.0.0
%{_libdir}/libdal-0.3.so.0
%{_libdir}/libreiserfs-0.3.so.0.0.0
%{_libdir}/libreiserfs-0.3.so.0
%{_sbindir}/cpfs.reiserfs
%{_sbindir}/resizefs.reiserfs
%{_sbindir}/tunefs.reiserfs
%{_datadir}/aclocal/progsreiserfs.m4
%{_mandir}/man8/*.8*

%files devel
%{_includedir}/dal
%{_includedir}/reiserfs
%{_libdir}/libdal.so
%{_libdir}/libdal.a
%{_libdir}/libdal.la
%{_libdir}/libreiserfs.a
%{_libdir}/libreiserfs.la
%{_libdir}/libreiserfs.so

%files conflict
%{_sbindir}/fsck.reiserfs
%{_sbindir}/mkfs.reiserfs

%changelog
* Fri Feb 20 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0.4
- Rebuilt for Fedora
* Wed Mar 3 2004 Dries Verachtert 0.3.0.4-1
- first packaging for Fedora Core 1
