Name:           xiangqi-chess
Version:        0.5
Release:        9.4
Summary:        SDL Chinese Chess Board
License:        GPL
URL:            https://sourceforge.net/projects/xiangqi-chess/
Source0:        https://sourceforge.net/projects/xiangqi-chess/files/xiangqi-chess/Version%200.5/xiangqi-chess_0.5.tar.bz2
BuildRequires:  gcc-c++, SDL-devel, SDL_ttf-devel, SDL_image-devel, SDL_gfx-devel, SDL_mixer-devel

%description
A Chinese Chess (xiangqi) game for Linux and Windows. Aims to be fast,
flexible and above all simple to use. You can play with your friends or
against the AI.

%prep
%setup -q -n %{name}
sed -i 's|-lSDL_draw||' src/Makefile
sed -i 's|data/|/usr/share/xiangqi-chess/|' src/*.cpp

%build
make -C src

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 xiangqi $RPM_BUILD_ROOT%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a data/images data/pieces $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Xiangqi
Type=Application
Categories=Game;BoardGame;
Icon=%{_datadir}/%{name}/images/board.png
Comment=SDL Chinese Chess Board
Exec=%{name}
EOF

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%changelog
* Sun Oct 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
