%global _name mars
%undefine _debugsource_packages

Summary:        Mars, Land Of No Mercy
Name:           marsnomercy
Version:        0.2.1
Release:        1
License:        GPL
Group:          Amusements/Games/Strategy/Turn Based
URL:            https://www.marsnomercy.org/
BuildRequires:  gcc-c++ SDL-devel SDL_image-devel SDL_ttf-devel
BuildRequires:  python2-scons <= 3.0.1
BuildRequires:  mesa-libGL-devel
BuildRequires:  SDL_mixer-devel
Source0:        %{_name}-%{version}-src.tar.gz
Source1:        %{_name}.png

%description
Mars, Land of No Mercy is a turn-based strategy game setting on Mars
during the early stages of human colonization.
The player embodies the leader of a mercenary team, 
landed on Mars to take advantage of conqueror battles 
between the Worldwide Colonizer Corporations.
The main purpose is to command his team trying to find them 
commissions, training and leading them in battle, while still 
being aware of financial and instrumental resources by administering them.
The Mech is the fundamental craft used by mercenaries, 
but they won't lack of other kind of units, as well as troops.

%prep
%setup -q -n %{_name}-%{version}

%build
scons

%install
install -D -m 755 mars %{buildroot}%{_bindir}/%{name}.bin
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/%{_name}
cp -a data %{buildroot}%{_datadir}/%{_name}
# adding shell script to start Mars, Land of No Mercy.
# if Mars is not started in the directory, where the data files reside
# it dropes either an error by itself or a SIG11
cat <<EOF > %{buildroot}%{_bindir}/%{name}
#!/bin/sh
cd %{_datadir}/%{_name}
%{_bindir}/%{name}.bin
EOF
chmod 0755 %{buildroot}%{_bindir}/%{name}

# Creating the Start Menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat <<EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Name=Mars, Land of No Mercy
Name[zh_TW]=火星殖民
Type=Application
GenericName=Strategy Game
Exec=%{name}
Icon=%{name}.png
Path=
Terminal=false
Categories=Game;StrategyGame;Game
EOF
chmod 644 %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_bindir}/%{name}.bin
%{_datadir}/%{_name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1
- Rebuilt for Fedora
* Mon Oct 20 2008 - john@ossii.com.tw
- Rebuild for M6(OSSII)
* Fri Dec 29 2006 - dominique-rpm@leuenberger.net
- Added MESA to BuildRequires for the GL Driver
* Mon Dec 25 2006 - dominique-rpm@leuenberger.net
- Update to version 0.2.1
* Fri Nov 10 2006 - dominique-rpm@leuenberger.net
- changed the startup shell script name to mars and 
- the bin file to mars.bin
* Wed Nov 09 2006 - dominique-rpm@leuenberger.net
- added shell script mars.run to start the game from all the directories.
- added Startmenu entry (mars.desktop)
* Tue Nov 08 2006 - dominique-rpm@leuenberger.net
- fixed SPEC File for support on SuSE Linux 9.3
* Mon Nov 07 2006 - dominique-rpm@leuenberger.net
- Initial SPEC File for release 0.2.0
- The game is in a very early stage of development.
- Not to much working yet.
- Start not yet able through menu, but only by:
- cd /usr/share/games/mars; mars
