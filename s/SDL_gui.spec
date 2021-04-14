Name: SDL_gui
Version: 0.10.3
Release: 4.1
Source0: http://67.37.196.70/~rhk/SDL_gui/%{name}-%{version}.tar.gz
Patch0: config.sub.patch
URL: http://67.37.196.70/~rhk/SDL_gui/
License: LGPL
Summary: A Graphical User Interface library for SDL
Group: System Environment/Libraries
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_ttf-devel

%description
SDL_gui is a library written in C++ for displaying and 
controlling user interface elements in an SDL application. 
It has the following set of widgets: Screen, Button, ToggleButton, 
Label, Picture, Panel, CardStack, TextEntry and ProgressBar.

%package devel
Summary: Libraries and include files to develop %{name} applications
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
SDL_gui is a library written in C++ for displaying and 
controlling user interface elements in an SDL application. 
It has the following set of widgets: Screen, Button, ToggleButton, 
Label, Picture, Panel, CardStack, TextEntry and ProgressBar.

%prep
%setup -q
%patch0 -p1 -b .config.sub

%build
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="-lstdc++"
%configure 
sed -i -e's,-Werror[^ ]*,,g' src/Makefile
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%doc README COPYING 
%{_libdir}/libSDL_gui-%{version}.so

%files devel
%{_includedir}/SDL/SDL_gui.h
%{_libdir}/libSDL_gui.so
%{_libdir}/libSDL_gui.a
%exclude %{_libdir}/libSDL_gui.la

%changelog
* Tue Jul 05 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10.3
- Rebuilt for Fedora
* Thu Apr 05 2007 Paulo Roma <roma@lcg.ufrj.br> 0.10.3-1
- Rebuilt for Fedora 6 x86_64.
- Adapted spec file.
- Used a newer config.sub
* Sat Sep 06 2003 Paul Eggleton <bluelightning@bluelightning.org>
- Fixed build for Red Hat 9.0
* Mon Jun 12 2000 Ray Kelm <rhk@newimage.com>
- removed ttf subpackages
* Thu Jun 08 2000 Ray Kelm <rhk@newimage.com>
- include libtool definition files in devel packages.
* Sun May 21 2000 Ray Kelm <rhk@newimage.com>
- added python subpackages
* Sun May 21 2000 Ray Kelm <rhk@newimage.com>
- split ttf lib into subpackage
* Sun Apr 30 2000 Ray Kelm <rhk@newimage.com>
- initial spec file
