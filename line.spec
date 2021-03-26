Name: line
Summary: Free Calls & Messages
Version: 3.1.6.0
Release: 1.bin
License: freeware
Group: Applications/Internet
Source0: LINE.zip
Source1: %{name}.desktop
Source2: %{name}.png
URL: http://line.me/
Requires: wine
BuildArch: noarch

%description
Mobile messenger app with various stickers and free voice & video call over
3G/4G & Wi-Fi.

%prep
%setup -q -n LINE

%build

%install
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a * %{buildroot}%{_datadir}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%__mkdir_p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
export WINEPREFIX=\$HOME/.wine.%{name}
cd %{_datadir}/%{name}
wine Line.exe "\$@"
EOF

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Thu Feb 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1.6.0
- Inital binary package
