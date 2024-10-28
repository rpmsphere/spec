Name:                   afternoonstalker
Version:                1.1.6
Summary:                A Night Stalker(TM) clone
License:                GPLv2
URL:                    https://sarrazip.com/dev/%{name}.html
Group:                  Amusements/Games
Release:                1
Source0:                %{name}-%{version}.tar.gz
BuildRequires:          desktop-file-utils
BuildRequires:          gcc-c++
BuildRequires:          libtool
BuildRequires:          SDL-devel
BuildRequires:          SDL_image-devel
BuildRequires:          SDL_mixer-devel
BuildRequires:          flatzebra-devel

%description
Clone of the Intellivision game Night Stalker.  You are in a
two-dimensional maze in which you are attacked by robots that
shoot at you and that you must shoot down.  You must pick up a
gun somewhere in the maze in order to have a few bullets to shoot.
Avoid the spiders and the bats, which can paralyze you long enough
for a robot to come and shoot you.  The bunker in the center is
your only protection.

%prep
%setup -q

%build
#export CFLAGS="-std=gnu++11"
%configure
%{__make} %{?jobs:-j%jobs}

%install
make install DESTDIR="$RPM_BUILD_ROOT" INSTALL="%{__install} -p"
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
rm $RPM_BUILD_ROOT/%{_datadir}/applications/*.desktop

cat <<_EOF_ >src/%{name}.desktop
[Desktop Entry]
Type=Application
Name=Afternoon Stalker
Categories=Game;ArcadeGame;
Comment=A robot-killing game
Exec=afternoonstalker
Icon=afternoonstalker
Terminal=false
_EOF_

install -D -m644 src/%{name}.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_datadir}/applications/*%{name}.desktop
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/sounds/%{name}
%{_mandir}/man*/*

%changelog
* Sun Apr 25 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.6
- Rebuilt for Fedora
