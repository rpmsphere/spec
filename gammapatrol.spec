Name:           gammapatrol
Version:        0.3
Release:        1
Summary:        An old-style, vertical scrolling space-shooter
Group:          Amusements/Games
License:        GPLv2+
URL:            http://pink.odahoda.de/attic/gammapatrol/
Source0:        http://pink.odahoda.de/attic/gammapatrol/gammapatrol-preview-0.3.tar.bz2
#Patch0:		exec_setting.patch
Patch0:		gammapatrol_fixed_compile_bug.patch

%description
Gamma Patrol is an old-style, vertical scrolling space-shooter.
You have to fight your way through lots of enemies using different
kinds of weapon systems.

%prep
#%setup -q -c %{name}-%{version}
%setup -q -n %{name}
%patch0 -p1


%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT

cat > %{name}.desktop << EOF
[Desktop Entry]
Type=Application
Version=1.0
Encoding=UTF-8
Name=Gamma Patrol
Name[zh_TW]=珈瑪巡邏艦
Comment=An old-style, vertical scrolling space-shooter
Comment[zh_TW]=舊式太空射擊遊戲
Icon=%{_datadir}/pixmaps/%{name}.png
Exec=%{name}
Terminal=false
StartupNotify=false
Categories=Application;Game;ArcadeGame;
EOF

cat > %{name}.sh <<EOF
cd %{_datadir}/%{name}
./%{name}
cd -
EOF

install -Dm 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 644 src/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm 755 %{name} %{buildroot}%{_datadir}/%{name}/%{name}
install -Dm 755 %{name}.sh %{buildroot}%{_bindir}/%{name}

for i in bob fnt gfx help libpsdl mus sfx src; do
	cp -a $i/ %{buildroot}%{_datadir}/%{name}/
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_bindir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Thu Dec  4 2008 milochen <milo_chen@mail2000.com.tw> - 0.3-1.ossii
- initial ossii package
