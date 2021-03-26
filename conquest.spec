Summary:	A real-time multi-player space warfare game
Name:		conquest
Version:	9.1
Release:	1
Source:		https://github.com/jtrulson/conquest/archive/conquest-%{version}.tar.gz#/conquest-%{version}.tar.gz
License:	MIT
Group:		Amusements/Games
URL:		https://github.com/jtrulson/conquest

%description
Conquest is a top-down, real time space warfare game. It was originally written
in RATFOR for the VAX/VMS system in 1983 by Jef Poskanzer and Craig Leres.

%prep
%setup -q

%build
./autogen.sh
%configure
make

%install
rm -rf %{buildroot}
#sed -i '/chgrp/d' src/Makefile
%make_install -i
install -Dm644 icon/conquest-icon-48.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop  <<EOF
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Conquest
Comment=A real-time multi-player space warfare game
Icon=%{name}
Exec=%{name}
Terminal=false
StartupNotify=false
Categories=Game;Strategy;
EOF

%clean
rm -rf %{buildroot}

%files
%{_docdir}/%{name}
%{_bindir}/*
%{_libexecdir}/*
%{_sysconfdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/*.6.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Sep 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 9.1
- Rebuild for Fedora