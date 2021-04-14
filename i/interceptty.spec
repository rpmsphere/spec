Name:         interceptty
Summary:      TTY Interceptor and Network Serial Port Client/Server Daemon
URL:          http://www.suspectclass.com/sgifford/interceptty
Group:        Network
License:      GPL
Version:      0.6
Release:      4.1
Source0:      http://www.suspectclass.com/interceptty/files/interceptty-%{version}.tar.gz
Patch:       interceptty.patch

%description
IntercepTTY is a program that can sit between a real (or fake)
serial port and an application, recording any communications
between the application and the device. It can also be used as a
network serial server or client, to provide an emulated serial port
connected to a program, and for various other tasks.

%prep
%setup -q
%patch -p0

%build
./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir}
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_bindir}/*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
