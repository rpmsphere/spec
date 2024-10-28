%undefine _debugsource_packages
%define __os_install_post %{nil}

Name:           sdlbasic
Version:        2012.12.15
Release:        8
URL:            https://sdlbasic.sourceforge.net/
Source0:        https://sourceforge.net/projects/sdlbasic/files/source/2012/sdlBasic-source-2012-12-15.tar.gz
Source1:        https://sourceforge.net/projects/sdlbasic/files/source/2012/sdlBrt-source-2012-12-15.tar.gz
License:        LGPL
Group:          Development/Other
Summary:        A small, efficient and multiplatform basic interpreter
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++, gtk2-devel, libtiff-devel, libjpeg-turbo-devel
BuildRequires:  SDL-devel SDL_mixer-devel SDL_image-devel SDL_ttf-devel SDL_net-devel smpeg-devel
Provides:       sdlbrt

%description
An easy basic in order to make games in 2d style amos for linux and windows.
The basic it comprises a module runtime, ide examples and games.

%prep
%setup -q -c -a 1
#sed -i -e 's|/opt/sdlBasic|%{buildroot}/usr|' -e 's|-o root -g root||' src/*/makefile src/*/*/makefile src/sdlBasic/gtk/sdlBasic.desktop 
#sed -i 's|/opt/sdlBasic|/usr|' src/sdlBasic/gtk/sdlBasic.desktop 
#sed -i 's|(guint)data|(unsigned long)data|' src/sdlBasic/gtk/SciTEGTK.cxx
#sed -i 's|CONFIGTHREADS=.*|CONFIGTHREADS=pkg-config --libs gmodule-2.0|' src/sdlBasic/gtk/makefile
sed -i '26i LIBS += -Wl,--allow-multiple-definition' cross/makefile

%build
mkdir -p ../linux/bin
make -f cross/makefile os=linux
make -C scintilla/gtk
make -C gtk

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
cp -r ../linux/bin ../linux/share $RPM_BUILD_ROOT/usr

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Sun May 22 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2012.12.15
- Rebuilt for Fedora
* Sun Dec 10 2006 Emmanuel Andry <eandry@mandriva.org> 20040425-2mdv2007.0
+ Revision: 94397
- Rebuild to fix missing requires
- Import sdlBasic
* Thu Jul 21 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 20040425-1mdk
- Initial package
