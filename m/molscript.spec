Name: molscript
Summary: MolScript (POVScript+ Mod)
Version: 2.1.2pov2.20
Release: 3.1
License: MolScript (https://www.avatar.se/molscript/obtain_info.html)
Source: molscript-%{version}.tar.gz
Group: Applications/Graphics
BuildRequires: gts-devel
BuildRequires: libpng12-devel
BuildRequires: netpbm

%description 
molscript is a program for creating schematic or detailed molecular
graphics images from molecular 3D coordinates, usually, but not
exclusively, protein structures. The user supplies an input file (the
script) which specifies the coordinate file, what objects to render
and the exact appearance of the objects through the graphics state
parameters. There is a helper program molauto, which produces a good
first-approximation input file from a coordinate file.

%prep
%setup -q
sed -i 's|png\.h|libpng12/png.h|' src/png_img.c
sed -i -e 's|EGifOpenFileHandle(fileno(outfile))|EGifOpenFileHandle(fileno(outfile),NULL)|' -e 's|EGifCloseFile (image)|EGifCloseFile (image,NULL)|' src/gif_img.c
sed -i -e 's|MakeMapObject|GifMakeMapObject|' -e 's|FreeMapObject|GifFreeMapObject|' -e '/PrintGifError/d' src/gif_img.c

%build
LDFLAGS=-Wl,--allow-multiple-definition
%configure
make

%install
%makeinstall

%files
%doc DISCLAIMER README NEWS AUTHORS INSTALL COPYING ChangeLog doc/*
%{_bindir}/*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.2pov2.20
- Rebuilt for Fedora
* Fri Nov  2 2007 Tim Fenn <fenn@stanford.edu>
- minor edits
* Sun Nov  5 2006 Tim Fenn <fenn@stanford.edu>
- add changelog entries, add prereq and dist tags
