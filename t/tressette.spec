Name:		tressette
Summary:	SDL Italian card game 4-player Tressette
Version:        0.7.4svn.12
Release:	16.4
URL:		http://invido.it/progetti/tressette_progetto.html
Source:         %{name}-%{version}.tar.xz
Patch0:		tressette_build.patch
Source1:        tressettetux.desktop
# replacing Arial-black, not redistributable AFAIK
Source2:        LiberationSans-Bold.ttf.tar.xz
License:	GPL-2.0+ and OFL-1.1 and SUSE-Bitstream-Vera
Group:		Amusements/Games/Board/Card
BuildRequires:  gcc-c++ pkgconfig libtool autoconf automake
BuildRequires:  expat-devel
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  libpng-devel libjpeg-devel pkgconfig(ogg) pkgconfig(vorbis) pkgconfig(zlib)
BuildRequires:  ghostscript-core ImageMagick

%description
The game of the Tressette (Italian card-game) with SDL graphics.
The version emulated is the game for 4 players, in team of two (computer+player vs. computer+computer).

%prep
%setup -q -a 2
%patch0 -p1
# move resources to an appropriate dir
pushd src/TreClientVs6
%__sed -i 's|data/font/ariblk.ttf|data/font/LiberationSans-Bold.ttf|' EngineApp.cpp
%__sed -i 's|\"\(data/[^\"]\+\)\"|\"%{_datadir}/%{name}/\1\"|' \
 cMusicManager.cpp OptionGameGfx.cpp OptionDeckGfx.cpp EngineApp.cpp cGameMainGfx.cpp cMenuMgr.cpp
popd
chmod a+x configure

%build
autoreconf -fiv
%configure
sed -i 's|-Werror=format-security||' Makefile */Makefile */*/Makefile
%{__make} %{?_smp_mflags} VERBOSE=1

%install
%make_install
%__install -D -m644 LiberationSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/data/font/LiberationSans-Bold.ttf
%__rm out/data/font/ariblk.ttf
%__cp -a out/data %{buildroot}%{_datadir}/%{name}
%__ln_s %{_datadir}/%{name}/data/help/tre.chm tre.chm
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}tux.desktop
mkdir -p %{buildroot}%{_datadir}/pixmaps
convert src/TreClientVs6/tre.ico\[0\] %{buildroot}%{_datadir}/pixmaps/%{name}tux.png

%files
%doc ReadMe.txt authors doc/manual/tresset.html tre.chm
%{_bindir}/%{name}tux
%{_datadir}/%{name}
%{_datadir}/applications/%{name}tux.desktop
%{_datadir}/pixmaps/%{name}tux.png

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.4svn.12
- Rebuilt for Fedora
* Wed Aug 21 2013 fa0sck@gmail.com
- Build latest stable version for openSUSE (from svn)
