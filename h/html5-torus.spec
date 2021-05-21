Summary: Torus in HTML5
Name: html5-torus
Version: 20081126
Release: 1
License: freeware
Group: Amusements/Games
Source0: %{name}.zip
URL: http://www.benjoffe.com/code/games/torus/
Requires: oxzilla
BuildArch: noarch

%description
This variation of Tetris seen in the Torus is actually worth a second look.
The game is also the perfect showcase of the 3d capabilities of HTML5.

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
Name=HTML5 Torus
Comment=Tetris game in HTML5
Categories=Game;ArcadeGame;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/images/skull.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -s 460x450 index.html
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
* Mon Sep 27 2010 Wei-Lun Chao <bluebat@member.fsf.org> 20081126-1
- Initial build
