Name:           angband
Version:        4.1.3
Release:        2
Summary:        Single-player dungeon exploration game in the universe of JRR Tolkien
Group:          Games/Adventure
License:        GPLv2
URL:            http://rephial.org
Source0:        http://rephial.org/downloads/4.1/%{name}-%{version}.tar.gz
Patch0:		angband-4.0.5-desktop.patch
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  python3-sphinx
Requires:       xorg-x11-fonts-misc

%description
Angband is a free, single-player dungeon exploration game.
You play an adventurer: seeking riches, fighting monsters, and
preparing for a final battle with Morgoth, the Lord of Darkness.

%files
%doc *.txt doc/manual.html
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%config(noreplace) %{_sysconfdir}/%{name}
%{_datadir}/%{name}

%prep
%setup -q
%patch0 -p1

%build
export CC="gcc -Wl,--allow-multiple-definition"
autoreconf -vfi
%configure --bindir=%{_bindir} \
               --enable-curses \
               --enable-x11 \
               --enable-sdl \
               --enable-sdl-mixer
%make_build

%install
%make_install

install -d %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_datadir}/%{name}/icons/*.desktop %{buildroot}%{_datadir}/applications/

for size in 16 32 128 256 512; do
  install -D -m644 %{buildroot}%{_datadir}/%{name}/icons/att-${size}.png \
      %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

%changelog
* Fri Jun 19 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.3
- Rebuild for Fedora
* Sun Nov 11 2018 abfonly <abfonly@gmail.com> 4.1.3-1
- (5c55223) Log: Update to 4.1.3
