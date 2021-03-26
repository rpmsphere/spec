Summary:	Program for secure cleaning of free space on file systems
Name:		wipefreespace
Version:	2.2.2
Release:	3.1
URL:		http://wipefreespace.sf.net
License:	GPLv2
Group:		Applications/System
Source:		https://sourceforge.net/projects/wipefreespace/files/wipefreespace/%{version}/%{name}-%{version}.tar.gz
Requires:	xfsprogs
BuildRequires:	xfsprogs
BuildRequires:	gcc, glibc, glibc-devel, glibc-headers, make
Obsoletes:	e2wipefreespace <= 0.5
Provides:	e2wipefreespace >= 0.6

%description
The wipefreespace is a program which securely cleans free space on given
file systems, making confidential removed data recovery impossible. It also
removes deleted files' names, so that no trace is left. Supported file systems
are: ext2/3/4, NTFS, XFS, ReiserFSv3/4, FAT12/16/32, MinixFSv1/2, JFS, HFS+
and OCFS.

%prep
%setup -q
sed -i -e '126i #include <sys/sysmacros.h>' -e '811i struct stat s;' src/wfs_util.c

%build
autoreconf -ifv
./configure --prefix=/usr --mandir=/usr/share/man \
	--infodir=/usr/share/info --libdir=/usr/lib
make

%install
%{__mkdir_p} $RPM_BUILD_ROOT/usr/share/info
%{__make} DESTDIR="$RPM_BUILD_ROOT" install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%exclude %{_infodir}/dir
%{_infodir}/wipefreespace.info.gz
%{_mandir}/man1/wipefreespace.1.gz
%doc README COPYING AUTHORS ChangeLog
%{_datadir}/locale/*/LC_MESSAGES/wipefreespace.mo

%changelog
* Wed May 16 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.2
- Rebuild for Fedora
* Sun Nov 03 2013 Bogdan Drozdowski <bogdandr@op.pl>
- Initial package
