Name:           instead-launcher
Version:        0.7.0
Release:        1
License:        GPL-2.0
Summary:        Game update/install/launch program for Instead
URL:            https://github.com/instead-hub/instead-launcher
Group:          Amusements/Games/Other
Source0:        https://github.com/instead-hub/instead-launcher/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  qt4-devel
BuildRequires:  zlib-devel
Requires:       instead

%description
Instead-launcher provides GUI for simple installing, updating and launching of
Instead games.

%prep
%setup -q

%build
qmake-qt4 QMAKE_CFLAGS="%{optflags}" QMAKE_CXXFLAGS="%{optflags}" PREFIX=/usr
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}/ %{buildroot}%{_datadir}/applications/

install -m 755 %{name} %{buildroot}%{_bindir}/
install -m 644 -p %{name}.desktop %{buildroot}%{_datadir}/applications/

#fix desktop file
sed -i 's|Icon=sdl_instead.png|Icon=sdl_instead|' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's|Version=0.6.1|Version=1.0|' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's|Categories=Game;|Categories=Game;AdventureGame;|' %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/*
%{_datadir}/applications/*

%changelog
* Sun Jun 26 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.0
- Rebuilt for Fedora
* Thu Jul  5 2012 devel.openSUSE.org@gmail.com
- Initial package creation - version 0.6.1
