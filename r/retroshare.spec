%undefine _debugsource_packages

Name:           retroshare
Version:        0.6.6git
Release:        1
License:        LGPL
Summary:        Secure chat and file sharing
Group:          Productivity/Networking/Other
URL:	        http:/retroshare.sourceforge.net/
#Source0:        http://sourceforge.net/projects/retroshare/files/RetroShare/%{version}/RetroShare-%{version}.tar.gz
Source0:	RetroShare-master.zip
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libupnp-devel libgpg-error libgnome-keyring-devel glib2-devel
BuildRequires:  gpgme-devel libXScrnSaver-devel
BuildRequires:  openssl-devel
BuildRequires:  speex-devel sqlite-devel libmicrohttpd-devel
BuildRequires:  sqlcipher-devel

%description
RetroShare is a cross-platform private p2p sharing program.
It lets you share securely your friends, using a web-of-trust
to authenticate peers and OpenSSL to encrypt all communication.
RetroShare provides filesharing, chat, messages and channels.

%prep
%setup -q -n RetroShare-master
#sed -i 's|CONFIG \*= rs_macos10.11|CONFIG *= unix|' retroshare.pri
#touch libretroshare/src/ThreadPool.h
sed -i 's|TurtleVirtualPeerId,RsGRouterTransactionChunkItem\*|TurtleVirtualPeerId|' libretroshare/src/grouter/p3grouter.cc
sed -i '23i #include <QTabBar>' retroshare-gui/src/gui/chat/ChatTabWidget.cpp
sed -i '27i #include <QStyle>' retroshare-gui/src/gui/feeds/GxsForumMsgItem.cpp retroshare-gui/src/gui/feeds/GxsChannelPostItem.cpp
sed -i '26i #include <QStyle>' retroshare-gui/src/gui/Posted/PostedItem.cpp

%build
#qmake-qt5 -recursive CONFIG=release CONFIG+=no_sqlcipher CONFIG+=no_retroshare_plugins
qmake-qt5
make

%install
mkdir -p $RPM_BUILD_ROOT
make install INSTALL_ROOT=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/retroshare

%changelog
* Sun Jul 4 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.6git
- Rebuilt for Fedora
* Wed Feb  8 2012 asamk@gmx.de
- Updated to version 0.5.3a
* Thu Aug 18 2011 asamk@gmx.de
- fix fedora requires
* Tue Aug 16 2011 asamk@gmx.de
- added conflicts
* Thu Aug 11 2011 asamk@gmx.de
- Updated to version 0.5.2a:
  * Bugfixes
  * Stable Connections.
  We've found most of the causes of disconnections and patched them up.
  Retroshare will now maintain most peer connections indefinitely!
  * Firewall-Busting Connections
  New UDP connections enable Retroshare to communicate through most Firewalls.
  This makes Retroshare plug and play, with no need to fiddle with router settings!
  (Obviously it is always better to forward a port, but it is no longer essential!)
