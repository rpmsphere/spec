Name:           nast
Version:        0.2.0
Release:        1408.1
License:        GPL-2.0
Summary:        Packet sniffer and a LAN analyzer based on Libnet and Libpcap
URL:            https://nast.berlios.de/
Group:          Productivity/Networking/Diagnostic
Source:         %{name}-%{version}.tar.bz2
Patch0:         nast-%{version}-config.patch
BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel
BuildRequires:  ncurses-devel

%description
Nast is a packet sniffer and a LAN analyzer based on Libnet and Libpcap.

It can sniff in normal mode or in promiscuos mode the packets on a network interface and log it.  It dumps the headers of packets and
the payload in ascii or ascii-hex format.  You can apply a filter. The sniffed data can be saved in a separated file.

As analyzer tool, it has many features like:
* Build LAN hosts list
* Follow a TCP-DATA stream
* Find LAN internet gateways
* Discorver promiscous nodes
* Reset an established connection
* Perform a single half-open portscanner
* Perform a multi half-open portscanner
* Find link type (hub or switch)
* Catch daemon banner of LAN nodes
* Control arp answers to discover possible arp-spoofings
* Byte couting with an optional filter
* Write reports logging

It also provides a new ncurses interface.

%prep
%setup -q
%patch 0

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-format-security"
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make

%install
%{__make} install DESTDIR=%{?buildroot}

%files
%doc README NCURSES_README BUGS TODO CREDITS AUTHORS VERSION
%doc %{_mandir}/man8/*
%{_bindir}/nast*

%changelog
* Sun May 05 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
* Thu Jan 26 2012 mseben@gmail.com
- modify spec file to fix SLE_10 build
* Sun Jan 16 2011 mseben@gmail.com
- enable ncurses build (added nast-0.2.0-include.patch and modified nast-0.2.0-config.patch)
- use optflags for build
* Thu Jan  6 2011 mseben@gmail.com
- fix build :use BuildRequires: libnet-devel for %%suse_version > 1130
- apply gitorious.org/opensuse/spec-cleaner on .spec file
* Tue Nov  4 2008 mseben@suse.cz
- Initial package
