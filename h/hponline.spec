%undefine _debugsource_packages
%define pkg_name HotPotatoOnline

Name:		hponline
Version:        1.2.0
Release:        1
Summary:        A fast paced arena sport game
Group:          Amusements/Games
License:        LGPL
URL:            https://wiki.mozilla.org/Special:Search?search=i18n&go=Go
Source0:        https://jaist.dl.sourceforge.net/sourceforge/hponline/%{pkg_name}Sources-v%{version}.tar.gz
Patch0:		%{pkg_name}Sources-v%{version}-glfont2.h.patch
BuildRequires:	libglpng-devel
BuildRequires:	freeglut-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	mesa-libGL-devel

%description
Hot Potato Online is a fast paced arena sport game where players try to
explode the opposition using a short-fused potato bomb.
Think dodgeball with a grenade!

%prep
%setup -q -n %{pkg_name}Sources-v%{version}
%patch0 -p0
sed -i '/errno/d' src/CServer.cpp
sed -i '1i #include <cstdlib>\n#include <cstring>\n#include <cstdio>' src/CConfigFile.cpp src/CHTTP.cpp src/CMessageBox.cpp src/CMessenger.h
sed -i -e 's|-lGLU|-lGLU -lX11 -lpthread|' -e 's|staticlibs/libglut.a staticlibs/libglpng.a|-lglut -lglpng|' src/Makefile

%build
make clean
make

%install
rm -rf %{buildroot}
rm -fr src
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0644 -p menu_title/menu_title_logo.png  $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

#Desktop
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF

[Desktop Entry]
Name=%{pkg_name}
Name[zh_TW]=熱血馬鈴薯
Comment=A fast paced arena sport game
Comment[zh_TW]=結合炸彈超人與橄欖球的玩法
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Game;Action;
EOF

#Exec
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
cd %{_datadir}/%{name}
./HotPotato
EOF

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora
* Mon Dec 08 2008 Feather Mountain <john@ossii.com.tw> 1.2.0-1.ossii
- Build for OSSII
