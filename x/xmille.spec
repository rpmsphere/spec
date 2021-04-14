%undefine _debugsource_packages

Name:		xmille
Version:	2.0
Release:	7.1
Summary:	Mille bournes game
Group:		Games
License:	Public Domain
URL:		ftp://ftp.x.org/R5contrib/%{name}.tar.Z
Source0:	ftp://ftp.x.org/R5contrib/%{name}.tar.Z
Source1:    xmille.png
Patch0:		xmille_2.0-13.diff.bz2
BuildRequires:	libXext-devel libX11-devel imake

%description
The classic game of Mille Bournes (or Mille Bornes).
A card game against the computer in which each player tries to reach 1000
miles. Each player tries to avoid accidents, flat tires, running out of
gas, and break downs while trying to cause these same maladies in the
opponent.

%prep
%setup -q -c
%patch0 -p0

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 755 xmille $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm 644 %{name}.man $RPM_BUILD_ROOT%{_datadir}/man/man6/%{name}.6
install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=XMille
Comment=Mille Bournes
GenericName=Mille Bournes Card Game
Name[fr]=xmille
Comment[fr]=Mille Bornes
GenericName[fr]=Jeux des Mille Bornes
Icon=xmille
Type=Application
Exec=xmille
Terminal=false
Categories=Game;CardGame;
EOF

%files
%doc README COPYRIGHT CHANGES
%{_bindir}/%{name}
%{_datadir}/man/man6/%{name}.6.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Sep 29 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
* Wed Oct 29 2008 Jean-Christophe Cardot <plf@cardot.net> 2.0-1jcc
- release based on Debian's xmille2.0-13
