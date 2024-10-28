Name:           cgoban
Version:        1.9.14
Release:        20.1
Summary:        A Go game client
License:        GPLv2+
Group:          Games/Boards
URL:            https://cgoban1.sourceforge.net/
Source:         https://sourceforge.net/projects/cgoban1/%{name}-%{version}.tar.bz2
BuildRequires:  libX11-devel

%description
Cgoban (Complete Goban) is for Unix systems with X11.  It has the ability
to be a computerized go board, view and edit smart-go files, and connect to
go servers on the Internet. Cgoban is also a smart interface for GNU Go.

%prep
%setup -q

%build
sed -i -e 's|\"./goDummy\"|\"/usr/games/gnugo --quiet\"|' src/cgoban.c
sed -i -e "s|-O2 -fomit-frame-pointer|%{optflags}|g" configure
chmod +x configure
%configure --x-includes=%{_includedir}/X11 --x-libraries=%{_libdir}
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man6
mkdir -p %{buildroot}/%{_datadir}/pixmaps
%makeinstall
cp cgoban_icon.png %{buildroot}/%{_datadir}/pixmaps/cgoban.png

mkdir -p %{buildroot}/%{_datadir}/applications
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=CGoban
Comment=Graphical game of Go
Exec=%{name}
Icon=cgoban
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

%files
%doc README TODO seigen-minoru.sgf
%{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Sun May 26 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.14
- Rebuilt for Fedora
* Fri Jan 11 2013 umeabot <umeabot> 1.9.14-16.mga3
+ Revision: 347631
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Sep 29 2011 fwang <fwang> 1.9.14-15.mga2
+ Revision: 150153
- cleanup br
* Mon Mar 14 2011 andre999 <andre999> 1.9.14-14.mga1
+ Revision: 71363
- imported package cgoban
