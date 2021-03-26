Name: spacewar
Version: 0.0.1
Release: 7.1
Source0: http://sourceforge.net/projects/pdp1spacewar/files/%{name}.tar.gz
License: GNU General Public License
Group: Amusements/Arcade
URL: http://sourceforge.net/projects/pdp1spacewar
Summary: SpaceWar on PDP-1 emulator
BuildRequires: gcc-c++, wxGTK3-devel, automake

%description
The original computer video game, SpaceWar!, implemented on a DEC PDP-1 emulator.
Written in C++ using wxWidgets, this program runs PDP-1 object code from the
original 1962 game. Based upon the Java version that had been available from MIT.

%prep
%setup -q -n %{name}
touch ChangeLog

%build
aclocal
automake --add-missing
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install
install -Dm 644 src/bitmaps/%{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=SpaceWar!
Comment=SpaceWar on PDP-1 emulator
Exec=spacewar
Icon=spacewar
Terminal=false
Categories=Game;ArcadeGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Dec 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuild for Fedora
