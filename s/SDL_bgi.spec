%undefine _debugsource_packages

Summary:    BGI-compatible 2D graphics C library
Name:       SDL_bgi
Version:    3.0.0
Release:    1
License:    ZLib
Group:      Libraries
Source:     https://sourceforge.net/projects/libxbgi/files/%{name}-%{version}.tar.gz
URL:        http://libxbgi.sourceforge.net/
BuildRequires: SDL2-devel

%description 
This package contains a Borland Graphics Interface (BGI) emulation
library based on SDL2. This library strictly emulates most BGI
functions, making it possible to compile SDL versions of programs
written for Turbo/Borland C. ARGB extensions and basic mouse support
are also implemented; further, native SDL2 functions may be used in
SDL_bgi programs.

%prep
%setup -q

%build
cd src
make

%install
rm -rf $RPM_BUILD_ROOT
cd src
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/SDL2
cp libSDL_bgi.so $RPM_BUILD_ROOT%{_libdir}
cp SDL_bgi.h $RPM_BUILD_ROOT%{_includedir}/SDL2

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -r /usr/include/graphics.h ]; then
  echo "graphics.h detected - skipping";
else 
  echo "creating symbolic link graphics.h -> SDL_bgi.h";
  ln -sf /usr/include/SDL2/SDL_bgi.h /usr/include/graphics.h
fi

%%postun
if [ -r /usr/include/graphics.h ]; then
  echo "Warning - /usr/include/graphics.h not deleted."
fi

%files
%doc AUTHORS ChangeLog doc/* LICENSE test/ TODO VERSION
%attr(755,root,root) %{_libdir}/*
%attr(644,root,root) %{_includedir}/SDL2/*

%changelog
* Sun Dec 18 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.0
- Rebuilt for Fedora
* Thu Nov 6 2014 Guido Gonzato <guido.gonzato at gmail.com>
- This is a generic rpm, buildable on Ubuntu
