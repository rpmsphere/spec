%global __os_install_post %{nil}

Name:			burgerspace
Version:		1.9.5
Summary:		A Burgertime(TM) clone
License:		GPLv2
URL:			https://sarrazip.com/dev/%{name}.html
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
BurgerSpace is a game in which you are a chef, and must walk over
hamburger ingredients (buns, meat, lettuce, etc) to make them fall from
floor to floor, until they end up on the plates at the bottom of the
screen. It requires the SDL multimedia library. It is a clone of the
1982 BurgerTime video game by Bally Midway.

%prep
%setup -q

%build
%configure
%{__make} %{?jobs:-j%jobs}

%install
make install DESTDIR="$RPM_BUILD_ROOT" INSTALL="%{__install} -p"
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}
rm %{buildroot}/%{_datadir}/applications/*.desktop

cat <<_EOF_ >src/%{name}.desktop
[Desktop Entry]
Type=Application
Name=BurgerSpace
Categories=Game;ArcadeGame;
Comment=A hamburger-smashing video game
Exec=burgerspace
Icon=burgerspace
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
%{_datadir}/%{name}
%{_mandir}/man*/*

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.5
- Rebuilt for Fedora
