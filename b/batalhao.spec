%undefine _debugsource_packages
Name:			batalhao
Version:		17
Release:		1
Summary:		Pilot a tank to petect the city
Summary(zh_TW): 指揮坦克的守城遊戲
Group:			Amusements/Games
License:		GPL
URL:			https://freshmeat.net/projects/batalho/
Source0:		%{name}19.tar.gz
Source1:		%{name}.png

%description
Batalhão is a game in which you have to pilot a tank to protect the city Antenna
 (like the NES game Battle City). You use the arrow keys to move around and the 
space bar to shoot.

%description -l zh_TW
Batalhão 是一款玩家必須率領坦克守護 Antenna 城的遊戲（類似 NES 的 Battle City 遊戲）
玩家使用方向鍵移動以及空白鍵發射砲彈。

%prep
%setup -q -n %{name}19

%build
%__make %{?_smp_mflags}

%install
%__rm -rf $RPM_BUILD_ROOT

# bin
%__install -d $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/bash
cd %{_datadir}/%{name}
./%{name} --sync 1>/dev/null
EOF
%__chmod 755 $RPM_BUILD_ROOT%{_bindir}/%{name}
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
%__install -m 755 %{name} -D $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name} 

# data
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/gfx
%__cp -aR gfx/*.bmp $RPM_BUILD_ROOT%{_datadir}/%{name}/gfx
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/mapas
%__cp -aR mapas/*.mapa $RPM_BUILD_ROOT%{_datadir}/%{name}/mapas

# icon
%__install -m 644 %{SOURCE1} -D $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

# .desktop
%__install -d $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Batalhao
Comment=Pilot a tank to petect the city
Comment[zh_TW]=指揮坦克的守城遊戲
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/gfx
%dir %{_datadir}/%{name}/mapas
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}
%{_datadir}/%{name}/gfx/*.bmp
%{_datadir}/%{name}/mapas/*.mapa
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 17
- Rebuilt for Fedora
* Thu Aug 26 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 17-2
- fix %%dist within .spec file
* Wed Aug 18 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 17-1
- Build rpm for this package
