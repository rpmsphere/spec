Name: spacecup
Summary: 3D ice-hockey or football in the space
Version: 0.3.1
Release: 13.1
Source0: http://download.sourceforge.net/spacecup/SpaceCup-%{version}.tar.gz
Source1: %{name}.32.xpm.bz2
Patch0: spacecup-fix-static-installdir.patch.bz2
Patch1: spacecup-add-datadir.patch.bz2
Patch2: spacecup-fix-datafiles-installpath.patch.bz2
URL: http://spacecup.sourceforge.net/
License: GPL
Group: Games/Arcade
BuildRequires: freeglut-devel
BuildRequires: libjpeg-turbo-devel
Requires: sox

%description
SpaceCup is a 3D game, look like a ice-hockey or football in the space with
many ball which rebound in all direction. The aim of the game is to score more
goal points than the adversary.

%prep
%setup -q -n SpaceCup
%patch0 -p0
%patch1 -p0
%patch2 -p0
sed -i -e 's|iostream\.h|iostream|' -e 's|cout|std::cout|' -e 's|cerr|std::cerr|' -e 's|endl|std::endl|' src/*.h src/*.cc src/sound/*.cc
sed -i '1i #include <cstring>' src/menu.cc
sed -i '42,44s|^extern ||' src/clavier.cc
%if %{fedora}>27
sed -i '/TOUCHE_SOUND,Stop/d' src/arene.cc
%endif

%build
make BINDIR=%{_bindir} DATADIR=%{_datadir} COPTS="$RPM_OPT_FLAGS -fpermissive" DEFS=-DDATADIR=\\\"/usr/share\\\"

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_datadir}/SpaceCup
make install BINDIR=$RPM_BUILD_ROOT/%{_bindir} DATADIR=$RPM_BUILD_ROOT/%{_datadir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.xpm
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Space Cup
Comment=3D ice-hockey or football in the space
Exec=spacecup
Icon=spacecup
Terminal=false
Categories=Game;ArcadeGame;
EOF

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%doc AUTHORS COPYING README README.fr
%{_bindir}/*
%{_datadir}/SpaceCup
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue May 15 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
* Wed Aug 30 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.3-1mdk
- first mdk version. thanks to fredl.
