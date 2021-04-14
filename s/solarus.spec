%undefine _debugsource_packages

Name:           solarus
URL:            http://www.solarus-engine.org/
BuildRequires:  gcc-c++ cmake SDL-devel SDL_image-devel SDL_ttf-devel openal-soft-devel libvorbis-devel libmodplug-devel lua-devel physfs-devel
BuildRequires: compat-lua-devel
License:        GPLv3 or later
Group:          Amusements/Games/RPG
Version:        1.1.1
Release:        9.1
Summary:        An open-source Zelda-like game engine
Source0:        http://www.solarus-games.org/downloads/solarus/%{name}-%{version}-src.tar.gz

%description
Solarus is an open-source Zelda-like game engine written in C++.

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX:PATH="%{_prefix}" -DCMAKE_BUILD_TYPE=Release -DLUA_INCLUDE_DIR=/usr/include/lua-5.1 .
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc ChangeLog license.txt readme.txt
%{_bindir}/%{name}

%changelog
* Fri Jan 03 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuilt for Fedora
* Wed Dec 28 2011 giacomosrv@gmail.com
- packaged solarus version 0.9.0
