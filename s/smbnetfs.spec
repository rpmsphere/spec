Summary:	SMBNetFS - using Samba/Microsoft Network as a regular filesystem
Summary(pl.UTF-8):	SMBNetFS - używanie Samby/Microsoft Network jako zwykłego systemu plików
Name:		smbnetfs
Version:	0.6.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/smbnetfs/%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/smbnetfs/
BuildRequires:	fuse-devel >= 2.5, samba-common, pkgconfig, libsmbclient-devel
Requires:	fuse, samba-client

%description
SMBNetFS is a Linux/FreeBSD filesystem that allow you to use
Samba/Microsoft Network in the same manner as the Network Neighborhood
in Microsoft Windows.

%description -l pl.UTF-8
SMBNetFS to system plików dla Linuksa/FreeBSD pozwalający używać Samby
lub sieci Microsoft Network w ten sam sposób, co Otoczenia sieciowego
w systemie Microsoft Windows.

%prep
%setup -q
touch NEWS

%build
autoconf
%configure CPPFLAGS=-I/usr/include/samba-4.0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog README TODO doc/*.FAQ
%attr(755,root,root) %{_bindir}/*

%changelog
* Tue Oct 08 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuild for Fedora
* Wed Jan 9 2008 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
$Log: smbnetfs.spec,v $
Revision 1.5  2008-01-09 15:46:36  wolvverine
- rel.1
Revision 1.4  2007-09-02 15:10:54  qboosh
- pl, more BRs
Revision 1.3  2007/09/01 09:16:34  sls
- install documentation properly
Revision 1.2  2007/08/31 22:01:03  sls
- include dir _docdir/name
- adapterized
Revision 1.1  2007/08/31 00:08:34  wolvverine
- init
