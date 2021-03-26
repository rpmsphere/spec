Summary: Helicopter in HTML5
Name: html5-helicopter
Version: 20100805
Release: 1
License: freeware
Group: Amusements/Games
Source0: %{name}.zip
URL: http://arandomurl.com/2010/08/05/html5-helicopter.html
Requires: oxzilla
BuildArch: noarch

%description
After having some fun writing pacman in HTML5 I decided to write another
classic game, this time Helicopter.

%prep
%setup -q -n %{name}

%build
rm -f *.mp3

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

# Install menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%{__cat} > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=HTML5 Helicopter
Comment=classical Helicopter game in HTML5
Categories=Game;ArcadeGame;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/heli.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -s 520x430 index.html
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
* Fri Sep 24 2010 Wei-Lun Chao <bluebat@member.fsf.org> 20100805-1
- Initial build
