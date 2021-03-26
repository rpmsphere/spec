Name:		pytego
Version:	0.02
Release:	1
Summary:	A classic boardgame "Stratego" from Milton Bradley
Group:		Amusements/Games
License:	GPL
URL:		http://members.cox.net/churchillrm/projects.html#pytego
Source0:	http://members.cox.net/churchillrm/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Requires:	python, pygame, SDL
BuildArch:	noarch

%description
Pytego is a two-player, cross-platform, networked clone of the
classic boardgame "Stratego" from Milton Bradley.
It is developed using Python, PyGame and SDL. I could not find a good,
networkable, free version of Stratego -- so I wrote my own. Mostly
because I was interested in developing a game, partially because 
I think Python is a terrific language and partially because I was bored (sssh!).

%prep
%setup -q

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/bash
cd %{_libdir}/%{name}
./%{name}.py
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_libdir}/%{name}
%__cp -a * $RPM_BUILD_ROOT%{_libdir}/%{name}
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Comment=A classic boardgame "Stratego"
Name=PyTego
Name[zh_TW]=智慧橋牌
Type=Application
Exec=%{name}
Icon=%{name}
Categories=Game;StrategyGame;
EOF

sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{_libdir}/%{name}/*.py

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.02
- Rebuild for Fedora
* Tue Nov 25 2008 Wind <yc.yan@ossii.com.tw> - 0.02-1
-First Build for OSSII.
