Name: llk_linux
Version: 2.3
Release: 1
License: GPL
Summary: LinLink for Linux
Summary(zh_CN): Linux下的连连看
Summary(zh_TW): Linux下的連連看
URL: https://llk-linux.sourceforge.net
Group: Amusements/Games
Source0: %{name}-%{version}beta1.tar.gz
Source1: %{name}.desktop
Source2: %{name}-%{version}.zh_TW.po
BuildRequires: gettext
BuildRequires: esound-devel, gtk2-devel
Requires: glib2, gtk2
Vendor: Alpher <alpher_zmx@yahoo.com.cn>

%description
LinLink for Linux. It is an arcade game.

%description -l zh_CN
Linux 下的连连看。它是一个街机游戏。

%description -l zh_TW
Linux 下的連連看，它是一個街機遊戲。

%prep
%setup -q
cp %{SOURCE2} po/zh_TW.po
sed -i 's/zh_CN/zh_CN zh_TW/' configure

%Build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure --prefix=/usr
sed -i 's|-Werror=format-security|-Wno-error -lX11|' src/Makefile
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/usr/share/applications/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
/usr/doc/%{name}
/usr/include/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3
- Rebuilt for Fedora
* Tue Feb 9 2006 KanKer <kanker@163.com>
- update 2.3beta1
* Sun Dec 11 2005 KanKer <kanker@163.com>
- first spec
