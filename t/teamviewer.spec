Name: teamviewer
Summary: TeamViewer (Remote Control Application)
Version: 6.0.9224
Release: 1.bin
License: Proprietary; free for personal use
Group: Applications/Internet
Source0: http://www.teamviewer.com/download/%{name}_linux.tar.gz
Source1: %{name}.desktop
Source2: %{name}.png
URL: http://www.teamviewer.com/
Requires: wine
ExclusiveArch: %ix86

%description
TeamViewer is a remote control application. TeamViewer provides easy, fast
and secure remote access to Linux, Windows PCs, and Macs.

TeamViewer is free for personal use. You can use TeamViewer completely
free of charge to access your private computers or to help
your friends with their computer problems.

To buy a license for commercial use, please visit http://www.teamviewer.com

%prep
%setup -q -n %{name}6

%build

%install
%__mkdir_p %{buildroot}/usr/lib/%{name}
%__cp .wine/drive_c/Program\ Files/TeamViewer/Version6/* %{buildroot}/usr/lib/%{name}
%__rm -rf .wine %{name}
%__cp -a * %{buildroot}/usr/lib/%{name}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%__mkdir_p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
export WINEPREFIX=\$HOME/.wine.%{name}
cd /usr/lib/%{name}
wine TeamViewer.exe "\$@"
EOF

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
/usr/lib/%{name}/CopyRights_DE.txt
/usr/lib/%{name}/CopyRights_EN.txt
/usr/lib/%{name}/Lizenz_TeamViewer_DE.txt
/usr/lib/%{name}/Lizenz_TeamViewer_EN.txt
/usr/lib/%{name}/license_foss.txt
/usr/lib/%{name}/linux_FAQ_DE.txt
/usr/lib/%{name}/linux_FAQ_EN.txt
/usr/lib/%{name}/TeamViewer.exe
/usr/lib/%{name}/TeamViewer_Resource_*.dll
/usr/lib/%{name}/tvwine.dll.so

%changelog
* Thu Feb 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 6.0.9224
- Inital binary package
