Name:           aseprite
Version:        1.2.25
Release:        1
Summary:        Animated sprite editor & pixel art tool
Group:          Graphics/Editors and Converters
License:        GPLv2+
URL:            www.aseprite.org
# Git repo: https://github.com/aseprite/aseprite
# Upstream zip archive repacked without unused third party libs
# rm -rf third_party/{curl,freetype2,giflib,gtest,jpeg,libpng,libwebp,libwebp-cmake,loadpng,pixman,pixman-cmake,tinyxml,zlib}
#Source0:        %{name}-%{version}.tar.gz
Source0:        Aseprite-v1.2.25-Source.zip
#Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.1
# From third_party/pixman/pixman/pixman-combine32.h
Source2:        pixman-combine32.h
Patch0:         aseprite-1.1.4-mga-shared-gtest.patch
Patch1:         aseprite-1.1.7-allegro-no-fix-aliases.patch
BuildRequires:  allegro-devel
BuildRequires:  cmake
BuildRequires:  giflib-devel
BuildRequires:  gtest-devel
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(tinyxml)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)

%description
Aseprite (aka ASE, Allegro Sprite Editor) is an open source program to
create animated sprites & pixel art. Sprites are little images that can
be used in your website or in a video game. You can draw characters with
movement, intros, textures, patterns, backgrounds, logos, color palettes,
isometric levels, etc.

%prep
%setup -qc
#autopatch -p1
#sed -i '1i #include <cstring>' third_party/simpleini/SimpleIni.h

# Needed to build doc-lib
mkdir -p third_party/pixman/pixman
cp %{_sourcedir}/pixman-combine32.h third_party/pixman/pixman/

# Stable version
sed -i data/gui.xml src/config.h -e 's/-dev//'

%build
# The window can't be resized/maximize when linked against the system allegro 4
# We build against the embedded version for now - patching allegro could be investigated too
# allegro is still needed as a BR for libloadpng
mkdir build; cd build
%cmake .. -DENABLE_UPDATER=OFF \
       -DENABLE_WEBSERVER=OFF \
       -DUSE_SHARED_ALLEGRO4=OFF \
       -DUSE_SHARED_CURL=ON \
       -DUSE_SHARED_FREETYPE=ON \
       -DUSE_SHARED_GIFLIB=ON \
       -DUSE_SHARED_GTEST=ON \
       -DUSE_SHARED_JPEGLIB=ON \
       -DUSE_SHARED_LIBPNG=ON \
       -DUSE_SHARED_LIBLOADPNG=ON \
       -DUSE_SHARED_LIBWEBP=ON \
       -DUSE_SHARED_PIXMAN=ON \
       -DUSE_SHARED_TINYXML=ON \
       -DUSE_SHARED_ZLIB=ON \
       -DWITH_WEBP_SUPPORT=ON \
       -DLIBPIXMAN_INCLUDE_DIR:PATH=%{_includedir}/pixman-1 \
       -DLIBPIXMAN_LIBRARY:FILEPATH=%{_libdir}/libpixman-1.so
%make_build

%install
cd build
%make_install

install -D -m644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

for size in 16 32 48 64; do
  install -D -m644 ../data/icons/ase${size}.png \
          %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

install -d %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Aseprite
GenericName=Sprite editor
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Type=Application
Categories=Graphics;2DGraphics;RasterGraphics;
EOF

%files
%doc CONTRIBUTING.md README.md
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Sep 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.25
- Rebuilt for Fedora
* Fri Feb 14 2020 umeabot <umeabot> 1.1.7-6.mga8
+ Revision: 1519208
- Mageia 8 Mass Rebuild
+ wally <wally>
- build with new cmake macros
* Sat Oct 06 2018 daviddavid <daviddavid> 1.1.7-5.mga7
+ Revision: 1318156
- fix embedded allegro app builds failing due to alcompat.h defining aliases for
  fadd / fdiv / fmull which conflict with system headers
+ umeabot <umeabot>
- Mageia 7 Mass Rebuild
- Mageia 7 Mass Rebuild
* Sun Aug 06 2017 daviddavid <daviddavid> 1.1.7-3.mga7
+ Revision: 1137572
- rebuild for new libwebp 0.6.0
* Sun Mar 12 2017 akien <akien> 1.1.7-2.mga6
+ Revision: 1092238
- Rebuild against allegro4
* Sat Aug 13 2016 akien <akien> 1.1.7-1.mga6
+ Revision: 1046148
- Version 1.1.7
- Strip the erroneous -dev suffix in version string
- Version 1.1.6
* Tue May 10 2016 akien <akien> 1.1.5.3-1.mga6
+ Revision: 1012252
- Version 1.1.5.3
* Tue Apr 12 2016 akien <akien> 1.1.4-1.mga6
+ Revision: 1000892
- Version 1.1.4
- Build against system giflib
* Thu Jan 07 2016 neoclust <neoclust> 1.0.9-3.mga6
+ Revision: 920432
- dont_use_x86_assembly.patch:
    - Added. Fixes FTBFS with GCC 5. ( From Debian )
* Thu Sep 03 2015 cjw <cjw> 1.0.9-2.mga6
+ Revision: 872501
- rebuild with gcc 5
* Thu Mar 05 2015 akien <akien> 1.0.9-1.mga5
+ Revision: 817871
- Remove Debian-specific content in the manpage
- Package some doc
- imported package aseprite
