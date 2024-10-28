%undefine _debugsource_packages

BuildRequires:  pkgconfig
BuildRequires:  SDL-devel       >= 1.2.4
BuildRequires:  SDL_image-devel >= 1.2.2
BuildRequires:  SDL_mixer-devel >= 1.2.4
BuildRequires:  libX11-devel
Name:                   vectoroids
Version:                1.1.0
Summary:                A clone of the classic "Asteroids" arcade game
License:                GPLv2
URL:                    https://www.newbreedsoftware.com/vectoroids/
Group:                  Amusements/Games/Action/Arcade
Release:                8.4
Source:                 %{name}-%{version}.tar.bz2
BuildRequires:  desktop-file-utils

%description
"Vectoroids" is a clone of the classic arcade game "Asteroids" by Atari.

Your objective is to maneuver a space ship within a field of asteroids,
and shoot them into smaller and smaller pieces, eventually destroying them
completely.

Vectoroids is based directly on the code for Agendaroids. It has been ported
from X-Window to SDL, so it runs on numerous platforms.

Vectoroids includes music, sound effects, and lots of cool color vector
graphics!

%prep
%setup -q
sed -e "s:PREFIX=/usr/local:PREFIX=%{_prefix}:g" -i Makefile

%build
%{__make} %{?jobs:-j%jobs}

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/images
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/sounds
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/music
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man6
install -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -m 644 %{name}.6 $RPM_BUILD_ROOT/%{_mandir}/man6/
install -m 644 data/images/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/images/
install -m 644 data/sounds/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/sounds/
install -m 644 data/music/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/music/

%files
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/%{name}
%doc CHANGES.txt COPYING.txt README.txt

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuilt for Fedora
