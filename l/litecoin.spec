Summary:	A peer-to-peer currency
Name:		litecoin
Version:	0.16.3
Release:	1
License:	MIT/X11
Group:		Databases
Source0:	https://github.com/litecoin-project/litecoin/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL:		http://www.litecoin.org
BuildRequires:	boost-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	libdb-cxx-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	openssl-devel
BuildRequires:	qrencode-devel
BuildRequires:	libevent-devel
BuildRequires:	protobuf-devel

%description
Litecoin is a peer-to-peer currency. Peer-to-peer means that no central
authority issues new money or tracks transactions. These tasks are
managed collectively by the network.

%package qt
Summary:	Qt-based Litecoin Wallet
Group:		Graphical desktop/KDE

%description qt
Qt-based Litecoin Wallet.

%prep
%setup -q
sed -i '33i #include <deque>' src/httpserver.cpp
sed -i 's| _\([1-6]\)| boost::placeholders::_\1|g' \
  src/validation.cpp src/validationinterface.cpp src/qt/clientmodel.cpp src/qt/bitcoingui.cpp src/qt/splashscreen.cpp src/qt/transactiontablemodel.cpp src/qt/walletmodel.cpp
sed -i '10i #include <QPainterPath>' src/qt/trafficgraphwidget.h

%build
./autogen.sh
%configure --with-incompatible-bdb
make

%install
%make_install
install -d %{buildroot}{%{_bindir},%{_mandir}/man{1,5},%{_localedir},%{_datadir}/applications,%{_datadir}/pixmaps,%{_datadir}/kde4/services}
#install -m755 src/litecoind %{buildroot}%{_bindir}/litecoind
#install litecoin-qt %{buildroot}%{_bindir}
sed -e 's#bitcoin#litecoin#g' -e 's#Bitcoin#Litecoin#g' contrib/debian/bitcoin-qt.desktop > %{buildroot}%{_datadir}/applications/litecoin-qt.desktop
sed -i 's|/usr/share/pixmaps/%{name}128.png|%{name}128|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-qt.desktop
sed -e 's#bitcoin#litecoin#g' -e 's#Bitcoin#Litecoin#g' contrib/debian/bitcoin-qt.protocol > %{buildroot}%{_datadir}/kde4/services/litecoin-qt.protocol
install -Dm644 share/pixmaps/bitcoin128.png %{buildroot}%{_datadir}/pixmaps/litecoin128.png

%files
%doc doc/*.txt contrib/debian/examples/bitcoin.conf
%{_bindir}/litecoind
%{_bindir}/bench_litecoin
%{_bindir}/litecoin-cli
%{_bindir}/litecoin-tx
%{_bindir}/test_litecoin
%{_includedir}/bitcoinconsensus.h
%{_libdir}/libbitcoinconsensus.*
%{_libdir}/pkgconfig/libbitcoinconsensus.pc
%{_mandir}/man1/litecoind.1.*
%{_mandir}/man1/litecoin-cli.1.*
%{_mandir}/man1/litecoin-tx.1.*

%files qt
%{_bindir}/litecoin-qt
%{_bindir}/test_litecoin-qt
%{_datadir}/kde4/services/litecoin-qt.protocol
%{_datadir}/applications/litecoin-qt.desktop
%{_datadir}/pixmaps/litecoin128.png
%{_mandir}/man1/litecoin-qt.1.*

%changelog
* Fri Dec 28 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.16.3
- Rebuilt for Fedora
* Fri Feb 07 2014 Alexander Khryukin <alexander@mezon.ru> 0.8.3.7-1
+ Revision: 05ae4a4
- init
