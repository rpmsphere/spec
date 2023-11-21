Name: atris
Summary: tetris-like game with a twist for Unix
Version: 1.0.7
Release: 1
Group: games
License: Free Software
URL: https://www.wkiri.com/projects/atris
Source0: %{name}-%{version}.tar.gz
BuildRequires: desktop-file-utils
BuildRequires: SDL_ttf-devel

%description
Alizarin Tetris includes multi-player support, user-extensible color, shape
and sound styles, can use TCP/IP networking and features a few different AI
opponents.

%prep
%setup -q

%build
export LDFLAGS="-Wl,--allow-multiple-definition"
%configure
sed -i 's|/games|/share|' Makefile
%make_build

%install
sed -i 's|^prefix = /usr|prefix = %{buildroot}/usr|' Makefile
%make_install
mkdir -p %{buildroot}/var/games/%{name}

%files
%doc README NEWS COPYING ChangeLog AUTHORS
%{_bindir}/%{name}
#%{_datadir}/applications/%{name}.desktop
#%{_datadir}/doc/%{name}/
%{_datadir}/%{name}
#%{_mandir}/*/man1/%{name}.1.gz
#%{_mandir}/man1/%{name}.1.gz
#%{_datadir}/menu/%{name}
/var/games/%{name}

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.7
- Rebuilt for Fedora
