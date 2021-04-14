Name: bombermaaan
Version: 1.4.0
Release: 1
Summary: A multi-player maze-style bomberman-like game
URL: http://bombermaaan.sourceforge.net/
Source: http://downloads.sourceforge.net/bombermaaan/Bombermaaan_%{version}.627_20081018_src.tar.gz
Source1: http://downloads.sourceforge.net/bombermaaan/Bombermaaan_%{version}.627_20081018_res.tar.gz
Source2: Bombermaaan-Levels.zip
Source3: http://bombermaaan.sourceforge.net/images/bomber_a.png
License: GPL
Group: Amusements/Games
BuildRequires: SDL-devel, SDL_mixer-devel

%description
A classic Bomberman game with multiplayer support, cloned on original SNES games.
Also similar to Dynablaster. Developed in C++. Runs on Win32 and Linux.

%prep
%setup -q -n Bombermaaan_%{version}.627_20081018_src -a 1 -a 2
cp -a Bombermaaan_%{version}.627_20081018_res/* .
sed -i 's/\$(INSTALL)/install -m755/' Bombermaaan/Makefile
sed -i 's|share/games|share|' Bombermaaan/CGame.cpp
sed -i 's/INSTALL = install/INSTALL = install -m 755/' RESGEN/Makefile
sed -i '74s/char/const char/' Bombermaaan/winreplace.cpp

%build
%ifarch aarch64
export CC=clang CXX=clang++
%endif
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 755 Bombermaaan/Bombermaaan $RPM_BUILD_ROOT%{_bindir}/bombermaaan
mkdir -p $RPM_BUILD_ROOT%{_libdir}
install -m 755 RESGEN/libbombermaaan.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}
ln -s libbombermaaan.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/libbombermaaan.so.1
ln -s libbombermaaan.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/libbombermaaan.so
install -Dm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/pixmaps/bombermaaan.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/bombermaaan
cp -a Levels $RPM_BUILD_ROOT%{_datadir}/bombermaaan

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/bombermaaan.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Bombermaaan
Name[zh_TW]=炸彈人
Comment=Multi-player strategy bomberman-like game
Comment[zh_TW]=Bombermaaan 類似炸彈超人的遊戲
Exec=bombermaaan
Icon=bombermaaan
Type=Application
Terminal=false
Categories=Game;
EOF

%files
%doc CHANGELOG.txt COPYING.txt Readme.html
%{_bindir}/*
%{_libdir}/libbombermaaan.so*
%{_datadir}/bombermaaan/*   
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.0
- Rebuilt for Fedora
