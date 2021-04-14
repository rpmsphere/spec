Name:           fireball12
Version:        3.2
Release:        1
Summary:        Fireball 12 is an arcade game project.
Group:          Amusements/Games
License:        LGPL
URL:            http://sourceforge.net/projects/fireball12/
Source0:        http://nchc.dl.sourceforge.net/sourceforge/fireball12/Fire12-%{version}.tar.gz
Requires:	pygame, alsa-lib
BuildArch:	noarch

%description
Fireball 12 is an arcade game project. You control a ship and simply defeat
the oncoming enemies with several different weapons. It is intended to be
flexible with highly configurable enemies, projectiles and weapons.

%prep
%setup -q -n Fireball_12-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -a . $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/*.py~
install -m0644 -p gfx/icon-vulcan.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

#Desktop
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Fireball 12
Name[zh_TW]=火球 12
Comment=Fireball 12 is an arcade game project
Comment[zh_TW]=控制宇宙船 Fireball 12，在太空中使用不同的武器與怪物大戰。
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Game;
EOF

#Exec
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
cd %{_datadir}/%{name}
python2 main.py
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Fri Mar 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2
- Rebuilt for Fedora
* Wed Feb 11 2009 Feather Mountain <john@ossii.com.tw> 3.2-1
- Build for OSSII
