%undefine _debugsource_packages

Name: smw
Summary: Super Mario War
Version: 1.8
Release: 17.4
License: GPLv2
Group: Amusements/Games/Action
Source0: smw-1.8.tar.gz
BuildRequires:	gcc-c++ make SDL-devel SDL_mixer-devel SDL_image-devel libogg-devel libpng12-devel libjpeg-devel libvorbis-devel
URL: https://github.com/erlehmann/Super-Mario-War 

%description
Super Mario War is a deathmatch game involving mario for multiple players.

%prep
%setup -q

%build
export CFLAGS=-I/usr/include/libpng12
sed -i 's|-lpng|-lpng12|' configure
./configure
make
#CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}/usr/games %{buildroot}/usr/bin
mv %{buildroot}/usr/share/games/smw %{buildroot}/usr/share/smw

%clean
rm -rf %{buildroot}

%files
/usr/bin/*
/usr/share/smw

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8
- Rebuilt for Fedora
