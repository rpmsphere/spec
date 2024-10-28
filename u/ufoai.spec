Name:           ufoai
Version:        2.5
Release:        1
Summary:        UFO: Alien Invasion
Group:          Amusements/Games
License:        GPLv2+
URL:            https://ufoai.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}-source.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}-ded.desktop
Patch0:         ufoai-2.2-libdir.patch
BuildRequires:  desktop-file-utils curl-devel freealut-devel gettext
BuildRequires:  libjpeg-devel libogg-devel libpng-devel libvorbis-devel
BuildRequires:  libXxf86dga-devel libXxf86vm-devel SDL-devel SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  gtkglext-devel gtksourceview2-devel texlive-pdfsync
Requires:       opengl-games-utils
Requires:       %{name}-data = %{version}

%package doc
Summary:        UFO: Alien Invasion user manual
Group:          Documentation
License:        GFDL
BuildRequires:  tetex-latex
BuildArch:      noarch

%description
UFO: ALIEN INVASION is a strategy game featuring tactical combat
against hostile alien forces which are about to infiltrate earth at
this very moment. You are in command of a small special unit which
has been founded to face the alien strike force. To be successful on
the long run, you will also have to have a research team study the
aliens and their technologies in order to learn as much as possible
about their technology, their goals and the aliens themselves.


%description doc
UFO: ALIEN INVASION is a strategy game featuring tactical combat
against hostile alien forces which are about to infiltrate earth at
this very moment.

This package contains the user manual for the game.


%prep
%setup -q -n %{name}-%{version}-source
## we do not like "arch-dependent-file" in /usr/share
# change the target for the library
#sed -i -e "s/base/./" build/game.mk
mkdir base
# allow to set the library path
#patch -p1
#sed -i 's|Z_DEFAULT_COMPRESSION|PNG_Z_DEFAULT_COMPRESSION|' src/shared/images.c

%build
export LDFLAGS="-lX11"
./configure --prefix=/usr --disable-ufo2map --enable-release
sed -i 's|CXXFLAGS :=|CXXFLAGS := -Wno-narrowing -std=gnu++11|' Makefile
make %{?_smp_mflags}
make %{?_smp_mflags} lang
# wrapper scripts - generated because we need arch dependent paths
cat > %{name}-wrapper.sh <<-EOF
#!/bin/sh

. /usr/share/opengl-games-utils/opengl-game-functions.sh

checkDriOK UFO:AI

exec ufo \\
        +set fs_libdir %{_libdir}/%{name} \\
        +set fs_basedir %{_datadir}/%{name} \\
        +set fs_i18ndir %{_datadir}/locale \\
        "\$@"
EOF

cat > ufoded-wrapper.sh <<-EOF
#!/bin/sh

exec ufoded \\
        +set fs_libdir %{_libdir}/%{name} \\
        +set fs_basedir %{_datadir}/%{name} \\
        +set fs_i18ndir %{_datadir}/locale \\
        "\$@"
EOF

# build documentation
cd src/docs/tex
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -D -m 0755 ufo %{buildroot}%{_bindir}/ufo
install -D -m 0755 ufoded %{buildroot}%{_bindir}
install -p -m 0755 %{name}-wrapper.sh %{buildroot}%{_bindir}
install -p -m 0755 ufoded-wrapper.sh %{buildroot}%{_bindir}
install -D -m 0755 base/game.so %{buildroot}%{_libdir}/%{name}/game.so
mkdir -p -m 0755 %{buildroot}%{_datadir}/locale
cp -pr base/i18n/* %{buildroot}%{_datadir}/locale/
mkdir -p -m 0755 %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
cp -p src/ports/linux/ufo.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
cp -p src/ports/linux/ufoded.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}-ded.png
desktop-file-install --vendor="fedora" \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --vendor="fedora" \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
%find_lang %{name}
# install documentation
mkdir -p -m 0755 %{buildroot}%{_docdir}/%{name}
cp -pr README LICENSES COPYING src/docs/tex/*.pdf \
        %{buildroot}%{_docdir}/%{name}/

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
        %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
        %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files -f %{name}.lang
# we need to use full path so %doc does not the cleanup
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/LICENSES
%doc %{_docdir}/%{name}/COPYING
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/32x32/apps/*

%files doc
%doc %{_docdir}/%{name}/*.pdf
%lang(en) %{_docdir}/%{name}/ufo-manual_EN.pdf

%changelog
* Wed Jul 31 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5
- Rebuilt for Fedora
* Tue Oct 21 2008 Feather Mountain <john@ossii.com.tw> 2.2.1-1.ossii
- Rebuild for M6(OSSII)
* Mon Jun 09 2008 Karel Volny <kvolny@redhat.com> 2.2.1-1
- Version bump
- Fixes Livna bug #1931
- Configure with --enable-release
* Tue Feb 26 2008 Karel Volny <kvolny@redhat.com> 2.2-5
- Added patch to allow setting fs_libdir, fixes Livna bug #1882
* Tue Feb 19 2008 Karel Volny <kvolny@redhat.com> 2.2-4
- Changed BuildRequires of the doc subpackage to tetex-latex instead of tetex
* Mon Feb 18 2008 Karel Volny <kvolny@redhat.com> 2.2-3
- Fixed BuildRequires to include SDL_mixer-devel
* Mon Feb 04 2008 Karel Volny <kvolny@redhat.com> 2.2-2
- Merged in ufoai-doc as a subpackage
- Added gtk-update-icon-cache to %%post and %%postun
* Tue Jan 22 2008 Karel Volny <kvolny@redhat.com> 2.2-1
- Version bump
- Added BuildRequires: curl-devel
- Changed language file handling
- Use bundled icons
- Added ufoded wrapper and menu entry
* Mon Jan 07 2008 Karel Volny <kvolny@redhat.com> 2.1.1-3
- Marked localisation files
- Some fixes according the comment #18 to bug #412001:
- Added BuildRequires: freealut-devel libXxf86vm-devel libXxf86dga-devel
- Improved .desktop file
- Added fix for mixed encoding within the file CONTRIBUTORS
* Thu Dec 06 2007 Karel Volny <kvolny@redhat.com> 2.1.1-2
- Split the game, data and additional music into separate packages
- Added wrapper script to use correct command line parameters and OpenGL Wrapper
- Added ufoai.desktop as a separate file
* Tue Dec 04 2007 Karel Volny <kvolny@redhat.com> 2.1.1-1
- Initial release for Fedora 8
