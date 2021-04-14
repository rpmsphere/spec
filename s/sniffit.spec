Summary: Program for demonstrating the unsafeness of TCP
Summary(es):	A network protocol analyzer
Summary(pl):	Program do nasłuchu połączeń TCP/UDP/ICMP
Summary(pt_BR):	Um analisador de protocolos de rede
Name: sniffit
Version: 0.5
Release: 1
License: distributable
Group: Monitoring
Source: %name-%name-%version.tar.gz
URL: https://github.com/resurrecting-open-source-projects/sniffit
BuildRequires: ncurses-devel libpcap-devel

%description
Sniffit is a packet sniffer for TCP/UDP/ICMP packets. Sniffit is able
to give you very detailed technical info on these packets (SEQ, ACK,
TTL, Window, ...) but also packet contence in different formats (hex
or plain text, ...).

%description -l es
Sniffit is a robust non-commercial network protocol analyzer or packet
sniffer. A packet sniffer basically listens to network traffic and
produces analysis based on the traffic and/or translates packets into
some level of human readable form.

%description -l pl
Sniffit jest programem do podsłuchu pakietów TCP/UDP/ICMP. Sniffit
jest w stanie podać Ci bardzo wiele informacji o tych pakietach (SEQ,
ACK, TTL, Okno, ...) a także ich zawartość w różnych formatach
(szesnastkowo lub w czystej postaci, ...).

%description -l pt_BR
Sniffit é um analisador de redes. Ele monitora o tráfego de rede e
produz uma análise compreensível por humanos.

%prep
%setup -q -n %name-%name-%version

%build
./autogen.sh
%configure --no-recursion
%make_build OBJ_OPT="" EXE_OPT="-lpcap"

%install
%make_install

%files
%doc *.md AUTHORS CHANGELOG CREDITS LICENSE docs/*
%_mandir/man?/*
%_sbindir/*

%changelog
* Mon Apr 27 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Mon Mar 26 2012 Fr. Br. George <george@altlinux.ru> 0.3.7-alt4
- Drop all old patches in favour of Debian one
* Tue Feb 16 2010 Fr. Br. George <george@altlinux.ru> 0.3.7-alt3
- Fix *64 build
* Sat Sep 27 2008 Fr. Br. George <george@altlinux.ru> 0.3.7-alt2
- Fix build
* Fri Jul 08 2005 Fr. Br. George <george@altlinux.ru> 0.3.7-alt1
- Adapted TLD Port
