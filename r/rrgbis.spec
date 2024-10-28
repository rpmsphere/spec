%global __os_install_post %{nil}

Name:     rrgbis
Version:  1.15
Release:  1
Summary:  Really Rather Good Battles In Space
Group:    Amusements/Games
License:  GPL
URL:      https://rrgbis.sourceforge.net/download.php
Source0:  rrgbis-1.15.tar.bz2
Source1:  rrgbis-1.13-data.tar.bz2
Source2:  rrgbis.desktop
Patch0:   rrgbis-1.13.patch

%description
Welcome to the webpage for Really Rather Good Battles In Space:
a free (open source) real time strategy game.

Features:
    * a short but relatively polished single player campaign
    * pretty (albeit 2d) graphics
    * spaceships
    * explosions

%prep
%setup -q -n rrgbis -b 1
#tar -jx -f %{SOURCE1} -C ..
#patch0 -p1
sed -i 's|-Wall|-Wall -fpermissive|' src/squirrel/squirrel/Makefile

%build
pushd src/FTGL
autoreconf -ifv
sed -i 's|-lglut|-lglut -lGL -lGLU -lm|' configure
./configure --prefix=/usr
popd
ECHO=echo make

%install
rm -rf $RPM_BUILD_ROOT

#menu
%__install -D -m 644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

#icon
%__install -D -m 644 %{name}.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png

%__mkdir_p ${RPM_BUILD_ROOT}%{_datadir}/%{name}
%__cp -a * %{buildroot}%{_datadir}/%{name}

%__mkdir_p ${RPM_BUILD_ROOT}%{_bindir}/
echo -e "#!/bin/sh\ncd %{_datadir}/%{name}\n./%{name}" > ${RPM_BUILD_ROOT}%{_bindir}/%{name}
chmod +x ${RPM_BUILD_ROOT}%{_bindir}/%{name}

%files
%{_datadir}/%{name}/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.15
- Rebuilt for Fedora
* Fri Aug 28 2009 Harry Chen <harry@server1.ossii.com.tw> - 1.13-1.ossii
- Initial package for ossii
