Summary: Guitar in HTML5
Name: html5-google_guitar
Version: 20110610
Release: 2
License: commercial
Group: Amusements/Games
Source0: google-guitar.zip
Source1: google-guitar.png
Requires: mongoose, oxzilla, flash-plugin
BuildArch: noarch

%description
Google Guitar for Les Paul's 96th Birthday.

%prep
%setup -q -n google-guitar

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
Name=HTML5 Guitar
Comment=Google Guitar in HTML5
Categories=Game;Emulator;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/google-guitar.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
_PORT=\$((\$RANDOM%16384+49152))
mongoose -p \$_PORT &
sleep 1
oxzilla -r -s 480x340 http://127.0.0.1:\$_PORT/lespaul.html
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
- Rebuilt for Fedora
* Mon Jun 20 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Initial build
