Name: devcpp
Summary: A portable C/C++/C++11 IDE
Version: 5.11
Release: 1.bin
License: GPLv3
Group: Development/Tools
Source0: http://sourceforge.net/projects/orwelldevcpp/files/Portable%20Releases/Dev-Cpp %{version} No Compiler Portable.7z
URL: http://orwelldevcpp.blogspot.tw/
BuildRequires: p7zip
BuildRequires: icoutils
Requires: wine
BuildArch: noarch

%description
A maintained version of Dev-C++ fork. Features:
* Syntax highlighting
* Code completion
* Shows information about code when hovering above code
* Provides user-editable shortcuts and tools
* GPROF profiling
* GDB debugging
* Devpak IDE extensions

%prep
%setup -q -n Dev-Cpp

%build

%install
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a * %{buildroot}%{_datadir}/%{name}

%__mkdir_p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Dev C++
Comment=A portable C/C++/C++11 IDE 
Exec=devcpp
Icon=devcpp
Type=Application
Categories=Development;
EOF

%__mkdir_p %{buildroot}%{_datadir}/pixmaps
wrestool -x -t 14 devcppPortable.exe |icotool -x -i 3 -o %{buildroot}%{_datadir}/pixmaps/%{name}.png -

%__mkdir_p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
export WINEPREFIX=\$HOME/.wine.%{name}
wine %{_datadir}/%{name}/devcpp.exe "\$@"
EOF

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Tue Jan 05 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 5.11
- Inital binary package
