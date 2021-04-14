Summary:         Solaris Porting Layer
Group:           Utilities/System
Name:            spl
Version:         0.7.10
Release:         3.1
License:         GPL
URL:             http://zfsonlinux.org/
Source:          http://archive.zfsonlinux.org/downloads/zfsonlinux/spl/%{name}-%{version}.tar.gz

%description
The Solaris Porting Layer (SPL) is a Linux kernel module which provides
many of the Solaris kernel APIs.  This shim layer makes it possible to
run Solaris kernel code in the Linux kernel with relatively minimal
modification.  This can be particularly useful when you want to track
upstream Solaris development closely and do not want the overhead of
maintaining a large patch which converts Solaris primitives to Linux
primitives.

%prep
%setup -q

%build
%configure --with-config=user
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING DISCLAIMER
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man?/*

%changelog
* Tue Sep 11 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.10
- Rebuilt for Fedora
