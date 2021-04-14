Name:           pyretro
Version:        57
Release:        4.1
License:        GPLv3
Summary:        A MAME frontend written in pygame
URL:            https://code.google.com/p/pyretro/
Group:          Games
Source0:        http://pyretro.googlecode.com/files/pyRetro_r%{version}.tar.gz
Requires:       pygame, mame
BuildArch:      noarch

%description
pyRetro is a MAME frontend written in pygame. It is easy to use and nearly
automatic configuration. It is focused for use in arcade machine in a cabinet.

%prep
%setup -q -n pyRetro

%build

%install
#build dirs
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a pyRetro tools %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=pyRetro
Comment=A MAME frontend written in pygame
Exec=%{name}
Icon=%{_datadir}/%{name}/pyRetro/background_default_small.png
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

mkdir p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
cd %{_datadir}/%{name}
exec python pyRetro/pyRetro.py
EOF

%files
%doc TODO README ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 57
- Rebuilt for Fedora
