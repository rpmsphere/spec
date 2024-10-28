%undefine _debugsource_packages

Name:           dcto9p
Version:        11.0
Release:        9.1
Summary:        Thomson TO9+ emulator
Group:          Emulators
License:        GPLv3+
URL:            https://dcto9p.free.fr/
Source0:        https://dcto9p.free.fr/v11/download/%{name}v%{version}.tar.gz
Source1:        %name-32.png
Source2:        %name-16.png
Patch0:         dcto9pv11.0-user_directory.patch.bz2
BuildRequires:  SDL-devel
BuildRequires:  SDL_ttf-devel

%description
DCTO9+ is an emulator for the Thomson TO9+ system.
This package is in PLF because of Mandriva policy concerning emulators.

%prep
%setup -q -c
%patch 0 -p0
sed -i 's|cc |cc -Wl,--allow-multiple-definition |' makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 755 dcto9p $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -Dm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=DCTO9+
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;Emulator;
EOF

%files
%doc documentation/* licence/*
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sat Sep 29 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 11.0
- Rebuilt for Fedora
* Mon Oct 27 2008 Jean-Christophe Cardot <plf@cardot.net> 11.0-1plf
- release
