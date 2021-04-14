Summary:	A 2d networked helicopter game
Name:		copter-commander
Version:	1.8
Release:	16.4
License:	GPLv2+
Group:		Games/Arcade
URL:		http://sourceforge.net/projects/coco/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-makefile-destdir.patch
Patch1:		copter-commander-1.8-lvalue.patch
Source1:	%{name}.png
BuildRequires:	libgnome-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	libtiff-devel
BuildRequires:	esound-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	udisks2

%description
A unique blend of arcade action and real time strategy, Copter Commander
is fun for novices but surprisingly deep. It supports one to four players 
via Internet play and is based on the game design of Rescue Raiders/Armor
Alley.

%prep
%setup -q
%patch0 -p0
%patch1 -p0 -b .lvalue

%build
make \
    CFLAGS="%{optflags} -Wl,--allow-multiple-definition" \
    COCO_OPTIMIZATION_FLAGS="-O2" \
    COCO_INSTALL_DIRECTORY=%{_prefix} \
    COCO_BIN_DIRECTORY=%{_bindir} \
    COCO_SHARE_DIRECTORY=%{_datadir}/%{name}/%{version}

%install
%make_install \
    COCO_INSTALL_DIRECTORY=%{_prefix} \
    COCO_BIN_DIRECTORY=%{_bindir} \
    COCO_SHARE_DIRECTORY=%{_datadir}/%{name}/%{version}

install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Copter Commander
Comment=Copter Commander
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-glx.desktop << EOF
[Desktop Entry]
Name=Copter-Commander Glx
Comment=Copter Commander OpenGL
Exec=%{name}-glx
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%files
%doc DEVEL GNOME-HACKS ChangeLog copyright
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*.desktop

%changelog
* Tue Feb 10 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8
- Rebuilt for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 1.8-12
+ Revision: e6c6107
- MassBuild#464: Increase release tag
