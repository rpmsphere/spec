Name:           asteroids3D
Summary:        A 3D first-person game of blowing up asteroids
Version:        0.5.1
Release:        10.1
License:        GPLv2+
Group:          Games/Arcade
Source0:        https://sourceforge.net/projects/a3d/%name-%version.tar.bz2
Source1:    %{name}.png
URL:            https://sourceforge.net/projects/a3d/   
BuildRequires:  mesa-libGL-devel, mesa-libGLU-devel, freeglut-devel

%description
A simple first person shooter of blowing up asteroids in 3D space.
The codebase also serves as an introduction to trigonometry and OpenGL.
The graphics more accurately reflect the future position of the
targeted asteroid and provide information about closure rate.

%prep
%setup -q 

%build
%configure --with-gamesdir=%_bindir --with-gamedatadir=%_datadir/%name
make %{?_smp_mflags}

%install
make install gamesdir=$RPM_BUILD_ROOT%{_bindir} gamedatadir=$RPM_BUILD_ROOT%{_datadir}/%name
install -Dm644 %{SOURCE1} %buildroot%{_datadir}/pixmaps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Categories=Game;ArcadeGame;
Name=Asteroids3D
Comment=A 3D first-person game of blowing up asteroids
EOF

%files
%doc COPYRIGHT README.html 
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.1
- Rebuilt for Fedora
* Fri Jan 11 2013 umeabot <umeabot> 0.5.1-3.mga3
+ Revision: 346472
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Wed May 11 2011 dmorgan <dmorgan> 0.5.1-2.mga1
+ Revision: 97133
- imported package asteroids3D
