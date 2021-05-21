Name:           breve
Version:        2.7
Release:        1
Summary:        A 3d Simulation Environment for Multi-Agent Simulations and Artificial Life 
Group:          Amusements/Games
License:        LGPL
URL:            http://www.spiderland.org/
Source0:        http://www.spiderland.org/download/%{name}_%{version}_source.tar.gz
Patch0:		%{name}_%{version}-breveFunctionsQGAME.cc.patch
Patch1:         %{name}_%{version}-joint.cc.patch 
Patch2:         %{name}_%{version}-movie.h.patch
Patch3:         %{name}_%{version}-sound.cc.patch     
Patch4:         %{name}_%{version}-sound.h.patch
Patch5:		%{name}_%{version}-movie.cc.patch
BuildRequires:  gsl-devel,glut-devel,bison,flex,ode-devel,ftgl-devel,mesa-libGLU-devel,enet-devel
BuildRequires:  mesa-libGL-devel,expat-devel,zlib-devel,mesa-libOSMesa-devel
BuildRequires:  libpng-devel,libjpeg-devel,qgame,ode-devel,portaudio-devel,python-devel

%description
breve is a free, open-source software package which makes it easy to build 3D simulations of multi-agent systems and artificial life. Using Python, or using a simple scripting language called steve, you can define the behaviors of agents in a 3D world and observe how they interact. breve includes physical simulation and collision detection so you can simulate realistic creatures, and an OpenGL display engine so you can visualize your simulated worlds.

%prep
%setup -q -n %{name}_%{version}_source
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0

sed -i 's|-Iinclude/breve|-Iinclude/breve -I/usr/include/ffmpeg|' configure* Makefile* 

%build
CXXFLAGS='-D__STDC_CONSTANT_MACROS -I/usr/include/python2.6' ./configure
sed -i 's/-lgslcblas/-lgslcblas -lpython2.6/' Makefile
make

%install
%__rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
#DESTDIR=$RPM_BUILD_ROOT make install 
cp bin/breve $RPM_BUILD_ROOT%{_bindir}
cp -a lib/classes $RPM_BUILD_ROOT%{_libdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m0644 -p docBuild/classImages/%{name}_icon.jpg $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

#Desktop
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
#[Desktop Entry]
Name=%{name}
Name[zh_TW]=人工生命
Comment=A 3d Simulation Environment for Multi-Agent Simulations and Artificial Life 
Comment[zh_TW]=一套 3D 模擬環境，可以開發出人工生命的遊戲。
Exec=%{name}.sh
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Game;
EOF

#Exec
%__cat > %{buildroot}%{_bindir}/%{name}.sh <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
breve tests/raytraceTest.tz
EOF

%clean
rm -rf %{buildroot}

%files
%{_datadir}/applications/*
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*
%{_bindir}/*
%{_libdir}/%{name}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7
- Rebuilt for Fedora
* Fri Dec 31 2008 Shadow John <john@ossii.com.tw> 2.7-1
- Build for OSSII
