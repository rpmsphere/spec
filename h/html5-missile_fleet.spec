Summary: Missile Fleet in HTML5
Name: html5-missile_fleet
Version: 20090126
Release: 1
License: freeware
Group: Amusements/Games
Source0: %{name}.zip
URL: http://glimr.rubyforge.org/cake/missile_fleet.html
Requires: oxzilla
BuildArch: noarch

%description
Missile Fleet was one of the first games on the web to take advantage
of HTML5's canvas technology. You are in charge of the red team in this
space strategy game and your task is to destroy the blue team.
Select multiple units using your mouse, and click where you want them to go.

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
Name=HTML5 Missile Fleet
Comment=Space game in HTML5
Categories=Game;ArcadeGame;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/fhtrbgtile.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -s 980x640 missile_fleet.html
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
* Mon Sep 27 2010 Wei-Lun Chao <bluebat@member.fsf.org> 20090126-1
- Initial build
