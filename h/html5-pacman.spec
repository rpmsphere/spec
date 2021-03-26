Summary: Pacman in HTML5
Name: html5-pacman
Version: 20100725
Release: 2
License: freeware
Group: Amusements/Games
Source0: %{name}.zip
Source1: pacman.png
URL: http://arandomurl.com/2010/07/25/html5-pacman.html
Requires: oxzilla, gstreamer-plugins-good, gstreamer-tools
BuildArch: noarch

%description
This is most of the Pacman game everyone knows and loves.
It currently uses localStorage, HTML5 Audio, Canvas and @font-face.

%prep
%setup -q -n %{name}

%build
rm -f audio/*.mp3

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
Comment=classical Pacman game in HTML5
Categories=Game;ArcadeGame;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/pacman.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -s 370x590 index.html
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
* Wed Oct 06 2010 Wei-Lun Chao <bluebat@member.fsf.org> 20100725-2
- Add Requires

* Mon Aug 16 2010 Wei-Lun Chao <bluebat@member.fsf.org> 20100725-1
- Initial build
