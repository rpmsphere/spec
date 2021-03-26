Name: sdlhana
Summary: SDL-based Hanafuda game
Version: 0.34
Release: 6.1
Group: Amusements/Games
License: GPLv2
URL: https://github.com/CecilHarvey/sdlhana
Source0: %{name}_%{version}-1.tar.gz
Source1: %{name}.png
BuildRequires: SDL-devel

%description
Hanafuda is a Japanese-oriented card game which is mostly played in Japan and
Korea, also known as "Hwa-T'u" in Korean.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=SDLHana
Comment=SDL-based Hanafuda game
Exec=sdlhana
Icon=sdlhana
Type=Application
Terminal=false
Categories=Game;CardGame;
EOF

%files
%doc AUTHORS ChangeLog CREDITS COPYING README NEWS TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jan 15 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.34
- Rebuild for Fedora
