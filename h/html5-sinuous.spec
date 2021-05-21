Summary: Canvas game in HTML5
Name: html5-sinuous
Version: 20100924
Release: 1
License: freeware
Group: Amusements/Games
Source0: %{name}.zip
Source1: sinuous.png
URL: http://hakim.se/experiments/html5/sinuous/01_mute/
Requires: oxzilla
BuildArch: noarch

%description
A game built using canvas which will test your mouse pointer reflexes.

%prep
%setup -q -n %{name}

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
Name=HTML5 Sinuous
Comment=Canvas game in HTML5
Categories=Game;ArcadeGame;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/sinuous.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -s 930x580 index.html
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
* Fri Sep 24 2010 Wei-Lun Chao <bluebat@member.fsf.org> 20100924-1
- Initial build
