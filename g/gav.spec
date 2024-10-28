%undefine _debugsource_packages
Name: gav
Version: 0.9.0
Release: 1
Summary: GPL rendition of old Arcade Volleyball game
URL: https://gav.sourceforge.net
Source0: %{name}-%{version}.tar.bz2
Source1: %{name}-themes-0.7.3.tar.bz2
Source2: gav.desktop
License: GPL
Group: Amusements/Games
BuildRequires: SDL-devel SDL_image-devel SDL_net-devel

%description
An SDL-based rendition of an old favorite CGA game featuring
two characters playing a volleyball-like game. This "revamped"
version is supposed to support theming, multiplayer games,
different input devices and networking.

%prep
%setup -q -b1
sed -i 's|share/games|share|' Makefile* Theme.h
sed -i '1i #include <cstring>' aarg.h
./build_linux.sh

%build
make depend
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -d $RPM_BUILD_ROOT/usr/bin
install gav $RPM_BUILD_ROOT/usr/bin/
install -d $RPM_BUILD_ROOT/usr/share/gav/themes/classic
install -d $RPM_BUILD_ROOT/usr/share/gav/sounds
install -d $RPM_BUILD_ROOT/usr/share/doc/gav-%{version}
install -d $RPM_BUILD_ROOT/usr/share/applications
install -d $RPM_BUILD_ROOT/usr/share/pixmaps
install %{SOURCE2} $RPM_BUILD_ROOT/usr/share/applications
install package/gav.png $RPM_BUILD_ROOT/usr/share/pixmaps
cp ../themes/yisus/* $RPM_BUILD_ROOT/usr/share/gav/themes/classic
rm -rf ../themes/yisus
cp -a sounds $RPM_BUILD_ROOT/usr/share/gav/

pushd ../themes
cp -a * $RPM_BUILD_ROOT/usr/share/gav/themes
popd

%files
%doc README CHANGELOG LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Rebuilt for Fedora
* Thu Apr 19 2007 kde <athena_star {at} 163 {dot} com> - 0.9.0-3mgc
- fix a typo in the spec file
* Thu Apr 19 2007 kde <athena_star {at} 163 {dot} com> - 0.9.0-2mgc
- add chinese translation for the spec file
* Thu Apr 19 2007 kde <athena_star {at} 163 {dot} com> - 0.9.0-1mgc
- port to Magic Linux
* Fri Apr 2 2004 Alessandro Tommasi <ale@ctrl-z-bg.org>
- Major Changes
