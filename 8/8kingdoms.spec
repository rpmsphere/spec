Name:			8kingdoms
Summary:		A 3D turn-based fantasy strategic game
URL:			http://kralovstvi.sourceforge.net/
Group:			Amusements/Games/Strategy/Turn Based
Version:		1.1.0
Release:		17.4
License:		GPL
BuildRequires:	expat-devel
BuildRequires:	gcc-c++
BuildRequires:	mesa-libGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	tcl-devel
BuildRequires:	desktop-file-utils
Source0:		8Kingdoms-%{version}.tar.gz
Source1:		%{name}.png
Patch0:         8Kingdoms-1.1.0-64bit.patch
Patch1:			8Kingdoms-1.1.0-gcc43.patch
Patch2:			8Kingdoms-tcl85.patch
Patch3:                 8Kingdoms-printf.patch

%description
8 Kingdoms is a 3D turn-based fantasy strategic game in which
players become kings, build their empires and conquer enemy
kingdoms.

Theme of the game 8 Kingdoms is inspirated by the world of fantasy.
Players play on a fully 3D hex map. They construct buildings,
recruit units including infantry, mounted units, mages, catapults
and finally they attack enemy or help allies. Units gain experiences
during the battle, each unit can get some abilities upgraded to be
stronger. Data are stored in XML and freely accessible - from
language versions to units' attributes, moreover map editor with
random map generator is included for comfortable map editing.

%prep
%setup -q -n 8Kingdoms-%{version}
%patch0 -p1
%patch1 -p1
%patch2
%patch3 -p1
autoreconf -fi
%__chmod -x doc/gui/gui_img1.png

%build
# configure won't recognize --datadir ...
%__sed -i 's|games/8Kingdoms|share/8Kingdoms|g' configure
%configure --datadir=%{_datadir}/%{name}
%__sed -i 's|-Werror=format-security|-Wno-error -ansi|g' Makefile
%__make %{?jobs:-j%{jobs}} pkgdatadir=%{_datadir}/%{name}

%install
%__rm -rf %{buildroot}
%makeinstall pkgdatadir=${RPM_BUILD_ROOT}%{_datadir}/%{name}

# icon
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps

#Desktop
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF

[Desktop Entry]
Encoding=UTF-8
Name=%{name}
Comment=8 Kingdoms is a 3D turn-based fantasy strategic game
Type=Application
Exec=8Kingdoms
Icon=%{name}
Categories=Game;StrategyGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYING README doc/*
%{_bindir}/8Kingdoms
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Jul 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuilt for Fedora
* Mon Nov 26 2007 Toni Graffy <toni@links2linux.de> - 1.1.0-0.pm.2
- added 64bit patch from Hans de Goede <j.w.r.degoede@hhs.nl>
* Fri Aug 10 2007 Toni Graffy <toni@links2linux.de> - 1.1.0-0.pm.1
- initial build 1.1.0
