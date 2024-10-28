Name:                   AlephOne-Marathon2
Summary:                Marathon 2 scenario files for AlephOne
Version:                1.0
Release:                1
License:                GPL
Group:                  Amusements/Games/3D/Shoot
#Source:                https://alephone.cebix.net/downloads/AlephOne-Marathon2-1.0.tar.gz
Source:                 %{name}-%{version}.tar.bz2
Source1:                AlephOne.png
URL:                    https://alephone.cebix.net
Requires:               AlephOne
#BuildRequires: update-desktop-files
Provides:               AlephOne-data
BuildArch:              noarch

%description
Aleph One is an Open Source 3D first-person shooter game, based on
the game Marathon 2 by Bungie Software. It is set in a Sci-Fi
universe dominated by deviant computer AIs and features a well
thought-out plot. Aleph One supports, but doesn't require, OpenGL
for rendering.

This package contains the Marathon 2 scenario files for AlephOne.

%prep
%setup -q

%build

%install
# startscript
%__install -dm 755 %{buildroot}%{_bindir}
%__cat > alephone-marathon2 << EOF
#! /bin/sh
export ALEPHONE_DATA=%{_datadir}/AlephOne:%{_datadir}/AlephOne/%{name}-%{version}
%{_bindir}/alephone $*
EOF
%__install -m 755 alephone-marathon2 \
        %{buildroot}%{_bindir}
%__rm alephone-marathon2

# data-files
%__install -dm 755 %{buildroot}%{_datadir}/AlephOne/%{name}-%{version}
%__cp -a . \
        %{buildroot}%{_datadir}/AlephOne/%{name}-%{version}

# done by %doc
%__rm %{buildroot}%{_datadir}/AlephOne/%{name}-%{version}/Marathon_2_Manual.pdf

# menu-entrie
%__cat > %{name}.desktop << EOF
[Desktop Entry]
Comment=AlephOne - Marathon 2
Comment[zh_TW]=阿爾發一號-馬拉桑 2，第一人稱射擊遊戲。
Exec=alephone-marathon2
Icon=AlephOne
Name=AlephOne - Marathon 2
Name[zh_TW]=阿爾發一號-馬拉桑 2
Path=
Terminal=false
Type=Application
Categories=Application;Game;Amusements;Games;Action;
EOF
%__install -dm 755 %{buildroot}/usr/share/applications
%__install -m 644 %{name}.desktop \
        %{buildroot}%{_datadir}/applications

# icon
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE1}  \
        %{buildroot}%{_datadir}/pixmaps


%files
%doc *.pdf
%{_bindir}/*
%{_datadir}/AlephOne/%{name}-%{version}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Wed Oct 15 2008 Feather Mountain <john@ossii.com.tw> - 1.0-0.1.ossii
- Rebuild for M6(OSSII)
* Wed Jun 06 2007 Toni Graffy <toni@links2linux.de> - 1.0-0.pm.1
- first package 1.0
- repacked as tar.bz2
