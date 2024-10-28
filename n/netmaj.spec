%undefine _debugsource_packages

Summary: Network Mahjong
Summary(ja_JP.utf8): ネットワーク対戦麻雀
Name: netmaj
Version: 2.0.7
Release: 11.1
Group: Amusements/Games
License: GPL
Source0: https://www.sfc.wide.ad.jp/~kusune/netmaj/files/%{name}-%{version}.tar.gz
Source1: https://www.sfc.wide.ad.jp/~kusune/netmaj/files/%{name}-xui-%{version}.tar.gz
Patch0: netmaj-2.0.7-turbolinux.patch
Patch1: netmaj-2.0.7-build.patch
URL: https://www.sfc.wide.ad.jp/~kusune/netmaj/
BuildRequires: libX11-devel
BuildRequires: libXpm-devel
BuildRequires: ncurses-devel
BuildRequires: imake

%description
network mahjong game.

%description -l ja_JP.utf8
ひとり遊びやネットワーク対戦が可能な麻雀です。
X 上やコンソール上で動作します。

%prep
%setup -q -n %{name} -a1
%patch 0 -p1 -b .turbolinux
%patch 1 -p1 -b .build

%build
#make libs
cd xui
xmkmf
cd ..
sed -i 's|-Llib|-Llib -Wl,--allow-multiple-definition|' Makefile
make

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/%{name}
make install PREFIX=${RPM_BUILD_ROOT}
make install-pf PREFIX=${RPM_BUILD_ROOT}
%ifarch x86_64 aarch64
mv ${RPM_BUILD_ROOT}/usr/lib ${RPM_BUILD_ROOT}/usr/lib64
%endif

%files
%doc COPYING.j DEVELOPMENT.j INPUT.j LOCALRULE.j
%doc PLAYING.j PLVIEW.j PROXY.j README.j THANKS.j TUNE.j WANTED.j
%doc html/
%{_bindir}/*
%{_libdir}/%{name}

%changelog
* Tue Jan 14 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.7
- Rebuilt for Fedora
* Wed Oct  8 2003 Noriyuki Suzuki <noriyuki@turbolinux.co.jp>
- Initial build for Turbolinux
