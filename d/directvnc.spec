Summary:	VNC Client Running on Linux Frame Buffer
Name:		directvnc
Version:	0.7.8
Release:	11.1
License:	GPL
Group:		Networking/Remote access
URL:		https://www.adam-lilienthal.de/directvnc/
Source:		https://cloud.github.com/downloads/drinkmilk/directvnc/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	gcc-c++
BuildRequires:	directfb-devel
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
BuildRequires:	xorg-x11-proto-devel

%description
DirectVNC is a client implementing the remote framebuffer protocol (rfb)
which is used by VNC servers.  DirectVNC is special; it uses the linux
framebuffer device through the DirectFB library which enables it to run
on anything that has a framebuffer without the need for a running X server.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
autoreconf -ifv
#libtoolize --force
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS changelog COPYING NEWS README THANKS
%{_bindir}/*
%{_mandir}/man?/*

%changelog
* Thu Aug 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.8
- Rebuilt for Fedora
* Tue Nov 25 2003 Abel Cheung <deaddog@deaddog.org> 0.7.5-1mdk
- First Mandrake package
