Name:			cosmosmash
Version:		1.4.8
Summary:		Clone of the Intellivision(TM) game Astrosmash(TM)
License:		GPLv2
URL:			http://sarrazip.com/dev/%{name}.html
Group:			Amusements/Games
Release:		1
Source:			%{name}-%{version}.tar.gz
BuildRequires:		desktop-file-utils
BuildRequires:		gcc-c++
BuildRequires:		libtool
BuildRequires:		SDL-devel
BuildRequires:		SDL_image-devel
BuildRequires:		SDL_mixer-devel
BuildRequires:		flatzebra-devel

%description
In this game, you control a base that must destroy rocks before they hit the
ground, or you lose points. You must also prevent "spinners" from touching
the ground, or your base will explode.

%prep
%setup -q

%build
%configure
make %{?jobs:-j%jobs}

%install
make install DESTDIR="$RPM_BUILD_ROOT" INSTALL="%{__install} -p"
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}
rm %{buildroot}/%{_datadir}/applications/*.desktop

cat <<_EOF_ >src/%{name}.desktop
[Desktop Entry]
Type=Application
Name=Cosmosmash
Categories=Game;ArcadeGame;
Comment=A space rock shooting video game
Exec=cosmosmash
Icon=cosmosmash
Terminal=false
_EOF_

install -D -m644 src/%{name}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_datadir}/applications/*%{name}.desktop
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/sounds/%{name}
%{_mandir}/man*/*

%changelog
* Sun Apr 25 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.8
- Rebuilt for Fedora
