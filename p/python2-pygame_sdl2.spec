Name: python2-pygame_sdl2
Version: 7.3.5
Release: 1
Summary: A reimplementation of the Pygame API using SDL2
Group: Development/Python
License: LGPL
URL: https://github.com/renpy/pygame_sdl2
Source0: https://www.renpy.org/dl/7.3.5/pygame_sdl2-2.1.0-for-renpy-7.3.5.tar.gz
Source1: pygame_sdl2-missing-headers.zip
BuildRequires: ctags python3-devel
BuildRequires: SDL2-devel SDL2_gfx-devel SDL2_image-devel SDL2_mixer-devel SDL2_ttf-devel
BuildRequires: libjpeg-devel libpng-devel time
#BuildRequires: python2-Cython python2-cssselect python2-html5lib

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

Install %%name-devel if you need the API development environment.

%prep
%setup -qn pygame_sdl2-2.1.0-for-renpy-7.3.5
#sed -i 's/sdl_libs = /sdl_libs = ["m"]+/' setup.py
#sed -i -e 's|MIX_INIT_MODPLUG|0x4|' -e 's|MIX_INIT_FLUIDSYNTH|0x20|' src/pygame_sdl2/mixer.pyx
#sed -i 's|2.1.0-for-renpy-7.3.5|7.3.5|' PKG-INFO

%build
python2 setup.py build
unzip %{SOURCE1} -d gen

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
sed -i 's|2.1.0-for-renpy-7.3.5|7.3.5|' %{buildroot}%{python2_sitearch}/pygame_sdl2-2.1.0_for_renpy_7.3.5-py2.7.egg-info/PKG-INFO

%files
%doc README*
%python2_sitearch/*

%files devel
%_includedir/python2.*/*

%changelog
* Thu Aug 20 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 7.3.5
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
