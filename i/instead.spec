Name:		instead
Version:	3.4.1
Release:	1
Summary:	Simply text adventures/visual novels engine and game
License:	GPLv2
Group:		Games/Adventure
URL:		https://github.com/instead-hub/instead
Source0:	https://github.com/instead-hub/instead/releases/download/%{version}/%{name}_%{version}.tar.gz
Patch0:		instead-desktop.patch
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(zlib)
BuildRequires: SDL2-devel

%description
Simply text adventures/visual novels engine and game.
It was designed to interpret games that are the mix of visual novels,
text quests and classical 90'ss quests.

%prep
%setup -q

%build
echo -e "2\n/usr" | ./configure.sh
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
* Sun Jun 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.4.1
- Rebuilt for Fedora
