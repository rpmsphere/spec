Name:			digger
Version:		20020314
Release:		1
Summary:		The Unix version of the old classic game Digger
Summary(zh_TW):	經典遊戲 Digger 的 Unix 版本
Group:			Amusements/Games
License:		GPL
URL:			http://www.digger.org/
Source0:		%{name}-%{version}.tar.gz
Source11:		%{name}-16x16.png
Source12:		%{name}-32x32.png
Source13:		%{name}-48x48.png
Patch0:			%{name}-optflags.patch
Patch1:			%{name}-fix_gcc_3.patch
Patch2:			%{name}-%{version}-update-%{name}.txt-with-legal-info.patch
BuildRequires:	SDL-devel, zlib-devel

%description
This is the Unix version of the old classic game Digger.
It has many new features including:
* Exit button
* Optional VGA graphics
* Recording and playback
* Real time speed control
* Keyboard redefinition
* Gauntlet mode
* Two player simultaneous mode

%description -l zh_TW
這是經典遊戲 Digger 的 Unix 版本
它具有許多新特色，包括：
* 離開按鈕
* 選擇性的 VGA 圖形
* 記錄和播放
* 即時速度控制
* 鍵盤重新定義
* 鎧甲模式
* 雙人模式

%prep
%setup -q
%patch0 -p0 -b .optflag
%patch1 -p0 -b .gcc3
%patch2 -p1 -b .legal

%build
make -f Makefile.sdl OPTFLAGS="$RPM_OPT_FLAGS"

%install
# bin
rm -rf $RPM_BUILD_ROOT
install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}

# .desktop
install -d $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Digger Remastered
Comment=The Unix version of the old classic game Digger
Comment[zh_TW]=經典遊戲 Digger 的 Unix 版本
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

# .png
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}-32x32.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}-48x48.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}-32x32.png
%{_datadir}/pixmaps/%{name}-48x48.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20020314
- Rebuild for Fedora
* Thu Aug 26 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 20020314-4
- add %%description of zh_TW
- fix Exec within .desktop file
* Wed Aug 18 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 20020314-3
- Fix comment
* Tue Aug 12 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 20020314-2
- Fix no icon in the menu 
* Tue Aug 10 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 20020314-1
- Build RPM and SRPM
