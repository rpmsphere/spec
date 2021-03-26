%global debug_package %{nil}

Name: xlife
Summary: A cellular-automaton laboratory
Version: 6.7.6
Release: 1
Group: Amusements/Games
License: GPL
URL: http://freecode.com/projects/xlife
Source0: http://litwr2.atspace.eu/xlife/%{name}-%{version}.tar.bz2
Source1: xlife.png
BuildRequires: imake
BuildRequires: libX11-devel
Patch0: xlife-6.7.patch

%description
This program will evolve patterns for John Horton Conway's game of Life.
It will also handle general cellular automata with the orthogonal and
nosymmetry neighborhood and up to 16 states (it's possible to recompile for
more states, but very expensive in memory).  Transition rules and sample
patterns are provided for the 8-state automaton of E. F. Codd, the Wireworld
automaton, and a whole class of `Prisoner's Dilemma' games, and many others.

%prep
%setup -q -n %{name}-6.7
%patch0 -p1 
#sed -i 's|-g -O5||' Imakefile

%build
#xmkmf -a
imake -DUseInstalled -I/usr/share/X11/config
sed -i 's|-D_BSD_SOURCE -D_SVID_SOURCE|-D_DEFAULT_SOURCE|' Makefile
make

cat > %{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=XLife
Comment=A cellular-automaton laboratory
Icon=xlife
Exec=xlife
Type=Application
Terminal=false
Categories=Game;Simulation;
EOF

%install
install -d %{buildroot}%{_bindir}
install -c -m 0755 xlife gen-multirules %{buildroot}%{_bindir}
install -c -m 0755 table2r.script %{buildroot}%{_bindir}/table2r
install -d %{buildroot}%{_mandir}/man6
install -c -m 0444 xlife._man %{buildroot}%{_mandir}/man6/xlife.6
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc doc/* changelog.debian changelog.openbsd CHANGES HACKING README SHORT-INFO XLIFE-HISTORY.dot
%{_bindir}/*
%{_mandir}/man6/%{name}.6.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Sep 06 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 6.7.6
- Rebuild for Fedora
