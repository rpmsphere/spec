Summary: Fast action game in HTML5
Name: html5-3bored
Version: 20110223
Release: 1
License: freeware
Group: Amusements/Games
Source0: %{name}.zip
URL: http://upsidedownturtle.com/boredboredbored/
Requires: oxzilla
BuildArch: noarch

%description
3Bored is one of the fastest actions games we have played in a browser.
You play the part of a little rocket-propelled creature under attack
from a whole host of enemies. You dart around the screen like a maniac
trying to avoid the bullets that are criss-crossing all around you.
The longer you avoid dying, the more points you get in this fun and
addictive survival game.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

# Install menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%{__cat} > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=HTML5 3Bored
Comment=Fast action game in HTML5
Categories=Game;ArcadeGame;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/help/images/healthy.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -s 640x480 index.html
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
- Rebuilt for Fedora
* Fri Sep 24 2010 Wei-Lun Chao <bluebat@member.fsf.org> 20091014-1
- Initial build
