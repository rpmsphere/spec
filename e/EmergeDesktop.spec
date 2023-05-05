Summary: Replacement shell for Windows
Name: EmergeDesktop
Version: 6.2.0.1328
Release: 1.bin
License: Free Software
Group: Applications
Source0: https://github.com/arthepsy/emergedesktop/archive/%{version}.tar.gz#/EmergeDesktop-%{version}.7z
Source1: EmergeDesktop.png
URL: https://github.com/arthepsy/emergedesktop
BuildRequires: p7zip
Requires: wine
BuildArch: noarch

%description
Emerge Desktop - replacement shell for Windows.

%prep
%setup -q -c

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
Name=Emerge Desktop
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Type=Application
Categories=System;
EOF

%__install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%__mkdir_p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
export WINEPREFIX=\$HOME/.wine.%{name}
wine %{_datadir}/%{name}/emerge.exe "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 6.2.0.1328
- Rebuilt for Fedora
