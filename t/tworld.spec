Name: tworld
Summary: Chip's Challenge Game Engine Emulation
Version: 1.3.2
Release: 1
License: GPL
Group: games
URL: http://www.muppetlabs.com/~breadbox/software/tworld/
Source0: http://www.muppetlabs.com/~breadbox/pub/software/%{name}/%{name}-%{version}-CCLPs.tar.gz
Source1: %{name}.xpm
BuildRequires: SDL-devel

%description
Tile World is an emulation of the game "Chip's Challenge".  "Chip's
Challenge" was originally written for the Atari Lynx by Chuck Sommerville,
and was later ported to MS Windows by Microsoft (among other ports).

Please note: Tile World is an emulation of the game engine(s) only.  It does
not come with the chips.dat file that contains the original level set.  This
file is copyrighted and cannot be freely distributed.  The chips.dat file
was originally part of the MS version of "Chip's Challenge".  If you have a
copy of this version of the game, you can use that file to play the game in
Tile World.  If you do not have a copy of this file, however, you can still
play Tile World with the many freely available level sets created by fans of
the original game, including CCLP2.  Because the version that Microsoft
released introduced a number of changes to the rules of the game, Tile World
is capable of emulating either the MS version or the original Atari Lynx
version of the game.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
sed -i -e 's|^sharedir = .*|sharedir = %{buildroot}%{_datadir}/%{name}|' -e 's|^bindir = .*|bindir = %{buildroot}%{_bindir}|' -e 's|^mandir = .*|mandir = %{buildroot}%{_mandir}|' Makefile
make install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Tile World
Icon=tworld
Exec=tworld
Categories=Game;LogicGame;
EOF

%files
%doc README COPYING BUGS Changelog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6*
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Thu Jun 15 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.2
- Rebuilt for Fedora
