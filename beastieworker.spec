%global debug_package %{nil}
%define _name BeastieWorker

Summary:   A 3D realization of SOCOBAN
Name:      beastieworker
Version:   0.4
Release:   1
License:   GPL
Group:     Games/Entertainment
Source0:   %{_name}-%{version}-Linux-2.2.x.tar.gz
URL:       http://beastieworker.sourceforge.net/
BuildRequires:  SDL-devel >= 1.2

%description
Fish Fillets NG is strictly a puzzle game. The goal in every of the seventy
levels is always the same: find a safe way out. The fish utter witty remarks
about their surroundings, the various inhabitants of their underwater realm
quarrel among themselves or comment on the efforts of your fish. The whole
game is accompanied by quiet, comforting music.

%prep
%setup -q -n %{_name}-%{version}

%build
make -C src

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a levels model sounds textures icon.bmp %{_name} $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
./%{_name}
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert icon.bmp $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Beastie Worker
Name[zh_TW]=小惡魔工人
Comment=A 3D realization of SOCOBAN
Comment[zh_TW]=Beastie Worker 是立體畫面的倉庫番
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
* Fri Nov 11 2009 Gene <gene@ossii.com.tw> 0.4-1
- Build for OSSII
