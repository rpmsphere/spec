Summary: A graphical game
Name: filler
Version: 1.01
Release: 1
License: GPL
URL: http://sourceforge.net/projects/filler
Group: Amusements/Games
Source: http://download.sourceforge.net/filler/%{name}-%{version}.tgz
Patch0: filler.Filler.java-patch
Patch1:	filler.Makefile-patch
BuildRequires:	java
Requires:	java
BuildArch:	noarch

%description
Filler is a graphical games where you occupy coloured hexes by changing
colours.

%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p0

%build
make

%install
%__rm -rf %{buildroot}
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp %name.jar $RPM_BUILD_ROOT%{_datadir}/%{name}
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__mkdir_p $RPM_BUILD_ROOT%{_bindir}
cp res/friendless/games/filler/.thumbnails/filler-screenshot.gif.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF

[Desktop Entry]
Name=%{name}
Name[zh_TW]=填滿者
Comment=A graphical game
Comment[zh_TW]=Filler 是一套爭地盤的益智遊戲，玩法類似魔法泡泡球
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Game;
EOF

%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
java -jar %{name}.jar
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Fri Mar 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.01
- Rebuilt for Fedora
* Fri Dec 31 2008 Shadow John <john@ossii.com.tw>
- Rebuild for M6(OSSII)
* Wed Dec 06 2000 John Farrell
- Passed FILLERPATH and DEST parameters to Makefile
* Sat Dec 02 2000 Tognon Stefano <ice00@users.sourceforge.net>
- Wrote first version of spec file.
