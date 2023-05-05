Summary: LCARS Desktop for Windows
Name: LCARS
Version: 2010.09.09
Release: 1.bin
License: Free Software
Group: Applications
Source0: Incremental_Build_09_09_2010.zip
Source1: LCARS.png
BuildRequires: unzip
BuildArch: noarch
Requires: mono-core

%description
LCARS (Library Computer Access and Retrieval System) is the GUI from
Star Trek: The Next Generation, Voyager, and Deep Space Nine.
This is a rainmeter suite that transforms your Windows GUI into LCARS.

%prep
%setup -q -n Incremental_Build_09_09_2010

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
Name=LCARS
Comment=%{summary}
Exec=LCARS
Icon=LCARS
Type=Application
Categories=System;
EOF

%__install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%__mkdir_p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
export WINEPREFIX=\$HOME/.wine.%{name}
mono %{_datadir}/%{name}/LCARSmain.exe "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2010.09.09
- Rebuilt for Fedora
