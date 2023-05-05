%global _name zsxd

Name:           solarus-quest-zsxd
URL:            https://www.solarus-games.org/games/the-legend-of-zelda-mystery-of-solarus-xd/
BuildRequires:  gcc-c++ cmake zip
Requires:       solarus
License:        GPLv3 or later
Group:          Amusements/Games/RPG
Version:        1.12.2
Release:        1
Summary:        The Legend of Zelda: Mystery of Solarus XD
Source0:        https://gitlab.com/solarus-games/%{_name}/-/archive/dev/%{_name}-dev.tar.gz
BuildArch:	noarch

%description
Zelda Mystery of Solarus XD: a humorous game that works with Solarus,
an open-source Zelda-like 2D game engine.
This is a parody of Mystery of Solarus DX.

%prep
%setup -q -n %{_name}-dev

%build
cmake -DCMAKE_INSTALL_PREFIX:PATH="%{_prefix}" .
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc license.txt *.md
%{_bindir}/%{_name}
%{_datadir}/solarus/%{_name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{_name}.png
%{_datadir}/pixmaps/%{_name}.png

%changelog
* Sun Dec 18 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.12.2
- Rebuilt for Fedora
* Thu Dec 29 2011 giacomosrv@gmail.com
- packaged zsxd version 1.4
