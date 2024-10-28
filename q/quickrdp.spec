%undefine _debugsource_packages
Name: quickrdp
Summary: Manages RDP, SSH, Telnet and VNC connections
Version: 2.4.3
Release: 5.1
License: GPLv3
Group: x11
URL: https://github.com/arnestig/quickrdp
Source0: https://github.com/arnestig/quickrdp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libcurl-devel
BuildRequires: wxGTK-devel

%description
quickrdp is a connection manager program for your remote desktop, Telnet,
SSH and VNC connections. Makes it easy to keep track of all your connections.
Some key features of quickrdp: custom commands against connections,
connection status indication, "connect when ready" - connects to the target
when a connection can be established, network scanner which can convert
scanned hosts to connections, netmask calculator and more.

Used with your own favorite RDP, SSH, telnet or VNC application, tailor the
arguments passed to the program of your choice to gain the most of quickrdp.

%prep
%setup -q
sed -i -e 's|-Wall|-Wall -fPIC|' -e 19,21d -e 's|-o root -g root||' Makefile
sed -i '39,58s|ConnectionType::ConnectionType|ConnectionType|' src/RDPDatabase.h

%build
make clean
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README COPYING AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Tue Mar 07 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.3
- Rebuilt for Fedora
