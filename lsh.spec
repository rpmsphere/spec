Summary:        Secure connections with secsh2 protocol
Name:           lsh
Version:        2.1
Release:        1
License:        GPL
Group:          Application/Internet
Source0:        ftp://ftp.lysator.liu.se/pub/security/lsh/%{name}-%{version}.tar.gz 
URL:            http://www.lysator.liu.se/~nisse/lsh/
BuildRequires:  gmp-devel
BuildRequires:  liboop-devel
BuildRequires:  nettle-devel

%description 
lsh is a GPLed implementation of the Secure SHell protocol version 2 (SSH2),
a secure replacement for rlogin, rsh, and rcp. This package contains the lsh
client used to log in to a remote lsh or SSH2 server.

%prep
%setup -q
sed -i -e '/#define __argp_fmtstream/d' -e '/#define __argp_usage/d' -e '/#define __option_is/d' src/argp/argp-namefrob.h

%build
./configure --prefix=/usr
make

%install
make prefix=$RPM_BUILD_ROOT%{prefix} install
install -d -m 0755 $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 0755 contrib/lshd.rhlinux.init \
        $RPM_BUILD_ROOT/etc/rc.d/init.d/lshd

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -e /etc/lsh_host_key -o ! -e /etc/lsh_host_key.pub ]
then
        rm -f /etc/lsh_host_key*
        /usr/bin/lsh-keygen -l 8 | /usr/bin/lsh-writekey -o /etc/lsh_host_key
fi

%files 
%doc AUTHORS COPYING ChangeLog FAQ NEWS README doc/*
%config /etc/rc.d/init.d/lshd
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/lsh*
%{_sbindir}/*

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuild for Fedora
* Wed Jun 28 2000 Thayne Harbaugh <thayne@plug.org>
- ripped out man install - make install now does it
- there is now an lsh.info that is handled
- various simplifications
- spelling error
* Thu Jan 06 2000 Thayne Harbaugh <thayne@northsky.com>
- lshd.rhlinux.init is now in contrib dir - removed Source1
- fixed preun $1 comparision - was [ "$1" -eq 1 ]
* Thu Sep 28 1999 Thayne Harbaugh <thayne@northsky.com>
- first rpm
