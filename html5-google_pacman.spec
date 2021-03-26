Summary: Pacman in HTML5
Name: html5-google_pacman
Version: 20100522
Release: 2
License: commercial
Group: Amusements/Games
Source0: google-pacman.zip
Source1: google-pacman.png
Requires: mongoose, oxzilla, flash-plugin
BuildArch: noarch

%description
May 22nd marked the 30th anniversary of the popular arcade game Pac-Man.
To celebrate this occasion, Google decided to create a playable version
of the classic arcade game as its Doodle of the day.

%prep
%setup -q -n google-pacman

%build

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a %{SOURCE1} * $RPM_BUILD_ROOT%{_datadir}/%{name}

# Install menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%{__cat} > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=HTML5 Pacman
Comment=Google Pacman in HTML5
Categories=Game;ArcadeGame;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/google-pacman.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
_PORT=\$((\$RANDOM%16384+49152))
mongoose -p \$_PORT &
sleep 1
oxzilla -r -s 600x420 http://127.0.0.1:\$_PORT/index.html
pkill -P \$\$ mongoose
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
* Mon Jun 20 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Initial build
