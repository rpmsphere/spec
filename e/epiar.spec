Name:           epiar
Version:        0.5.0
Release:        1
Summary:        A space trading/exploring arcade game
Group:          Amusements/Games
License:        GPLv2+
URL:            https://epiar.net/
Source0:        https://epiar.net/files/epiar/releases/0.5.0/%{name}-%{version}.tar.bz2
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  libxml2-devel
BuildRequires:  ftgl-devel
BuildRequires:  physfs-devel

%description
Epiar (ep-ee-are) is a space trading/exploring arcade simulation game
in which the player navigates space from planet to planet, saving
money to buy ship upgrades and new ships. The player can also join
mercenary missions, attack other ships to steal their money and
technology, and explore the universe.

%prep
%setup -q
sed -i 's|-Wall|-Wall -fPIC|' Source/Lua/src/Makefile

%build
autoreconf -ifv
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --vendor "" --delete-original      \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
        %{_builddir}/%{name}-%{version}/%{name}.desktop

%files
%doc COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuilt for Fedora
* Mon May 21 2012 Tony Lo <tony.lo@ossii.com.tw> 0.5.0
- ox2 version 0.5.0.
* Mon May 16 2011 Christopher Thielen <chris@epiar.net> 0.5.0
- Initial creation using Epiar version 0.5.0.
