%define		oname	GoOllie

Name:		goollie
Version:	1.3
Release:	2
URL:		http://tweeler.com/index.php?PAGE=goollie_linux
License:	GPLv3 and CC-BY-SA
Group:		Games/Arcade
Summary:	Arcage game about Ollie the Oligocheata, a worm on a mission
# http://www.tweeler.com/GoOllie_1.3_src.tar.gz
Source:		%{oname}-%{version}.tar.bz2
Source1:	%{oname}.png
Patch0:		%{oname}.patch
BuildRequires:	cmake
BuildRequires:	libtuxcap-devel

%description
Ollie the Oligocheata is a worm on a mission
He is on a mission to bring mouse controlled platforming fun to everyone!

Go Ollie is a free Linux game with beautifully rendered scenes and animations.
The latest in innovative mouse controlled platform gaming featuring a unique
fusion of platform and match three gaming mechanics.

Two gameplay modes:
- Story Mode with over 60 individual levels each with different objectives
- Fast and furious action game with unlimited re-playability

Authors:
--------
	Game design and game code - Charlie Dog
	Art - Simon Lissaman
	Music - Michael Watts / Encore Music
	GNU/Linux port - W.P. van Paassen

%prep
%setup -q -n %{oname}-%{version}
%patch0
sed -i -e "s|SetAppResourceFolder.*|SetAppResourceFolder(\"%{_datadir}/%{name}\");|g" src/main.cpp

%build
%cmake
%{__make}

%install
%__rm -rf %{buildroot}
%__install -s -D -m 0755 %{oname} %{buildroot}%{_bindir}/%{name}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a data/* %{buildroot}%{_datadir}/%{name}
%__cp -a src/*.py %{buildroot}%{_datadir}/%{name}
%__install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%__mkdir_p %{buildroot}%{_datadir}/applications/
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=GoOllie
Comment=Ollie the Oligocheata, a worm on a mission
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING README other_licenses/
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue May 22 2012 johnwu<johnwu@server1.ossii.com.tw>
- rebuild for OX

* Sun Mar 11 2012 Andrey Bondrov <abondrov@mandriva.org> 1.3-1
+ Revision: 784086
- imported package goollie
