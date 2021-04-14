Summary:		UFO2000 is a turn based tactical squad simulation multiplayer game
Name:			ufo2000
Version:		0.7.1086
Release:		1
License:		GPL
Group:			Amusements/Games
URL:			http://ufo2000.sourceforge.net/
Source:			%{name}-%{version}-src.tar.bz2
Source1:		%{name}.png
Source2:		dumb-0.9.2.tar.gz
Source3:		%{name}-music-2004.zip
Patch:			%{name}-gcc43.patch
BuildRequires:	allegro-devel
BuildRequires:	expat
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gcc-c++
BuildRequires:	hawknl-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	sqlite-devel
BuildRequires:	unzip
BuildRequires:	desktop-file-utils
Requires:	hawknl-devel
Requires:	allegro-devel

%description
UFO2000 is free and opensource turn based tactical squad simulation
multiplayer game. It is heavily inspired by the famous X-COM: UFO
Defense game. While UFO2000 engine was specifically designed to be
compatible with the graphics resources and maps from X-COM, you
don't need any proprietary data files to play as a new fan-made
set of graphics exists and is included in UFO2000 distribution by
default, so the game is ready to run out of the box.

But if you want an exact X-COM look and feel, you have an option
of installing original X-COM and TFTD data files and use them for
extending UFO2000 with additional maps, weapon sets and units.

NOTE:
You must be a member of group game to play the game!

%prep
%setup -q -c -n %{name}_%{version} -a2
%patch -p1

find . -name .svn | xargs %__rm -rf

# some sound files ..
pushd newmusic
	%__mv readme.txt readme.txt.org
	%__unzip -q %{SOURCE3}
	%__mv readme.txt readme.txt-soundtrack
	%__mv readme.txt.org readme.txt
popd

# dumb will be linked static
sed -i 's|-laldmb -ldumb|dumb/lib/unix/libaldmb.a dumb/lib/unix/libdumb.a|g' makefile
sed -i 's|${shell svnversion .}|unknown|' makefile
sed -i 's|-s$|-s -lm|' dumb/Makefile
sed -i 's/ | O_BINARY//' src/*.cpp
sed -i -e '/stdlib.h/d' -e '19i #include <stdlib.h>' src/fdlibm/fdlibm.h
sed -i 's|<png\.h>|<libpng12/png.h>|' src/loadpng/*png.c
sed -i -e 's|fcos(|cos(|' -e 's|fsin(|sin(|' -e 's|fmul(|fixmul(|g' src/map.cpp
sed -i -e 's|fatan2(|atan2(|' src/soldier.cpp
%ifarch aarch64
sed -i 's|__x86_64__|__aarch64__|' src/fdlibm/ieeefp.h
%endif
 
%build
# first build dumb, will be linked static
pushd dumb
%__cat > make/config.txt << EOF
include make/unix.inc
ALL_TARGETS := core core-examples core-headers
ALL_TARGETS += allegro allegro-examples allegro-headers
PREFIX := /usr
EOF
%__make \
	OFLAGS="$RPM_OPT_FLAGS -fPIC"
popd

%__make %{?jobs:-j%{jobs}} \
	OPTFLAGS="$RPM_OPT_FLAGS -Wno-format-security -I/usr/include/hawknl -Idumb/include" \
	DATA_DIR="%{_datadir}/%{name}" \
	all server

%install
%__install -dm 755 %{buildroot}/usr/
%__install -m 755 %{name} \
	%{buildroot}/usr/
%__install -m 755 %{name}-srv \
	%{buildroot}/usr/

%__install -dm 775 %{buildroot}%{_datadir}/%{name}
%__install -m 664 %{name}.default.ini \
	%{buildroot}%{_datadir}/%{name}/%{name}.ini

for i in arts extensions fonts init-scripts newmaps newmusic newunits script translations; do
	%__cp -a $i \
		%{buildroot}%{_datadir}/%{name}
done
%__install -dm 775 %{buildroot}%{_datadir}/%{name}/TFTD
%__install -dm 775 %{buildroot}%{_datadir}/%{name}/XCOM
for i in keyboard.dat select_option.ini soundmap.xml squad.default.lua \
	ufo2000.dat %{name}.default.ini xcom_folder.ini; do
	%__install -m 644 $i \
		%{buildroot}%{_datadir}/%{name}
done
%__install -m 664 ufo2000-srv.conf \
	%{buildroot}%{_datadir}/%{name}

find %{buildroot}%{_datadir}/%{name} -type d -print0 | xargs -0 chmod 775
#find %{buildroot}%{_datadir}/games/%{name} -type f -print0 | xargs -0 chmod 644

# create menu and icon
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE1} \
	%{buildroot}%{_datadir}/pixmaps

%__cat > %{name}.desktop << EOF
[Desktop Entry]
Name=UFO2000
Comment=UFO2000 is a turn based tactical squad simulation multiplayer game
Exec=%{name}
Icon=%{name}.png
Name[zh_TW]=幽浮二０００
Terminal=false
Encoding=UTF-8
Categories=Game;StrategyGame;
Type=Application
EOF
%__install -Dm 755 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -Dm 777 %{buildroot}/usr/ufo2000 %{buildroot}%{_bindir}/ufo2000
%__install -Dm 777 %{buildroot}/usr/ufo2000-srv %{buildroot}%{_bindir}/ufo2000-srv
rm -f %{buildroot}/usr/ufo2000
rm -f %{buildroot}/usr/ufo2000-srv

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYING *.txt *.html readme_select.ini
%doc docs/*
%{_bindir}/ufo2000
%{_bindir}/ufo2000-srv
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/%{name}*.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.1086
- Rebuilt for Fedora
* Tue Dec  3 2008 milochen <milo_chen@mail2000.com.tw> - 0.7.1086-1.ossii
- Initial ossii package
* Tue Sep 25 2007 Toni Graffy <toni@links2linux.de> - 0.7.1086-0.pm.1
- Initial RPM release
