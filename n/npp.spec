Name: npp
Summary: Notepad plus plus
Version: 6.8.8
Release: 1.bin
License: GPL
Group: Applications/Editors
Source0: https://notepad-plus-plus.org/repository/6.x/%{version}/npp.%{version}.bin.minimalist.7z
URL: http://notepad-plus-plus.org/
BuildRequires: p7zip
BuildRequires: icoutils
Requires: wine
BuildArch: noarch

%description
Notepad++ is a free (as in "free speech" and also as in "free beer") source
code editor and Notepad replacement that supports several languages.

%prep
%setup -q -c

%build

%install
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a * %{buildroot}%{_datadir}/%{name}

%__mkdir_p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Notepad++
Comment=Notepad plus plus
Exec=npp
Icon=npp
Type=Application
Categories=Utility;TextEditor;
EOF

%__mkdir_p %{buildroot}%{_datadir}/pixmaps
wrestool -x -t 14 notepad++.exe |icotool -x -i 1 -o %{buildroot}%{_datadir}/pixmaps/%{name}.png - || :

%__mkdir_p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
export WINEPREFIX=\$HOME/.wine.%{name}
wine %{_datadir}/%{name}/notepad++.exe "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Fri Dec 11 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 6.8.8
- Inital binary package
