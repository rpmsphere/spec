Name:           instead-launcher
Version:        0.6.1
Release:        7.1
License:        GPL-2.0
Summary:        Game update/install/launch program for Instead
URL:            http://instead-launcher.googlecode.com
Group:          Amusements/Games/Other
Source0:        https://instead-launcher.googlecode.com/files/%{name}_%{version}.tar.gz
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

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/applications/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuild for Fedora
* Thu Jul  5 2012 devel.openSUSE.org@gmail.com
- Initial package creation - version 0.6.1
