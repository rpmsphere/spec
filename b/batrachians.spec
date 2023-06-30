Name:			batrachians
Version:		0.1.7
Summary:		A Frog Bog(TM) clone
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
Batrachians is a game where you control a frog and your goal is to
eat more flies and score more points than the computer's frog.
This is a clone of the 1982 Frog Bog video game by Mattel Electronics.

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
Name=Batrachians
Categories=Game;ArcadeGame;
Comment=A fly-eating frog game
Exec=batrachians
Icon=batrachians
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
* Sun Apr 25 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.7
- Rebuilt for Fedora
