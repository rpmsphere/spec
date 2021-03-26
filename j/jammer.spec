%define _prefix	/usr

Name:			jammer
Summary:		Jammer The Gardener
Version:		1.0
Release:		3
Group:			Amusements/Games/3D/Other
License:		GPL
Source0:		Jammer-TheGardener-1.0.celzip
Source1:		celstart.cfg
Source2:		translator.xml
Source3:		jammer-the-gardener.sh
Source4:		vfs.cfg
Source5:		setup.dat
URL:			http://jammers.sourceforge.net/
BuildRequires:	unzip
#BuildRequires:	update-desktop-files
BuildRequires:	desktop-file-utils
BuildRequires:	zip
Requires:		CELStart
BuildArch:		noarch

%description
Live the life of a aspiring gardener on his quest through several
highly dynamic environments spanning the world of Jammer T.

The aim of the game is to fight off slugs and wasps that are intent
on attacking your garden using the colour coded weapons.

Author: Dariusz Dawidowski <DarekDawidowski@users.sourceforge.net>


%prep
%setup -q -c -n %{name}-%{version}

# unzip the celzip and add language de/en
# set Translator.language to de as default
%__install -dm 755 tmp
pushd tmp
	unzip -q %{SOURCE0}
	%__cp %{SOURCE1} .
	%__cp %{SOURCE2} data/text
	zip -q -r ../Jammer-TheGardener-1.0.celzip *
popd

%__cp %{SOURCE3} .

%build

%install
%__install -dm 755 %{buildroot}%{_bindir}
%__install -m 755 %{SOURCE3} %{buildroot}%{_bindir}

%__install -dm 755 %{buildroot}%{_datadir}/games/%{name}
%__install -m 644 Jammer-TheGardener-1.0.celzip \
	%{buildroot}%{_datadir}/games/%{name}
%__install -m 644 %{SOURCE4} \
	%{buildroot}%{_datadir}/games/%{name}
%__install -m 644 %{SOURCE5} \
	%{buildroot}%{_datadir}/games/%{name}

# icon and menu-entry
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 tmp/celstart.icon.png \
	%{buildroot}%{_datadir}/pixmaps/%{name}.png

%__install -dm 755 %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Comment=Jammer - The gardener
Exec=jammer-the-gardener.sh
Icon=%{name}
Name=Jammer - The Gardener
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc tmp/ChangeLog tmp/README tmp/gpl*
%{_bindir}/*.sh
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Thu Aug 26 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 1.0-3
- add %dist
* Tue Aug 24 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 1.0-2
- fix the name of src.rpm
* Wed Aug 11 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 1.0-1
- build 1.0-1 RPM

* Mon Jun 23 2008 Toni Graffy <toni@links2linux.de> - 1.0-0.pm.1
- initial build 1.0
