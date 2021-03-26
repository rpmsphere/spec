Name:           gmchess
Version:        0.29.6
Release:        1
Summary:	one chinese chess game
Group:          Amusements/Games
License:        LGPL
URL:            http://code.google.com/p/gmchess/
Source0:        http://gmchess.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1:	gmchess-0.29.3.zh_TW.po
BuildRequires:	intltool, gettext
BuildRequires:  gtkmm24-devel
BuildRequires:	libglademm24-devel

%description
The current release can load chess collection of records now. The supports of records can be created by  QQ象棋, 联众象棋, 中游象棋 and 象棋演播室.
  How-To: Menu->File->Open ( Then choice the record you waana review. Or drag and drop the record file into the GMChess. )

This project is base on gtkmm library and 象棋巫師 open source code. Especially to appreciate 象棋巫師's author 黃晨, becouse of the unlimit idea from programming process ideas and webs solutions. And thanks the other author Wind, though he was disvisibled busy for another project.

%description -l zh_CN
目前有读谱功能，支持qq象棋，联众象棋，中游象棋，象棋演播室等软件生成的棋谱。
使用方法：选菜单->文件->打开，选择相应的棋谱文件即可
或者直接将棋谱拖到棋盘上即可打开。

本软件基于gtkmm库，以及开源程序象棋巫师的源码。因此非常感谢象棋巫师的作者黄晨先生，他的程序及网站给我提供了无限的资源及灵感。同时也感谢本软件另一作者wind，虽然他现在忙于工作而隐身中。

%prep
%setup -q
cp %{SOURCE1} po/zh_TW.po
echo "zh_TW" >> po/LINGUAS
sed -i '234s/"1"/"0"/' src/MainWindow.cc

%build
export CXXFLAGS="-fPIC -fpermissive"
%configure
make 

%install
rm -rf %{buildroot}
DESTDIR=$RPM_BUILD_ROOT make install 
install -Dm0644 ./data/gmchess.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

#Desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=GMChess
Name[zh_TW]=天書棋談
Name[zh_CN]=天书棋谈
Comment=Chinese Chess, made by Lerosua
Comment[zh_TW]=中國象棋遊戲
Comment[zh_CN]=中国象棋游戏
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Game;BoardGame;
EOF

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/locale/*/LC_MESSAGES/gmchess.mo
%{_libdir}/lib*
%{_datadir}/man/man6/*.6.gz

%changelog
* Wed Sep 04 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.29.6
- Rebuild for Fedora
* Thu Jun 11 2009 Kami <kami@ossii.com.tw> 0.20-1.ossii
- Rebuild practice
* Wed Apr 29 2009 Feather Mountain <john@ossii.com.tw> 0.20-1.ossii
- Update to 0.20
- Support fight to AI
* Fri Mar 27 2009 Feather Mountain <john@ossii.com.tw> 0.10-1.ossii
- Build for OSSII
- Add zh_TW.po
