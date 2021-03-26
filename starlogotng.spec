%define __os_install_post %{nil}

Name: starlogotng
Summary: The Next Generation of StarLogo
Version: 1.5
Release: 1.bin
License: freeware
Group: Development/Languages
Source0: StarLogoTNG-V1.5.zip
Source1: %{name}.desktop
Source2: %{name}.png
URL: http://education.mit.edu/projects/starlogo-tng
Requires: wine
BuildArch: noarch

%description
StarLogo TNG is The Next Generation of StarLogo modeling and simulation
software. While this version holds true to the premise of StarLogo as a tool
to create and understand simulations of complex systems, it also brings with
it several advances - 3D graphics and sound, a blocks-based programming
interface, and keyboard input - that make it a great tool for programming
educational video games.

%prep
%setup -q -n "StarLogo TNG"

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
wine StarLogoTNG.exe "\$@"
EOF

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Thu Feb 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Inital binary package
