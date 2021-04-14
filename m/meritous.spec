%undefine _debugsource_packages

Name: meritous
Version: 1.2
Release: 6.4
Summary: Action-adventure dungeon crawl game
License: GPLv3
Group: Games/Adventure
Source: http://www.asceai.net/files/meritous_v12_src.tar.bz2
Source1: %name.sh
URL: http://www.asceai.net/meritous/
BuildRequires: SDL-devel SDL_image-devel SDL_mixer-devel zlib-devel

%description
Far below the surface of the planet is a secret.
A place of limitless power. Those that seek to
control such a utopia will soon bring an end
to themselves.

Seeking an end to the troubles that plague him,
PSI user MERIT journeys into the hallowed Orcus
Dome in search of answers.

%prep
%setup -n meritous_v12_src
find . -type f \( -name \*.txt -o -name \*.c -o -name \*.h \) -exec sed -i 's/
//' {} \;
sed -i 's/ -lz/ -lz -lm/' Makefile

%build
make

%install
install -Ds %name %buildroot%_bindir/%name.bin
install -D %SOURCE1 %buildroot%_bindir/%name
mkdir -p %buildroot%_datadir/%name
cp -a dat %buildroot%_datadir/%name/

%files
%doc readme.txt
%_datadir/%name/*
%_bindir/*

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
* Mon May 28 2012 Fr. Br. George <george@altlinux.ru> 1.2-alt2
- DSO list completion
* Thu Dec 04 2008 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Initial build from scratch
