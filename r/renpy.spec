Name:           renpy
Version:        7.3.5
Release:        1
Summary:        Framework for developing visual-novel type games
Group:          Development/Libraries
License:        LGPLv2+
URL:            http://www.renpy.org/
Source0:        http://www.renpy.org/dl/%{version}/%{name}-%{version}-source.tar.bz2
BuildRequires:	libpng-devel
BuildRequires:	libpng12
BuildRequires:  glew-devel, pygame-devel, freetype-devel, fribidi-devel, python2-Cython
BuildRequires:  lapack, atlas-devel
BuildRequires:  glib2-devel, ffmpeg-devel
BuildRequires:  SDL2-devel
BuildRequires:  python2-pygame_sdl2-devel
Requires:	python2-renpy

%description
Ren'Py is a programming language and runtime, intended to ease the creation
of visual-novel type games. It contains features that make it easy to
display thoughts, dialogue, and menus; to display images to the user; to
write game logic; and to support the saving and loading of games.

Ren'Py tries to be like an executable script, allowing you to get a working
game without much more effort than is required to type the game script into
the computer.

%package -n python2-%{name}
Summary:	The native Python module for renpy

%description -n python2-%{name}
Ren'Py is implemented on top of Python, and that Python heritage shows
through in many places. Many Ren'Py statements allow Python expressions
to be used, and there are also Ren'Py statements that allow for the
execution of arbitrary Python code. Many of the less-used features of
Ren'Py are exposed to the user by way of Python. By only requiring use of
the simplest features of Python, it's hoped that Ren'Py will be usable by
all game authors.

%package demo
Summary:	Full playable examples of renpy
Requires:	renpy

%description demo
This package includes a full playable example showing the features of the framework.

%prep
%setup -q -n %{name}-%{version}-source
#sed -i '139,142s|lib|ffmpeg/lib|' module/setup.py
#sed -i 's|-Wno-unused-function||' module/setup.py
#sed -i "s|'lib')|'lib', 'lib64')|" module/setup.py
#sed -i -e '/^library(/d' -e 's/library("GLEW", optional=True)/True/' module/setup.py
##sed -i "s|AVCODEC_MAX_AUDIO_FRAME_SIZE|192000|" module/ffdecode.c

%build
export CFLAGS="-I/usr/include/SDL2"
cd module
RENPY_DEPS_INSTALL=/usr python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
chmod +x renpy.py
cp -a renpy.py launcher renpy the_question tutorial $RPM_BUILD_ROOT%{_datadir}/%{name}
cd module
RENPY_DEPS_INSTALL=/usr python2 setup.py install --skip-build --root $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
./%{name}.py
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Ren'Py
Comment=Framework for developing visual-novel type games
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/launcher/game/images/logo.png
Categories=Application;Development;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE.txt
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.py*
#{_datadir}/%{name}/common
%{_datadir}/%{name}/launcher
%{_datadir}/%{name}/renpy
#{_datadir}/%{name}/template
%{_datadir}/applications/%{name}.desktop

%files -n python2-%{name}
%doc doc/*
%{python2_sitearch}/*

%files demo
%{_datadir}/%{name}/the_question
%{_datadir}/%{name}/tutorial

%changelog
* Thu Aug 20 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 7.3.5
- Rebuild for Fedora
