%undefine _debugsource_packages

Name: qmandelbrowse
Summary: Qt Mandelbrot Browser
Version: 0.91
Release: 2.1
Group: science
License: GPLv2
URL: http://qmandelbrowse.sourceforge.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires: qt5-qtbase-devel
BuildRequires: glew1-devel
BuildRequires: freeglut-devel

%description
Interactive, user friendly, Mandelbrot set browser:
* Interactive and responsive
* Multiple rendering methods (FPU [float, double, long double], SSE, OpenGL)
* Navigation history
* Real-time color editing
* Saving image to file

%prep
%setup -q
%ifarch aarch64
sed -i '/emmintrin.h/d' src/RenderingJob.cpp
%endif

%build
qmake-qt5
%ifarch x86_64 aarch64
sed -i -e 's|-mmmx||' -e 's|-msse2||' Makefile.* mandel.pro
%endif
make

%install
make install INSTALL_ROOT=%{buildroot}/usr
install -Dm644 screenshots/icon-small-orange.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Qt Mandelbrot Browser
Exec=%{name}
Terminal=false
Comment=Interactive, user friendly, Mandelbrot set browser
Type=Application
Categories=Application;Graphics;
Icon=%{name}
EOF

%files
%doc README LICENSE
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Mar 06 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.91
- Rebuilt for Fedora
