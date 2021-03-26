Name: qchat
Version: 0.3
Release: 12.1
Summary: Simple crossplatform LAN chat
License: GPLv2+
Group: Networking/Chat
URL: http://sourceforge.net/projects/q-chat/
Source0: http://sourceforge.net/projects/q-chat/files/QChat/%name-%version/%name-%version.tar.bz2
Source1: %name.desktop
BuildRequires: qt4-devel

%description
QChat is a simple crossplatform LAN chat.
It is written using Qt4 so you can compile
it on any platform supported by Qt >= 4.3.

%prep
%setup -q

%build
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags"
make

%install
%__install -d %buildroot%_bindir
%__install -Dp -m 0644 %SOURCE1 %buildroot%_datadir/applications/%name.desktop
%__install -Dp -m 0644 src/icons/tray-icon.png %buildroot%_datadir/pixmaps/%name.png
%make_install INSTALL_ROOT=%buildroot install

%files
%doc README COPYING
%_bindir/%{name}*
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png
%_datadir/%name

%changelog
* Sun Jun 02 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Sun Oct 14 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2.2-alt1
- new version
* Sun Sep 16 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2.1-alt0.M40.1
- initial build for ALT Linux (M40)
