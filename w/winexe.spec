Summary:    Remote Windows®-command executor
Name:       winexe
Version:    1.00
Release:    4
License:    GPL3
Group:      Networking/Other
Source:     %{name}-%{version}.tar.gz
URL:        https://sourceforge.net/projects/winexe/
Patch0:     heimdal-make-proto.patch
Patch1:     pidl.patch
Patch2:     gnutls.patch
BuildRequires: automake
BuildRequires: patch
BuildRequires: python2-devel
BuildRequires: util-linux
BuildRequires: which
Requires:      samba-client

%description
Winexe remotely executes commands on Windows NT/2000/XP/2003 systems
from GNU/Linux (and possibly also from other Unices capable of building
the Samba 4 software package).

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
sed -i 's|defined(@$podl)|@$podl|' pidl/lib/Parse/Pidl/ODL.pm
sed -i 's|defined @$pidl|@$pidl|' pidl/pidl
sed -i '/gnutls_certificate_type_set_priority/d' source4/lib/tls/tls.c

%build
export PYTHON=/usr/bin/python2
export LDFLAGS=-Wl,--allow-multiple-definition
cd source4
./autogen.sh
%configure --enable-fhs
make "CPP=gcc -E -ffreestanding" basics idl bin/winexe

%install
install -Dm755 source4/bin/winexe %{buildroot}%_bindir/winexe

%files
%_bindir/winexe

%changelog
* Mon Jul 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.00
- Rebuilt for Fedora
* Fri Feb 12 2016 umeabot <umeabot> 1.00-4.mga6
+ Revision: 959178
- Mageia 6 Mass Rebuild
* Sun Sep 13 2015 neoclust <neoclust> 1.00-3.mga6
+ Revision: 878885
- Fix samba require
* Wed Sep 09 2015 neoclust <neoclust> 1.00-2.1.mga6
+ Revision: 874804
- Fix build against new gcc
- imported package winexe
