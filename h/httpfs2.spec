Name:		httpfs2
Version:	0.1.5
Release:	6
Summary:	FUSE filesystem for mounting files from HTTP servers
License:	GPLv2+
Group:		Networking/Remote access
URL:		http://httpfs.sourceforge.net/
Source0:	http://sourceforge.net/projects/httpfs/files/%{name}/%{name}-%{version}.tar.gz
Patch0:		httpfs2-0.1.5-mga-add_makeinstall_rule.patch
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	asciidoc

%description
httpfs2 is a FUSE based filesystem for mounting HTTP or HTTPS URLS as files
in the filesystem. There is no notion of listable directories in HTTP so
only a single URL can be mounted. The server must be able to send byte ranges.

%prep
%setup -q
%autopatch -p1
sed -i 's/\r$//' httpfs2.1.txt

%build
%make_build

%install
%make_install

%files
%doc httpfs2.1.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-mt
%{_bindir}/%{name}-ssl
%{_bindir}/%{name}-ssl-mt
%{_mandir}/man1/%{name}*.1.*

%changelog
* Sat Apr 3 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.5
- Rebuilt for Fedora
* Thu Feb 13 2020 umeabot <umeabot> 0.1.5-6.mga8
+ Revision: 1513508
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%makeinstall_std
* Sun Sep 23 2018 umeabot <umeabot> 0.1.5-5.mga7
+ Revision: 1298217
- Mageia 7 Mass Rebuild
* Tue Mar 08 2016 blino <blino> 0.1.5-4.mga6
+ Revision: 987267
- rebuild for armv5tl (also missed in first Mga6 mass rebuild)
* Mon Jan 11 2016 luigiwalser <luigiwalser> 0.1.5-3.mga6
+ Revision: 921811
- rebuild for gnutls
* Sat Dec 20 2014 daviddavid <daviddavid> 0.1.5-2.mga5
+ Revision: 804514
- add missing BR on gnutls-devel to enable SSL support
- rediff patch0 to improve installation of binaries and manpages files
- adjust file list
* Sat Dec 20 2014 daviddavid <daviddavid> 0.1.5-1.mga5
+ Revision: 804469
- imported package httpfs2
