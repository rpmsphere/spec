Summary:        Chess variant that cause surronding pieces to disappear
Name:           nuclearchess
Version:        1.0.0
Release:        7.1
License:        GPLv2
Source:         https://user.cs.tu-berlin.de/~karlb//%{name}/%{name}-%{version}.tar.gz
Group:          Games/Boards
URL:            https://www.linux-games.com/nuclearchess/
BuildRequires:  SDL_image-devel

%description
NuclearChess is a chess variant. Whenever a piece is captured, both
pieces and all pieces on neighbour fields die.

%prep
%setup -q

%build
export LDFLAGS="-lm"
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=/usr/share/nuclearchess/gfx/atom.png
Comment=%{summary}
Categories=BoardGame;
Name=Nuclear Chess
EOF

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Oct 03 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.0.0-6
- (3d9f5bd) MassBuild#1257: Increase release tag
