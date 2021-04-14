Summary:          A generalization of Conway's Game of Life
Name:             smoothlife
Version:          004
Release:          6.1
URL:              http://sourceforge.net/projects/smoothlife/
License:          GPLv2
Group:		  Amusements/Games
Source:           http://sourceforge.net/projects/smoothlife/files/SmoothLifeAll%{version}.zip
Source1:	  %{name}.desktop
Source2:	  %{name}.png
Source3:	  Courier.ttf
BuildRequires:    gcc-c++, mesa-libGL-devel, mesa-libGLU-devel, GLee-devel, SDL-devel, SDL_ttf-devel

%description
Conway's Game of Life is generalized to a continuous domain. OpenGL and GLSL
shaders are used for real-time 2D and 3D graphics. Time stepping is done via
a real to complex FFT based convolution operation.

%prep
%setup -q -n SmoothLifeAll
sed -i '/wglSwapIntervalEXT/d' */main.cpp
sed -i -e 's|glu.h|glew.h|' -e '50d' SmoothLifeSDL/main.cpp

%build
cd SmoothLifeSDL
g++ %{optflags} -I/usr/include/GL -lGL -lGLU -lGLee -lGLEW -lSDL -lSDL_ttf main.cpp -o SmoothLife

%install
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -a readme.txt SmoothLife/SmoothLifeConfig.txt SmoothLife/shaders %{SOURCE3} $RPM_BUILD_ROOT%{_libdir}/%{name}
install -m755 SmoothLifeSDL/SmoothLife $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat <<EOF > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/bash
cd %{_libdir}/%{name}
exec ./SmoothLife
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed May 16 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 004
- Rebuilt for Fedora
