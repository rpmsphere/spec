%undefine _auto_set_build_flags

Summary:        A Bust-A-Move/Puzzle Bubble clone
Name:           xbubble
Version:        0.5.11.2
Release:        17.1
URL:		https://alioth.debian.org/projects/xbubble/
Source0:	https://alioth.debian.org/frs/download.php/file/1582/%{name}-%{version}.tar.gz
License:	GPL
Group:          Games/Arcade
BuildRequires:  libX11-devel, libpng-devel, libpng12-devel

%description
XBubble is an X Window based clone of the famous arcade game
Bust-A-Move/Puzzle Bubble. You can play it alone, against an opponent,
or even against the computer. It has nice scalable and customizable
graphics.

%prep
%setup -q
sed -i 's|<png\.h>|<libpng12/png.h>|' src/loadpng.c
sed -i 's|1\.9|1.16|g' bootstrap

%build
./bootstrap --datadir=/usr/share
./configure --prefix=/usr --build=x86_64
sed -i -e 's|-lpng|-lpng12|' -e 's|-Werror||' src/Makefile
sed -i -e 's|$(SHELL)||' -e 's|@MKINSTALLDIRS@|mkdir -p|' po/Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_bindir}/*
%{_datadir}/*

%changelog
* Tue Jan 16 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.11.2
- Rebuilt for Fedora
* Thu May 15 2003 chl <chl@tuxfamily.org> 20030515-1mdk
- first release from cvs
