%undefine _debugsource_packages

Name:           solarus
URL:            https://www.solarus-engine.org/
BuildRequires:  gcc-c++ cmake SDL2_image-devel SDL2_ttf-devel openal-soft-devel libvorbis-devel libmodplug-devel luajit-devel physfs-devel
BuildRequires:	compat-lua-devel
License:        GPLv3 or later
Group:          Amusements/Games/RPG
Version:        1.6.5
Release:        1
Summary:        An open-source Zelda-like game engine
Source0:	https://gitlab.com/solarus-games/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

%description
Solarus is an open-source Zelda-like game engine written in C++.

%package devel
Summary:	Development files for solarus
Requires:	%{name}

%description devel
Development files for Solarus, including header files.

%package gui
Summary:        Graphical user interface to launch Solarus games
Requires:       %{name}

%description gui
This package provides a graphical user interface to launch games
based on the Solarus engine.

%prep
%setup -q -n %{name}-v%{version}

%build
cmake -DCMAKE_INSTALL_PREFIX:PATH="%{_prefix}" -DCMAKE_BUILD_TYPE=Release -DLUA_INCLUDE_DIR=/usr/include/lua-5.1 .
make -j1

%install
make DESTDIR=%{buildroot} install

%files
%doc license* *.md
%{_bindir}/%{name}-run
%{_libdir}/lib%{name}.so.*
%{_datadir}/icons/hicolor/*/apps/org.solarus_games.solarus.Runner*.*
%{_mandir}/man?/%{name}-run.*
%{_datadir}/pixmaps/org.solarus_games.solarus.Runner.png

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-gui.so

%files gui
%{_bindir}/%{name}-launcher
%{_libdir}/lib%{name}-gui.so.*
%{_datadir}/applications/org.solarus_games.solarus.Launcher.desktop
%{_datadir}/icons/hicolor/*/apps/org.solarus_games.solarus.Launcher*.*
%{_mandir}/man?/%{name}-launcher.*
%{_datadir}/metainfo/org.solarus_games.solarus.appdata.xml
%{_datadir}/pixmaps/org.solarus_games.solarus.Launcher.png
%{_datadir}/solarus-gui

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.5
- Rebuilt for Fedora
* Wed Dec 28 2011 giacomosrv@gmail.com
- packaged solarus version 0.9.0
