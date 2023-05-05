Summary: Read & Write Utility
Name: Rw
Version: 1.7
Release: 1.bin
License: Freeware
Group: Applications
URL: http://rweverything.com/
Source0: http://rweverything.com/downloads/RwPortableV%{version}.zip
Source1: https://cdn.lo4d.com/t/icon/48/rw-read-write.png
BuildRequires: unzip
BuildArch: noarch
Requires: wine-core

%description
This utility access almost all the computer hardware, including PCI (PCI Express),
PCI Index/Data, Memory, Memory Index/Data, I/O Space, I/O Index/Data, Super I/O,
Clock Generator, DIMM SPD, SMBus Device, CPU MSR Registers, ATA/ATAPI Identify Data,
Disk Read Write, ACPI Tables Dump (include AML decode), Embedded Controller,
USB Information, SMBIOS Structures, PCI Option ROMs, MP Configuration Table, E820,
EDID and Remote Access. And also a Command Window is provided to access hardware manually.

%prep
%setup -q -n Win32/Portable

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
Name=Read & Write
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Type=Application
Categories=System;Hardware;
EOF

%__install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%__mkdir_p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
export WINEPREFIX=\$HOME/.wine.%{name}
wine %{_datadir}/%{name}/Rw.exe "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
