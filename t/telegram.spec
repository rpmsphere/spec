%undefine _debugsource_packages
%global _name Telegram

Summary: Telegram Desktop
Name: telegram
Version: 4.6.2
Release: 1.bin
License: Freeware
Group: Applications
URL: https://desktop.telegram.org/
Source0: https://updates.tdesktop.com/tlinux/tsetup.%{version}.tar.xz
Source1: %{name}.png
ExclusiveArch: x86_64

%description

%prep
%setup -q -n %{_name}

%build
#No build

%install
%__mkdir_p %{buildroot}%{_libexecdir}/%{name}
%__cp -a * %{buildroot}%{_libexecdir}/%{name}

%__mkdir_p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Telegram
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Type=Application
Categories=Network;
EOF

%__install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
%__install -d %{buildroot}%{_bindir}
ln -s ../libexec/%{name}/%{_name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 4.6.2
- Rebuilt for Fedora
