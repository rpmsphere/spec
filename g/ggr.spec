%undefine _debugsource_packages
%global __os_install_post %{nil}

Name:           ggr
Version:        0.47
Release:        1
Summary:        A remake of a classic Ghouls and ghosts
Group:          Amusements/Games
License:        GPL
URL:            https://www.valarsoft.com/ramuso/?dpage=pagine&page=pagine&pagID=8#GhoulsAndGhostsRemix
Source0:        https://www.valarsoft.com/ramuso/down/%{name}_047.zip
BuildRequires:  gcc, allegro-devel, mesa-libGL-devel

%description
With some addiction taked from Ghouls and ghosts, Ghosts and goblins and Super
ghouls and ghosts. The code of this game its developed under GNU/GPL. You can
discuss about Ghouls and ghosts remix in this forum, english and italian are allowed.

%prep
%setup -q -c %{name}

%build
chmod +x ccl
./ccl

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m0644 -p icon.ico $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

#Desktop
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Name[zh_TW]=惡魔城
Comment=A remake of a classic Ghouls and ghosts with some addiction taked from Ghouls and ghosts, Ghosts and goblins and Super ghouls and ghosts. 
Comment[zh_TW]=一套由大型電玩 Ghouls and ghosts 重製的橫向捲軸遊戲
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Game;Action;
EOF

#Exec
cat > %{buildroot}%{_bindir}/%{name} <<EOF
cd %{_datadir}/%{name}
./game.exe
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.47
- Rebuilt for Fedora
* Fri Sep 12 2008 Feather Mountain <john@ossii.com.tw> 1.5-1
- Build for OSSII
