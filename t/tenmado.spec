Name: tenmado
Version: 0.10
Release: 5.1
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.png
Source2: %{name}.desktop
License: GNU General Public License
Group: Amusements/Games/Action/Arcade
URL: http://www.interq.or.jp/libra/oohara/tenmado/
Summary: Hard-core shoot 'em up game in blue-or-red world
BuildRequires:  SDL_image-devel, libXpm-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
tenmado is a vertically scrolling, late 1990s style (that is, a massive number
of enemy shots against a smaller-than-it-looks spaceship) shoot 'em up game.
A very accurate collision detection makes it a game of dexterity. If something
looks like a triangle, it is a triangle, not a rectangle of similar size.

However, surviving is only 20% of the game. The main feature of tenmado is the
"color chain bonus". You can get a very big score (about 100 times bigger than
a normal enemy-destruction point) by destroying enemies of the same color
successively. It is easy or difficult depending on how greedy you are.

%prep
%setup -q

%build
%configure --with-sdl
make

%install
make DESTDIR=${RPM_BUILD_ROOT} mandir=%{_mandir} install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications
%__install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/games/%{name}
%{_datadir}/man/man6/%{name}.6.*
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat Sep 29 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10
- Rebuilt for Fedora
