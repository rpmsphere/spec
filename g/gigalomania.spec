%undefine _debugsource_packages

Name: gigalomania
Summary: A 2D real time strategy game clone of Mega-Lo-Mania
Version: 0.26
Release: 11.4
Group: Amusements/Games
License: GPLv2+
URL: https://homepage.ntlworld.com/mark.harman/comp_gigalomania.html
Source0: https://launchpad.net/gigalomania/trunk/%{version}/+download/%{name}src.zip
BuildRequires: SDL-devel
BuildRequires: SDL_mixer-devel
BuildRequires: SDL_image-devel

%description
Gigalomania is an open source 2D Real Time Strategy god game, available for
all popular desktop and mobile platforms, on PCs, tablets and phones. The
gameplay consists of researching and developing new technology with which to
conquer your enemies, from rocks and sticks to nuclear weapons and spaceships.
You can advance through ten different ages, from the stone age to the future.
There are 28 different maps to play through.

%prep
%setup -q -n %{name}src
sed -i 's|/opt|%{_datadir}|' Makefile
sed -i 's|this_h = abs|this_h = std::abs|' image.cpp

%build
make

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/pixmaps
%make_install
mv %{buildroot}%{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}
rm %{buildroot}%{_datadir}/applications/%{name}_fullscreen.desktop
sed -i 's|^Categories=Game;|Categories=Game;StrategyGame;|' %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}64.png

%changelog
* Wed Jan 15 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.26
- Rebuilt for Fedora
