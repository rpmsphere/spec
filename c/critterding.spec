%undefine _debugsource_packages

Name: critterding
Summary: Evolving Artificial Life
Version: 1.0beta14
Release: 16.1
Group:  Science/Engineering
License: GPLv3
URL: http://critterding.sourceforge.net/
Source0: http://sourceforge.net/projects/critterding/files/critterding/sources/%{name}-beta14.tar.bz2
BuildRequires: gcc-c++
BuildRequires: freetype-devel
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel, cmake, libpng-devel, boost-devel, freeglut-devel, libgomp, zlib-devel
BuildRequires: qt4-devel

%description
Critterding is a "Petri dish" universe in 3D that demonstrates evolving
artificial life. Critters start out with completely random brains and bodies,
but will automatically start evolving into something with much better survival
skills.

%prep
%setup -q -n %{name}-beta14
sed -i 's|_1|boost::placeholders::_1|' src/common/be_command_system.cpp src/scenes/critterding/evolution.cpp

%build
cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README Changelog LICENSE AUTHORS
%{_bindir}/*
%{_datadir}/*

%changelog
* Thu Dec 15 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0beta14
- Rebuilt for Fedora
