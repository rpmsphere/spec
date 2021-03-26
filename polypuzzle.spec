Summary:	A game based on a tesselation puzzle named Beat the Computer
Name:		polypuzzle
Version:	1.8.2
Release:	1
License:	LGPLv2+
Group:		Amusements/Games
URL:		http://tkgames.sourceforge.net
Source0:	http://dl.sourceforge.net/sourceforge/tkgames/%{name}-%{version}.tgz
BuildArch:	noarch
Requires:	tk

%description
Based on a tesselation puzzle named Beat the Computer.
Just visit http://tkgames.sourceforge.net to get more info.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
%__mkdir_p %{buildroot}%{_libdir}/%{name}
%__cp * %{buildroot}%{_libdir}/%{name}
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_libdir}/%{name}
./%{name}
cd -
EOF

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=PolyPuzzle
Comment=
Exec=polypuzzle
Terminal=false
StartupNotify=true
Categories=Applications;Game
Icon=%{name}.png
Name[zh_TW]=多連形智慧盤
Comment[zh_TW]=PolyPuzzle 將數個面積相同而形狀各異的棋子，排列組合到固定形狀的盤子內
EOF

%__mkdir_p %{buildroot}%{_datadir}/pixmaps
convert %{buildroot}%{_libdir}/%{name}/polylogo.gif %{buildroot}%{_datadir}/pixmaps/%{name}.png

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%attr(0755,root,root) %{_bindir}/polypuzzle
%{_libdir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.2
- Rebuild for Fedora
* Thu Sep 11 2008 Wind Win <yc.yan@ossii.com.tw> 1.8.1-2
- Initial RPM build.
