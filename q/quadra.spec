Summary:	Multiplayer puzzle game
Name:		quadra
Version:	1.2.0
Release:	10.1
License:	LGPLv2+
Group:		Games/Arcade
URL:		http://code.google.com/p/quadra/
Source0:	http://quadra.googlecode.com/files/%{name}-%{version}.tar.gz
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
# fix str fmt, patch sent upstream 08 Jun 2009
Patch0:	%{name}-1.2.0-fix-str-fmt.patch
BuildRequires:	bc
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(libpng)

%description
This is the official release %{version} of Quadra, a full-featured
multiplayer action puzzle game for the X Window System and Svgalib.
Features include:
 - Recursive block chaining
 - Blocks shadows
 - Teams playing
 - TCP/IP networking (free Internet playing! Supports SOCKS proxies)
 - Smooth block falling
 - Sound effects
 - Watches on other players
 - Chat window
 - CD-based music
 - And much more!

%prep
%setup -q
%patch0 -p1

cat << EOF > %{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Quadra
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%build
sed -i 's|/games||' server/qserv.pl config/config.* packages/*.in
./configure --prefix=/usr
make

%install
%make_install
install -D -m644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m644 %SOURCE5 %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -D -m644 %SOURCE6 %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m644 %SOURCE7 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files
%doc ChangeLog LICENSE README
%{_bindir}/*
%{_datadir}/quadra.res
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*.png

%changelog
* Thu May 28 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora
* Sun Dec 07 2014 Bernhard Rosenkraenzer <bero@bero.eu> 1.2.0-14
+ Revision: 3afc8d3
- MassBuild#609: Increase release tag
