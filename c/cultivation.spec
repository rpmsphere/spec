Name:	    cultivation
Version:    9
Release:    8
Summary:    A game about the interactions within a gardening community
License:    Public Domain
Group:	    Games/Strategy
URL:	    https://cultivation.sourceforge.net/
Source0:    https://sourceforge.net/projects/cultivation/files/cultivation/v9/Cultivation_%{version}_UnixSource.tar.gz
Patch0:     Cultivation-9-deb-portaudio.patch
#Patch1:     Cultivation-9-deb-abs_paths.patch
Patch2:     Cultivation-9-deb-math_h.patch
Patch3:     Cultivation-9-upstream-fix_crash.patch
Patch4:     Cultivation-9-mageia-build64bit.patch
BuildRequires:	mesa-libGLU-devel
BuildRequires:	freeglut-devel
BuildRequires:	portaudio-devel
BuildRequires:	libpng-devel
BuildRequires:	ghostscript-core ImageMagick

%description
Cultivation is a game about a community of gardeners growing food
for themselves in a shared space.

Cultivation is quite different from most other games. It is a
social simulation, and the primary form of conflict is over land
and plant resources --- there is no shooting, but there are plenty
of angry looks. It is also an evolution simulation. Within the
world of Cultivation, you can explore a virtually infinite
spectrum of different plant and gardener varieties.

All of the graphics, sounds, melodies,and other content in
Cultivation are 100% procedurally generated at playtime. In other
words, there are no hand-painted texture maps --- instead, each
object has a uniquely 'grown' appearance. Every time you play,
Cultivation generates fresh visuals, music, and behaviors.

%prep
%setup -q -n Cultivation_%{version}_UnixSource
%patch0 -p1
#patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
sed -i 's|PortAudioStream|PaStream|' game2/gameSource/sound/SoundPlayer.h
sed -i 's|GetDefaultOutputDeviceID|GetDefaultOutputDevice|' game2/gameSource/sound/SoundPlayer.cpp
sed -i -e 's|uint32_t|long unsigned int|' -e 's|PaTimestamp|PaTime|' game2/gameSource/sound/SoundPlayer.cpp
sed -i -e '163,165d' -e '167,169d' -e '172d' game2/gameSource/sound/SoundPlayer.cpp

%build
export CFLAGS+=" $RPM_OPT_FLAGS -fPIC -DPIC"
pushd game2
	chmod u+x configure
	./configure --linux
popd
	convert -type Grayscale -negate ./game2/build/macOSX/icon128_mask.png mask.png
	composite -compose CopyOpacity mask.png ./game2/build/macOSX/icon128_color.png cultivation.png
	mkdir -p 32x32
	convert -scale 32x32 cultivation.png 32x32/cultivation.png
	convert 32x32/cultivation.png 32x32/cultivation.xpm
	sed -i -e 's/-lX11//' game2/gameSource/Makefile
	sed -i -e 's/^DEBUG_FLAG = .*/DEBUG_FLAG = /' game2/gameSource/Makefile
	sed -i -e 's/^OPTIMIZE_FLAG = .*/OPTIMIZE_FLAG = /' game2/gameSource/Makefile
	sed -i -e 's/^COMPILE_FLAGS = /COMPILE_FLAGS = ${CFLAGS} -fpermissive /' game2/gameSource/Makefile
	%__make -C game2/gameSource CFLAGS="${CFLAGS} -DDATADIR=%{_datadir}/%{name}"

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 game2/gameSource/Cultivation \
	%{buildroot}%{_bindir}/%{name}.real

install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 644 game2/gameSource/font.tga \
	%{buildroot}%{_datadir}/%{name}
install -m 644 game2/gameSource/features.txt \
	%{buildroot}%{_datadir}/%{name}
install -m 644 game2/gameSource/language.txt \
	%{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/%{name}/languages
install -m 644 game2/gameSource/languages/*.txt \
	%{buildroot}%{_datadir}/%{name}/languages

# startscript
cat > %{buildroot}%{_bindir}/%{name} <<'EOF'
#!/bin/bash
if [ ! -d $HOME/.%{name} ]; then
	mkdir -p $HOME/.%{name}
	cd $HOME/.%{name}
	cp %{_datadir}/%{name}/*.txt .
	ln -s %{_datadir}/%{name}/*.tga .
	ln -s %{_datadir}/%{name}/languages .
	ln -s %{_bindir}/%{name}.real .
fi

cd $HOME/.%{name}

# Basic switch of language according to locale defined in Unix systems
case "$LC_MESSAGES" in
    fr* )
        language="French"
	;;
    pt* )
        language="Portuguese"
	;;
    * )
        language="English"
	;;
esac
echo $language > ./language.txt

./%{name}.real
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

# icon
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 cultivation.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%summary
Exec=soundwrapper %{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;Simulation;
EOF

%files
%doc game2/documentation/*
%{_bindir}/%{name}
%{_bindir}/%{name}.real
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 9
- Rebuilt for Fedora
* Fri Jan 11 2013 umeabot <umeabot> 9-8.mga3
+ Revision: 348411
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sat Nov 24 2012 zezinho <zezinho> 9-7.mga3
+ Revision: 321659
- soundwrapper needed so added to desktop file
* Fri Jun 08 2012 dams <dams> 9-6.mga3
+ Revision: 257758
- clean/update specfile
- change game icon to have a better render
* Mon Mar 12 2012 zezinho <zezinho> 9-5.mga2
+ Revision: 222840
- disable abs path patch as it disables i18n
* Wed Sep 14 2011 fwang <fwang> 9-4.mga2
+ Revision: 143264
- br freeglut
- fix br
- rebuild for new libpng
  + zezinho <zezinho>
    - switch to freeglut-devel
    - missing build require
    - simple patch to build on current cauldron
    - update tarball
    - update to latest version and some debian patches to remove the bundled libs
  + stormi <stormi>
    - add imagemagick buildrequires
* Sun Jul 10 2011 stormi <stormi> 9-0.20071217.7.mga2
+ Revision: 121437
- increase release so that it's higher than in mageia 1
* Sat Jul 09 2011 stormi <stormi> 9-0.20071217.6.mga2
+ Revision: 120907
- bump release to ease migration from mandriva
* Wed Jun 08 2011 zezinho <zezinho> 9-0.20071217.5.mga2
+ Revision: 102046
- Upstream patches to build with current make and fix a crash
  + ennael <ennael>
    - clean spec file
    - imported package cultivation
