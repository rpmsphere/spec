Name:			cnchess
Group:			Applications/Games
Version:		0.3
Release:		1
License:		GPL
Summary:		A Chinese Chess Game.
Summary(zh_CN):		中国象棋游戏
Summary(zh_TW):		中國象棋遊戲
URL:			http://netbay.blogchina.com/
Source0:		%{name}-%{version}.src.tar.bz2
Source1:		cnchess.sh
Source2:		%{name}.xpm
Patch0:			%{name}-bookfile.patch
BuildRequires:		qt3-devel

%description
A Chinese Chess game, Only fight to computer.

%description -l zh_CN
一个中国象棋游戏，仅能人机对战，棋力较弱。

%description -l zh_TW
一套中國象棋遊戲，僅能人機對戰，棋力較弱。

%prep
%setup -q -n %{name}
%patch0 -p1
sed -i -e 's|/usr/lib/qt|%{_libdir}/qt|g' -e 's|-march=i386 -mcpu=i686||' Makefile */Makefile
sed -i '1i #include <unistd.h>' src/cnchessview.cpp

%build
make

%install
rm -rf %{buildroot}
install -Dm 755 bin/cnchess %{buildroot}%{_datadir}/cnchess/bin/cnchess
install -Dm 644 book/OPENNINGBOOK.DAT %{buildroot}%{_datadir}/cnchess/book/OPENNINGBOOK.DAT
cp -a chesses %{buildroot}%{_datadir}/cnchess
install -Dm 755 %{SOURCE1} %{buildroot}%{_bindir}/cnchess
install -Dm 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/cnchess.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/cnchess.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=CNChess
Name[zh_TW]=中國象棋
Name[zh_CN]=中国象棋
Comment=A Chinese Chess Game.
Comment[zh_CN]=一个中国象棋游戏，仅能人机对战。
Comment[zh_TW]=一套中國象棋遊戲，僅能人機對戰。
Exec=%{name}
Icon=%{name}.xpm
Terminal=false
Type=Application
Categories=Application;Game;
EOF

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_usr}/share/cnchess/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Sat Dec 31 2005 kde <jack@linux.net.cn> 0.3-2mgc
- fix the menu
* Wed Sep 07 2005 sejishikong <sejishikong@263.net> 0.3-1mgc
- initial RPM
