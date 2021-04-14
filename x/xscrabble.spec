%undefine _debugsource_packages

Name:         xscrabble
Summary:      X version of the popular board game
Group:        Amusements/Games
License:      GPL
Version:      2.10
Release:      17.1
URL:          ftp://ftp.ac-grenoble.fr/ge/educational_games
Source0:      %{name}-%{version}.tar.bz2
Source1:      %{name}_en.tgz
Source2:      %{name}_fr.tgz
Source10:	scrabble-48.png
Patch:        %{name}-%{version}.patch
BuildRequires:    imake
BuildRequires:    libX11-devel
BuildRequires:    libXt-devel
BuildRequires:    libXmu-devel
BuildRequires:    libXaw-devel

%description
X version of the popular board game, for 1 to 4 players.

%prep
%setup -q -a1 -a2
%patch

%build
export IMAKEINCLUDE=-I/usr/share/X11/config
./build bin

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT ./build install
DESTDIR=$RPM_BUILD_ROOT ./build lang fr 
DESTDIR=$RPM_BUILD_ROOT ./build lang en

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 644 %SOURCE10 %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}/%_bindir
mv %{buildroot}/usr/games/xscrab %{buildroot}%_bindir/xscrab
mv %{buildroot}/usr/games/xscrabble %{buildroot}%_bindir/xscrabble
mv %{buildroot}/usr/X11R6/lib/X11 %{buildroot}%_datadir/X11
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=XScrabble
Comment=A popular board gamer
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGES LICENSE README
%_bindir/xscrab
%_bindir/xscrabble
%_datadir/games/scrabble/
%_datadir/X11/app-defaults/*
%config(noreplace) %attr(664,games,games) /var/games/scrabble*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Apr 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.10
- Rebuilt for Fedora
* Mon Apr 02 2012 Neal <nealbrks0 at gmail dot com> 2.1.0-1pclos2012
- 64bit build
* Wed Jan 06 2010 Texstar <texstar at gmail.com> 2.1.0-3pclos2010
- rebuild
* Sun Jun 24 2007 Texstar <texstar@gmail.com> 2.1.0-2pclos2007
- Fix Synaptic Section geesh
* Sat Jun 23 2007 Texstar <texstar@houston.rr.com> 2.1.0-1pclos2007
- import into pclos
