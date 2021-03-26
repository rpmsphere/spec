%global debug_package %{nil}

Name:          fraqtive
Version:       0.4.8
Release:       7.1
Summary:       Drawing Mandelbrot and Julia fractals
Group:         Graphical Desktop/Applications/Graphics
URL:           http://fraqtive.mimec.org
Source:        http://downloads.sourceforge.net/fraqtive/%{name}-%{version}.tar.bz2
License:       GPL
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: libICE-devel
BuildRequires: libpng-devel
BuildRequires: qt4-devel
BuildRequires: libSM-devel
BuildRequires: libstdc++-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrender-devel
BuildRequires: zlib-devel

%description
Fraqtive is a program for drawing Mandelbrot and Julia fractals.
It uses a very fast algorithm and generates high quality, smooth images.
It is fully interactive, allowing for real-time mouse navigation
and dynamic generation of the Julia fractal preview.
OpenGL-rendered 3D view of the fractals is also supported.

%prep
%setup -q

%build
%ifarch aarch64
./configure -prefix %{_prefix} -no-sse2
%else
./configure -prefix %{_prefix}
%endif
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING ChangeLog README
%{_bindir}/fraqtive
%{_datadir}/applications/fraqtive.desktop
%{_datadir}/icons/hicolor/*/apps/fraqtive.png

%changelog
* Wed Mar 04 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.8
- Rebuild for Fedora
* Fri May 07 2010 Automatic Build System <autodist@mambasoft.it> 0.4.5-1mamba
- automatic update by autodist
* Sat Nov 07 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.4.4-1mamba
- update to 0.4.4
* Tue Nov 22 2005 Silvan Calarco <silvan.calarco@mambasoft.it> 0.3.1-1qilnx
- package created by autospec
