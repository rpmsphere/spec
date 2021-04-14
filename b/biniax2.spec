%undefine _debugsource_packages

Name:           biniax2
Version:        1.2
Release:        1
Summary:        Original and entertaining game
Group:          Amusements/Games
License:        GPLv2+
URL:            http://mordred.dir.bg/biniax
Source0:        http://mordred.dir.bg/biniax/biniax2-fullsrc.tar.gz
Patch0:		exec_setting.patch

%description
Biniax is original and entertaining game.
Takes a minute to learn and gives you hours of gameplay.

%prep
%setup -q -c
%patch0 -p0
convert icon.ico biniax2.png

%build
make

%install
rm -rf $RPM_BUILD_ROOT
cat > %{name}.desktop << EOF
[Desktop Entry]
Type=Application
Version=1.0
Encoding=UTF-8
Name=%{name}
Name[zh_TW]=方塊遊戲
Comment=a PSP square game that developed by the programmer JORDAN TUZSUZOV
Comment[zh_TW]=JORDAN TUZSUZOV 原創的方塊遊戲
Icon=%{name}
Exec=%{name}
Terminal=false
StartupNotify=false
Categories=Application;Game;ArcadeGame;
EOF

install -Dm 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm 755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
* Thu Dec  4 2008 milochen <milo_chen@mail2000.com.tw> - 1.2-1.ossii
- initial ossii package
