Name: gnchess
Summary: A Chinese Chess Game
Version: 1.0
Release: 12.3
Group: Amusements/Games
URL: http://code.google.com/p/gnchess/
Source0: http://gnchess.googlecode.com/files/%{name}-%{version}.tar.gz
License: GPLv2
BuildRequires: thorlib-devel, gtkmm24-devel, librsvg2-devel

%description
Gnchess is a simple chinese chess game.

%prep
%setup -q
rename cnchess gnchess cnchess.desktop po/zh_CN/cnchess.po
sed -i 's|cnchess|gnchess|g' gnchess.desktop po/zh_CN/gnchess.po engine.cc Makefile po/zh_CN/Makefile ui.cc
sed -i 's|Game;|Game;BoardGame;|' gnchess.desktop
sed -i 's|-Wall|-Wall -std=gnu++11 -Wno-narrowing|' Makefile

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
