%undefine _debugsource_packages

Name:		dcmo5
Version:	11.2
Release:	12.1
Summary:	Thomson MO5 emulator
Group:		Emulators
License:	GPLv3+
URL:		https://dcmo5.free.fr/
Source0:	https://dcmo5.free.fr/v11/download/%{name}v11.0.tar.gz
Source1:	https://dcmo5.free.fr/v11/download/%{name}v%{version}.tar.gz
Source2:	%name-32.png
Source3:	%name-16.png
Source4:	%name.rom
Patch0:		dcmo5v11.2-dcmo5options.patch.bz2
Patch1:		dcmo5v11.2-dc6809emul.patch.bz2
Patch2:		dcmo5v11.2-user_directory.patch.bz2
BuildRequires:  SDL-devel
BuildRequires:  SDL_ttf-devel

%description
DCMO5 is an emulator for the Thomson MO5 system.
This package is in PLF because of Mandriva policy concerning emulators.

%prep
%setup -q -a 1 -c
%patch0 -p0
%patch1 -p0
%patch2 -p0
sed -i 's|cc |cc -Wl,--allow-multiple-definition |' makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 755 dcmo5 $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm 644 %{_sourcedir}/%{name}-32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -Dm 644 %{_sourcedir}/%{name}-16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=DCMO5
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;Emulator;
EOF

install -Dm 644 %{_sourcedir}/%{name}.rom $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.rom

%files
%doc documentation/* licence/*
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{name}.rom

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Sep 29 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 11.2
- Rebuilt for Fedora
* Mon Dec 22 2008 Guillaume Rousse <guillomovitch@zarb.org> 11.2-2plf2009.1
- bug fixes from upstream, to be integrated in next official version
- contributed by Jean-Christophe Cardot (<plf@cardot.net>)
* Sun Nov 09 2008 Guillaume Rousse <guillomovitch@zarb.org> 11.2-1plf2009.1
-  contributed by Jean-Christophe Cardot (<plf@cardot.net>)
* Mon Oct 27 2008 Jean-Christophe Cardot <plf@cardot.net> 11.0-1plf
- release
