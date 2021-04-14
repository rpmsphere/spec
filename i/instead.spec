%undefine _debugsource_packages

Name:		instead
Version:	1.9.0
Release:	10.4
Summary:	Simply text adventures/visual novels engine and game
License:	GPLv2
Group:		Games/Adventure
URL:		http://instead.googlecode.com
Source0:	http://instead.googlecode.com/files/%{name}_%{version}.tar.gz
Patch0:		instead-desktop.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(zlib)
Requires:	instead-launcher

%description
Simply text adventures/visual novels engine and game.
It was designed to interpret games that are the mix of visual novels,
text quests and classical 90'ss quests.

%prep
%setup -q
%patch0 -p1
#sed -i 's|Mix_LoadMUS_RW(mus->rw);|Mix_LoadMUS_RW(mus->rw,0);|' src/sdl-instead/sound.c

%build
rpm -e SDL2-devel --nodeps||:
echo 2 | ./configure.sh
make PREFIX=/usr

%install
%make_install PREFIX=/usr

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/doc/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/*/%{name}.*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.0
- Rebuilt for Fedora
