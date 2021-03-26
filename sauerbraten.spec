%define _fversion 2008_06_17

Name:          sauerbraten
Version:       20080711
Release:       1
License:       zlib
Summary:       free multiplayer/singleplayer FPS game
URL:	       http://www.sauerbraten.org/
Group:         Amusements/Games/Action
Source:        %{name}_%{_fversion}_ctf_edition_linux.tar.bz2
Source1:       sauerbraten.desktop
Source2:       sauerbraten.png
Source100:     patch_2008_06_20_linux.tar.bz2
Source101:     patch_2008_07_11_linux.tar.bz2
BuildRequires: gcc-c++ SDL_image-devel SDL_mixer-devel 
BuildRequires: mesa-libGL-devel
Requires:      sauerbraten-data = %{version}

%description
Much like the original Cube, the aim of this game is not necessarily to produce
the most features & eyecandy possible, but rather to allow map/geometry editing
to be done dynamically in-game, to create fun gameplay and an elegant engine.

%package server
Summary:  Sauerbraten standalone server
Requires: %{name} = %{version}

%description server
Sauerbraten standalone server

%package data
Summary:  Sauerbraten data files
Requires: %{name} = %{version}

%description data
Data files needed for cube 2 Sauerbraten

%prep
%setup -q -n %{name} -b100 -b101
sed -i 's|-Wall|-Wall -Wno-narrowing -lX11|' src/Makefile
sed -i 's|lastteam = false;|lastteam = NULL;|' src/fpsgame/capture.h

%build
cd src
make

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p bin
mv src/sauer_client bin/client
mv src/sauer_server bin/server
mkdir -p $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -a bin $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}

cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh

SAUER_DIR=%{_datadir}/%{name}
SAUER_DIR_PRIVATE=\$HOME/.sauerbraten
cd \$SAUER_DIR_PRIVATE
test -L data && rm data
test -L packages && rm packages
test -d data || mkdir data
test -d packages || mkdir packages
exec %{_libdir}/%{name}/bin/client -r -q\$SAUER_DIR_PRIVATE "\$@" -k\$SAUER_DIR 
EOF

chmod 755 $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -sf %{_libdir}/%{name}/bin/server $RPM_BUILD_ROOT%{_bindir}/%{name}-server

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/sauerbraten
cp -a data packages $RPM_BUILD_ROOT/%{_datadir}/sauerbraten

%clean
rm -fr $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/bin
%{_libdir}/%{name}/bin/client
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files server
%{_bindir}/%{name}-server
%dir %{_libdir}/%{name}/bin
%{_libdir}/%{name}/bin/server

%files data
%doc docs/*
%dir %{_datadir}/sauerbraten
%{_datadir}/sauerbraten/data
%{_datadir}/sauerbraten/packages

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20080711
- Rebuild for Fedora
* Wed Oct 15 2008 Feather Mountain <john@ossii.com.tw> - 20080711-1.37.ossii
- Rebuild for M6(OSSII)
