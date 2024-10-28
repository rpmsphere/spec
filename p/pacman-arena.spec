%undefine _debugsource_packages

Name:           pacman-arena
Version:        0.15
Release:        10
Summary:        Pacman clone in full 3D with a few surprises
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
URL:            https://pacmanarena.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}-icons.tar
Source3:        %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE - pacman-arena-0.15-Makefile.patch -- Fix paths, CFLAGS and LDFLAGS
Patch0:         %{name}-0.15-Makefile.patch
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_net)
BuildRequires:  pkgconfig(sdl)
Requires:       opengl-games-utils

%description
Pacman Arena is a Pacman clone in full 3D with a few surprises.
Rockets, bombs and explosions abound.

A Pacman clone gone mad

Yes, it's Pacman. With rockets. And bombs. And spoiled gameplay. And in full 3D.
Finally, a version of Pacman which will bring your shiny new machine
down to it's knees.

%prep
%setup -q -b 2
%patch 0 -p1

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# install icons
for i in 32 48 64 72 96; do
    install -Dm 0644 ../icons/%{name}_${i}x${i}.png \
            %{buildroot}/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# install Desktop file
install -D -m 644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

# symlink OpenGL Wrapper
ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/%{name}-wrapper

%files
%doc COPYING README
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}

%changelog
* Wed Apr 22 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.15
- Rebuilt for Fedora
* Sun Jun 21 2015 nemysis@gmx.ch
- license update: GPL-2.0+ No indication that this is GPL-2.0 (only)
* Thu Jan  1 2015 nemysis@gmx.ch
- Add right description for patch
- Use for patch %%{name}-version instead of %%{name}-%%{version}
- Add BuildRoot
* Thu Nov 13 2014 nemysis@gmx.ch
- Remove Mesa-devel, forgotten in previous commit
* Thu Nov 13 2014 nemysis@gmx.ch
- Add Source3 pacman-arena-rpmlintrc
* Thu Nov 13 2014 nemysis@gmx.ch
- Change Desktop entry file, use GenericName Pac-Man instead of
  Arcade Game
- Rename pacman-arena-Makefile.patch to pacman-arena-0.15-Makefile.patch
- Remove BuildRequires for desktop-file-utils and Mesa-devel
- Add BuildRequires for fdupes
- Use BuildRequires pkgconfig(SDL_mixer), pkgconfig(SDL_net) and
  pkgconfig(sdl) instead of libSDL-devel, libSDL_mixer-devel and
  libSDL_net-devel
* Wed Oct  1 2014 nemysis@gmx.ch
- Change Desktop entry file
- Reordering BuildRequires
- Add BuildRequires for desktop-file-utils and hicolor-icon-theme
- Change icons, use %%{name}-icons.tar
- Change description
- Add %%{name}-rpmlintrc, use OpenGL Wrapper
* Sun Nov 27 2011 PVince81@opensuse.org
- Added -lm to the Makefile patch to fix openSUSE 12.1 compilation
  issue.
* Wed Oct  7 2009 PVince81@yahoo.fr
- Initial package
