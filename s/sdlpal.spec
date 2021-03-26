Name: sdlpal
Summary: An SDL-based reimplemention of the classic Chinese RPG game
Version: 190728
Release: 1
Group: Amusements/Games
License: GPLv2
URL: https://github.com/sdlpal/sdlpal
Source0: %{name}-master.zip
Source1: %{name}.png
#Source2: pal.tar.bz2
BuildRequires: SDL-devel
#Requires: %{name}-data

%description
SDLPAL is an SDL-based reimplementation of the classic Chinese-language RPG
"Xian Jian4 Qi2 Xia2 Zhuan4" (also known as PAL or Legend of Sword and Fairy).

%prep
%setup -q -n %{name}-master
#sed -i '75,81d' common.h
sed -i 's|-lm|-lm -Wl,--allow-multiple-definition|' unix/Makefile

%build
make -C unix %{?_smp_mflags}

cat > %{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=SDL PAL
Comment=An SDL-based reimplemention of Xian Jian Qi Xia Zhuan
Icon=sdlpal
Exec=sdlpal
Type=Application
Terminal=false
Categories=Game;
EOF

cat > %{name}.sh <<EOF
#!/bin/sh
cd %{_libexecdir}/%{name}
exec %{name}
EOF

%install
install -Dm755 %{name}.sh %{buildroot}%{_bindir}/%{name}
install -Dm755 unix/%{name} %{buildroot}%{_libexecdir}/%{name}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS LICENSE README.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jul 31 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 190728
- Rebuild for Fedora
