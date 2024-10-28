%undefine _debugsource_packages

Name:           meteor
Version:        1.4.2
Release:        12.4
Summary:        A GameBoy Advance emulator
License:        GPLv3+
Group:          Emulators
URL:            https://github.com/blastrock/meteor
Source0:        https://sourceforge.net/projects/meteorgba/files/%{name}-%{version}.tar.gz
Patch0:         meteor-1.4.0-gcc4.7.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  compat-SFML16-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(glew) >= 2.0.0
BuildRequires:  nasm
Source1:        gameboy.png

%description
Meteor is a GameBoy Advance emulator with GTK2 frontend.
Icon by Natsu714 from https://natsu714.deviantart.com/art/Free-Gameboy-Icon-288655907

%prep
%setup -q
%patch 0 -p1
sed -i -e '15s|sfml-graphics|sfml-system-1.6|' -e '18s|sfml-window|sfml-window-1.6|' -e '21s|sfml-system|sfml-graphics-1.6|' CMakeLists.txt
sed -i 's|-pipe|-pipe -std=c++11 -fPIC -I/usr/include/sfml1|' CMakeLists.txt
sed -i '21,25d' mym/source/CMakeLists.txt
sed -i '220,222d' mym/source/window.cpp

%build
%cmake -DDISABLE_ASM:BOOL=ON .
%cmake_build

%install
%cmake_install

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Meteor
Comment=GameBoy Advance emulator
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Game;Emulator;
EOF
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc README.md COPYING AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jun 16 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.2
- Rebuilt for Fedora
* Mon Mar 19 2012 Andrey Bondrov <abondrov@mandriva.org> 1.3.0-1mdv2012.0
+ Revision: 785545
- Update BuildRequires
- imported package meteor
