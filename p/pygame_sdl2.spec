Name: pygame_sdl2
Version: 6.99.14.2
Release: 1.1
Summary: A reimplementation of the Pygame API using SDL2
Group: Development/Python
License: LGPL
URL: https://github.com/renpy/pygame_sdl2
Source: %{name}-master.zip
BuildRequires: ctags python3-devel
BuildRequires: SDL2-devel SDL2_gfx-devel SDL2_image-devel SDL2_mixer-devel SDL2_ttf-devel
BuildRequires: libjpeg-devel libpng-devel python3-Cython python3-cssselect python3-html5lib time

%description
Pygame_sdl2 is a reimplementation of the Pygame API using SDL2 and
related libraries. The initial goal of this project are to allow games
written using the pygame API to run on SDL2 on desktop and mobile
platforms. We will then evolve the API to expose SDL2-provided
functionality in a pythonic manner.

%package devel
Summary: Pygame_SDL2 development headers
Group: Development/Python
Requires: %{name}

%description devel
Pygame_sdl2 is a reimplementation of the Pygame API using SDL2 and
related libraries. The initial goal of this project are to allow games
written using the pygame API to run on SDL2 on desktop and mobile
platforms. We will then evolve the API to expose SDL2-provided
functionality in a pythonic manner.

Install %name-devel if you need the API development environment.

%prep
%setup -n %name-master
#sed -i 's/sdl_libs = /sdl_libs = ["m"]+/' setup.py
sed -i -e 's|MIX_INIT_MODPLUG|0x4|' -e 's|MIX_INIT_FLUIDSYNTH|0x20|' src/pygame_sdl2/mixer.pyx

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%doc README*
%python3_sitearch/*

%files devel
%_includedir/python3.*/*

%changelog
* Tue Feb 27 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 6.99.14.2
- Rebuilt for Fedora
* Fri Jul 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.99.10.1227-alt2
- Reimported sources and fixed build
* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 6.99.10.1227-alt1
- Autobuild version bump to 6.99.10.1227
* Mon Nov 23 2015 Fr. Br. George <george@altlinux.ru> 6.99.6.739-alt2
- Synchronize with Nov 3, 2015 version
* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 6.99.6.739-alt1
- Autobuild version bump to 6.99.6.739
* Thu Apr 23 2015 Fr. Br. George <george@altlinux.ru> 6.99.0.303-alt1
- Initial build for ALT
