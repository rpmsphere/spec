%global _name Gambit

Name:           gambitchess
Version:        1.0.4
Release:        5.4
Summary:        A cross-platform chess game
License:        Public Domain
Group:          Games/Boards
URL:            https://sourceforge.net/projects/gambitchess/
Source0:        http://downloads.sourceforge.net/%{name}/%{_name}-%{version}-src.tar.gz
BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel

%description
Gambit is a cross-platform chess game.

%prep
%setup -q -n %{_name}-%{version}-src
 
%build
cmake -DCONFIG_GUPTA_ENGINE_DIRECTORY=%{_bindir} -DCONFIG_RESOURCE_PATH_PREFIX=%{_datadir}/%{name} .
%make_build
cd engine/gupta
make release

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm755 engine/gupta/gupta %{buildroot}%{_bindir}/gupta
install -d %{buildroot}%{_datadir}/%{name}
cp -a data/* %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=%{_name} Chess
Comment=A cross-platform chess game
Exec=%{name}
Icon=%{_datadir}/%{name}/icons/gambit/gambit-64.png
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

%files
%doc CHANGES.txt LICENSE.txt
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_bindir}/gupta
%{_datadir}/%{name}

%changelog
* Mon Mar 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.4
- Rebuilt for Fedora
