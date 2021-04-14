%undefine _debugsource_packages

Name: maxishoot
Summary: Kill as many enemies as you can
Version: 1.0.3
Release: 14.1
Group: Amusements/Games
License: GPLv3
URL: http://congelli.eu/prog_info_maxishoot.html
Source0: http://congelli.eu/download/maxishoot/%{name}-%{version}.tar.gz
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: compat-SFML16-devel

%description
Maxishoot is a little game. The goal is very simple : kill as many enemies as
you can (missiles, shells, planes, fire balls...), protect your base and save
the bonuses (health, additional bullets, slight) which are only active when
they touch your protection shield. Moreover, you can create your own levels
and change completely the game!

%prep
%setup -q
cat > sfml.pc <<EOF
prefix=/usr
exec_prefix=\${prefix}
libdir=\${exec_prefix}/%{_lib}
includedir=\${prefix}/include/sfml1

Name: SFML
Description: Simple and Fast Multimedia Library
Version: 1.6
Requires: gl
Libs: -L\${libdir} -lsfml-graphics-1.6 -lsfml-system-1.6 -lsfml-window-1.6 -lsfml-network-1.6 -lsfml-audio-1.6 -lGLU -lGL
Cflags: -I\${includedir}
EOF

%build
export PKG_CONFIG_PATH=.
%configure
make %{?_smp_mflags} CXXFLAGS+=-fPIC

%install
%make_install
sed -i 's|Game;|Game;ActionGame;|' %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuilt for Fedora
