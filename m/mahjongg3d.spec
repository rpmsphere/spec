Name:		mahjongg3d
Version:	0.96
Release:	20.1
Summary:	MahJongg 3D Solitaire
License:	GPLv2+
Group:		Games/Boards
URL:		http://www.reto-schoelly.de/mahjongg3d/
Source:		http://www.reto-schoelly.de/mahjongg3d/%{name}-%{version}.tar.bz2
Source1:	http://www.reto-schoelly.de/mahjongg3d/%{name}-0.96-patch2.tar.bz2
Source10:	http://www.reto-schoelly.de/mahjongg3d/hieroglyph_tileset.tar.bz2
Source11:	http://www.reto-schoelly.de/mahjongg3d/lab_layout.tar.bz2
Source20:	%{name}-16.png
Source21:	%{name}-32.png
Source22:	%{name}-48.png
Patch:		mahjongg3d-0.96-mdv-64bit-fix.patch
BuildRequires:	qt3-devel
BuildRequires:	libXmu-devel
BuildRequires:	pkgconfig(glu)

%description
MahJongg Solitaire 3D is an OpenGL enhanced solitaire version of the ancient
chinese board game "Mah Jongg".

%prep
%setup -q -n mahjongg3d.release -a 1
%patch -p1 -b .build+x64-fix
tar xf %{SOURCE10} -C bin
tar xf %{SOURCE11} -C bin
cp -fr patch2/* .
rm -fr patch2
sed -i -e 's/openglwidget.h/OpenGLWidget.h/' src/MainDialogBase.ui

%build
export QTDIR=%{_libdir}/qt-3.3
$QTDIR/bin/qmake
$QTDIR/bin/qmake src/src.pro -o src/Makefile
cat > src/gamedata_path.h <<EOF
#define GAMEDATA_BASE_PATH "/usr/share/mahjongg3d"
EOF
make PREFIX=%{_prefix} GAMEDATA_PREFIX=%_datadir

%install
rm -rf %buildroot
install -d %buildroot%{_datadir}/%{name}/backgrounds
install -d %buildroot%{_datadir}/%{name}/gra
install -d %buildroot%{_datadir}/%{name}/layouts
install -d %buildroot%{_datadir}/%{name}/tilesets
install -d %buildroot%{_datadir}/%{name}/tilesets/default
install -d %buildroot%{_datadir}/%{name}/tilesets/flowers
install -d %buildroot%{_datadir}/%{name}/tilesets/hiero
install -d %buildroot%{_datadir}/%{name}/tilesets/runes
install -d %buildroot%{_datadir}/%{name}/tilesets/traditional

install -d %buildroot%{_bindir}
install -d %buildroot%{_mandir}/man6
install -m 0755 bin/%{name} %buildroot%{_bindir}/
install -m 0644 bin/backgrounds/* %buildroot%{_datadir}/%{name}/backgrounds/
install -m 0644 bin/gra/* %buildroot%{_datadir}/%{name}/gra/
install -m 0644 bin/layouts/* %buildroot%{_datadir}/%{name}/layouts/
install -m 0644 bin/tilesets/*.tileset %buildroot%{_datadir}/%{name}/tilesets/
install -m 0644 bin/tilesets/default/* %buildroot%{_datadir}/%{name}/tilesets/default/
install -m 0644 bin/tilesets/flowers/* %buildroot%{_datadir}/%{name}/tilesets/flowers/
install -m 0644 bin/tilesets/hiero/* %buildroot%{_datadir}/%{name}/tilesets/hiero/
install -m 0644 bin/tilesets/runes/* %buildroot%{_datadir}/%{name}/tilesets/runes/
install -m 0644 bin/tilesets/traditional/* %buildroot%{_datadir}/%{name}/tilesets/traditional/
install -m 0644 %{name}.6 %buildroot%{_mandir}/man6/
install -m 644 -D %{SOURCE20} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 644 -D %{SOURCE21} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 644 -D %{SOURCE22} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=MahJongg 3D Solitaire
Comment=A board game using OpenGL, with several themes
Exec=%{name}
Icon=%{name}
Type=Application
Categories=Game;BoardGame;Qt;
EOF

%files
%doc Changelog COPYING INSTALL_CUSTOM README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Thu May 07 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.96
- Rebuilt for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.96-10
+ Revision: 84a7485
- MassBuild#464: Increase release tag
