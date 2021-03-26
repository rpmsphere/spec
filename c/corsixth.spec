%define oname CorsixTH

Summary:	Open source clone of Theme Hospital
Name:		corsixth
Version:	0.63
Release:	1
Epoch:		1
License:	MIT
Group:		Games/Strategy
URL:		https://github.com/CorsixTH/CorsixTH
Source0:	https://github.com/CorsixTH/CorsixTH/archive/v%{version}/%{oname}-%{version}.tar.gz
Patch0:		CorsixTH-0.50-lua53.patch
BuildRequires:	cmake
BuildRequires:	ffmpeg-devel
BuildRequires:	lua-devel
BuildRequires:  luajit-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_mixer)
Requires:	lua-filesystem
Requires:	lua-lpeg
Requires:	timidity++

%description
This project aims to reimplement the game engine of Theme Hospital, and
be able to load the original game data files. This means that you will
need a purchased copy of Theme Hospital in order to enjoy CorsixTH.

%files
%doc LICENSE.txt README.txt
%{_bindir}/*
%{_datadir}/corsix-th
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop
%{_mandir}/man6/corsix-th.6.gz
%{_datadir}/metainfo/*.xml

%prep
%setup -q -n %{oname}-%{version}
#patch0 -p 1

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DWITH_LUAJIT=ON
%make_build

%install
%make_install

install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{oname} << EOF
#!/bin/bash
%{_datadir}/%{oname}/%{oname}
EOF
chmod +x %{buildroot}%{_bindir}/%{oname}
install -d %{buildroot}%{_datadir}/%{oname}/th-files/
install -D -m 0644 %{oname}/Original_Logo.svg -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=CorsixTH
Name[ru]=CorsixTH
Comment=Open Source clone of Theme Hospital game
Comment[ru]=Клон игры Theme Hospital
Exec=%{oname}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-mapedit.desktop << EOF
[Desktop Entry]
Name=CorsixTh MapEdit
Name[ru]=Редактор карт CorsixTh
Comment=Map Editor for Theme Hospital
Comment[ru]=Редактор карт для Theme Hospital
Exec=MapEdit
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

%changelog
* Mon Sep 09 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.63
- Rebuild for Fedora
* Mon Feb 27 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:0.60-5
- (e9dde4e) MassBuild#1264: Increase release tag
