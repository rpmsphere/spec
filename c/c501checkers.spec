%undefine _debugsource_packages

Name: c501checkers
Summary: A checkers game
Version: 1.1.3
Release: 20.1
Group: Amusements/Games
License: GPLv3
URL: http://congelli.eu/prog_info_c501checkers.html
Source0: http://congelli.eu/download/c501checkers/%{name}-%{version}.tar.gz
BuildRequires: wxGTK2-devel
BuildRequires: compat-SFML16-devel

%description
You can use international rules (10x10 sized board) or English rules
(8x8 sized board). Moreover, you can fight against your computer
(5 levels are available) or another human.

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
sed -i 's|Game;|Game;BoardGame;|' %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-icon.png

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.3
- Rebuilt for Fedora
