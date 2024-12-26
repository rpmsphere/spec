%global __os_install_post %{nil}
%undefine _debugsource_packages

Name:                   quadrupleback
Version:                0.2.0
Summary:                A clone of the 1982 Doubleback(TM)
License:                GPLv2
URL:                    https://sarrazip.com/dev/%{name}.html
Group:                  Amusements/Games
Release:                1
Source:                 %{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  flatzebra-devel

%description
This is the home page for Quadrupleback, a video game where intruders must be
circled. It is a clone of the 1982 Doubleback game by Dale Lear for the Tandy
Color Computer.

%prep
%setup -q

%build
autoreconf -ifv
#sed -i '16128,16171d' configure
#sed -i '17129,17160d' configure
./configure --prefix=/usr
sed -i 's|-D_REENTRANT|-D_REENTRANT -fPIE|' Makefile src/Makefile
%{__make} %{?jobs:-j%jobs}

%install
make install DESTDIR="$RPM_BUILD_ROOT" INSTALL="%{__install} -p"
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}
rm %{buildroot}/%{_datadir}/applications/*.desktop

cat <<_EOF_ >src/%{name}.desktop
[Desktop Entry]
Type=Application
Name=Quadrupleback
Categories=Game;ArcadeGame;
Comment=A clone of the 1982 Doubleback
Exec=quadrupleback
Icon=quadrupleback
Terminal=false
_EOF_

install -D -m644 src/%{name}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_datadir}/applications/*%{name}.desktop
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/sounds/%{name}
%{_datadir}/%{name}

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
