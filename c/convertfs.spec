Summary:	Tool that allows you to change type of file system in the lack of backup space
Name:		convertfs
Version:	13jan2005
Release:	5.1
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	https://tzukanov.narod.ru/convertfs/%{name}-%{version}.tar.gz
Source1:	https://members.optusnet.com.au/clausen/ideas/convertfs.txt
# Source0-md5:	71e8065e321898e259a55c8cefdfd75d
Patch0:		%{name}-safety.patch
Patch1:		%{name}-Makefile.patch
URL:		https://tzukanov.narod.ru/convertfs/
BuildRequires:	sed >= 4.0
Requires:	util-linux
Requires:	coreutils

%description
This simple toolset allows you to change type of file system in the
lack of backup space. The idea is to use sparse files support of
primary filesystem. We create a sparse image of block device, mkfs
secondary filesystem on it, mount it, mv files from primary filesystem
to mounted image and then map image to the device.

Remapping utility uses some kind of journaling to avoid breakage in
case of power failure. It's expected that you have Linux 2.4, glibc
2.2, recent util-linux, fileutils.

You can convert from virtually any filesystem type to virtually any
one as long as they are both block-oriented and supported by Linux for
read/write, and as long as primary filesystem supports sparse files.

%prep
%setup  -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install convertfs_dumb devclone devremap prepindex contrib/convertfs $RPM_BUILD_ROOT%{_sbindir}
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/convertfs.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_docdir}/*

%changelog
* Mon Feb 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 13jan2005
- Rebuilt for Fedora

* Mon Feb 12 2007 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: convertfs.spec,v $
Revision 1.9  2007/02/12 21:23:51  glen
- tabs in preamble

Revision 1.8  2007/02/12 00:48:42  baggins
- converted to UTF-8

Revision 1.7  2006/05/08 13:10:27  darekr
- added -Makefile patch to pass CC instead of using sed

Revision 1.6  2005/01/16 15:10:09  charles
- Epoch 1 (18mar2002 > 13jan2005)

Revision 1.5  2005/01/16 14:16:57  charles
- updated to 13jan2005

Revision 1.4  2004/08/16 15:33:54  twittner
- typo.

Revision 1.3  2003/08/25 10:53:17  qboosh
- pl, BR: new sed

Revision 1.2  2003/08/24 04:59:56  aredridel
- added safety patch. Still needs work

Revision 1.1  2003/08/23 17:27:05  arekm
- initial pld release
