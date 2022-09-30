%global __os_install_post %{nil}

Summary:   Manipulating and mirroring directories
Name:      mirrordir
Version:   0.10.49
Release:   16.1
License: GPL
Group:     Applications/System          
Source0:  %name-%{version}.tar.bz2
URL: http://pkgs.repoforge.org/mirrordir/
Patch0: mirrordir-0.10.49-datadir-fix.patch
Patch1: mirrordir-0.10.49-zlib-1.1.3-zfree.patch
Source1: tcpd.h

%description
mirrordir  is  a set of useful utilities for manipulating and mirroring directories. Included is also the
command pslogin - an alternative to ssh(1), and forward(1) for forwarding arbitrary  TCP  socket  connec-
tions over encrypted secure channels.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i 's|mirrordir $(bindir)|mirrordir $(DESTDIR)$(bindir)|' src/Makefile.*
cp %{SOURCE1} vfs/
sed -i 's|stderr,m|stderr, "%s", m|' vfs/secure-mcserv.c

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%if %{fedora}>22
cp /usr/share/libtool/build-aux/config.* .
%else
cp /usr/share/libtool/config/config.* .
%endif
./configure --prefix=/usr --libdir=%{_libdir} --mandir=/usr/share/man
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
/usr/bin/forward
/usr/bin/copydir
/usr/bin/mirrordir
/usr/bin/pslogin
/usr/bin/recursdir
/usr/bin/secure-mcserv
/usr/share/man/man1/*
%config /etc/secure-mcservusers
%dir /etc/pam.d/
%config /etc/pam.d/secure-mcserv
%{_libdir}/lib*
%{_datadir}/%{name}

%changelog
* Fri Jan 03 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10.49
- Rebuilt for Fedora
* Mon Jan 09 2012 cyberbeat
- Rebuilt for Fedora
