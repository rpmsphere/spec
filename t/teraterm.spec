Summary: Tera Terminal Emulator
Name: teraterm
Version: 4.106
Release: 1.bin
License: Freeware
Group: Applications
URL: https://osdn.net/projects/ttssh2/
Source0: https://osdn.net/projects/ttssh2/downloads/74780/teraterm-%{version}.zip
Source1: https://static-cdn.osdn.net/thumb/g/4/899/36x36_0.png
BuildRequires: unzip
BuildArch: noarch
Requires: wine-core

%description
Tera Term is Tera Term Pro 2.3 succession version and is being officially
recognized by the original author. Tera Term is open source free software
terminal emulator supporting UTF-8 protocol. Now TTSSH supports SSH2 protocol
(Original version supports SSH1).

%prep
%setup -q

%build
#No build

%install
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a * %{buildroot}%{_datadir}/%{name}

%__mkdir_p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Tera Term
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Type=Application
Categories=System;Utility;
EOF

%__install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%__mkdir_p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
export WINEPREFIX=\$HOME/.wine.%{name}
wine %{_datadir}/%{name}/ttermpro.exe "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 4.106
- Rebuilt for Fedora
