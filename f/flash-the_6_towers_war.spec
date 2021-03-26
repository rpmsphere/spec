Summary: The 6 Towers War in Flash
Name: flash-the_6_towers_war
Version: 20110719
Release: 1
License: freeware
Group: Amusements/Games
Source0: http://chat.kongregate.com/gamez/0011/9268/live/ThreeTowersGame6_final.swf
Source1: %{name}.png
URL: http://www.kongregate.com/games/Tuzi82/the-6-towers-war
Requires: oxzilla, flash-plugin
BuildArch: noarch

%description
The 6 Towers War created by Tuzi82.
Select your card units to conquer the enemy's towers!
Click with the mouse to your card units to attack the opponent.
Be faster than your opponent to conquer at least 2 towers!

%prep
%setup -q -T -c

%build

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}

# Install menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%{__cat} > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Flash The 6 Towers War
Comment=The 6 Towers War in Flash
Categories=Game;StrategyGame;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/%{name}.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -s 800x600 ThreeTowersGame6_final.swf
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Fri Sep 02 2011 Wei-Lun Chao <bluebat@member.fsf.org> 20110719
- Initial build
