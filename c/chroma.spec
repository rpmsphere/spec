Name:           chroma
BuildRequires:  SDL-devel SDL_image-devel freetype-devel gettext-devel ncurses-devel
Summary:        Abstract puzzle game with complex patterns of colourful shapes
Version:        1.20
Release:        1
License:        GPLv2
Group:          Amusements/Games/Action/Arcade
Source:         http://www.level7.org.uk/chroma/download/%{name}-%{version}.tar.bz2
Source1:        %{name}-curses.png
Source2:        %{name}-curses.desktop
Source3:        %{name}.png
Source4:        %{name}.desktop
Patch0:         %{name}-permissions.patch
URL:            http://www.level7.org.uk/chroma/

%description
Chroma is an abstract puzzle game. A variety of colourful shapes are arranged
in a series of increasingly complex patterns, forming fiendish traps that must
be disarmed and mysterious puzzles that must be manipulated in order to give
up their subtle secrets. Initially so straightforward that anyone can pick it
up and begin to play, yet gradually becoming difficult enough to tax even the
brightest of minds.

It features:
* twenty one levels, ranging from beginner to expert
* infinite undo and redo capability, as well as replay of solutions
* a choice of smooth graphics or a minimal, text based version
* a level editor to allow you to design your own puzzles
* released under an open source licence, free to play

Have you got what it takes to solve Chroma? 

%prep
%setup -q
%patch0 -p1
sed -i 's|inline void|void|' sdlshadowdisplay.c

%build
%configure
make

%install
make DESTDIR=%{buildroot} install
install -m 755 -D -d %{buildroot}%{_datadir}/pixmaps/
install -m 755 -D -d %{buildroot}%{_datadir}/applications/
install -m 644 -D %{S:1} %{buildroot}%{_datadir}/pixmaps/
install -m 644 -D %{S:3} %{buildroot}%{_datadir}/pixmaps/
install -m 644 -D %{S:2} %{buildroot}%{_datadir}/applications/
install -m 644 -D %{S:4} %{buildroot}%{_datadir}/applications/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING CHANGELOG
%{_bindir}/%{name}
%{_bindir}/%{name}-curses
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}-curses.desktop
%{_datadir}/pixmaps/%{name}-curses.png

%changelog
* Sun Jan 15 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.20
- Rebuilt for Fedora
* Mon Feb  1 2010 PVince81@yahoo.fr
- Initial package
