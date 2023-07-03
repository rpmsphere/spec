%undefine _debugsource_packages

Name: syobon
Summary: An SDL-based port of Syobon Action
Version: 0.2
Release: 15.4
Group: Amusements/Games
License: GPLv2
URL: https://syobon.codeplex.com/
Source0: syobon-87914.zip
Source1: syobon.png
BuildRequires: SDL-devel
BuildRequires: SDL_mixer-devel

%description
OpenSyobon-M is based on OpenSyobon rc2. This project is an unofficial
modified version and in no way affiliated with OpenSyobon project or the
original authors of Syobon Action.

%prep
%setup -q -n SyobonAction
sed -i 's|\./data|%{_datadir}/%{name}|' Makefile DxLib.h

%build
make %{?_smp_mflags}

cat > %{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=OpenSyobon-M
Comment=An SDL-based port of Syobon Action
Icon=syobon
Exec=syobon
Type=Application
Terminal=false
Categories=Game;ArcadeGame;
EOF

%install
install -Dm755 SyobonAction %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a data/* %{buildroot}%{_datadir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Wed Jan 15 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
