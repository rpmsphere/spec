%define experimental 0

Summary: 	Fbi IMproved
Name: 		fim
Version: 	0.6
Release: 	0.1621
License: 	GPLv2
Group: 		Graphics
URL: 		http://www.nongnu.org/fbi-improved/
Source0: 	http://download.savannah.gnu.org/releases/fbi-improved/%{name}-%{version}-trunk.tar.gz
Source1: 	fim.desktop
BuildRequires: gcc-c++ automake
BuildRequires: gd-devel 
BuildRequires: pkgconfig(libpng)
BuildRequires: flex bison 
BuildRequires: giflib-devel 
BuildRequires: pkgconfig(ddjvuapi) 
BuildRequires: pkgconfig(libspectre)
BuildRequires: pkgconfig(sdl)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: readline-devel
BuildRequires: pkgconfig(poppler)
BuildRequires: pkgconfig(poppler-cpp)
BuildRequires: ghostscript-core ImageMagick
#BuildRequires: pkgconfig(GraphicsMagick)
#BuildRequires: pkgconfig(imlib2)
#BuildRequires: aalib-devel
BuildRequires: pkgconfig(libexif)

%description
FIM aims to be a highly customizable and scriptable 
image viewer targeted at users who are comfortable 
with software like the Vim text editor or the 
Mutt mail user agent. 
It is based on the Fbi image viewer, by Gerd Hoffmann, 
and works in the Linux framebuffer console mode, 
as well as under X/Xorg, using the SDL library. 
The right video mode gets auto-detected at runtime, 
and may be configured out at build time, if necessary. 

%prep
%setup -qn %{name}-%{version}-trunk
#sed -i 's|gFalse, gBgColor, bitmapTopDown|gFalse, gBgColor, bitmapTopDown, splashThinLineDefault|' src/FbiStuffPdf.cpp

%build
#export LDFLAGS="$LDFLAGS -lexif"
./autogen.sh
%configure \
    --prefix=/usr \
    --disable-debug \
    --enable-screen \
    --enable-unicode \
    --enable-pdf \
    --enable-hardcoded-font \
    --enable-recursive-dirs \
    --enable-poppler \
    --enable-scan-consolefonts \
%if %{experimental}
    --enable-graphicsmagick \
    --enable-imlib2 \
    --enable-exif \
    --enable-aa \
    --enable-custom-status-bar \
    --enable-optimizations \
    --enable-read-dirs \
    --enable-warnings 
%endif

make

%install
%make_install
install -pD -m644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -pD -m644  media/fim.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_bindir}/fimgs
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Sun Aug 28 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
* Thu May 01 2014 symbianflo <symbianflo@symbianflo> 0.4-rc1
+ Revision: 1b90f44
- Imported from SRPM
