Name:            echovnc
Summary:         A secure, "firewall-friendly" remote-desktop tool
Version:         1.1.2
Release:         16.1
License:         GPL
Group:           Productivity/Networking/Remote Desktop
Source:          %{name}-%{version}.tar.bz2
Patch:           echovnc-1.1.2-gcc.patch
BuildRequires:   libpng-devel
BuildRequires:   gcc-c++, libsigc++20-devel
BuildRequires:   gtkmm24-devel >= 2.8.0
BuildRequires:   openssl-devel >= 0.9.6

%description
EchoVNC is a secure, "firewall-friendly" remote-desktop tool with
support for VNC, Remote Desktop, and RAdmin servers and viewers.
With it, a Windows PC or OSX Mac can be remotely accessed regardless
of firewall, router or web-proxy configuration.

EchoVNC uses echoWare toolkit to establish its connections. With
echoWare, client-server and peer-to-peer Internet application can
easily and securely connect with each other regardless of any
intervening firewalls, routers, or web-proxies. EchoWare-enabled
clients interconnect with each other via a server application
called echoServer.

%prep
%setup -q
%patch -p1
sed -i '1i #include <unistd.h>' echoware/Globals.h echoware/ProxyConnect.cpp src/ConnectionItem.cpp

%build
aclocal
automake --add-missing
autoconf
CFLAGS="$RPM_OPT_FLAGS -Wno-narrowing" \
CXXFLAGS="$RPM_OPT_FLAGS -std=c++11 -Wno-narrowing" \
%configure \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir}

%{__make} %{?jobs:-j%jobs}

%install
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYRIGHT LICENSE NEWS README TODO VERSION.txt
%{_bindir}/%{name}

%changelog
* Thu Mar 10 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.2
- Rebuilt for Fedora
* Tue Feb 03 2009 -  <chris@computersalat.de> - 1.1.2
- initial build
