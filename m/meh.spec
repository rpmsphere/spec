%undefine _debugsource_packages

Name: meh
Version: 0.3
Release: 3.1
Summary: A small, simple, super fast image viewer using raw XLib
Group: Graphics
License: MIT
URL: http://www.johnhawthorn.com/meh/
Source: http://web.uvic.ca/~jhawthor/%name-%version.tar.gz
BuildRequires: libXext-devel giflib-devel libjpeg-devel libpng-devel
Requires: ImageMagick

%description
meh is similar to feh, but faster and simpler.
meh can use ImageMagick's convert to view almost 200 file formats,
though it is slower for these formats. Built in formats are JPEG, PNG,
BMP, and netpbm.

Features
    Fast
    Tiny
    Fast JPEG, PNG, GIF and BMP support
    Fast netpbm support (.ppm, .pgm, .pbm, .pnm)
    ImageMagick support by calling convert
        All ImageMagick formats (almost 200)
        This allows limited support for PDF's and SVG's
    Scales images to window size
    Preserves aspect ratio (either via EWMH hints or by padding the window)
    XSHM Support
    Minimal dependencies (Xlib, libjpeg, libpng, giflib)

%prep
%setup -q
sed -i -e 's|DGifOpenFileHandle(fileno(f))|DGifOpenFileHandle(fileno(f),NULL)|' -e 's|DGifCloseFile(g->gif)|DGifCloseFile(g->gif,NULL)|' -e '/PrintGifError/d' src/gif.c

%build
%make_build

%install
mkdir -p %buildroot%_bindir
make install PREFIX=%buildroot/usr

%files
%doc AUTHORS BUGS COPYING NEWS README THANKS
%_bindir/%name

%changelog
* Mon Feb 06 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.1
- Rebuilt with libpng15
* Fri Apr 13 2012 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Linux Sisyphus
