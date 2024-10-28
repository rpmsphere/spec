Name:           pydance
Version:        1.0.3
Release:        1
URL:            https://icculus.org/pyddr/
License:        GNU General Public License (GPL)
Group:          Amusements/Games/Arcade
Summary:        Fun dancing game for experience asian dance beat!
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}-songs.tar.bz2
Source2:        %{name}.desktop
Source3:        %{name}.png
Patch0:         %{name}-%{version}-config.patch
BuildArch:      noarch
#BuildRequires:  SDL-devel SDL_mixer-devel 
Requires:       pygame

%description
pydance is fun dancing game for experience asian dance beat!
Showing friends your hot move with big score! Highly configurable,
colorful animated arrow motion, limitless numbers of dance steps,
1 or 2 players, professionally written music, laughter provoking
sound effects, and yes, even graphical transitions.

%prep
%setup -q -a 1
%patch 0

%build
python2 setup.py

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/games/pydance/songs
cp songs/* $RPM_BUILD_ROOT%{_datadir}/games/pydance/songs

# Install Desktop & Icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/* %{buildroot}%{_datadir}/games/%{name}/%{name}.py

%files
%doc CREDITS HACKING README TODO ChangeLog
%config(noreplace) %{_sysconfdir}/pydance.cfg
%{_bindir}/findbpm
%{_prefix}/games/pydance
%{_datadir}/games/pydance/*
%{_mandir}/man?/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuilt for Fedora
* Tue Oct 21 2008 Feather Mountain <john@ossii.com.tw> - 1.0.3.ossii
- Rebuild for M6(OSSII)
* Wed Jun 20 2007 prusnak@suse.cz
- created package - version 1.0.3
