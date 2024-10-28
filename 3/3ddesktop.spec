Summary:   3D OpenGL virtual desktop switcher
Name:      3ddesktop
Version:   0.2.9
Release:   8.1
License:   GPL
Group:     User Interface/Desktops
Source0:   https://prdownloads.sourceforge.net/desk3d/3ddesktop-%{version}.tar.gz
URL:       https://desk3d.sourceforge.net/
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  imlib2-devel
Source1:   imlib2-config

%description 
3d Destkop is an OpenGL program for switching virtual desktops in a
seamless 3-dimensional manner. The current desktop is mapped into a 3D
space where you may choose other screens. When activated the current
desktop appears to zoom out into the 3D view.  Several different
visualization modes are available.

%prep
%setup -q
sed -i 's/unsigned int/unsigned long/' event.hpp
sed -i '1i #include <cstring>' config.cpp
cp %{SOURCE1} .

%build
export PATH=$PATH:.
%configure
sed -i -e 's/@my_libs@//' -e 's/-Werror=format-security/-lImlib2 -lglut -lGLU -lGL -lSM -lICE -lSM -lICE -lX11 -lXext -lXmu -lXt -lXi/' Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc README COPYING ChangeLog TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/3ddesktop/digits.bmp
%{_sysconfdir}/3ddesktop.conf
%{_mandir}/man1/3ddesk.1.gz
%{_mandir}/man1/3ddeskd.1.gz

%changelog
* Tue Feb 03 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.9
- Rebuilt for Fedora
* Tue Aug 13 2002 wiget@pld-linux.org
- move 3ddesktop.spec to 3ddesktop.spec.in and make VERSION substitute automagicaly
- small changes for easy future development
