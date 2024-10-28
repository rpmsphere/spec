Name:      glito
Summary:   FLTK-based explorer for two-dimensional IFS
Version:   1.1
Release:   21.1
License:   GPL
Group:     Amusements/Graphics
Source0:   https://emmanuel.debanne.free.fr/glito/%{name}-%{version}.tar.gz
Source1:   %{name}.desktop
Source2:   %{name}.png
URL:       https://emmanuel.debanne.free.fr/glito/#english
BuildRequires: fltk-devel
BuildRequires: libpng12-devel

%description
Glito is free software. It is an explorer of IFS (Iterated Function Systems) in 2D.
IFS are a type of fractals. They are built by calculating the iterated images of a
point by contractive affine mappings. An IFS is a set of n (n ≥ 2) functions. A
function is chosen randomly to give a new image of a point.

Glito deals with linear functions:

Xn+1 = x1 Xn + x2 Yn + xc
Yn+1 = y1 Xn + y2 Yn + yc

and sinusoidal functions:

Xn+1 = x1 cos(Xn) + x2 sin(Yn) + xc
Yn+1 = y1 sin(Xn) + y2 cos(Yn) + yc

Glito can be used to draw Julia sets as well. Theorically we just need to draw the
points defined by:

Zn+1 = √( Zn - c )

where c is the parameter of the Julia. In Glito the equation is modified to make the
manipulation easier and to benefite from the linear mappings. We define, with
Zn = Xn + i Yn and c = xc + i yc:

Zn+1 = √( x1 Xn + x2 Yn + i (y1 Xn + y2 Yn) + c² )

Glito represents a function by a parallelogram. The center of the parallelogram has
for coordinates (xc, yc) and two contiguous edges correspond to the vectors (x1, y1)
and (x2, y2).

Glito's features:

    * modification by translation, rotation, dilation... of the IFS functions
      thanks to mouse

    * real-time visualization of the modifications

    * animations (transition between 2 IFS, rotation, zoom)

    * IFS can be saved under an XML format or under the Fractint format

    * images and animations can be saved in gray level, transparent or not.
      File formats: PNG, PGM, BMP and MNG for the animations

%prep
%setup -q
sed -i 's|Fl/Fl.H|FL/Fl.H|' configure
sed -i '18i #include <cstdlib>' src/Formula.cpp
sed -i '19i #include <cmath>\n#include <limits>\n#include <cstring>' src/Image.cpp
sed -i 's|Image::Image|Image|' src/Image.hpp
sed -i 's|png\.h|libpng12/png.h|' src/ImageGray.hpp
sed -i '1i #include <cstdlib>' src/Image.hpp src/Skeleton.cpp

%build
cp -f /usr/lib/rpm/redhat/config.* .
./configure --prefix=%{_prefix} --disable-debug --disable-static --enable-optimize --enable-shared
#--build=x86_64
sed -i 's|-O2|-O2 -fpermissive -lz|' */Makefile
make

%install
make prefix=%{buildroot}%{_prefix} install
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
cp %{SOURCE1} %{buildroot}%{_datadir}/applications
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps

%files
%doc COPYING NEWS README TODO
%{_bindir}/glito
%{_datadir}/doc/glito/manual_*.html
%{_datadir}/locale/*/LC_MESSAGES/glito.mo
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%exclude %{_datadir}/locale/locale.alias

%changelog
* Sun Mar 26 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Mon Sep 05 2005 Mirco Mueller <macslow at bangang dot de> 1.1-2
- fixed a ugly mishap in the .spec-file
* Mon Mar 07 2005 Mirco Mueller <macslow at bangang dot de> 1.1-1
- initial .spec file written for glito-1.1.tar.gz
- added an icon
- also added a .desktop file
