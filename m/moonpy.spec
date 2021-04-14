Name:           moonpy
Version:        0.8.21
Release:        1
Summary:        Open-source remake of Moonbase Commander
Group:          Game/StrategyGame
License:        GPLv3
URL:		http://code.google.com/p/tether/
Source0:        http://code.google.com/p/tether/%{name}-%{version}-package-source.tar.gz
Requires:	pygame, python-twisted
BuildArch:	noarch

%description
MoonPy is an open-source remake of the classic strategy game Moonbase Commander.
A multiplayer turn-based game. On their turn the player can spend energy points
by attacking their opponents and/or adding more buildings to their base.
Turns continue until all players either pass or run out of energy. The round
then ends, players regain energy, and continue taking turns. All buildings are
ground-based and are attached by a tether to the building that created them.
All units need to be "launched" similar to many artillery games though in a
top-down perspective.

%prep
%setup -q -c
sed -i 's|Exec=/usr/local/games/moonpy/run_moonpy.sh|Exec=moonpy|' moonpy.desktop
sed -i 's|local/games|share|' run_moonpy.sh moonpy.desktop

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dm 755 run_moonpy.sh $RPM_BUILD_ROOT%{_bindir}/moonpy
%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__cp} -rf moon.py client/ common/ data/ server/ $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__install} -Dm 644 moonpy.desktop $RPM_BUILD_ROOT%{_datadir}/applications/moonpy.desktop

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/moonpy/moon.py

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 13 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.21
- Rebuilt for Fedora
* Mon May 28 2012 David Hung <david@ossii.com.tw> 0.8.21
- first
