%undefine _debugsource_packages

Summary: The Fruitloving Snake
Name: snake4
Version: 1.0.14
Release: 1
URL: https://shh.thathost.com/pub-unix/html/snake4.html
License: Free Software
Group: Games
Source0: https://shh.thathost.com/pub-unix/files/snake4-1.0.14.tar.gz
Source1: https://shh.thathost.com/pub-unix/files/shhmsg-1.4.2.tar.gz
Source2: https://shh.thathost.com/pub-unix/files/shhopt-1.1.7.tar.gz

%description
Steer this fruitloving snake around the screen, and pick up fruit.
The snake grows in length as it eats. Watch out for lethal mushrooms,
rotten fruit, and evil headbangers. Features a site-wide highscore file
for fun and excitement.

This package includes:
shhmsg - library for displaying messages
shhopt - library for parsing command line options

%prep
%setup -q -a 1 -a 2
sed -i -e 's|-I/local/include|-fPIE -I.|' -e 's|-L/local/lib|-L.|' -e 's|/var/local/lib/games|/etc|' Makefile
sed -i 's|-Wall|-fPIE -Wall|' */Makefile

%build
make -C shhmsg-1.4.2
mv shhmsg-1.4.2/{libshhmsg.a,shhmsg.h} .
make -C shhopt-1.1.7
mv shhopt-1.1.7/{libshhopt.a,shhopt.h} .
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
ln -s %{name} %{buildroot}%{_bindir}/%{name}scores
install -Dm644 %{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6
#install -Dm644 %{name}.score %{buildroot}/etc/%{name}.score

%files
%doc ChangeLog README.md TODO
%{_bindir}/%{name}*
%{_mandir}/man?/*
#config /etc/%{name}.score

%changelog
* Sat Jan 18 2025 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.14
- Rebuilt for Fedora
