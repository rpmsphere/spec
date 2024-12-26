%undefine _debugsource_packages
%global __os_install_post %{nil}

Name: qb64
Version: 2.1
Release: 1
URL: https://www.qb64.net/
#Source0: https://www.qb64.net/qb64_%{version}_lnx.tar.gz
Source0: https://codeload.github.com/Galleondragon/qb64/tar.gz/v%{version}#/%{name}-%{version}.tar.gz
Source1: qb64.desktop
Source2: https://www.qb64.net/qb64_trans.png
License: GPL
Group: Development/Other
BuildRequires: gcc-c++, libX11-devel, SDL-devel, SDL_mixer-devel, SDL_ttf-devel, SDL_net-devel, SDL_image-devel
BuildRequires: freeglut-devel, xmessage
Summary: IDE and Compiler for the QB64 Programming Language

%description
QB64 is a multiplatform, 100% QBASIC/QB4.5 compatible programming language
with access to modern features such as TCP/IP, graphics loading(many formats
supported) & transformations, sound(MP3,MIDI,WAV and many more), devices
(joysticks), screen capture & macro-like output, TTF fonts, UNICODE & IME
input, clipboard access, etc.

%prep
%setup -q
#cp internal/source/* internal/temp
sed -i 's|-Wall|-Wall -fpermissive|' internal/c/libqb/os/lnx/setup_build.sh
sed -i '/exit 1/d' setup_lnx.sh

%build
#cd internal/c
#g++ -c -w -Wall libqb.cpp `sdl-config --cflags`
#g++ libqb.o qbx.cpp `sdl-config --cflags --libs` -lSDL_mixer -lSDL_ttf -lSDL_net -lSDL_image -lX11 -lGL -lGLU -lglut -o ../../qb64
#rm -rf internal/temp/*
./setup_lnx.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_libdir}/%{name}
./%{name}
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -a internal qb64 source $RPM_BUILD_ROOT%{_libdir}/%{name}
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%doc licenses/*
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuilt for Fedora
